
# UNIDADE CURRICULAR: PROJETO APLICADO I
# SCRIPT DE GERAÇÃO DO DICIONÁRIO DE DADOS
# Prof. MSc. Hugo Menezes Barra | Prof. Rodrigo Losina

conteudo_dicionario = """# 02_dicionario.md — Dicionário de Dados do Sistema
**Unidade Curricular:** Projeto Aplicado I
**Empresa Parceira:** Schulz S.A.
**Tema 02:** Modelagem e Implementação de Banco de Dados (SQLite)
**Professores:** Prof. MSc. Hugo Menezes Barra | Prof. Rodrigo Losina

---

## 1. Mapeamento das Tabelas e Campos

### 1.1. Tabela: `tecnico` (Técnicos / Solicitantes)
| Nome do Campo | Tipo (SQLite) | Restrições / Chaves | Descrição / Regra de Negócio |
| :--- | :--- | :--- | :--- |
| `id_tecnico` | INTEGER | PRIMARY KEY AUTOINCREMENT | Identificador único do técnico. |
| `nome_tecnico` | TEXT | NOT NULL | Nome completo do profissional. |
| `matricula` | TEXT | NOT NULL, UNIQUE | Matrícula única do técnico. |
| `email` | TEXT | NOT NULL | E-mail do profissional. |
| `setor` | TEXT | NOT NULL | Setor de atuação do profissional. |
| :--- | :--- | :--- | :--- |
### 1.2. Tabela: `equipamento` (Instrumentos e Máquinas)
| Nome do Campo | Tipo (SQLite) | Restrições / Chaves | Descrição / Regra de Negócio |
| :--- | :--- | :--- | :--- |
| `id_equipamento` | INTEGER | PRIMARY KEY AUTOINCREMENT | Identificador único do equipamento.
|
| `codigo_tag` | TEXT | NOT NULL, UNIQUE | Código/Tag gravado no instrumento. |
| `nome_equipamento`| TEXT | NOT NULL | Descrição do equipamento (Ex: Paquímetro). |
| `fabricante` | TEXT | NOT NULL | Fabricante (Ex: Mitutoyo, Starrett). |
| `modelo` | TEXT | NOT NULL | Modelo do instrumento. |
| :--- | :--- | :--- | :--- |
### 1.3. Tabela: `medicao` (Registro das Calibrações / Ensaios)
| Nome do Campo | Tipo (SQLite) | Restrições / Chaves | Descrição / Regra de Negócio |
| :--- | :--- | :--- | :--- |
| `id_medicao` | INTEGER | PRIMARY KEY AUTOINCREMENT | Identificador único da medição. |
| `id_equipamento` | INTEGER | NOT NULL, FOREIGN KEY | Identifica o equipamento medido. |
| `id_tecnico` | INTEGER | NOT NULL, FOREIGN KEY | Identifica o técnico responsável. |
| `parametro_medido` | TEXT | NOT NULL | Característica avaliada na medição. |
| `valor_nominal` | REAL | NOT NULL | Valor de referência da característica. |
| `tolerancia_min` | REAL | NOT NULL | Limite inferior informado para a avaliação. |
| `tolerancia_max` | REAL | NOT NULL | Limite superior informado para a avaliação. |
| `valor_obtido` | REAL | NOT NULL | Resultado numérico da medição. |
| `status_resultado` | TEXT | NOT NULL, CHECK | Status restrito a APROVADO ou REPROVADO. |
| `data_medicao` | DATETIME | DEFAULT CURRENT_TIMESTAMP | Data e hora do registro, preenchidas automaticamente por padrão. |

"""

nome_arquivo = "02_dicionario.md"

try:
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo_dicionario)

    print("=" * 60)
    print(f"SUCESSO: Arquivo '{nome_arquivo}' criado com sucesso!")
    print("=" * 60)

except Exception as e:
    print(f"ERRO ao criar arquivo: {e}")
