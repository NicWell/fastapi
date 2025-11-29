from fastapi import APIRouter, Depends, HTTPException
from models import Usuario, db
from dependencies import pegar_sessao
from sqlalchemy.orm import sessionmaker #criar secao
from main import bcrypt_context
from schemas import UsuarioSchema
from sqlalchemy.orm import Session
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
async def criar_conta(usuario_schema:UsuarioSchema, session:Session=Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email==usuario_schema.email).first()
    if usuario:
        raise HTTPException(status_code=400,detail='E-mail ja cadastrado')
    else:
        senha_criptografada = bcrypt_context.hash(usuario_schema.senha) 
        novo_usuario = Usuario(usuario_schema.nome,usuario_schema.email,senha_criptografada, usuario_schema.ativo, usuario_schema.admin) 
        #cria um novo usuario
        session.add(novo_usuario)
        session.commit()
        return{"mensagem":f"Usuario Cadastrado com Sucesso, {usuario_schema.email}"}