from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Categoria(BaseModel):
    id: int
    nombre: str

fake_categorias_db = [
    Categoria(id=1, nombre='Hombres'),
    Categoria(id=2, nombre='Mujeres')
]

@router.get('/categorias', response_model=List[Categoria])
async def get_categorias():
    return fake_categorias_db

@router.get('/categorias/{categoria_id}', response_model=Categoria)
async def get_categoria(categoria_id: int):
    categoria = next((c for c in fake_categorias_db if c.id == categoria_id), None)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria not found")
    return categoria

@router.post('/categorias', response_model=Categoria)
async def create_categoria(categoria: Categoria):
    fake_categorias_db.append(categoria)
    return categoria

@router.put('/categorias/{categoria_id}', response_model=Categoria)
async def update_categoria(categoria_id: int, updated_categoria: Categoria):
    categoria = next((c for c in fake_categorias_db if c.id == categoria_id), None)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria not found")
    categoria.nombre = updated_categoria.nombre
    return categoria

@router.delete('/categorias/{categoria_id}')
async def delete_categoria(categoria_id: int):
    global fake_categorias_db
    fake_categorias_db = [c for c in fake_categorias_db if c.id != categoria_id]
    return {"message": "Categoria deleted"}
