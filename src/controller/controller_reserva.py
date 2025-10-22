from datetime import datetime
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

        cpf = input("CPF do hóspede: ")
        numero_quarto = int(input("Número do quarto: "))
        data_checkin = input("Data de check-in (YYYY-MM-DD): ")
        data_checkout = input("Data de check-out (YYYY-MM-DD): ")
        qtd_hospedes = int(input("Quantidade de hóspedes: "))
        status = input("Status (Ativa, Finalizada, Cancelada): ")

       
        df_hospede = oracle.sqlToDataFrame(f"SELECT * FROM hospede WHERE cpf = '{cpf}'")
        if df_hospede.empty:
            print(f"O hóspede com CPF {cpf} não existe.")
            return None
        hospede = Hospede(
            df_hospede.cpf.values[0],
            df_hospede.nome.values[0],
            df_hospede.telefone.values[0],
            str(df_hospede.data_cadastro.values[0])
        )

        df_quarto = oracle.sqlToDataFrame(f"SELECT * FROM quarto WHERE numero_quarto = {numero_quarto}")
        if df_quarto.empty:
            print(f"O quarto {numero_quarto} não existe.")
            return None
        quarto = Quarto(
            df_quarto.numero_quarto.values[0],
            df_quarto.tipo.values[0],
            df_quarto.valor_diaria.values[0],
            df_quarto.status.values[0]
        )

        
        checkin = datetime.strptime(data_checkin, "%Y-%m-%d")
        checkout = datetime.strptime(data_checkout, "%Y-%m-%d")
        dias = (checkout - checkin).days
        if dias <= 0:
            print("A data de check-out deve ser posterior à data de check-in.")
            return None

        valor_total = dias * quarto.get_valor_diaria()

        oracle.write(f"""
            INSERT INTO reserva (
                id_reserva, cpf, numero_quarto, data_checkin, data_checkout,
                qtd_hospedes, valor_total, status, criado_em
            ) VALUES (
                reserva_seq.NEXTVAL,
                '{cpf}', {numero_quarto},
                TO_DATE('{data_checkin}', 'YYYY-MM-DD'),
                TO_DATE('{data_checkout}', 'YYYY-MM-DD'),
                {qtd_hospedes}, {valor_total}, '{status}', SYSTIMESTAMP
            )
        """)

        df_reserva = oracle.sqlToDataFrame("""
            SELECT * FROM (
                SELECT * FROM reserva ORDER BY id_reserva DESC
            ) WHERE ROWNUM = 1
        """)

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

        print("\nReserva criada com sucesso!")
        print(nova_reserva.to_string())
        return nova_reserva

    def verifica_existencia_reserva(self, oracle: OracleQueries, id_reserva: int) -> bool:
        df = oracle.sqlToDataFrame(f"SELECT id_reserva FROM reserva WHERE id_reserva = {id_reserva}")
        return not df.empty
