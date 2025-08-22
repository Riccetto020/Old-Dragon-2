import random
from abc import ABC, abstractmethod
from typing import List, Dict
from colorama import Fore, Style, init

init(autoreset=True)

def titulo_principal(texto):
    print(Fore.RED + "╔" + "═" * (len(texto) + 2) + "╗")
    print("║ " + texto + " ║")
    print(Fore.YELLOW + "╚" + "═" * (len(texto) + 2) + "╝" + Style.RESET_ALL)

def mostrar_atributo(nome, valor):
    print(Fore.CYAN + f"{nome:<15}: {valor}" + Style.RESET_ALL)

def mensagem_erro(texto):
    print(Fore.RED + texto + Style.RESET_ALL)

def mensagem_info(texto):
    print(Fore.GREEN + texto + Style.RESET_ALL)

class Atributos:
    def __init__(self, forca: int, destreza: int, constituicao: int,
                 inteligencia: int, sabedoria: int, carisma: int):
        self.forca = forca
        self.destreza = destreza
        self.constituicao = constituicao
        self.inteligencia = inteligencia
        self.sabedoria = sabedoria
        self.carisma = carisma

    @classmethod
    def from_dict(cls, data: Dict[str, int]):
        return cls(
            forca=data.get("Força", 0),
            destreza=data.get("Destreza", 0),
            constituicao=data.get("Constituição", 0),
            inteligencia=data.get("Inteligência", 0),
            sabedoria=data.get("Sabedoria", 0),
            carisma=data.get("Carisma", 0)
        )

    def mostrar(self):
        mostrar_atributo("Força", self.forca)
        mostrar_atributo("Destreza", self.destreza)
        mostrar_atributo("Constituição", self.constituicao)
        mostrar_atributo("Inteligência", self.inteligencia)
        mostrar_atributo("Sabedoria", self.sabedoria)
        mostrar_atributo("Carisma", self.carisma)

class MetodoDistribuicao(ABC):
    @abstractmethod
    def distribuir(self) -> Atributos:
        pass

class EstiloClassico(MetodoDistribuicao):
    def _rolar_3d6(self) -> int:
        return sum(random.randint(1, 6) for _ in range(3))

    def distribuir(self) -> Atributos:
        mensagem_info("\nGerando atributos no Estilo Clássico (3d6, em ordem)...")
        input(Fore.MAGENTA + "Pressione Enter para rolar os dados..." + Style.RESET_ALL)

        forca = self._rolar_3d6()
        mensagem_info(f"Sua Força é: {forca}")
        destreza = self._rolar_3d6()
        mensagem_info(f"Sua Destreza é: {destreza}")
        constituicao = self._rolar_3d6()
        mensagem_info(f"Sua Constituição é: {constituicao}")
        inteligencia = self._rolar_3d6()
        mensagem_info(f"Sua Inteligência é: {inteligencia}")
        sabedoria = self._rolar_3d6()
        mensagem_info(f"Sua Sabedoria é: {sabedoria}")
        carisma = self._rolar_3d6()
        mensagem_info(f"Seu Carisma é: {carisma}")

        return Atributos(forca, destreza, constituicao, inteligencia, sabedoria, carisma)

