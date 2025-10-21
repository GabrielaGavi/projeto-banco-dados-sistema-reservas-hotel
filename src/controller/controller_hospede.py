from model.hospede import Hospede
from conexion.oracle_queries import OracleQueries
from datetime import datetime

class Controller_Hospede:
    def __init__(self):
        pass
        
    def inserir_hospede(self) -> Hospede:
        
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        
        cpf = input("CPF (Novo): ")

        if self.verifica_existencia_hospede(oracle, cpf):
            nome = input("Nome (Novo): ")
            telefone = input("Telefone (Novo): ")
            data_cadastro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            
            oracle.write(f"""
                INSERT INTO hospede (cpf, nome, telefone, data_cadastro)
                VALUES ('{cpf}', '{nome}', '{telefone}', TO_DATE('{data_cadastro}', 'YYYY-MM-DD HH24:MI:SS'))
            """)

            
            df_hospede = oracle.sqlToDataFrame(f"SELECT cpf, nome, telefone, data_cadastro FROM hospede WHERE cpf = '{cpf}'")
            novo_hospede = Hospede(
                df_hospede.cpf.values[0],
                df_hospede.nome.values[0],
                df_hospede.telefone.values[0],
                str(df_hospede.data_cadastro.values[0])
            )
            print("\nHóspede inserido com sucesso!\n")
            print(novo_hospede.to_string())
            return novo_hospede
        else:
            print(f"\nO CPF {cpf} já está cadastrado.\n")
            return None

    def atualizar_hospede(self) -> Hospede:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        cpf = input("CPF do hóspede que deseja atualizar: ")

        if not self.verifica_existencia_hospede(oracle, cpf):
            nome = input("Novo nome: ")
            telefone = input("Novo telefone: ")
            data_cadastro = input("Nova data de cadastro (AAAA-MM-DD): ")

            oracle.write(f"""
                UPDATE hospede
                SET nome = '{nome}', telefone = '{telefone}', data_cadastro = TO_DATE('{data_cadastro}', 'YYYY-MM-DD')
                WHERE cpf = '{cpf}'
            """)

            df_hospede = oracle.sqlToDataFrame(f"SELECT cpf, nome, telefone, data_cadastro FROM hospede WHERE cpf = '{cpf}'")
            hospede_atualizado = Hospede(
                df_hospede.cpf.values[0],
                df_hospede.nome.values[0],
                df_hospede.telefone.values[0],
                str(df_hospede.data_cadastro.values[0])
            )
            print("\nHóspede atualizado com sucesso!\n")
            print(hospede_atualizado.to_string())
            return hospede_atualizado
        else:
            print(f"\nO CPF {cpf} não existe.\n")
            return None

    def excluir_hospede(self):
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        cpf = input("CPF do hóspede que deseja excluir: ")

        if not self.verifica_existencia_hospede(oracle, cpf):
            df_hospede = oracle.sqlToDataFrame(f"SELECT cpf, nome, telefone, data_cadastro FROM hospede WHERE cpf = '{cpf}'")
            oracle.write(f"DELETE FROM hospede WHERE cpf = '{cpf}'")

            hospede_excluido = Hospede(
                df_hospede.cpf.values[0],
                df_hospede.nome.values[0],
                df_hospede.telefone.values[0],
                str(df_hospede.data_cadastro.values[0])
            )
            print("\nHóspede removido com sucesso!\n")
            print(hospede_excluido.to_string())
        else:
            print(f"\nO CPF {cpf} não existe.\n")

    def verifica_existencia_hospede(self, oracle: OracleQueries, cpf: str = None) -> bool:
        df_hospede = oracle.sqlToDataFrame(f"SELECT cpf FROM hospede WHERE cpf = '{cpf}'")
        return df_hospede.empty
