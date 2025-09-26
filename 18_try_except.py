def divisao (a , b):

    try:
        resultado = a / b
        print(f"O resultado da divisão de {a} e {b} é: {resultado}")

    except ValueError:
        print("")


    except Exception as descricao:
        print("Erro inesperado")

    else: 
        print("Divisão realizada com sucesso! ")

divisao (10,2)
divisao (10,0)
divisao (10,"1dois")
divisao ("10",2)