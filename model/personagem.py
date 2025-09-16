from typing import Optional # Adicione esta linha
from .atributos import Atributos
# Outros imports, se houver, como .racas e .classes

class Personagem:
    def __init__(self, nome: str, raca, classe_, atributos_obj: Optional[Atributos] = None, metodo_distribuicao=None):
        self.nome = nome
        self.raca = raca
        self.classe = classe_
        
        if atributos_obj:
            self.atributos = atributos_obj
        else:
            self.atributos = metodo_distribuicao.distribuir()

    def mostrar_ficha(self):
        # Este método deve ser removido ou adaptado
        # para não usar 'print' e ser puramente lógica.
        pass