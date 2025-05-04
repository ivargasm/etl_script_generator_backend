from fastapi import APIRouter, UploadFile, File
import pandas as pd
from utils.file_loader import parse_uploaded_file

router = APIRouter(prefix="/file", tags=["File Preview"])

@router.post("/preview")
async def preview_file(file: UploadFile = File(...)):
    df = await parse_uploaded_file(file)
    return {
        "columns": df.columns.tolist(),
        "sample": df.head(10).to_dict(orient="records")
    }
