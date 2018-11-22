nomealuno = str(input("Digite o nome do aluno: "))
numero1 = float(input("Digite a nota do primeiro bimestre do aluno: "))
numero2 = float(input("Digite a nota do segundo bimestre do aluno: "))
numero3 = float(input("Digite a nota do terceiro bimestredo aluno: "))
numero4 = float(input("Digite a nota do quarto bimestredo aluno: "))

media = float((numero1+numero2+numero3+numero4)//4)

print("A nota do final aluno", nomealuno,"foi igual à:",media)
