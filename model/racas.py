# model/racas.py
class Raca:
    def __init__(self, nome, habilidades=None, movimento=0, infravisao="não possui", alinhamento="qualquer um"):
        self.nome = nome
        self.habilidades = habilidades if habilidades else []
        self.movimento = movimento
        self.infravisao = infravisao
        self.alinhamento = alinhamento

    def mostrar_info(self):
        # Este método é mais útil para a versão de linha de comando,
        # mas pode ser usado para exibir detalhes em outra rota do Flask, se desejar.
        print(f"\nRaça: {self.nome}")
        print(f"Movimento base: {self.movimento} metros")
        print(f"Infravisão: {self.infravisao}")
        print(f"Alinhamento: {self.alinhamento}")
        if self.habilidades:
            print("Habilidades de Raça:")
            for habilidade in self.habilidades:
                print(f"  - {habilidade}")

elfo = Raca(
    nome="Elfo",
    habilidades=[
        "Visão Aguçada: detectar portas e passagens secretas com 1 em 1d6 (ou 1-2 se procurando ativamente)",
        "Graciosos: +1 em qualquer teste de JPD",
        "Arma Racial: +1 em dano de ataques à distância com arcos",
        "Imunidades: imune a sono e paralisia causada por Ghoul"
    ],
    movimento=9,
    infravisao="18 metros",
    alinhamento="tendem à neutralidade"
)

anao = Raca(
    nome="Anão",
    habilidades=[
        "Mineradores: detectar anomalias em pedras com 1 em 1d6 (ou 1-2 se procurando ativamente)",
        "Vigoroso: +1 em qualquer teste de JPC",
        "Armas grandes: armas grandes são consideradas médias para anões",
        "Inimigos: ataques contra orcs, ogros e hobgoblins são considerados fáceis"
    ],
    movimento=6,
    infravisao="18 metros",
    alinhamento="tendem à ordem"
)

halfling = Raca(
    nome="Halfling",
    habilidades=[
        "Furtivos: chance de 1-2 em 1d6 para se esconder; +1 em Furtividade se for Ladrão",
        "Destemidos: +1 em qualquer teste de JPS",
        "Bons de Mira: ataques à distância com armas de arremesso são fáceis",
        "Pequenos: +2 em testes de Furtividade e em testes de JPC contra ataques corpo a corpo"
    ],
    movimento=9,
    infravisao="não possui",
    alinhamento="tendem à neutralidade"
)

humano = Raca(
    nome="Humano",
    habilidades=[
        "Aprendizado: recebe +10% de XP",
        "Adaptabilidade: +1 em uma JP à escolha"
    ],
    movimento=9,
    infravisao="não possui",
    alinhamento="qualquer um"
)

todas_racas = [elfo, anao, halfling, humano]