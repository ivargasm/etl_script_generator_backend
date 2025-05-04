from fastapi import FastAPI
from routers import generate_script, file_preview
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="ETL Script Generator API")

# Habilitar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://etl-script-generator-frontend.vercel.app"
    ],  # Orígenes permitidos (Frontend)
    # allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # Métodos permitidos (GET, POST, etc.)
    allow_headers=["*"],  # Encabezados permitidos
)

app.include_router(generate_script.router)
app.include_router(file_preview.router)
