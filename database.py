import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , declarative_base

# load_dotenv() lê o arquivo .env e injeta as variáveis dele em os.environ,
# como se tivessem sido definidas no ambiente antes de rodar o python.
# Se o .env não existir (ex: em produção, onde a variável já vem do painel
# do Render/Railway), load_dotenv() simplesmente não faz nada — sem erro.
load_dotenv()

# os.getenv(nome, padrao) devolve a variável de ambiente se ela existir,
# ou o valor padrão (SQLite) caso contrário — assim o projeto continua
# rodando local sem Postgres configurado, exatamente como antes.
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./labtrack.db")

# check_same_thread é um parâmetro específico do driver sqlite3: só faz
# sentido (e só é aceito) quando o banco é SQLite. Passar isso pro driver
# do Postgres geraria um erro, já que ele não reconhece esse argumento.
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()