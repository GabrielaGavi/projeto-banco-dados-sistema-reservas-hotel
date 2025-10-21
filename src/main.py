from utils import config
from utils.splash_screen import SplashScreen
from reports.relatorios import Relatorios
from controller.controller_hospede import Controller_Hospede
from controller.controller_quarto import Controller_Quarto
from controller.controller_reserva import Controller_Reserva


tela_inicial = SplashScreen()
relatorio = Relatorios()
ctrl_hospede = Controller_Hospede()
ctrl_quarto = Controller_Quarto()
ctrl_reserva = Controller_Reserva()

def reports(opcao_relatorio: int = 0):
    if opcao_relatorio == 1:
        relatorio.relatorio_reservas_por_status()
    elif opcao_relatorio == 2:
        relatorio.relatorio_reservas_detalhado()
    elif opcao_relatorio == 3:
        relatorio.relatorio_reservas_por_mes()
    elif opcao_relatorio == 4:
        relatorio.relatorio_hospedes()

def inserir(opcao_inserir: int = 0):
    if opcao_inserir == 1:
        ctrl_hospede.inserir_hospede()
    elif opcao_inserir == 2:
        ctrl_quarto.inserir_quarto()
    elif opcao_inserir == 3:
        ctrl_reserva.inserir_reserva()

def atualizar(opcao_atualizar: int = 0):
    if opcao_atualizar == 1:
        ctrl_hospede.atualizar_hospede()
    elif opcao_atualizar == 2:
        ctrl_quarto.atualizar_quarto()
    elif opcao_atualizar == 3:
        ctrl_reserva.atualizar_reserva()

def excluir(opcao_excluir: int = 0):
    if opcao_excluir == 1:
        ctrl_hospede.excluir_hospede()
    elif opcao_excluir == 2:
        ctrl_quarto.excluir_quarto()
    elif opcao_excluir == 3:
        ctrl_reserva.excluir_reserva()

def run():
    print(tela_inicial.get_updated_screen())
    config.clear_console()

    while True:
        print(config.MENU_PRINCIPAL)
        opcao = int(input("Escolha uma opção [1-5]: "))
        config.clear_console(1)

        if opcao == 1: 
            print(config.MENU_RELATORIOS)
            opcao_relatorio = int(input("Escolha uma opção [0-4]: "))
            config.clear_console(1)
            reports(opcao_relatorio)
            config.clear_console(2)

        elif opcao == 2:  
            print(config.MENU_ENTIDADES)
            opcao_inserir = int(input("Escolha uma opção [1-3]: "))
            config.clear_console(1)
            inserir(opcao_inserir=opcao_inserir)
            config.clear_console()
            print(tela_inicial.get_updated_screen())
            config.clear_console()

        elif opcao == 3:  
            print(config.MENU_ENTIDADES)
            opcao_atualizar = int(input("Escolha uma opção [1-3]: "))
            config.clear_console(1)
            atualizar(opcao_atualizar=opcao_atualizar)
            config.clear_console()

        elif opcao == 4:  
            print(config.MENU_ENTIDADES)
            opcao_excluir = int(input("Escolha uma opção [1-3]: "))
            config.clear_console(1)
            excluir(opcao_excluir=opcao_excluir)
            config.clear_console()
            print(tela_inicial.get_updated_screen())
            config.clear_console()

        elif opcao == 5:
            print(tela_inicial.get_updated_screen())
            config.clear_console()
            print("Obrigado por utilizar o nosso sistema.")
            exit(0)
        else:
            print("Opção incorreta.")
            exit(1)

if __name__ == "__main__":
    run()
