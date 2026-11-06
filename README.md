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

Para rodar o projeto, é necessária a instalação das seguintes dependências:

- [Python](python.org/download)

## Relatório de Desenvolvimento do Projeto

No início do desenvolvimento do projeto, foi considerado o uso de uma LLM local, cuja qual seria, muito menos custosa de ser executada no ambiente do que se comunicar com uma API de um modelo tradicional. Para tal, foi utilizado o modelo Llama 3.2 de 1 bilhão de parâmetros.

No entanto, durante o desenvolvimento do projeto, alguns problemas foram encontrados, como reprodutibilidade em outros dispositivos, e a ineficiência devido ao fato de rodar muitos recursos do computador, tornando-o lento, além do modelo supracitado ser completamente impreciso.

Desse modo, após algumas pesquisar, foi constatado que a API do Google Gemini seria a ideal, pois ela disponibliza uma chave de API inclusa no seuplano gratuito, e contornaria todos os problemas encontrados ao utilizar a LLM local.

"Rascunho: mudei novamente a llm do projeto, dessa vez para a llm disponiblizada pela própria softex"

### Uso de Inteligência Artificial

1. Desenvolvimento do conjunto de instruções repassada à LLM;
2. Revisão de Erros e pequenas sugestões de melhoria;
