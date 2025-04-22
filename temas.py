import random

# Dicionário com temas e palavras
temas = {
    "Frutas": ["maçã", "banana", "laranja", "abacaxi", "manga"],
    "Animais": ["cachorro", "gato", "elefante", "tigre", "leão"],
    "Cidades": ["são paulo", "rio de janeiro", "salvador", "curitiba", "porto alegre"],
    "Filmes": ["matrix", "inception", "interstellar", "avengers", "batman"],
    "Cores": ["azul", "vermelho", "verde", "amarelo", "preto"]
}

def escolher_tema():
    print("Escolha um tema:")
    for i, tema in enumerate(temas.keys(), 1):
        print(f"{i} - {tema}")
    
    while True:
        escolha = input("Digite o número do tema escolhido: ").strip()
        if escolha.isdigit() and 1 <= int(escolha) <= len(temas):
            tema_selecionado = list(temas.keys())[int(escolha) - 1]
            print(f"Você escolheu o tema: {tema_selecionado}")
            return tema_selecionado
        else:
            print("Escolha inválida. Tente novamente.")

def escolher_palavra(tema):
    return random.choice(temas[tema])
