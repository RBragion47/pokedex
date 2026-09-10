# Pokédex

Projeto desenvolvido para a disciplina de desenvolvimento de software, com o objetivo de criar uma aplicação web completa utilizando front-end, back-end e banco de dados.

O projeto será desenvolvido em etapas, recebendo novas funcionalidades ao longo das entregas.

---

## Objetivo

A aplicação funciona como uma Pokédex interativa.

O usuário pode pesquisar Pokémon por nome ou número, visualizar informações detalhadas e acessar os Pokémon pesquisados recentemente.

Além disso, o projeto utiliza a PokéAPI para obter informações dos Pokémon e SQLite para armazenar dados localmente.

---

## Funcionalidades da AC1

Na primeira etapa do projeto foram desenvolvidas as funcionalidades principais de consulta da Pokédex.

- Pesquisa de Pokémon por nome
- Pesquisa de Pokémon pelo número da Pokédex
- Consulta de dados através da PokéAPI
- Exibição da imagem oficial do Pokémon
- Exibição do número da Pokédex
- Exibição do nome do Pokémon
- Exibição dos tipos
- Cores diferentes para cada tipo
- Exibição da altura
- Exibição do peso
- Exibição das habilidades
- Exibição dos atributos base:
  - HP
  - Ataque
  - Defesa
  - Ataque Especial
  - Defesa Especial
  - Velocidade
- Cards de Pokémon na página inicial
- Cards clicáveis para visualizar os detalhes
- Histórico dos Pokémon acessados
- Histórico exibido sem repetição
- Exibição de 8 cards na página inicial
- Organização dos Pokémon recentes nos primeiros cards
- Preenchimento dos espaços restantes com Pokémon padrão
- Substituição automática dos cards conforme novos Pokémon são acessados
- Opção para limpar o histórico
- Layout responsivo

---

## Tecnologias utilizadas

### Front-end

- HTML5
- CSS3
- Jinja2

### Back-end

- Python
- Flask

### Banco de dados

- SQLite

### API externa

- PokéAPI

---

## Arquitetura do projeto

A aplicação utiliza uma arquitetura dividida em três camadas principais.

```text
Usuário
   |
   v
HTML + CSS
Front-end
   |
   v
Python + Flask
Back-end
   |
   +----------------+
   |                |
   v                v
PokéAPI          SQLite
```

### Front-end

Responsável pela interface apresentada ao usuário.

Utiliza HTML, CSS e Jinja2 para exibir:

- Campo de pesquisa
- Cards dos Pokémon
- Imagens
- Tipos
- Informações detalhadas
- Habilidades
- Atributos

### Back-end

Desenvolvido utilizando Python e Flask.

É responsável por:

- Receber as pesquisas realizadas pelo usuário
- Consultar a PokéAPI
- Processar os dados recebidos
- Enviar os dados para o front-end
- Registrar os Pokémon acessados no banco de dados
- Controlar as rotas da aplicação
- Organizar os Pokémon exibidos na página inicial

### Banco de dados

O projeto utiliza SQLite para armazenar o histórico dos Pokémon acessados pelo usuário.

---

## Banco de dados

O banco de dados utilizado pelo projeto é:

```text
pokedex.db
```

Atualmente o banco possui a tabela:

```text
historico
```

Estrutura da tabela:

```sql
CREATE TABLE historico (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pokemon TEXT NOT NULL,
    data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

O sistema realiza atualmente operações de:

- INSERT
- SELECT
- DELETE

Essas operações permitem registrar os Pokémon acessados, consultar o histórico e limpar os dados armazenados.

---

## PokéAPI

A aplicação utiliza a PokéAPI para obter os dados dos Pokémon.

Entre as informações utilizadas estão:

- Nome
- Número da Pokédex
- Imagem oficial
- Tipo
- Altura
- Peso
- Habilidades
- HP
- Ataque
- Defesa
- Ataque Especial
- Defesa Especial
- Velocidade

---

## Funcionamento da página inicial

A página inicial sempre apresenta 8 cards de Pokémon.

Inicialmente são exibidos alguns Pokémon padrão.

Quando um novo Pokémon é pesquisado ou acessado, ele passa a aparecer entre os primeiros cards da página inicial.

Os Pokémon acessados mais recentemente ficam nas primeiras posições e os espaços restantes são preenchidos pelos Pokémon padrão.

Caso um Pokémon que já esteja entre os cards seja acessado novamente, ele passa para a primeira posição sem aparecer duplicado visualmente.

---

## Estrutura do projeto

```text
pokedex/
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── pokedex.db
├── requirements.txt
├── .gitignore
└── README.md
```

A pasta `venv` é utilizada no ambiente de desenvolvimento, mas não é enviada para o repositório GitHub.

---

## Como executar o projeto

### 1. Baixar ou clonar o projeto

Abra a pasta do projeto no Visual Studio Code.

### 2. Criar o ambiente virtual

No terminal:

```bash
python -m venv venv
```

### 3. Ativar o ambiente virtual

No Windows utilizando o CMD:

```cmd
venv\Scripts\activate.bat
```

Quando o ambiente virtual estiver ativado, o terminal deverá apresentar:

```text
(venv)
```

antes do caminho da pasta.

### 4. Instalar as dependências

Execute:

```bash
pip install -r requirements.txt
```

### 5. Executar a aplicação

Execute:

```bash
python app.py
```

### 6. Abrir a aplicação no navegador

Acesse:

```text
http://127.0.0.1:5000
```

---

## Próximas funcionalidades

Nas próximas entregas, o projeto poderá ser expandido com novas funcionalidades, como:

- Entradas mais completas da Pokédex
- Descrições dos Pokémon
- Informações sobre espécie e geração
- Cadeia de evolução
- Tabela de fraquezas
- Resistências e imunidades
- Cálculo de efetividade entre tipos
- Criação de times com até 6 Pokémon
- Análise de fraquezas do time
- Análise de cobertura de tipos
- Estatísticas do time

Essas funcionalidades serão adicionadas progressivamente nas próximas etapas do projeto.

---

## Status do projeto

### AC1

Em funcionamento.

Atualmente a aplicação permite pesquisar Pokémon, visualizar suas informações, acessar cards interativos e armazenar o histórico de acessos utilizando SQLite.

### Próximas etapas

Planejadas para as próximas entregas.

---

## Desenvolvedor

Projeto acadêmico desenvolvido individualmente por Richard Bragion.