class EstiloAventureiro(MetodoDistribuicao):
    def _rolar_3d6(self) -> int:
        return sum(random.randint(1, 6) for _ in range(3))

    def distribuir(self) -> Atributos:
        mensagem_info("\nGerando atributos no Estilo Aventureiro (3d6, distribua como quiser)...")
        input(Fore.MAGENTA + "Pressione Enter para rolar os 6 valores..." + Style.RESET_ALL)

        rolagens = [self._rolar_3d6() for _ in range(6)]
        return self._distribuir_valores_interativo(rolagens)

    def _distribuir_valores_interativo(self, rolagens: List[int]) -> Atributos:
        nomes_atributos = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]
        atributos_finais = {}

        mensagem_info("\nVocê rolou os seguintes valores: " + str(sorted(rolagens, reverse=True)))

        for atributo_atual in nomes_atributos:
            print(Fore.YELLOW + "\n-----------------------------" + Style.RESET_ALL)
            print(Fore.MAGENTA + f"Valores disponíveis: {rolagens}" + Style.RESET_ALL)
            valor_escolhido = 0
            while True:
                try:
                    valor_input = int(input(Fore.CYAN + f"Qual valor você quer para {atributo_atual}? " + Style.RESET_ALL))
                    if valor_input in rolagens:
                        valor_escolhido = valor_input
                        break
                    else:
                        mensagem_erro("Valor inválido. Por favor, escolha um dos valores da lista.")
                except ValueError:
                    mensagem_erro("Entrada inválida. Por favor, digite um número.")
            atributos_finais[atributo_atual] = valor_escolhido
            rolagens.remove(valor_escolhido)

        mensagem_info("\nDistribuição concluída!")
        return Atributos.from_dict(atributos_finais)

class EstiloHeroico(EstiloAventureiro):
    def _rolar_4d6_drop_lowest(self) -> int:
        rolagens = [random.randint(1, 6) for _ in range(4)]
        rolagens.remove(min(rolagens))
        return sum(rolagens)

    def distribuir(self) -> Atributos:
        mensagem_info("\nGerando atributos no Estilo Heróico (4d6 drop tirando o menor, distribua como quiser)...")
        input(Fore.MAGENTA + "Pressione Enter para rolar os 6 valores..." + Style.RESET_ALL)
        rolagens = [self._rolar_4d6_drop_lowest() for _ in range(6)]
        return self._distribuir_valores_interativo(rolagens)

class Personagem:
    def __init__(self, nome: str, metodo_distribuicao: MetodoDistribuicao):
        self.nome = nome
        mensagem_info(f"\nIniciando a criação de '{self.nome}'...")
        self.atributos = metodo_distribuicao.distribuir()

    def mostrar_ficha(self):
        titulo_principal(f"ATRIBUTOS DE: {self.nome.upper()}")
        self.atributos.mostrar()
        print(Fore.CYAN + "═" * (len(f"ATRIBUTOS DE: {self.nome.upper()}") + 4) + Style.RESET_ALL)

if __name__ == "__main__":
    while True:
        titulo_principal("CRIADOR DE PERSONAGENS DE RPG")
        print(Fore.YELLOW + "\nEscolha o método de distribuição de atributos:" + Style.RESET_ALL)
        print(Fore.CYAN + "1. Estilo Clássico (3d6 em ordem, aleatório e desafiador)")
        print(Fore.CYAN + "2. Estilo Aventureiro (3d6, você distribui os resultados)")
        print(Fore.CYAN +"3. Estilo Heróico (4d6 tira o menor, você distribui os resultados)")
        print(Fore.CYAN +"4. Sair" + Style.RESET_ALL)

        escolha = input(Fore.MAGENTA + "\nDigite sua opção (1-4): " + Style.RESET_ALL)

        if escolha == '4':
            mensagem_info("\nObrigado por jogar! Até a próxima aventura.")
            break

        if escolha in ['1', '2', '3']:
            nome_personagem = input(Fore.CYAN + "\nQual é o nome do seu personagem? " + Style.RESET_ALL)
            metodo_escolhido = None

            if escolha == '1':
                metodo_escolhido = EstiloClassico()
            elif escolha == '2':
                metodo_escolhido = EstiloAventureiro()
            elif escolha == '3':
                metodo_escolhido = EstiloHeroico()

            novo_personagem = Personagem(nome_personagem, metodo_escolhido)
            novo_personagem.mostrar_ficha()
            input(Fore.MAGENTA + "\nPressione Enter para continuar..." + Style.RESET_ALL)
        else:
            mensagem_erro("Opção inválida. Por favor, tente novamente.")
