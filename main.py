import random
from forca import jogar_forca
from temas import escolher_tema, escolher_palavra

def main():
    print("Bem-vindo ao Jogo da Forca!")
    
    tema = escolher_tema()
    palavra = escolher_palavra(tema)
    
    jogar_forca(palavra)

if __name__ == "__main__":
    main()