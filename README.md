# 🧪 LabTrack API

API REST para gerenciamento laboratorial: experimentos, amostras e reagentes.

Projeto em desenvolvimento, criado como parte da minha transição de carreira de Biotecnologia/Biologia Química para desenvolvimento back-end. Une meu background científico com programação, com foco em healthtech.

## 🚀 Tecnologias utilizadas

- **Python**
- **FastAPI** — framework para construção da API REST
- **SQLAlchemy** — ORM para mapear classes Python em tabelas do banco de dados
- **Pydantic** — validação de dados de entrada e saída
- **SQLite** — banco de dados usado em desenvolvimento (compatível com migração futura para PostgreSQL)

## 📋 Status atual do projeto

Este projeto está sendo construído em etapas, como parte do meu aprendizado prático de back-end. Progresso até aqui:

- [x] Configuração inicial do FastAPI
- [x] Conexão com banco de dados via SQLAlchemy
- [x] Modelo de dados `Experiment`
- [x] Schemas Pydantic para validação (`ExperimentCreate`, `ExperimentOut`)
- [ ] Rotas CRUD completas para Experimentos
- [ ] Modelos de Amostra (`Sample`) e Reagente (`Reagent`)
- [ ] Relacionamento entre Experimento e Amostra
- [ ] Documentação Swagger completa

## ⚙️ Como rodar localmente

```bash
# Clone o repositório
git clone https://github.com/LufeCovizzi/labtrack-api.git
cd labtrack-api

# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate      # Windows

# Instale as dependências
pip install fastapi uvicorn sqlalchemy

# Rode a aplicação
uvicorn main:app --reload
```

A API estará disponível em `http://localhost:8000`, com documentação interativa em `http://localhost:8000/docs`.

## 👤 Autor

**Luiz Fernando Covizzi Castilho**
Desenvolvedor Back-End Python em transição de carreira, com background científico em Biotecnologia (UFU) e Mestrado em Biologia Química (UNIFESP).

- GitHub: [github.com/LufeCovizzi](https://github.com/LufeCovizzi)
- LinkedIn: [linkedin.com/in/luiz-fernando-covizzi](https://linkedin.com/in/luiz-fernando-covizzi)