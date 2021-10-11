from pulp import *
import numpy as np

prob = LpProblem('problema das calças e camisas', LpMaximize)

#variáveis
#Máquina 1 
x1c = LpVariable(name='Calças  máquina 1', lowBound=0) 
x1m = LpVariable(name='Camisas máquina 1', lowBound=0) 

#Máquina 2
x2c = LpVariable(name='Calças  máquina 2', lowBound=0) 
x2m = LpVariable(name='Camisas máquina 2', lowBound=0)  

#função objetivo
prob += 500 * (x1c + x2c) + 800 * (x1m + x2m)

#restrições

#restriões referentes aos operários
prob +=  10 * (x1c + x2c) + 20 * (x1m + x2m) <= 50                  # não especializados
prob +=  10 * (x1m + x2m) <= 30                                     # espcializados

#restriçõe associadas aos materiais:
prob += 12 * (x1c + x2c ) + 8  * (x1m + x2m) <= 120                 # Matéria Prima A
prob += 10 * (x1c + x2c ) + 15 * (x1m + x2m) <= 100                 # Matéria Prima B

# restrições associadas às máquinas:
prob += 20 * x1c + 10 * x1m <=  80                                   # Máquina 1
prob += 30 * x2c + 35 * x2m <= 130                                   # Máquina 2


prob.solve()
for v in prob.variables():
    print(v.name, "=", v.varValue)
print("lucro máximo = ", value(prob.objective))