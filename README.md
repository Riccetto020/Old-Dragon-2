# Criador de Personagens RPG - Old Dragon

Projeto em Python para criar personagens de RPG no estilo Old Dragon, permitindo escolher **raça**, **classe** e **atributos**, exibindo a ficha completa no terminal com cores estilizadas.

---

## Estrutura do Projeto

- **`main.py`**: Arquivo principal que executa o fluxo do jogo, integra escolhas de raça, classe e distribuição de atributos, e exibe a ficha final do personagem.

- **`interface.py`**: Funções de interface com o usuário, incluindo títulos, mensagens de erro e informação, utilizando cores no terminal via `colorama`.

- **`racas.py`**: Define as raças disponíveis (Humano, Elfo, Anão, Halfling), suas habilidades e movimento base.

- **`classes.py`**: Define as classes do jogo (Guerreiro, Mago, Bardo), suas habilidades, restrições e características especiais.

- **`personagem.py`**: Contém a classe `Personagem`, que armazena nome, atributos, raça e classe do personagem, além de exibir a ficha completa.

- **`metodos.py`**: Métodos de distribuição de atributos (Estilo Clássico, Estilo Aventureiro e Estilo Heróico), incluindo a lógica de rolagem e alocação de valores.

---

## Requisitos

- Python 3.10 ou superior
- Biblioteca `colorama` para cores no terminal

Instalação da biblioteca:

```bash
pip install colorama
