from pulp import *
import numpy as np

prob = LpProblem('problema das Ligas Metálicas', LpMaximize)

x1 = LpVariable(name='Baixa resistência', lowBound=0)
x2 = LpVariable(name='Alta resistência', lowBound=0)

#função objetivo
prob += 3000 * x1 + 5000 * x2

#restrições
prob += 0.5 * x1 + 0.2 * x2 <= 16
prob += 0.25 * x1 + 0.3 * x2 <= 11
prob += 0.25 * x1 + 0.5 * x2 <= 15


prob.solve()
for v in prob.variables():
    print(v.name, "=", v.varValue)
print("Receita Bruta máxima = ", value(prob.objective))
