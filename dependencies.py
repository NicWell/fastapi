from models import db
from sqlalchemy.orm import sessionmaker #criar secao
def pegar_sessao():
    try:
        Session = sessionmaker(bind=db) #localiza o banco
        session = Session() #cria a secao
        yield session #envia o retorno da criação da seççao
    finally:
        session.close()