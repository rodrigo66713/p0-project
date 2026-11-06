import os
from dotenv import load_dotenv
from ollama import Client
from ollama import chat

load_dotenv()

OLLAMA_HOST = os.getenv("OLLAMA_HOST")
client = Client()

# Armazena o histórico de interações
history = [{
            "role": "system",
            "content": 
            """
                Um estudante de Sistemas de Informação enviará uma lista de atividades escolares nas mensagens seguintes.

                Sua tarefa é analisar cada atividade e categorizá-la em um dos seguintes segmentos:

                - Escritas: atividades que envolvam produzir textos, responder questões, elaborar relatórios, resumos ou realizar pesquisas escritas.
                - Práticas: atividades que envolvam o desenvolvimento de projetos práticos nos computadores, como o desenvolvimento de um programa.
                - Apresentações: atividades que envolvam apresentar conteúdos oralmente ou visualmente, como seminários, exposições e apresentações de trabalhos.
                - Outros: atividades que não se enquadrem adequadamente nas categorias anteriores.

                Classifique cada atividade individualmente, preservando sua descrição original.

                Retorne os resultados organizados por categoria, utilizando listas. Não invente atividades nem omita itens da lista original.

                Se uma atividade puder se enquadrar em mais de uma categoria, considere sua finalidade principal para determinar a classificação.

                Se a descrição for insuficiente para uma classificação confiável, coloque a atividade em Outros.

                Não classifique esta instrução como uma atividade. Aguarde o envio da lista de atividades pelo estudante.
                    
                Corrija qualquer erro de sintaxe digitado na entrada.
            """
        }]

def categorization(activities: str):
    history.append({
        "role": "user", 
        "content": activities
    })

    # Cria o chat para a categorização
    response = chat(
        model= "llama3.2:1b",
        messages= history,
        stream= False,
    )

    # Armazena a categorização anterior no histórico
    history.append({
        "role": "assistant",
        "content": response["message"]["content"]
    })

    print(response["message"]["content"])

categorization("escrever relatorio")