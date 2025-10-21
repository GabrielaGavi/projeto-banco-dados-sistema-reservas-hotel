from model.reserva import Reserva
from model.hospede import Hospede
from model.quarto import Quarto
from conexion.oracle_queries import OracleQueries

class Controller_Reserva:
    def __init__(self):
        pass

    def inserir_reserva(self) -> Reserva:
        

        oracle = OracleQueries(can_write=True)
        oracle.connect()

        id_reserva = input("ID da reserva (Novo): ")

        if self.verifica_existencia_reserva(oracle, id_reserva):
            cpf = input("CPF do hóspede: ")
            numero_quarto = input("Número do quarto: ")

            
            df_hospede = oracle.sqlToDataFrame(f"SELECT * FROM hospede WHERE cpf = '{cpf}'")
            df_quarto = oracle.sqlToDataFrame(f"SELECT * FROM quarto WHERE numero_quarto = {numero_quarto}")

            if df_hospede.empty:
                print(f"\nNão existe hóspede com CPF {cpf}.\n")
                return None
            if df_quarto.empty:
                print(f"\nNão existe quarto número {numero_quarto}.\n")
                return None

            data_checkin = input("Data de check-in (AAAA-MM-DD): ")
            data_checkout = input("Data de check-out (AAAA-MM-DD): ")
            qtd_hospedes = input("Quantidade de hóspedes: ")
            valor_total = input("Valor total: ")
            status = input("Status da reserva (ativa/cancelada/finalizada): ")
            criado_em = input("Data de criação (AAAA-MM-DD): ")

            oracle.write(f"""
                INSERT INTO reserva (
                    id_reserva, cpf, numero_quarto, data_checkin,
                    data_checkout, qtd_hospedes, valor_total, status, criado_em
                )
                VALUES (
                    {id_reserva}, '{cpf}', {numero_quarto},
                    TO_DATE('{data_checkin}', 'YYYY-MM-DD'),
                    TO_DATE('{data_checkout}', 'YYYY-MM-DD'),
                    {qtd_hospedes}, {valor_total}, '{status}',
                    TO_DATE('{criado_em}', 'YYYY-MM-DD')
                )
            """)

            df_reserva = oracle.sqlToDataFrame(f"""
                SELECT id_reserva, cpf, numero_quarto, data_checkin, data_checkout,
                       qtd_hospedes, valor_total, status, criado_em
                FROM reserva
                WHERE id_reserva = {id_reserva}
            """)

            hospede = Hospede(df_hospede.cpf.values[0], df_hospede.nome.values[0], df_hospede.telefone.values[0], str(df_hospede.data_cadastro.values[0]))
            quarto = Quarto(df_quarto.numero_quarto.values[0], df_quarto.tipo.values[0], df_quarto.valor_diaria.values[0], df_quarto.status.values[0])

            nova_reserva = Reserva(
                df_reserva.id_reserva.values[0],
                hospede,
                quarto,
                str(df_reserva.data_checkin.values[0]),
                str(df_reserva.data_checkout.values[0]),
                df_reserva.qtd_hospedes.values[0],
                df_reserva.valor_total.values[0],
                df_reserva.status.values[0],
                str(df_reserva.criado_em.values[0])
            )

            print("\nReserva criada com sucesso!\n")
            print(nova_reserva.to_string())
            return nova_reserva
        else:
            print(f"\nJá existe uma reserva com ID {id_reserva}.\n")
            return None

    def atualizar_reserva(self) -> Reserva:
        

        oracle = OracleQueries(can_write=True)
        oracle.connect()

        id_reserva = input("ID da reserva que deseja atualizar: ")

        if not self.verifica_existencia_reserva(oracle, id_reserva):
            cpf = input("Novo CPF do hóspede: ")
            numero_quarto = input("Novo número do quarto: ")

            df_hospede = oracle.sqlToDataFrame(f"SELECT * FROM hospede WHERE cpf = '{cpf}'")
            df_quarto = oracle.sqlToDataFrame(f"SELECT * FROM quarto WHERE numero_quarto = {numero_quarto}")

            if df_hospede.empty:
                print(f"\nNão existe hóspede com CPF {cpf}.\n")
                return None
            if df_quarto.empty:
                print(f"\nNão existe quarto número {numero_quarto}.\n")
                return None

            data_checkin = input("Nova data de check-in (AAAA-MM-DD): ")
            data_checkout = input("Nova data de check-out (AAAA-MM-DD): ")
            qtd_hospedes = input("Nova quantidade de hóspedes: ")
            valor_total = input("Novo valor total: ")
            status = input("Novo status: ")

            oracle.write(f"""
                UPDATE reserva
                SET cpf = '{cpf}', numero_quarto = {numero_quarto},
                    data_checkin = TO_DATE('{data_checkin}', 'YYYY-MM-DD'),
                    data_checkout = TO_DATE('{data_checkout}', 'YYYY-MM-DD'),
                    qtd_hospedes = {qtd_hospedes},
                    valor_total = {valor_total},
                    status = '{status}'
                WHERE id_reserva = {id_reserva}
            """)

            df_reserva = oracle.sqlToDataFrame(f"""
                SELECT id_reserva, cpf, numero_quarto, data_checkin, data_checkout,
                       qtd_hospedes, valor_total, status, criado_em
                FROM reserva
                WHERE id_reserva = {id_reserva}
            """)

            hospede = Hospede(df_hospede.cpf.values[0], df_hospede.nome.values[0], df_hospede.telefone.values[0], str(df_hospede.data_cadastro.values[0]))
            quarto = Quarto(df_quarto.numero_quarto.values[0], df_quarto.tipo.values[0], df_quarto.valor_diaria.values[0], df_quarto.status.values[0])

            reserva_atualizada = Reserva(
                df_reserva.id_reserva.values[0],
                hospede,
                quarto,
                str(df_reserva.data_checkin.values[0]),
                str(df_reserva.data_checkout.values[0]),
                df_reserva.qtd_hospedes.values[0],
                df_reserva.valor_total.values[0],
                df_reserva.status.values[0],
                str(df_reserva.criado_em.values[0])
            )

            print("\nReserva atualizada com sucesso!\n")
            print(reserva_atualizada.to_string())
            return reserva_atualizada
        else:
            print(f"\nA reserva {id_reserva} não existe.\n")
            return None

    def excluir_reserva(self):
        

        oracle = OracleQueries(can_write=True)
        oracle.connect()

        id_reserva = input("ID da reserva que deseja excluir: ")

        if not self.verifica_existencia_reserva(oracle, id_reserva):
            df_reserva = oracle.sqlToDataFrame(f"SELECT * FROM reserva WHERE id_reserva = {id_reserva}")
            oracle.write(f"DELETE FROM reserva WHERE id_reserva = {id_reserva}")

            print("\nReserva removida com sucesso!\n")
            print(df_reserva)
        else:
            print(f"\nA reserva {id_reserva} não existe.\n")

    def verifica_existencia_reserva(self, oracle: OracleQueries, id_reserva: int = None) -> bool:
        
        df_reserva = oracle.sqlToDataFrame(f"SELECT id_reserva FROM reserva WHERE id_reserva = {id_reserva}")
        return df_reserva.empty
