#  Juliana está coordenando entregas de projetos e precisa calcular o tempo total necessário 
# para finalizar três tarefas: X, Y e Z.
#  Se alguma tarefa estiver com o tempo de entrega negativo, deve-se exibir uma mensagem de 
# erro e não somar o total.

Dia_01 = int (input)("Digite o tempo em que foi feito a tarefaX")
Dia_02 = int (input)("Digite o tempo em que foi feito a tarefaY")
Dia_03 = int (input)("Digite o tempo em que foi feito a tarefaZ")

if Dia_01 < 0 or Dia_02 < 0 or Dia_03 < 0:
    print ("erro numeros negativos")
else:
    soma = Dia_01 + Dia_02 + Dia_03 
    print(f"tempo total da atividade: {soma} dias ")
    


    
    
     