from fastapi import FastAPI, Depends
from .dependencies import get_file_storage
from soundmesh_core.abstractions import FileStorage

app = FastAPI()

@app.get("/files/")
async def get_file_metadata(file_path:str, storage: FileStorage = Depends(get_file_storage)):
    """Возвращает метаданные файла по его пути и названию

    Args:
        file_path (str): путь к файлу
        storage (FileStorage, optional): _description_. Defaults to Depends(get_file_storage).

    Returns:
        _type_: метаданные файла в виде словаря
    """    
    content = storage.get_file(file_path)
    return {"file_name": content.metadata.name, 
            "extension": content.metadata.extension, 
            "file_size": content.metadata.size}