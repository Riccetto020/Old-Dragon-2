from colorama import Fore, Style
from interface import titulo_principal, mensagem_info, mensagem_erro
from personagem import Personagem
from metodos import EstiloClassico, EstiloAventureiro, EstiloHeroico
from racas import todas_racas
from classes import CLASSES
import os


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


while True:
    titulo_principal("CRIADOR DE PERSONAGENS DE RPG")

    while True:
        print(Fore.YELLOW + "\nEscolha a raça do seu personagem:" + Style.RESET_ALL)
        for idx, raca in enumerate(todas_racas, start=1):
            print(Fore.CYAN + f"{idx}. {raca.nome}" + Style.RESET_ALL)
        print(Fore.CYAN + "0. Voltar" + Style.RESET_ALL)

        escolha_raca = input(Fore.MAGENTA + "\nDigite o número da raça: " + Style.RESET_ALL)
        if escolha_raca == '0':
            break  

        try:
            raca_escolhida = todas_racas[int(escolha_raca)-1]
            print(Fore.YELLOW + "\nInformações da raça selecionada:" + Style.RESET_ALL)
            raca_escolhida.mostrar_info()
            break
        except (IndexError, ValueError):
            mensagem_erro("Opção inválida. Por favor, tente novamente.")

    if escolha_raca == '0':
        continue

    while True:
        print(Fore.YELLOW + "\nEscolha a classe do seu personagem:" + Style.RESET_ALL)
        for idx, classe in enumerate(CLASSES, start=1):
            print(Fore.CYAN + f"{idx}. {classe.nome}" + Style.RESET_ALL)
        print(Fore.CYAN + "0. Voltar" + Style.RESET_ALL)

        escolha_classe = input(Fore.MAGENTA + "\nDigite o número da classe: " + Style.RESET_ALL)
        if escolha_classe == '0':
            escolha_raca = '0'  
            break  

        try:
            classe_escolhida = CLASSES[int(escolha_classe)-1]
            classe_escolhida.mostrar_habilidades()
            break
        except (IndexError, ValueError):
            mensagem_erro("Opção inválida. Por favor, tente novamente.")

    if escolha_raca == '0':
        continue  


    print(Fore.YELLOW + "\nEscolha o método de distribuição de atributos:" + Style.RESET_ALL)
    print(Fore.CYAN + "1. Estilo Clássico")
    print(Fore.CYAN + "2. Estilo Aventureiro")
    print(Fore.CYAN + "3. Estilo Heróico")
    print(Fore.CYAN + "4. Voltar" + Style.RESET_ALL)

    escolha_metodo = input(Fore.MAGENTA + "\nDigite sua opção (1-4): " + Style.RESET_ALL)
    if escolha_metodo == '4':
        continue  

    if escolha_metodo in ['1','2','3']:
        nome_personagem = input(Fore.CYAN + "\nQual é o nome do seu personagem? " + Style.RESET_ALL)
        metodo_escolhido = {'1': EstiloClassico, '2': EstiloAventureiro, '3': EstiloHeroico}[escolha_metodo]()
        novo_personagem = Personagem(nome_personagem, metodo_escolhido, raca_escolhida, classe_escolhida)

        limpar_tela()  # Limpa a tela antes de mostrar a ficha final
        novo_personagem.mostrar_ficha()

        input(Fore.MAGENTA + "\nPressione Enter para continuar..." + Style.RESET_ALL)
    else:
        mensagem_erro("Opção inválida. Por favor, tente novamente.")


