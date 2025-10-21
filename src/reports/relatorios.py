from conexion.oracle_queries import OracleQueries

class Relatorios:
    def __init__(self):
        self.oracle = OracleQueries()

    def executar_relatorio(self, caminho_sql: str):
        
        with open(caminho_sql, "r") as f:
            query = f.read()
        self.oracle.connect()
        df = self.oracle.sqlToDataFrame(query)
        print(df)
        return df

    def relatorio_reservas_por_status(self):
        print("\n### RELATÓRIO DE RESERVAS POR STATUS ###")
        return self.executar_relatorio("src/sql/relatorio_reservas_por_status.sql")

    def relatorio_reservas_detalhado(self):
        print("\n### RELATÓRIO DE RESERVAS DETALHADO ###")
        return self.executar_relatorio("src/sql/relatorio_reservas_detalhado.sql")

    def relatorio_reservas_por_mes(self):
        print("\n### RELATÓRIO DE RESERVAS POR MÊS ###")
        return self.executar_relatorio("src/sql/relatorio_reservas_por_mes.sql")

    def relatorio_hospedes(self):
        print("\n### RELATÓRIO DE HÓSPEDES ###")
        return self.executar_relatorio("src/sql/relatorio_hospedes.sql")
