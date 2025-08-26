from colorama import Fore, Style

class Raca:
    def __init__(self, nome, habilidades=None, movimento=0, infravisao="não possui", alinhamento="qualquer um"):
        self.nome = nome
        self.habilidades = habilidades if habilidades else []
        self.movimento = movimento
        self.infravisao = infravisao
        self.alinhamento = alinhamento

    def mostrar_info(self):
        print(Fore.MAGENTA + f"\nRaça: {self.nome}" + Style.RESET_ALL)
        print(Fore.CYAN + f"Movimento base: {self.movimento} metros" + Style.RESET_ALL)
        print(Fore.BLUE + f"Infravisão: {self.infravisao}" + Style.RESET_ALL)
        print(Fore.BLUE + f"Alinhamento: {self.alinhamento}" + Style.RESET_ALL)
        if self.habilidades:
            print(Fore.GREEN + "Habilidades de Raça:" + Style.RESET_ALL)
            for habilidade in self.habilidades:
                print(Fore.GREEN + f"  - {habilidade}" + Style.RESET_ALL)

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

elfo = Raca(
    nome="Elfo",
    habilidades=[
        "Percepção Natural: detectar portas e passagens secretas com 1 em 1d6 (ou 1-2 se procurando ativamente)",
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
        "Pequenos: ataques de criaturas grandes ou maiores são difíceis de acertar",
        "Restrições: só pode usar armaduras de couro ou especiais; armas grandes proibidas; armas médias usadas como se fossem de duas mãos"
    ],
    movimento=6,
    infravisao="não possui",
    alinhamento="tendem à neutralidade"
)

todas_racas = [humano, elfo, anao, halfling]
