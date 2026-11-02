# Projeto Aplicado I: Sistema de Calibração

Projeto acadêmico desenvolvido na unidade curricular **Projeto Aplicado I**, tendo como referência o contexto de calibração de equipamentos da empresa parceira Schulz S.A.

## Objetivo

Desenvolver progressivamente um sistema de gerenciamento de calibrações, utilizando conceitos de banco de dados relacional e Programação Orientada a Objetos.

## Tecnologias utilizadas

- **Python:** implementação das classes, regras de negócio e operações de persistência.
- **SQLite:** armazenamento relacional dos registros.
- **SQL:** criação de tabelas, inserção, consulta, atualização e relacionamentos.
- **Visual Studio Code:** ambiente de desenvolvimento.
- **Git e GitHub:** versionamento e disponibilização do projeto.

## AV02 — Estruturação do banco de dados

Nesta etapa, foram desenvolvidas a estrutura relacional do banco de dados, sua documentação e rotinas de criação e verificação.

Principais arquivos:

- `01_estrutura.md`
- `02_dicionario.md`
- `03_banco.sql`

## AV03 — Construção do MVP (Parte 1)

Implementação das classes `Tecnico`, `Equipamento`, `Medicao` e `BancoDados`, utilizando Programação Orientada a Objetos em Python e persistência SQLite.

Funcionalidades desenvolvidas:

- Cadastro de técnicos e equipamentos;
- Registro e validação de medições;
- Classificação de resultados como APROVADO ou REPROVADO;
- Consultas relacionais com INNER JOIN;
- Atualização de informações cadastrais;
- Tratamento de erros nas operações SQL;
- Geração de relatório de calibração no terminal.

Os arquivos correspondentes estão disponíveis na pasta `AV03`.

## Como executar a AV03

1. Instale o Python 3.
2. Abra um terminal na pasta `AV03`.
3. Execute:

```bash
python 05_main.py
```

O programa utiliza o banco SQLite de demonstração incluído na pasta e apresenta o resultado de uma medição no terminal.

**Observação:** cada execução registra uma nova medição de demonstração. Os cadastros existentes de técnico e equipamento são reutilizados.

## Documentação

A documentação técnica está disponível em `AV03/06_mvp_parte1.md`, acompanhada do relatório consolidado `AV03/AV03_Relatorio_Tecnico.pdf`.

## Finalidade

Projeto desenvolvido para fins acadêmicos, como exercício de aplicação de conceitos de desenvolvimento de sistemas.
