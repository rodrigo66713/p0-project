import os
import openai
from dotenv import load_dotenv
import gradio as gr

load_dotenv()

LLM_API_HOST = os.getenv("LLM_API_HOST")
LLM_API_KEY = os.getenv("LLM_API_KEY")
LLM_VERSION = os.getenv("LLM_VERSION")

client = openai.OpenAI(
    base_url = LLM_API_HOST, 
    api_key= LLM_API_KEY,
    http_client=openai.DefaultHttpxClient(verify=False),
    timeout=300
)

def categorization(activities, history):
    # Organiza o histórico implementado pelo GradIO
    messages = [
        {
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
        },
        *history,
        {"role": "user", "content": activities}
    ]

    # Armazena todo o "payload" que será enviado ao servidor
    # (*) -> descompacta listas em tuplas
    # (**) -> descompacta bibliotecas em tuplas
    payload = {
        "model": LLM_VERSION,
        "messages": [*messages],
        "stream": False,
        "temperature": 0
    }

    # Envia o payload para a LLM 
    response = client.chat.completions.create(**payload)

    return response.choices[0].message.content

# Interface básica do Gradio
gr.ChatInterface(
    fn=categorization,
    title="Categorização automática de atividades",
    chatbot=gr.Chatbot(show_label="Insira aqui a lista de atividades a serem categorizadas", buttons=[]),
).launch(
    server_name="0.0.0.0",
    server_port=8080,
    theme=gr.themes.Soft(),
    footer_links=[],
)