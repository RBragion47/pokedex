from flask import Flask, render_template, request, redirect, url_for
import requests
import sqlite3

app = Flask(__name__)


# ==================================================
# BANCO DE DADOS
# ==================================================

def criar_banco():
    conexao = sqlite3.connect("pokedex.db")
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS historico (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pokemon TEXT NOT NULL,
            data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conexao.commit()
    conexao.close()


def salvar_pesquisa(nome_pokemon):
    conexao = sqlite3.connect("pokedex.db")
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO historico (pokemon) VALUES (?)",
        (nome_pokemon,)
    )

    conexao.commit()
    conexao.close()


def buscar_historico():
    conexao = sqlite3.connect("pokedex.db")
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT pokemon, MAX(id) AS ultimo_id
        FROM historico
        GROUP BY pokemon
        ORDER BY ultimo_id DESC
        LIMIT 8
    """)

    historico = cursor.fetchall()

    conexao.close()

    return historico


def limpar_historico():
    conexao = sqlite3.connect("pokedex.db")
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM historico")

    conexao.commit()
    conexao.close()


# ==================================================
# POKÉAPI
# ==================================================

def buscar_pokemon(nome):

    url = f"https://pokeapi.co/api/v2/pokemon/{nome}"
    resposta = requests.get(url)

    if resposta.status_code == 200:

        dados = resposta.json()

        return {
            "nome": dados["name"],
            "id": dados["id"],
            "imagem": dados["sprites"]["other"]["official-artwork"]["front_default"],
            "altura": dados["height"] / 10,
            "peso": dados["weight"] / 10,

            "tipos": [
                tipo["type"]["name"]
                for tipo in dados["types"]
            ],

            "habilidades": [
                habilidade["ability"]["name"]
                for habilidade in dados["abilities"]
            ],

            "hp": dados["stats"][0]["base_stat"],
            "ataque": dados["stats"][1]["base_stat"],
            "defesa": dados["stats"][2]["base_stat"],
            "ataque_especial": dados["stats"][3]["base_stat"],
            "defesa_especial": dados["stats"][4]["base_stat"],
            "velocidade": dados["stats"][5]["base_stat"]
        }

    return None


def buscar_card_pokemon(nome):

    url = f"https://pokeapi.co/api/v2/pokemon/{nome}"
    resposta = requests.get(url)

    if resposta.status_code == 200:

        dados = resposta.json()

        return {
            "id": dados["id"],
            "nome": dados["name"],
            "imagem": dados["sprites"]["other"]["official-artwork"]["front_default"],

            "tipos": [
                tipo["type"]["name"]
                for tipo in dados["types"]
            ]
        }

    return None


# ==================================================
# MONTA OS 8 CARDS DA HOME
# ==================================================

def montar_lista_home():

    pokemons_padrao = [
        "bulbasaur",
        "charmander",
        "squirtle",
        "pikachu",
        "gengar",
        "lucario",
        "eevee",
        "snorlax"
    ]

    historico = buscar_historico()

    nomes_home = []

    # Primeiro entram os Pokémon recentes
    for item in historico:
        nome = item[0]

        if nome not in nomes_home:
            nomes_home.append(nome)


    # Depois completa com os Pokémon padrão
    for nome_padrao in pokemons_padrao:

        if nome_padrao not in nomes_home:
            nomes_home.append(nome_padrao)

        if len(nomes_home) == 8:
            break


    # Garante que teremos apenas 8
    nomes_home = nomes_home[:8]


    lista_pokemons = []

    for nome in nomes_home:

        card = buscar_card_pokemon(nome)

        if card:
            lista_pokemons.append(card)


    return lista_pokemons


# ==================================================
# PÁGINA INICIAL
# ==================================================

@app.route("/", methods=["GET", "POST"])
def inicio():

    pokemon = None
    erro = None


    # ==================================================
    # PESQUISA
    # ==================================================

    if request.method == "POST":

        nome = request.form.get("pokemon", "").lower().strip()

        if nome:

            pokemon = buscar_pokemon(nome)

            if pokemon is None:

                erro = "Pokémon não encontrado."

            else:

                salvar_pesquisa(pokemon["nome"])

        else:

            erro = "Digite o nome ou número de um Pokémon."


    historico = buscar_historico()

    lista_pokemons = montar_lista_home()


    return render_template(
        "index.html",
        pokemon=pokemon,
        erro=erro,
        lista_pokemons=lista_pokemons,
        historico=historico
    )


# ==================================================
# DETALHES AO CLICAR EM UM CARD
# ==================================================

@app.route("/pokemon/<nome>")
def detalhes_pokemon(nome):

    pokemon = buscar_pokemon(nome)

    if pokemon is None:

        return "Pokémon não encontrado.", 404


    # Ao clicar, também vira um Pokémon recente
    salvar_pesquisa(pokemon["nome"])


    historico = buscar_historico()


    return render_template(
        "index.html",
        pokemon=pokemon,
        erro=None,
        lista_pokemons=[],
        historico=historico
    )


# ==================================================
# LIMPAR HISTÓRICO
# ==================================================

@app.route("/limpar-historico", methods=["POST"])
def apagar_historico():

    limpar_historico()

    return redirect(url_for("inicio"))


# ==================================================
# INICIAR A APLICAÇÃO
# ==================================================

if __name__ == "__main__":

    criar_banco()

    app.run(debug=True)