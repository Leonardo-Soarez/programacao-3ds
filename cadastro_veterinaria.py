class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def registrar(self):
        return f"Registrado: {self.especie} - {self.nome}"

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, "Cachorro")
        self.raca = raca

    def registrar(self):
        return f"Registrado: {self.especie} ({self.raca}) - {self.nome}"

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, "Gato")
        self.cor = cor

    def registrar(self):
        return f"Registrado: {self.especie} ({self.cor}) - {self.nome}"

# Exemplo de uso com polimorfismo
animais = [
    Cachorro("Bob", "Chihuahua"),
    Gato("Mimi", "Branco")
]

for a in animais:
    print(a.registrar())
