from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Date, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# --- CONFIGURACIÓN DE DB ---
DATABASE_URL = "postgresql+psycopg2://felipe_dev:felipe1234@localhost:5432/ventas_db_"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# --- MODELO DE TABLA ---
class Venta(Base):
    __tablename__ = "ventas"
    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date, nullable=False)
    producto = Column(String, nullable=False)
    cantidad = Column(Integer, nullable=False)
    precio = Column(Numeric(10, 2), nullable=False)

# --- SCHEMA Pydantic ---
class VentaSchema(BaseModel):
    fecha: str
    producto: str
    cantidad: int
    precio: float

    class Config:
        orm_mode = True

# --- APP FastAPI ---
app = FastAPI(title="Ventas API")

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

# --- ENDPOINTS ---
@app.get("/ventas")
def get_ventas():
    db = SessionLocal()
    ventas = db.query(Venta).all()
    db.close()
    return ventas

@app.post("/ventas")
def create_venta(venta: VentaSchema):
    db = SessionLocal()
    nueva = Venta(
        fecha=venta.fecha,
        producto=venta.producto,
        cantidad=venta.cantidad,
        precio=venta.precio
    )
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    db.close()
    return nueva

@app.get("/ventas/{venta_id}")
def get_venta(venta_id: int):
    db = SessionLocal()
    venta = db.query(Venta).filter(Venta.id == venta_id).first()
    db.close()
    if not venta:
        raise HTTPException(status_code=404, detail="Venta no encontrada")
    return venta
