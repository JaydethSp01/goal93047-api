from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Stock(BaseModel):
    id: int
    producto: str
    cantidad: int

fake_stocks_db = [
    Stock(id=1, producto='Camiseta', cantidad=100),
    Stock(id=2, producto='Jeans', cantidad=50)
]

@router.get('/stocks', response_model=List[Stock])
async def get_stocks():
    return fake_stocks_db

@router.get('/stocks/{stock_id}', response_model=Stock)
async def get_stock(stock_id: int):
    stock = next((s for s in fake_stocks_db if s.id == stock_id), None)
    if not stock:
        raise HTTPException(status_code=404, detail="Stock not found")
    return stock

@router.post('/stocks', response_model=Stock)
async def create_stock(stock: Stock):
    fake_stocks_db.append(stock)
    return stock

@router.put('/stocks/{stock_id}', response_model=Stock)
async def update_stock(stock_id: int, updated_stock: Stock):
    stock = next((s for s in fake_stocks_db if s.id == stock_id), None)
    if not stock:
        raise HTTPException(status_code=404, detail="Stock not found")
    stock.producto = updated_stock.producto
    stock.cantidad = updated_stock.cantidad
    return stock

@router.delete('/stocks/{stock_id}')
async def delete_stock(stock_id: int):
    global fake_stocks_db
    fake_stocks_db = [s for s in fake_stocks_db if s.id != stock_id]
    return {"message": "Stock deleted"}
