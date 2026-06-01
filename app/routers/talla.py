from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Talla(BaseModel):
    id: int
    nombre: str

fake_tallas_db = [
    Talla(id=1, nombre='S'),
    Talla(id=2, nombre='M'),
    Talla(id=3, nombre='L')
]

@router.get('/tallas', response_model=List[Talla])
async def get_tallas():
    return fake_tallas_db

@router.get('/tallas/{talla_id}', response_model=Talla)
async def get_talla(talla_id: int):
    talla = next((t for t in fake_tallas_db if t.id == talla_id), None)
    if not talla:
        raise HTTPException(status_code=404, detail="Talla not found")
    return talla

@router.post('/tallas', response_model=Talla)
async def create_talla(talla: Talla):
    fake_tallas_db.append(talla)
    return talla

@router.put('/tallas/{talla_id}', response_model=Talla)
async def update_talla(talla_id: int, updated_talla: Talla):
    talla = next((t for t in fake_tallas_db if t.id == talla_id), None)
    if not talla:
        raise HTTPException(status_code=404, detail="Talla not found")
    talla.nombre = updated_talla.nombre
    return talla

@router.delete('/tallas/{talla_id}')
async def delete_talla(talla_id: int):
    global fake_tallas_db
    fake_tallas_db = [t for t in fake_tallas_db if t.id != talla_id]
    return {"message": "Talla deleted"}
