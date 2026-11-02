# Projeto P0: Primeiro Fluxo de LLM

## Problema  

Um aluno de Sistemas de Informação busca classificar a lista de avaliações recebidas pelos professores nas seguintes categorias:

- Avaliações escritas;
- Avaliações práticas;
- Apresentações;
- Entregas;

### Justificativa

O uso de uma LLM, nesse caso, é justificável, tendo em vista que ela é capaz de interpretar as atividades recebidas, e segregá-las nas seções supracitadas. Com isso, busca-se eliminar a necessidade do professor especificar qual tipo de atividade será delegada ao aluno, além de facilitar a organização do aluno, abrindo portas para o aluno saber quais são os tipos de atividade os quais ele deve priorizar ao longo de seu período letivo.

## Instalação

Para rodar o projeto, é necessária a instalação das seguintes dependências:

- [Python](python.org/download)
- [Ollama](ollama.com/download)
- [Llama 3.2 - 1B](https://ollama.com/library/llama3.2:1b)

## Desenvolvimento

Para o desenvolvimento do projeto, foi constatado que uma LLM Local seria muito mais barata de ser executado no ambiente do que se comunicar com uma API de um modelo tradicional.

Para esse projeto, foi utilizado o modelo Llama 3.2 de 1 bilhão de parâmetros, pois é um modelo leve e que é capaz de fazer essa categorização de modo eficiente.

1. O Ambiente Virtual Python (.venv) foi criado.
2. Foram instaladas as seguintes dependências no ambiente virtual:

- Ollama SDK: `pip install ollama`
