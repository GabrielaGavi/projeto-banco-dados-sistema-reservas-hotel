# 🏨 Sistema de Reservas de Hotel

Sistema de gerenciamento e reservas de hotel desenvolvido em **Python** integrado ao **Oracle Database**. O sistema oferece controle completo de hóspedes, quartos e reservas (CRUD), além de relatórios analíticos de ocupação, reservas mensais e faturamento.

---

## 👥 Integrantes do Grupo

- **Davi Pereira de Sousa**
- **Gabriela Gave Gavi**
- **José Luiz dos Santos Azeredo**
- **Pedro Henrique Bispo**
- **Pedro Henrique Ferreira Bonela**

---

## 🎥 Demonstração em Vídeo

Confira o vídeo demonstrativo do funcionamento do sistema:  
🔗 [Assistir demonstração no YouTube](https://youtu.be/sDj567Ca_x8)

---

## 🚀 Funcionalidades

### 1. Gestão de Hóspedes
- Cadastro de novos hóspedes com validação de CPF
- Consulta e listagem de hóspedes cadastrados
- Atualização de dados cadastrais (telefone, e-mail, endereço)
- Exclusão com integridade referencial

### 2. Gestão de Quartos
- Cadastro de quartos com tipo (Simples, Duplo, Suíte) e valor da diária
- Listagem e status de disponibilidade dos quartos
- Alteração de valores e categorias
- Bloqueio ou desativação de quartos

### 3. Gestão de Reservas
- Criação de reservas vinculando hóspede e quarto
- Definição de período (data de check-in e check-out)
- Cálculo automático do valor total baseado na diária e quantidade de dias
- Cancelamento e atualização de status da reserva

### 4. Relatórios Analíticos
- 📋 **Listagem Completa de Hóspedes**: Dados cadastrais e histórico.
- 📊 **Reservas por Mês**: Quantidade e volume financeiro consolidado por período.
- 📈 **Taxa de Ocupação por Quarto**: Indicadores de ocupação para gestão hoteleira.
- 📌 **Reservas por Status**: Filtro detalhado por status (Confirmada, Pendente, Cancelada, Concluída).

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem**: Python 3.10+
- **Banco de Dados**: Oracle Database
- **Driver de Conexão**: `oracledb` (v2.3.0)
- **Manipulação e Análise de Dados**: `pandas` (v2.2.2)

---

## 📁 Estrutura do Projeto

```text
projeto-banco-dados-sistema-reservas-hotel/
├── diagrams/
│   ├── DIAGRAMA_RELACIONAL_SISTEMA_RESERVAS.mmd   # Diagrama Mermaid
│   └── DIAGRAMA_RELACIONAL_SISTEMA_RESERVAS.pdf   # Modelo Relacional em PDF
├── sql/
│   ├── create_tables_hotel.sql                    # Script DDL de criação das tabelas
│   └── inserting_samples_records.sql              # Script DML com dados de exemplo
├── src/
│   ├── conexion/
│   │   └── oracle_queries.py                      # Conector e execução de queries Oracle
│   ├── controller/
│   │   ├── controller_hospede.py                  # Regras de negócio de hóspedes
│   │   ├── controller_quarto.py                   # Regras de negócio de quartos
│   │   └── controller_reserva.py                  # Regras de negócio de reservas
│   ├── model/
│   │   ├── hospede.py                             # Entidade Hóspede
│   │   ├── quarto.py                              # Entidade Quarto
│   │   └── reserva.py                             # Entidade Reserva
│   ├── reports/
│   │   └── relatorios.py                          # Geração de relatórios com pandas
│   ├── sql/                                       # Consultas SQL dos relatórios
│   ├── utils/
│   │   ├── config.py                              # Configuração de credenciais do banco
│   │   └── splash_screen.py                       # Interface de apresentação no terminal
│   ├── main.py                                    # Ponto de entrada do sistema
│   └── requirements.txt                           # Dependências do projeto
└── README.md
```

---

## ⚙️ Como Executar o Projeto

### Pré-requisitos
- Python 3 instalado
- Acesso a uma instância do Oracle Database com as tabelas criadas

### 1. Clonar o repositório
```bash
git clone https://github.com/GabrielaGavi/projeto-banco-dados-sistema-reservas-hotel.git
cd projeto-banco-dados-sistema-reservas-hotel
```

### 2. Instalar dependências
```bash
pip install -r src/requirements.txt
```

### 3. Configurar Banco de Dados
Execute os scripts contidos na pasta `sql/` no seu cliente Oracle (SQL Developer, DBeaver ou SQL*Plus):
1. `sql/create_tables_hotel.sql` (Criação de tabelas, PKs, FKs e sequences)
2. `sql/inserting_samples_records.sql` (Carga inicial de dados)

Configure as credenciais de acesso no arquivo `src/utils/config.py`.

### 4. Executar o sistema
```bash
python src/main.py
```