from pulp import *
import numpy as np

prob = LpProblem('problema do sítio', LpMaximize)

#variáveis
xt = LpVariable(name='Trigo', lowBound=400) 
xa = LpVariable(name='Arroz', lowBound=800)
xm = LpVariable(name='Milho', lowBound=10000)

#função objetivo
prob += 2.16 * xt + 1.26 * xa + 0.812 * xm

#restrições
prob +=  xt + xa + xm <= 200000                         # restrição de área
prob += 0.2 * xt + 0.3 * xa + 0.4 * xm <= 60000         # restrição de peso

prob.solve()
for v in prob.variables():
    print(v.name, "=", v.varValue)
print("lucro máximo = ", value(prob.objective))