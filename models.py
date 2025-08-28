from sqlalchemy import Column, Integer, String, Float, Date
from database import Base

class Venta(Base):
    __tablename__ = "ventas"

    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date, index=True)  # si quieres exactitud usa Date
    producto = Column(String, index=True)
    cantidad = Column(Integer)
    precio = Column(Float)