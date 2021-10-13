# O Problema da Refinaria

## Enunciado

Em uma determinada refinaria, o petróleo bruto sofre os seguintes processamentos antes de ser transformado em gás/óleo ou gasolina bruta:

Gasolina:\
Destilação -> dessulfurização -> reforming

Gás/óleo:\
Destilação -> Cracking -> dessulfurização

A Tabela representa a capacidade máxima de processamento de cada unidade de operação. Formular o problema de modo a maximizar os lucros totais, solucionando-o graficamente.

| Processo         | capacidae Máx. Gasolina (ton/ano) | capacidae Máx. Gasolina (ton/ano) |
|------------------|-----------------------------------|-----------------------------------|
| Destilação       | 500000                            | 600000                            |
| Dessulfurização  | 700000                            | 500000                            |
| Reforming        | 400000                            |                                   |
| Cracking         |                                   | 450000                            |
| Lucros Unitários | 10,00 reais/ton                   | 7,00 reais/ton                    |


## Solução

### Função de Decisão

A variável de decisão já foi informada no enunciado é as toneladas produzidas por ano de cada produto, sendo x1 := gasolina e x2 := gás/óleo. Nossa função para ser maximizada será `f(x) = 10 * x1 + 7 * x2`

### Restrições

Como há uma capacidade máxima para cada etapa do processo e depende de produto que será feito a partir do petróleo, a capacidade da etapa de `Destilação` se dá pela fórmula abaixo:

`x1 / 500000 = 1 - (x2 / 600000)`

Desse modo se destilarmos 500000 toneladas de petróleo p/ gasolina não podemos destilar mais para gás/óleo. Da mesma forma se segue a dessulfurização:

`x1 / 700000 = 1 - (x2 / 500000)`

As duas etapas restantes são exclusivas de cada produto final logo a restrição de `x1` não depende de `x2` e vice-versa:

Reforming:\
`x1 < 400000`

Cracking:\
`x2 < 450000`
