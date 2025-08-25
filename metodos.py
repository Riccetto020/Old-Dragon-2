import random
from abc import ABC, abstractmethod
from typing import List
from atributos import Atributos
from interface import mensagem_info, mensagem_erro
from colorama import Fore, Style

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
        return Atributos(
            self._rolar_3d6(),
            self._rolar_3d6(),
            self._rolar_3d6(),
            self._rolar_3d6(),
            self._rolar_3d6(),
            self._rolar_3d6()
        )

class EstiloAventureiro(MetodoDistribuicao):
    def _rolar_3d6(self) -> int:
        return sum(random.randint(1, 6) for _ in range(3))

    def distribuir(self) -> Atributos:
        mensagem_info("\nGerando atributos no Estilo Aventureiro (3d6, distribua como quiser)...")
        input(Fore.MAGENTA + "Pressione Enter para rolar os 6 valores..." + Style.RESET_ALL)
        rolagens = [self._rolar_3d6() for _ in range(6)]
        return self._distribuir_valores_interativo(rolagens)

    def _distribuir_valores_interativo(self, rolagens: List[int]) -> Atributos:
        from interface import mensagem_info, mensagem_erro
        nomes_atributos = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]
        atributos_finais = {}
        mensagem_info("\nVocê rolou os seguintes valores: " + str(sorted(rolagens, reverse=True)))
        for atributo_atual in nomes_atributos:
            while True:
                try:
                    valor_input = int(input(Fore.CYAN + f"Qual valor você quer para {atributo_atual}? " + Style.RESET_ALL))
                    if valor_input in rolagens:
                        atributos_finais[atributo_atual] = valor_input
                        rolagens.remove(valor_input)
                        break
                    else:
                        mensagem_erro("Valor inválido.")
                except ValueError:
                    mensagem_erro("Entrada inválida.")
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
