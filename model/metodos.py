import random
from abc import ABC, abstractmethod
from typing import List
from .atributos import Atributos

class MetodoDistribuicao(ABC):
    @abstractmethod
    def distribuir(self) -> List[int]:
        pass

class EstiloClassico(MetodoDistribuicao):
    def _rolar_3d6(self) -> int:
        return sum(random.randint(1, 6) for _ in range(3))

    def distribuir(self) -> Atributos:
        # Este método permanece o mesmo, pois não há interação.
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

    def distribuir(self) -> List[int]:
        # Apenas rola os dados e retorna a lista de valores
        return [self._rolar_3d6() for _ in range(6)]

class EstiloHeroico(MetodoDistribuicao):
    def _rolar_4d6_drop_lowest(self) -> int:
        rolagens = [random.randint(1, 6) for _ in range(4)]
        rolagens.remove(min(rolagens))
        return sum(rolagens)

    def distribuir(self) -> List[int]:
        # Apenas rola os dados e retorna a lista de valores
        return [self._rolar_4d6_drop_lowest() for _ in range(6)]