from fastapi import FastAPI, Depends
from .dependencies import get_file_storage
from soundmesh_core.abstractions import FileStorage

app = FastAPI()

@app.get("/files/")
async def get_file(file_path:str, storage: FileStorage = Depends(get_file_storage)):
    content = storage.get_file(file_path)
    return {"file_name": content.metadata.name, 
            "extension": content.metadata.extension, 
            "file_size": content.metadata.size}