import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

def categorization(activity: str):
    client = genai.Client(api_key=GEMINI_API_KEY)
    
    interaction = client.interactions.create(
        model="gemini-3-flash-preview",
        system_instruction= """
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
                    """,
        input= activity,
        stream= True
    )

    for event in interaction: 
        if event.event_type == 'step.delta':
            if event.delta.type == 'text':
                print(event.delta.text, end="", flush=True)

categorization("fazer relatório, desenvolver programa, apresentação sobre python, maquete de um computador")