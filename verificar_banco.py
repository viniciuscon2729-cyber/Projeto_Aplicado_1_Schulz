
import sqlite3
from pathlib import Path

# Localizar o banco de dados
pasta_projeto = Path(__file__).resolve().parent
arquivo_banco = pasta_projeto / "schulz_calibracao.db"

# Conectar ao banco existente
with sqlite3.connect(arquivo_banco) as conexao:
    conexao.execute("PRAGMA foreign_keys = ON;")

    # Verificar as chaves estrangeiras da tabela medicao
    chaves = conexao.execute(
        "PRAGMA foreign_key_list(medicao);"
    ).fetchall()

    print("CHAVES ESTRANGEIRAS DA TABELA MEDICAO:")

    for chave in chaves:
        print(f"Tabela relacionada: {chave[2]}")
        print(f"Campo de origem: {chave[3]}")
        print(f"Campo de destino: {chave[4]}")
        print("-" * 40)

    # Verificar problemas de integridade referencial
    problemas = conexao.execute(
        "PRAGMA foreign_key_check;"
    ).fetchall()

    if not problemas:
        print("Nenhuma violação de chave estrangeira encontrada.")
    else:
        print("Violações encontradas:", problemas)