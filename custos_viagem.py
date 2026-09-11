```python
def calcular_custo_total(veiculos):
    distancia = 200
    custo_total = 0

    for veiculo in veiculos:
        custo_total += veiculo.calcular_custo(distancia)

    return custo_total


class Carro:
    def __init__(self, consumo, preco_combustivel):
        self.consumo = consumo
        self.preco_combustivel = preco_combustivel

    def calcular_custo(self, distancia):
        litros = distancia / self.consumo
        return litros * self.preco_combustivel


class Moto:
    def __init__(self, consumo, preco_combustivel):
        self.consumo = consumo
        self.preco_combustivel = preco_combustivel

    def calcular_custo(self, distancia):
        litros = distancia / self.consumo
        return litros * self.preco_combustivel


class Caminhao:
    def __init__(self, consumo, preco_combustivel):
        self.consumo = consumo
        self.preco_combustivel = preco_combustivel

    def calcular_custo(self, distancia):
        litros = distancia / self.consumo
        return litros * self.preco_combustivel


veiculos = [
    Carro(12, 6.00),
    Moto(25, 6.00),
    Caminhao(4, 6.00)
]

total = calcular_custo_total(veiculos)

print("Custo total da viagem de 200 km: R$", round(total, 2))
```
