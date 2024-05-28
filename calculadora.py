print("Universidade Estácio")
print("Curso: Desenvolvimento Full Stack")
print("Período: 2024.1")

print("Missão Prática")

#===========================================
# Missão Prática | Desvendando a caixa preta
#===========================================

#entrada do primeiro número
txt_1 = input("Informe o primeiro número: ")
txt_2 = input("Informe o segundo  número: ")

#convertendo para variáveis numéricas do tipo int
num_1 = int(txt_1)
num_2 = int(txt_2)

#impressão dos resultados
print("Resultados")
print("Resultado da adição:        " + str(num_1 + num_2))
print("Resultado da subtração:     " + str(num_1 - num_2))
print("Resultado da multiplicação: " + str(num_1 * num_2))
#verifica se o segundo número é igual a zero
#caso seja, avisa que não pode ser efetuada a divisão por zero
if (num_2 != 0):
    print("Resultado da divisão:   " + str(num_1 / num_2))
else:
    print("Não é possivel divisão por 0 (zero)")
