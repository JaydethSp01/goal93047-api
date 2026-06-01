from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Proveedor(BaseModel):
    id: int
    nombre: str

fake_proveedores_db = [
    Proveedor(id=1, nombre='Proveedor A'),
    Proveedor(id=2, nombre='Proveedor B')
]

@router.get('/proveedores', response_model=List[Proveedor])
async def get_proveedores():
    return fake_proveedores_db

@router.get('/proveedores/{proveedor_id}', response_model=Proveedor)
async def get_proveedor(proveedor_id: int):
    proveedor = next((p for p in fake_proveedores_db if p.id == proveedor_id), None)
    if not proveedor:
        raise HTTPException(status_code=404, detail="Proveedor not found")
    return proveedor

@router.post('/proveedores', response_model=Proveedor)
async def create_proveedor(proveedor: Proveedor):
    fake_proveedores_db.append(proveedor)
    return proveedor

@router.put('/proveedores/{proveedor_id}', response_model=Proveedor)
async def update_proveedor(proveedor_id: int, updated_proveedor: Proveedor):
    proveedor = next((p for p in fake_proveedores_db if p.id == proveedor_id), None)
    if not proveedor:
        raise HTTPException(status_code=404, detail="Proveedor not found")
    proveedor.nombre = updated_proveedor.nombre
    return proveedor

@router.delete('/proveedores/{proveedor_id}')
async def delete_proveedor(proveedor_id: int):
    global fake_proveedores_db
    fake_proveedores_db = [p for p in fake_proveedores_db if p.id != proveedor_id]
    return {"message": "Proveedor deleted"}
