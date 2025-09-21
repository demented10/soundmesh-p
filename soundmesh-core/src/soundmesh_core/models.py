from pydantic import BaseModel

class FileMetadata(BaseModel):
    name: str

class FileResponse(BaseModel):
    content: bytes
    metadata: FileMetadata