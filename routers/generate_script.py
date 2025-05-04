from fastapi import APIRouter, Body
from services.script_builder import build_etl_script
from fastapi.responses import FileResponse

router = APIRouter(prefix="/generate", tags=["Generate Script"])

@router.post("/script")
def generate_script(config: dict = Body(...)):
    script_path = build_etl_script(config)
    # return FileResponse(script_path, media_type="text/x-python", filename="generated_etl.py")
    return {"success": True, "code": script_path}
