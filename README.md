# 📊 API de Ventas con FastAPI y PostgreSQL

Este proyecto es una **API RESTful** construida con [FastAPI](https://fastapi.tiangolo.com/) y [PostgreSQL](https://www.postgresql.org/), desplegada en [Render](https://render.com/).  
Permite **gestionar ventas**, almacenarlas en una base de datos relacional y consultarlas mediante endpoints.

---

## 🚀 Tecnologías utilizadas
- **FastAPI** → Framework web para la API  
- **PostgreSQL** → Base de datos relacional  
- **SQLAlchemy** → ORM para manejar modelos y consultas  
- **Uvicorn** → Servidor ASGI  
- **Render** → Hosting de la API  

---

## 📂 Estructura del proyecto

├── main.py # Punto de entrada de la aplicación
├── models.py # Modelos de la base de datos
├── schemas.py # Esquemas Pydantic para validación
├── database.py # Conexión a PostgreSQL
├── requirements.txt # Dependencias del proyecto
└── README.md # Documentación


---

## 🔑 Endpoints principales

### ➤ Crear ventas en lote
`POST /ventas/bulk`

Ejemplo de request:
```bash
curl -X POST https://postgreapi-7h0v.onrender.com/ventas/bulk \
  -H "Content-Type: application/json" \
  -d '[
    {"producto": "Laptop", "categoria": "Electrónica", "precio": 1200, "cantidad": 2, "fecha": "2025-08-01"},
    {"producto": "Camiseta", "categoria": "Ropa", "precio": 25, "cantidad": 5, "fecha": "2025-08-03"}
  ]'
'
```

### ➤ Listar todas las ventas
`GET /ventas`

Ejemplo de request:
```bash
curl https://TU-API.onrender.com/ventas
```

🛠️ Instalación local

Clonar el repositorio:

git clone https://github.com/TU-USUARIO/fastapi-ventas-api.git
cd fastapi-ventas-api


Crear un entorno virtual (opcional pero recomendado):

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows


Instalar dependencias:

pip install -r requirements.txt


Ejecutar el servidor:

uvicorn main:app --reload


Abrir en navegador:

http://127.0.0.1:8000/docs

🌐 Demo en línea

https://postgreapi-7h0v.onrender.com/docs

👨‍💻 Autor

Felipe Toro

Data Analyst & Developer

Enfoque en automatización, análisis de datos y desarrollo de APIs




