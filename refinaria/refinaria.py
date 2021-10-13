from pulp import *
import numpy as np

prob = LpProblem('problema das calças e camisas', LpMaximize)

#variáveis
x1 = LpVariable(name='gasolina',    lowBound=0) 
x2 = LpVariable(name='gás',         lowBound=0) 

#função objetivo
prob += 10 * x1 + 7 * x2

#restrições
#restriões associadas às etapas de destilação e dessulfurização
prob += x1 * (1 / 500000) == 1 - (x2 * (1 / 600000))
prob += x1 * (1 / 700000) == 1 - (x2 * (1 / 500000))

#restrições associadas as etapas exclusivas
prob += x1 <= 400000                                 #Reforming
prob += x2 <= 450000                                 #Cracking


prob.solve()
for v in prob.variables():
    print(v.name, "=", v.varValue)
print("lucro máximo = ", value(prob.objective))