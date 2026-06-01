from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Alerta(BaseModel):
    id: int
    descripcion: str

fake_alertas_db = [
    Alerta(id=1, descripcion='Stock bajo de camisetas'),
    Alerta(id=2, descripcion='Stock bajo de jeans')
]

@router.get('/alertas', response_model=List[Alerta])
async def get_alertas():
    return fake_alertas_db

@router.get('/alertas/{alerta_id}', response_model=Alerta)
async def get_alerta(alerta_id: int):
    alerta = next((a for a in fake_alertas_db if a.id == alerta_id), None)
    if not alerta:
        raise HTTPException(status_code=404, detail="Alerta not found")
    return alerta

@router.post('/alertas', response_model=Alerta)
async def create_alerta(alerta: Alerta):
    fake_alertas_db.append(alerta)
    return alerta

@router.put('/alertas/{alerta_id}', response_model=Alerta)
async def update_alerta(alerta_id: int, updated_alerta: Alerta):
    alerta = next((a for a in fake_alertas_db if a.id == alerta_id), None)
    if not alerta:
        raise HTTPException(status_code=404, detail="Alerta not found")
    alerta.descripcion = updated_alerta.descripcion
    return alerta

@router.delete('/alertas/{alerta_id}')
async def delete_alerta(alerta_id: int):
    global fake_alertas_db
    fake_alertas_db = [a for a in fake_alertas_db if a.id != alerta_id]
    return {"message": "Alerta deleted"}
