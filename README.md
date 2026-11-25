# Projeto P0: Primeiro Fluxo de LLM

## Problema  

Um aluno de Sistemas de Informação busca classificar a lista de avaliações recebidas pelos professores nas seguintes categorias:

- Avaliações escritas;
- Avaliações práticas;
- Apresentações;
- Outros;

### Justificativa

O uso de uma LLM, nesse caso, é justificável, tendo em vista que ela é capaz de interpretar as atividades recebidas, e segregá-las nas seções supracitadas. Com isso, busca-se eliminar a necessidade do professor especificar qual tipo de atividade será delegada ao aluno, além de facilitar a organização do aluno, abrindo portas para o aluno saber quais são os tipos de atividade os quais ele deve priorizar ao longo de seu período letivo.

## Instalação

### Pré-requisitos

Para fazer a instalação da ferramenta, é necessário estar instalado o Docker e o Git Bash

- Siga as instruções para a instalação do [Docker](https://www.docker.com/products/docker-desktop/).
- Siga as instruções para a instalação do [Git Bash](https://git-scm.com/install/).

### Configuração

**1.** Clone o repositório no seu dispositivo

``` bash
git clone https://github.com/rodrigo66713/p0-project.git
```

**2.** Acesse a pasta do repositório

``` bash
cd p0-project
```

**3.** Configure as variáveis de ambiente:

Na pasta do projeto, crie um arquivo ``.env``, tomando como referência o ``.env.example``. Configure as credenciais necessárias para a inicialização do projeto.

### Execução

**1.** Construa a imagem Docker:

Com o Docker Desktop em execução, execute os seguinte comando.

``` cmd
docker build -t categorizacao 
```

**2.** Inicialize o container:

``` cmd
docker run --env-file .env categorizacao 
```

Após esses passos, a ferramenta estará disponível para a utilização.

## Relatório de Desenvolvimento do Projeto

No início do desenvolvimento do projeto, foi considerado o uso de uma LLM local, cuja qual seria, muito menos custosa de ser executada no ambiente do que se comunicar com uma API de um modelo tradicional. Para tal, foi utilizado o modelo Llama 3.2 de 1 bilhão de parâmetros.

No entanto, durante o desenvolvimento do projeto, alguns problemas foram encontrados, como reprodutibilidade em outros dispositivos, e a ineficiência devido ao fato de rodar muitos recursos do computador, tornando-o lento, além do modelo supracitado ser completamente impreciso.

Desse modo, após algumas pesquisar, foi constatado que a API do Google Gemini seria a ideal, pois ela disponibliza uma chave de API inclusa no seuplano gratuito, e contornaria todos os problemas encontrados ao utilizar a LLM local.

"Rascunho: mudei novamente a llm do projeto, dessa vez para a llm disponiblizada pela própria softex"

### Uso de Inteligência Artificial

1. Desenvolvimento do conjunto de instruções repassada à LLM;
2. Revisão de Erros e pequenas sugestões de melhoria;
