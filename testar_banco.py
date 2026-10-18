
import sqlite3
from pathlib import Path

# Localizar o banco de dados
pasta_projeto = Path(__file__).resolve().parent
arquivo_banco = pasta_projeto / "schulz_calibracao.db"

# Verificar se o banco existe
if not arquivo_banco.exists():
    raise FileNotFoundError("Banco de dados não encontrado.")

# Conectar ao banco SQLite
with sqlite3.connect(arquivo_banco) as conexao:

    # Ativar as chaves estrangeiras
    conexao.execute("PRAGMA foreign_keys = ON;")

    # TESTE 01 - Cadastrar um técnico fictício
    conexao.execute("""
        INSERT OR IGNORE INTO tecnico
        (nome_tecnico, matricula, email, setor)
        VALUES (?, ?, ?, ?);
    """, (
        "Tecnico Teste",
        "MAT-001",
        "tecnico.teste@exemplo.com",
        "Metrologia"
    ))

    # TESTE 02 - Cadastrar um equipamento fictício
    conexao.execute("""
        INSERT OR IGNORE INTO equipamento
        (codigo_tag, nome_equipamento, fabricante, modelo)
        VALUES (?, ?, ?, ?);
    """, (
        "EQ-001",
        "Paquimetro Digital",
        "Fabricante Teste",
        "Modelo A"
    ))

    # Recuperar os identificadores cadastrados
    id_tecnico = conexao.execute("""
        SELECT id_tecnico
        FROM tecnico
        WHERE matricula = 'MAT-001';
    """).fetchone()[0]

    id_equipamento = conexao.execute("""
        SELECT id_equipamento
        FROM equipamento
        WHERE codigo_tag = 'EQ-001';
    """).fetchone()[0]

    # TESTE 03 - Registrar uma medição fictícia
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
        id_equipamento,
        id_tecnico,
        "Comprimento",
        10.0,
        9.9,
        10.1,
        10.02,
        "APROVADO"
    ))

    conexao.commit()

    # Consultar os registros inseridos
    resultados = conexao.execute("""
        SELECT
            m.id_medicao,
            t.nome_tecnico,
            e.nome_equipamento,
            m.parametro_medido,
            m.valor_obtido,
            m.status_resultado
        FROM medicao AS m
        JOIN tecnico AS t
            ON m.id_tecnico = t.id_tecnico
        JOIN equipamento AS e
            ON m.id_equipamento = e.id_equipamento;
    """).fetchall()

    print("RESULTADOS DOS TESTES:")

    for resultado in resultados:
        print(resultado)

print("Testes de inserção executados com sucesso!")