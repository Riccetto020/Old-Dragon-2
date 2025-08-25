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
