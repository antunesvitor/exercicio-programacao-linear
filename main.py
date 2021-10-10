from pulp import *
import numpy as np

prob = LpProblem('problema da cooperativa agrícula ', LpMaximize)

#variáveis
#fazenda 1 
x1m = LpVariable(name='Milho na fazenda 1', lowBound=0) 
x1a = LpVariable(name='Arroz na fazenda 1', lowBound=0) 
x1f = LpVariable(name='Feijão na fazenda 1', lowBound=0) 

#fazenda 2
x2m = LpVariable(name='Milho na fazenda 2', lowBound=0) 
x2a = LpVariable(name='Arroz na fazenda 2', lowBound=0) 
x2f = LpVariable(name='Feijão na fazenda 2', lowBound=0) 

#fazenda 3
x3m = LpVariable(name='Milho na fazenda 3', lowBound=0)
x3a = LpVariable(name='Arroz na fazenda 3', lowBound=0) 
x3f = LpVariable(name='Feijão na fazenda 3', lowBound=0) 

#função objetivo
prob += 5000 * (x1m + x2m + x3m) + 4000 * (x1a + x2a + x3a) + 1800 * (x1f + x2f + x3f)

#restrições

#restriões referentes a área de cultivo
prob +=  x1m + x1a + x1f <= 400                         # restrição da fazenda 1 
prob +=  x2m + x2a + x2f <= 650                         # restrição da fazenda 2 
prob +=  x3m + x3a + x3f <= 350                         # restrição da fazenda 3

#restriões referentes ao consumo de água
prob += 5.5 * x1m + 4 * x1a + 3.5 * x1f <= 1800         # restrição da fazenda 1 
prob += 5.5 * x2m + 4 * x2a + 3.5 * x2f <= 2200         # restrição da fazenda 2 
prob += 5.5 * x3m + 4 * x3a + 3.5 * x3f <= 950          # restrição da fazenda 3

#restriões associadas ao plantio por cultura
prob +=  x1m + x2m + x3m <= 660                         # restrição da fazenda 1 
prob +=  x1a + x2a + x3a <= 880                         # restrição da fazenda 2 
prob +=  x1f + x2f + x3f <= 400                         # restrição da fazenda 3

#restrição associada à proporção de área cultivada:
prob += (x1m + x1a + x1f)/400 == (x2m + x2a + x2f)/650
prob += (x2m + x2a + x2f)/650 == (x3m + x3a + x3f)/350


prob.solve()
for v in prob.variables():
    print(v.name, "=", v.varValue)
print("lucro máximo = ", value(prob.objective))