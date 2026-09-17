# LabTrack API

API REST para gerenciamento laboratorial: experimentos, amostras e reagentes.

Projeto em desenvolvimento, criado como parte da minha transição de carreira de Biotecnologia/Biologia Química para desenvolvimento back-end. Une meu background científico com programação, com foco em healthtech.

## Tecnologias utilizadas

- **Python**
- **FastAPI** - framework para construção da API REST
- **SQLAlchemy** - ORM para mapear classes Python em tabelas do banco de dados
- **Pydantic** - validação de dados de entrada e saída
- **SQLite** - banco de dados usado em desenvolvimento (compatível com migração futura para PostgreSQL)

## Funcionalidades

### Experiments

- `POST /experiments` - cria um experimento
- `GET /experiments` - lista todos os experimentos
- `GET /experiments/{id}` - busca um experimento específico
- `PUT /experiments/{id}` - atualiza campos de um experimento
- `DELETE /experiments/{id}` - remove um experimento

### Samples

Cada amostra é vinculada a um experimento (`experiment_id`, chave estrangeira).

- `POST /samples` - cria uma amostra, validando que o experimento referenciado existe
- `GET /samples` - lista todas as amostras
- `GET /samples/{id}` - busca uma amostra específica
- `PUT /samples/{id}` - atualiza campos de uma amostra
- `DELETE /samples/{id}` - remove uma amostra

### Reagents

- `POST /reagents` - cria um reagente
- `GET /reagents` - lista todos os reagentes
- `GET /reagents/{id}` - busca um reagente específico
- `PUT /reagents/{id}` - atualiza campos de um reagente
- `DELETE /reagents/{id}` - remove um reagente

## Status atual do projeto

Este projeto está sendo construído em etapas, como parte do meu aprendizado prático de back-end. Progresso até aqui:

- [x] Configuração inicial do FastAPI
- [x] Conexão com banco de dados via SQLAlchemy
- [x] Modelo de dados `Experiment`
- [x] Schemas Pydantic para validação (`ExperimentCreate`, `ExperimentOut`, `ExperimentUpdate`)
- [x] Rotas CRUD completas para Experimentos (POST, GET, PUT, DELETE)
- [x] Modelos de Amostra (`Sample`) e Reagente (`Reagent`)
- [x] Rotas CRUD completas para Samples e Reagents
- [x] Relacionamento entre Experimento e Amostra (chave estrangeira)
- [ ] Documentação Swagger completa (descrições e exemplos em cada rota)

### Próximos passos

- [ ] Migração do banco de dados para PostgreSQL
- [ ] Testes automatizados (pytest)
- [ ] Autenticação de usuários
- [ ] Deploy da API

## Como rodar localmente

```bash
# Clone o repositório
git clone https://github.com/LufeCovizzi/labtrack-api.git
cd labtrack-api

# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate # Windows

# Instale as dependências
pip install -r requirements.txt

# Rode a aplicação
uvicorn main:app --reload
```

A API estará disponível em `http://localhost:8000`, com documentação interativa em `http://localhost:8000/docs`.

## Autor

**Luiz Fernando Covizzi Castilho**
Desenvolvedor Back-End Python em transição de carreira, com background científico em Biotecnologia (UFU) e Mestrado em Biologia Química (UNIFESP).

- GitHub: [github.com/LufeCovizzi](https://github.com/LufeCovizzi)
- LinkedIn: [linkedin.com/in/luiz-fernando-covizzi](https://linkedin.com/in/luiz-fernando-covizzi)
