from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Producto(BaseModel):
    id: int
    nombre: str
    precio: float

fake_productos_db = [
    Producto(id=1, nombre='Camiseta', precio=19.99),
    Producto(id=2, nombre='Jeans', precio=39.99)
]

@router.get('/productos', response_model=List[Producto])
async def get_productos():
    return fake_productos_db

@router.get('/productos/{producto_id}', response_model=Producto)
async def get_producto(producto_id: int):
    producto = next((p for p in fake_productos_db if p.id == producto_id), None)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto not found")
    return producto

@router.post('/productos', response_model=Producto)
async def create_producto(producto: Producto):
    fake_productos_db.append(producto)
    return producto

@router.put('/productos/{producto_id}', response_model=Producto)
async def update_producto(producto_id: int, updated_producto: Producto):
    producto = next((p for p in fake_productos_db if p.id == producto_id), None)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto not found")
    producto.nombre = updated_producto.nombre
    producto.precio = updated_producto.precio
    return producto

@router.delete('/productos/{producto_id}')
async def delete_producto(producto_id: int):
    global fake_productos_db
    fake_productos_db = [p for p in fake_productos_db if p.id != producto_id]
    return {"message": "Producto deleted"}
