from colorama import Fore, Style

class Classe:
    def __init__(self, nome: str, habilidades: str):
        self.nome = nome
        self.habilidades = habilidades

    def mostrar_habilidades(self):
        print(Fore.CYAN + f"\nHABILIDADES DE CLASSE: {self.nome.upper()}" + Style.RESET_ALL)
        print(Fore.GREEN + self.habilidades + Style.RESET_ALL)


GUERREIRO = Classe(
    "Guerreiro",
    """Armas: pode usar todas as armas.
Armaduras: pode usar todas as armaduras.
Itens Mágicos: não pode usar cajados, varinhas e pergaminhos mágicos (exceto pergaminhos de proteção).

Aparar: pode sacrificar seu escudo ou arma para absorver dano.
Maestria em Arma: recebe bônus no dano de armas escolhidas.
Ataque Extra: no 6º nível adquire um segundo ataque consecutivo."""
)

MAGO = Classe(
    "Mago",
    """Armas: apenas pequenas.
Armaduras: nenhuma.
Itens Mágicos: podem usar todos os tipos.

Magias Arcanas: lança magias diárias memorizadas no grimório.
Ler Magias: pode decifrar inscrições mágicas uma vez por dia por nível.
Detectar Magias: percebe a presença de magia em até 9m + 3m por nível, necessitando concentração."""
)

BARDO = Classe(
    "Bardo",
    """Restrições: perde Ataque Furtivo, mantém Ouvir Ruídos e talentos de Ladrão adaptados.

Cultura: substitui Arrombar, permitindo conhecer folclore, lendas e história.
Decifrar: substitui Armadilha, permite decifrar textos em outros idiomas."""
)

LADRAO = Classe(
    "Ladrão",
    """Armas: pode usar armas simples e de lâmina.
Armaduras: pode usar armaduras leves.
Itens Mágicos: pode usar todos os tipos.

Ataque Furtivo: causa dano extra quando ataca um oponente desprevenido.
Arrombar: pode abrir fechaduras e desarmar armadilhas.
Ouvir Ruídos: permite detectar sons e identificar sua origem."""
)

# A lista de classes que será importada em outros arquivos
CLASSES = [GUERREIRO, MAGO, BARDO, LADRAO]