
from colorama import Fore, Style

class Atributos:
    def __init__(self, forca, destreza, constituicao, inteligencia, sabedoria, carisma):
        self.forca = forca
        self.destreza = destreza
        self.constituicao = constituicao
        self.inteligencia = inteligencia
        self.sabedoria = sabedoria
        self.carisma = carisma

    @classmethod
    def from_dict(cls, d):
        return cls(
            forca=d.get("forca", 0),
            destreza=d.get("destreza", 0),
            constituicao=d.get("constituicao", 0),
            inteligencia=d.get("inteligencia", 0),
            sabedoria=d.get("sabedoria", 0),
            carisma=d.get("carisma", 0)
        )

    def mostrar(self):
        print(Fore.GREEN + "ATRIBUTOS DO PERSONAGEM:" + Style.RESET_ALL)
        print(Fore.GREEN + f"Força: {self.forca}" + Style.RESET_ALL)
        print(Fore.GREEN + f"Destreza: {self.destreza}" + Style.RESET_ALL)
        print(Fore.GREEN + f"Constituição: {self.constituicao}" + Style.RESET_ALL)
        print(Fore.GREEN + f"Inteligência: {self.inteligencia}" + Style.RESET_ALL)
        print(Fore.GREEN + f"Sabedoria: {self.sabedoria}" + Style.RESET_ALL)
        print(Fore.GREEN + f"Carisma: {self.carisma}" + Style.RESET_ALL)