# ETL Script Generator - Backend

Este es el backend del generador de scripts ETL, construido con FastAPI.

## Tecnologías utilizadas

- FastAPI
- Pydantic
- Uvicorn

## Instalación

```bash
python -m venv venv
source venv/bin/activate  # en Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## Endpoints principales

- `POST /generate/script`: Recibe la configuración en JSON y genera un script Python.

## Deploy

Puedes desplegarlo en Render, Railway o cualquier servicio compatible con FastAPI.

