from fastapi import APIRouter
from models import Usuario, db
from sqlalchemy.orm import sessionmaker #criar secao
auth_router = APIRouter(prefix="/auth", tags=["autenticacao"])

#criando o roteador
@auth_router.get("/")
async def home():
    """_summary_

    Returns:
        Essa é a rota padrão de autenticação do nosso sistema
    """
    return {"Mensagem":"Voce acessou a rota de autenticacao", "autenticado":False}

@auth_router.post("/criar_conta")
async def criar_conta(email:str,senha:str, nome: str):
    Session = sessionmaker(bind=db) #localiza o banco
    session = Session() #cria a secao
    usuario = session.query(Usuario).filter(Usuario.email==email).first()
    if usuario:
        return {"mensagem":"o email ja foi utilizado por outro usuario"}
    else: 
        novo_usuario = Usuario(nome,email,senha)
        session.add(novo_usuario)
        session.commit()
        return{"mensagem":"Usuario Cadastrado com Sucesso"}