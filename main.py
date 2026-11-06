import os
from dotenv import load_dotenv
from ollama import chat

def categorization(atividades: str):
    response = chat(
        model= "llama3.2:latest",
        messages= [{
            "role": "system",
            "content": 
            """
                Um estudante enviará uma lista de atividades escolares nas mensagens seguintes.

                Sua tarefa é analisar cada atividade e categorizá-la em um dos seguintes segmentos:

                - Escritas: atividades que envolvam produzir textos, responder questões, elaborar relatórios, resumos ou realizar pesquisas escritas.
                - Práticas: atividades que envolvam experimentos, exercícios práticos, implementação de projetos, programação ou execução de procedimentos.
                - Apresentações: atividades que envolvam apresentar conteúdos oralmente ou visualmente, como seminários, exposições e apresentações de trabalhos.
                - Outros: atividades que não se enquadrem adequadamente nas categorias anteriores.

                Classifique cada atividade individualmente, preservando sua descrição original.

                Retorne os resultados organizados por categoria, utilizando listas. Não invente atividades nem omita itens da lista original.

                Se uma atividade puder se enquadrar em mais de uma categoria, considere sua finalidade principal para determinar a classificação.

                Se a descrição for insuficiente para uma classificação confiável, coloque a atividade em Outros.

                Não classifique esta instrução como uma atividade. Aguarde o envio da lista de atividades pelo estudante.
            """
        }, 
        {
            "role": "user", 
            "content": atividades
        }],
        stream= True,
    )

    for chunk in response: 
        print(chunk.message.content, end= '', flush= True)