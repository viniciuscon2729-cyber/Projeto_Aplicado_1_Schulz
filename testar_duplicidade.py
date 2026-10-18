
import sqlite3
from pathlib import Path

pasta_projeto = Path(__file__).resolve().parent
arquivo_banco = pasta_projeto / "schulz_calibracao.db"

with sqlite3.connect(arquivo_banco) as conexao:

    try:
        conexao.execute("""
            INSERT INTO tecnico (
                nome_tecnico,
                matricula,
                email,
                setor
            )
            VALUES (?, ?, ?, ?);
        """, (
            "Segundo Tecnico Teste",
            "MAT-001",
            "segundo.teste@exemplo.com",
            "Metrologia"
        ))

        conexao.commit()
        print("FALHA: Matrícula duplicada foi aceita!")

    except sqlite3.IntegrityError as erro:
        conexao.rollback()
        print("TESTE APROVADO!")
        print("O SQLite impediu a matrícula duplicada.")
        print("Motivo:", erro)