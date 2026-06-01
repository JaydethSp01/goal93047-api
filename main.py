from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import producto, categoria, talla, proveedor, stock, alerta
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=os.environ.get("CORS_ORIGINS", "*").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(producto.router)
app.include_router(categoria.router)
app.include_router(talla.router)
app.include_router(proveedor.router)
app.include_router(stock.router)
app.include_router(alerta.router)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}