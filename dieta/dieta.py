from pulp import *
import numpy as np

prob = LpProblem('problema da dieta', LpMinimize)

#variáveis
x1 = LpVariable(name='Leite', lowBound=0)
x2 = LpVariable(name='Carne', lowBound=0)
x3 = LpVariable(name='Peixe', lowBound=0)
x4 = LpVariable(name='Salada', lowBound=0)

#função objetivo
prob += 2 * x1 + 4 * x2 + 1.5 * x3 + x4

#restrições
prob +=  2 * x1 +  2 * x2 + 10 * x3 + 20 * x4 >= 11    # vitamina A
prob += 50 * x1 + 20 * x2 + 10 * x3 + 30 * x4 >= 70    # vitamina C
prob += 80 * x1 + 70 * x2 + 10 * x3 + 80 * x4 >= 250   # vitamina D

prob.solve()
for v in prob.variables():
    print(v.name, "=", v.varValue)
print("custo mínimo = ", value(prob.objective))


