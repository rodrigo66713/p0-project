from ollama import generate

def explanation():
    response = generate(
        model= "llama3.2:1b",
        prompt= "Explique, em uma frase, o que é python.",
        stream= True,
    )

    for chunk in response: 
        print(chunk.response, end= '', flush= True)

explanation()