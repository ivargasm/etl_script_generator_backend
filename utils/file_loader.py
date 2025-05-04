import pandas as pd
from fastapi import UploadFile
import io

async def parse_uploaded_file(file: UploadFile) -> pd.DataFrame:
    contents = await file.read()
    filename = file.filename.lower()
    if filename.endswith(".csv") or filename.endswith(".txt"):
        return pd.read_csv(io.BytesIO(contents), sep="\t" if filename.endswith(".txt") else ",")
    elif filename.endswith(".xlsx"):
        return pd.read_excel(io.BytesIO(contents))
    else:
        raise ValueError("Unsupported file type")
