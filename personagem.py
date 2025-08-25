class Personagem:
    def __init__(self, nome: str, metodo_distribuicao, raca, classe_):
        self.nome = nome
        self.atributos = metodo_distribuicao.distribuir()
        self.raca = raca
        self.classe = classe_

    def mostrar_ficha(self):
        from interface import titulo_principal
        from colorama import Fore, Style
        titulo_principal(f"PERSONAGEM: {self.nome.upper()}")
        print(Fore.CYAN + f"RAÇA: {self.raca.nome}" + Style.RESET_ALL)
        print(Fore.CYAN + f"CLASSE: {self.classe.nome}" + Style.RESET_ALL)
        self.atributos.mostrar()
        self.classe.mostrar_habilidades()
        print(Fore.CYAN + "="*50 + Style.RESET_ALL)
