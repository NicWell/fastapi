from fastapi import APIRouter


auth_router = APIRouter(prefix="/auth", tags=["autenticacao"])

#criando o roteador
@auth_router.get("/")
async def autenticar():
    """_summary_

    Returns:
        Essa é a rota padrão de autenticação do nosso sistema
    """
    return {"Mensagem":"Voce acessou a rota de autenticacao", "autenticado":False}