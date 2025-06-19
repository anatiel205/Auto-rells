backend/main.py

from fastapi import FastAPI, HTTPException, BackgroundTasks from pydantic import BaseModel from typing import Optional from reels_worker import iniciar_bot_para_usuario import crud

app = FastAPI()

----------- MODELOS -----------

class UsuarioInput(BaseModel): nome: str token_instagram: str instagram_id: str termo_busca: str legenda_fixa: str intervalo_minutos: int

class ComandoInput(BaseModel): nome: str  # Nome do usuário

----------- ROTAS -----------

@app.post("/registrar") def registrar_usuario(usuario: UsuarioInput): if crud.usuario_existe(usuario.nome): raise HTTPException(status_code=400, detail="Usuário já existe.") crud.criar_usuario(usuario) return {"msg": "Usuário registrado com sucesso!"}

@app.post("/iniciar") def iniciar(usuario: ComandoInput, background_tasks: BackgroundTasks): dados = crud.buscar_usuario(usuario.nome) if not dados: raise HTTPException(status_code=404, detail="Usuário não encontrado.") if dados['autorizado'] == 0: raise HTTPException(status_code=403, detail="Usuário não autorizado pelo administrador.") background_tasks.add_task(iniciar_bot_para_usuario, dados) return {"msg": f"Bot do usuário {usuario.nome} iniciado."}

@app.get("/status/{nome}") def status(nome: str): usuario = crud.buscar_usuario(nome) if not usuario: raise HTTPException(status_code=404, detail="Usuário não encontrado.") return usuario

@app.post("/autorizar") def autorizar(usuario: ComandoInput): if crud.autorizar_usuario(usuario.nome): return {"msg": f"Usuário {usuario.nome} autorizado."} raise HTTPException(status_code=404, detail="Usuário não encontrado.")

@app.post("/bloquear") def bloquear(usuario: ComandoInput): if crud.bloquear_usuario(usuario.nome): return {"msg": f"Usuário {usuario.nome} bloqueado."} raise HTTPException(status_code=404, detail="Usuário não encontrado.")

