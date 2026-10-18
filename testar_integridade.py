
import sqlite3
from pathlib import Path

pasta_projeto = Path(__file__).resolve().parent
arquivo_banco = pasta_projeto / "schulz_calibracao.db"

with sqlite3.connect(arquivo_banco) as conexao:

    # Ativar a integridade referencial
    conexao.execute("PRAGMA foreign_keys = ON;")

    try:
        # Tentar inserir uma medição com equipamento inexistente
        conexao.execute("""
            INSERT INTO medicao (
                id_equipamento,
                id_tecnico,
                parametro_medido,
                valor_nominal,
                tolerancia_min,
                tolerancia_max,
                valor_obtido,
                status_resultado
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?);
        """, (
            -999,
            1,
            "Comprimento",
            10.0,
            9.9,
            10.1,
            10.02,
            "APROVADO"
        ))

        conexao.commit()
        print("FALHA: A medição inválida foi inserida!")

    except sqlite3.IntegrityError as erro:
        conexao.rollback()
        print("TESTE APROVADO!")
        print("O SQLite bloqueou a medição inválida.")
        print("Motivo:", erro)