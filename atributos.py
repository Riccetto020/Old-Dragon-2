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
        # Espera d ser um dict com as keys corretas
        return cls(
            forca=d.get("Força", 0),
            destreza=d.get("Destreza", 0),
            constituicao=d.get("Constituição", 0),
            inteligencia=d.get("Inteligência", 0),
            sabedoria=d.get("Sabedoria", 0),
            carisma=d.get("Carisma", 0)
        )

    def mostrar(self):
        print(Fore.GREEN + "ATRIBUTOS DO PERSONAGEM:" + Style.RESET_ALL)
        print(Fore.GREEN + f"Força: {self.forca}" + Style.RESET_ALL)
        print(Fore.GREEN + f"Destreza: {self.destreza}" + Style.RESET_ALL)
        print(Fore.GREEN + f"Constituição: {self.constituicao}" + Style.RESET_ALL)
        print(Fore.GREEN + f"Inteligência: {self.inteligencia}" + Style.RESET_ALL)
        print(Fore.GREEN + f"Sabedoria: {self.sabedoria}" + Style.RESET_ALL)
        print(Fore.GREEN + f"Carisma: {self.carisma}" + Style.RESET_ALL)
