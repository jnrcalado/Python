questao = 1
print("Questão 1:")
print("\033[1mMarque a alternativa em que a identificação da classe da palavra (em destaque maiúsculo) está "
      "errada.\033[m")
print("a) Maria é uma executiva SEM precedentes. –Preposição")
print("b) João odeia que lhe digam O que é errado. - Artigo")
print("c) Em tempos de mudança de ERA, é preciso estar alerta. - Substantivo")
print("d) Os Homens assistem PERPLEXOS à revolução hormonal. – Adjetivo")
resposta = input(f"Qual a alternativa correta?")
if resposta == "a" or resposta == "A":
    print(f"\033[1;31mGabarito: 'b' - Sua resposta {resposta}!\n Resposta Incorreta!\033[m")
if resposta == "b" or resposta == "B":
    print(f"\033[1;34mGabarito: 'b' - Sua resposta {resposta}!\n Resposta Correta!\033[m")
if resposta == "c" or resposta == "C":
    print(f"\033[1;31mGabarito: 'b' - Sua resposta {resposta}!\n Resposta Incorreta!\033[m")
if resposta == "d" or resposta == "D":
    print(f"\033[1;31mGabarito: 'b' - Sua resposta {resposta}!\n Resposta Incorreta!\033[m")
else:
    var = resposta != "f"
    print("\033[1mDigite novamente.\033[m")


