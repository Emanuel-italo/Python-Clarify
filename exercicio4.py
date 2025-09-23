nome_aluno = input("Digite o nome do aluno: ")
turma_aluno = int(input("Digite aqui a turma do aluno: "))

nota1 = float(input("Digite aqui a primeira nota do aluno: "))
nota2 = float(input("Digite aqui a segunda nota do aluno: "))
nota3 = float(input("Digite aqui a terceira nota do aluno: "))
nota4 = float(input("Digite aqui a quarta nota do aluno: "))


soma = nota1 + nota2 + nota3 + nota4

media = soma / 4

if media >=7:
    print("Aprovado")

else:
    print("reprovado")
