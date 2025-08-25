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
Como Executar

Abra o terminal na pasta do projeto.

Execute o arquivo principal:

python main.py


Siga o fluxo:

Escolha a raça do personagem.

Escolha a classe do personagem.

Distribua os atributos (dependendo do método escolhido).

Visualize a ficha completa do personagem.

Exemplo de Uso
CRIADOR DE PERSONAGENS DE RPG

Escolha a raça do seu personagem:
1. Humano
2. Elfo
3. Anão
4. Halfling

Digite o número da raça: 1
Humano selecionado!

Escolha a classe do seu personagem:
1. Guerreiro
2. Mago
3. Bardo

Digite o número da classe: 1
Guerreiro selecionado!

Distribuição de atributos (Estilo Clássico, 3d6 em ordem)...

Ficha do Personagem:
Nome: Aramis
Raça: Humano
Classe: Guerreiro
Atributos:
Força: 15
Destreza: 12
Constituição: 14
Inteligência: 10
Sabedoria: 13
Carisma: 11
Movimento: 9 metros

Observações

O projeto mantém o estilo de cores no terminal para facilitar a visualização das mensagens.

Futuras melhorias podem incluir:

Mais raças e classes.

Salvamento de personagens em arquivo.

Sistema de evolução de níveis.
