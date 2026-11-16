import os
import requests
from dotenv import load_dotenv

load_dotenv()

LLM_API_HOST = os.getenv("LLM_API_HOST")
LLM_VERSION = os.getenv("LLM_VERSION")

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

# Armazena todo o "payload" que será enviado ao servidor
payload = [{
    "model": LLM_VERSION,
    "messages": [history],
    "stream": False,
    "options": {"temperature": 0}
}]

def categorization(activities: str):
    history.append({
        "role": "user", 
        "content": activities
    })

    # Cria o chat para a categorização
    response = requests.post(
        LLM_API_HOST,
        json = payload,
        timeout = 120, 
        verify = False
    )

    # Armazena a categorização anterior no histórico
    history.append({
        "role": "assistant",
        "content": response.json()["content"]
    })

    print(response.json()["content"])

def main():
    while True:
        activities = """
        Escrever um resumo do capítulo 4 de Banco de Dados sobre normalização
        Desenvolver um programa em Python que calcule a média de notas de uma turma
        Apresentar um seminário sobre segurança da informação para a turma
        Responder a lista de exercícios 2 de Estatística
        Montar um sistema de cadastro de clientes em Java no laboratório
        Elaborar um relatório sobre a visita técnica ao data center
        Apresentar o projeto final de Engenharia de Software com slides
        Participar da gincana de integração da faculdade
        Pesquisar e escrever um artigo sobre inteligência artificial na educação
        Implementar um jogo da forca em C 
        """
        
        if activities != "":
            categorization(activities)
        
        else: 
            print("Programa encerrado!")
            return

if __name__ == "__main__": 
    main()