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

## Relatório de Desenvolvimento do Projeto

Durante as etapas iniciais de desenvolvimento, considerei a utilização de uma LLM executada localmente, com o objetivo de reduzir os custos de operação da aplicação. Para isso, utilizei o modelo **Llama 3.2 1B**, por meio do Ollama.

Entretanto, durante os testes, identifiquei algumas limitações importantes nessa abordagem. O modelo apresentava baixa precisão nas respostas, além de consumir uma quantidade considerável de recursos computacionais, tornando sua execução pouco eficiente e comprometendo o desempenho do dispositivo. Dessa forma, concluí que a utilização de uma LLM local não seria adequada para os objetivos do projeto.

Diante dessas dificuldades, optei pela migração para a API do **Google Gemini**. Minha escolha foi motivada principalmente pela disponibilidade de uma modalidade gratuita que, apesar de possuir limites de utilização, permitia o acesso a modelos mais precisos sem custos de operação. Além disso, sua integração apresentava menor complexidade.

Essa mudança exigiu a substituição da SDK do Ollama pela SDK do Gemini, além da adaptação da estrutura de comunicação com o modelo. Como resultado, observei melhorias significativas na precisão das respostas e no tempo de processamento das requisições, além da eliminação do consumo de recursos computacionais locais associado à execução da LLM.

Posteriormente, realizei uma nova migração, dessa vez para a infraestrutura disponibilizada pela própria instituição. Foi disponibilizado um servidor Ollama, acessível internamente pelo ambiente de execução da aplicação, utilizando o modelo **Qwen 3.5 9B**.

A decisão foi motivada principalmente pela questão financeira, uma vez que os custos de utilização da API do Gemini seriam de minha responsabilidade, enquanto a instituição já disponibilizava uma infraestrutura própria para a execução de modelos de linguagem.

Para realizar essa integração, precisei adaptar novamente a comunicação com o modelo. Inicialmente, tentei utilizar a biblioteca `requests` para realizar as requisições diretamente ao servidor, mas essa abordagem não apresentou os resultados esperados. Após identificar que o servidor disponibilizado era compatível com a API da OpenAI, optei pela utilização da SDK oficial da OpenAI. Essa escolha permitiu aproveitar sua estrutura de comunicação sem depender dos serviços ou modelos da própria OpenAI, mantendo o servidor Ollama institucional como responsável pelo processamento das requisições.

A comunicação entre a aplicação e o servidor institucional é realizada por meio de um endereço interno, definido através de uma variável de ambiente e utilizado durante a inicialização do container.

Em relação aos resultados, observei que o modelo institucional apresentou uma qualidade de respostas semelhante à alternativa anterior. Entretanto, identifiquei algumas limitações operacionais, principalmente a indisponibilidade ocasional do servidor e o elevado tempo de processamento, presente em todas as requisições realizadas.

Apesar dessas limitações, defini a utilização da infraestrutura institucional como a solução definitiva para o projeto, principalmente por eliminar os custos de utilização de serviços externos e permitir o aproveitamento dos recursos disponibilizados pela própria instituição.

### Uso de Inteligência Artificial

1. Desenvolvimento do conjunto de instruções repassada à LLM;
2. Revisão de Erros e pequenas sugestões de melhoria;
