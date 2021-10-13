# Problema das camisas e calças


Uma determinada confecção opera com dois produtos: calças e camisas. Como tratam-se de produtos semelhantes, possuem uma produtividade comparável e compartilham os mesmos recursos. A programação da produção é realizada por lotes de produto.

O departamento de produção informa que são necessários 10 homens por hora para um lote de calças e 20 homens por hora para um lote de camisas. Sabe-se que não é necessária mão de obra especializada para a produção de calças, mas são necessários 10 homens por hora desse tipo de mão de obra para produzir um lote de camisas. O departamento de pessoal informa que a força máxima de trabalho disponível é de 30 homens por hora de operários especializados e de 50 homens por hora de não especializados.

Da planta de produção, sabemos que existem apenas duas máquinas com capacidade de produzir os dois tipos de produto, sendo que a máquina 1 pode produzir um lote de calças a cada 20 horas e um lote de camisas a cada 10 horas, não podendo ser utilizada por mais de 80 horas no período considerado. A máquina 2 pode produzir um lote de calças a cada 30 horas e um lote de camisas a cada 35 horas, não podendo ser utilizada por mais de 130 horas no período considerado.

São necessários dois tipos de matéria-prima para produzir calças e camisas. Na produção de um lote de calças são utilizados 12 quilos da matéria-prima A e 10 da B. Na produção de um lote de camisas são utilizados 8 quilos da matéria-prima A e 15 da B.

O almoxarifado informa que, por imposições de espaço, só pode fornecer 120 quilos de A e 100 quilos de B no período considerado.

Sabendo-se que o lucro pela venda é de 800 reais nos lotes de camisas e de 500 reais nos lotes de calças, formule o problema de maximizar o lucro da operação produtiva em pauta.


Primeiro vamos criar tabelas que ilustrem o problema que estamos lidando

| Tipo Lote | Homens/hora | especialistas/hora |Kgs matéria prima A|Kgs matéria prima B| lucro |
|-----------|-------------|--------------------|-------------------|-------------------|-------|
| Calças    | 10          | 0                  |12                 |10                 | 500   |
| Camisas   | 20          | 10                 |8                  |15                 | 800   |

Agora sobre as máquinas 

| Máquina   | tempo p/ lote calça(horas) | tempo p/ lote camisa(horas) | tempo máximo em operação (horas) |
|-----------|----------------------------|-----------------------------|----------------------------------|
| Máquina 1 | 20                         | 10                          | 80                               |
| Máquina 2 | 30                         | 35                          | 130                              |


Nossas variáveis de decisão é a quantidade de lote produzido por uma máquina sendo:
- x1c := lotes de calças produzidos pela máquina 1
- x2m := lotes de calças produzidos pela máquina 1
- x1c := lotes de calças produzidos pela máquina 2
- x2m := lotes de calças produzidos pela máquina 2

Elas formam uma função do tipo `f(x) = 500 * (x1c + x2c) + 800 * (x1m + x2m)`


E sujeito a:
- restrições associada a quantidade de operários:
  - não especializados: `10 * (x1c + c2c) + 20 * (x1m + x2m) <= 50`
  - especializados: `10 * (x1m + x2m) <= 30`

- restrições associadas aos materiais:
  - matéria prima A: `12 * (x1c + x2c) + 8  * (x1m + x2m) <= 120`
  - matéria prima B: `10 * (x1c + x2c) + 15 * (x1m + x2m) <= 100`

- restrições associadas as máquinas:
  - máquina 1: `20 * x1c + 10 * x1m <= 80`
  - máquina 2: `30 * x2c + 35 * x2m <= 130`