from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel
from database import SessionLocal, engine, Base
import models

app = FastAPI()

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

# Dependencia para abrir/cerrar la DB en cada request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic para validar datos de entrada
class VentaCreate(BaseModel):
    fecha: str
    producto: str
    cantidad: int
    precio: float

# Crear una venta
@app.post("/ventas/")
def create_venta(venta: VentaCreate, db: Session = Depends(get_db)):
    db_venta = models.Venta(**venta.dict())
    db.add(db_venta)
    db.commit()
    db.refresh(db_venta)
    return db_venta

# Crear varias ventas a la vez
@app.post("/ventas/bulk")
def create_ventas_bulk(ventas: List[VentaCreate], db: Session = Depends(get_db)):
    db_ventas = [models.Venta(**venta.dict()) for venta in ventas]
    db.add_all(db_ventas)
    db.commit()
    return {"insertados": len(db_ventas)}

# Obtener todas las ventas
@app.get("/ventas/")
def get_ventas(db: Session = Depends(get_db)):
    return db.query(models.Venta).all()
