palavra = "restaurante"

contador = 0

for letra in palavra:
    contador = contador + 1
    print(f" {contador} - {letra}")

cidades = ["poa","fortaleza","sao miguel","belem","recife","sao paulo"]

for cidade in cidades:
    print(cidade)


botaoExecutar = True
contador2 = 0

while botaoExecutar:
    print(contador2)
    contador2 = contador2 + 1
    if contador2 >=200:
        botaoExecutar = False
    
