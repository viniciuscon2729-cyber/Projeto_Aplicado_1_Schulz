import sqlite3
from pathlib import Path

# Localizar os arquivos na pasta do projeto
pasta_projeto = Path(__file__).resolve().parent
arquivo_sql = pasta_projeto / "03_banco.sql"
arquivo_banco = pasta_projeto / "schulz_calibracao.db"

try:
    with sqlite3.connect(arquivo_banco) as conexao:
        # Ativar a verificação das chaves estrangeiras
        conexao.execute("PRAGMA foreign_keys = ON;")

        # Ler o arquivo SQL
        script_sql = arquivo_sql.read_text(encoding="utf-8")

        # Executar os comandos SQL
        conexao.executescript(script_sql)

        # Consultar as tabelas criadas
        tabelas = conexao.execute("""
            SELECT name
            FROM sqlite_master
            WHERE type = 'table'
              AND name NOT LIKE 'sqlite_%'
            ORDER BY name;
        """).fetchall()

    print("Banco de dados criado com sucesso!")
    print("Tabelas encontradas:")

    for tabela in tabelas:
        print("-", tabela[0])

except (sqlite3.Error, OSError) as erro:
    print(f"ERRO ao criar o banco: {erro}")
