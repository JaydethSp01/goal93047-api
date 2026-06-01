from pydantic import BaseModel

class Producto(BaseModel):
    id: int
    nombre: str
    precio: float
    categoria_id: int

class Categoria(BaseModel):
    id: int
    nombre: str

# Add models for Talla, Proveedor, Stock, Alerta as needed