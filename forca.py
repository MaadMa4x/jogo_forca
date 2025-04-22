def jogar_forca(palavra):
    tentativas = 6  # Número de tentativas
    letras_erradas = []
    letras_corretas = ["_"] * len(palavra)
    
    print("Vamos começar o jogo da forca!")
    
    while tentativas > 0 and "_" in letras_corretas:
        print("\nPalavra: " + " ".join(letras_corretas))
        print(f"Tentativas restantes: {tentativas}")
        print(f"Letras erradas: {' '.join(letras_erradas)}")
        
        tentativa = input("Digite uma letra: ").strip().lower()
        
        if len(tentativa) != 1 or not tentativa.isalpha():
            print("Por favor, digite apenas uma letra válida.")
            continue
        
        if tentativa in letras_erradas or tentativa in letras_corretas:
            print("Você já tentou essa letra. Tente outra.")
            continue
        
        if tentativa in palavra:
            print(f"Boa! A letra '{tentativa}' está na palavra.")
            for i, letra in enumerate(palavra):
                if letra == tentativa:
                    letras_corretas[i] = tentativa
        else:
            print(f"A letra '{tentativa}' não está na palavra.")
            letras_erradas.append(tentativa)
            tentativas -= 1
    
    if "_" not in letras_corretas:
        print(f"\nParabéns, você acertou a palavra: {''.join(letras_corretas)}!")
    else:
        print(f"\nVocê perdeu! A palavra era: {palavra}")