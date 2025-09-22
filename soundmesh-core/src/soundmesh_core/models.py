from pydantic import BaseModel, PlainSerializer, PlainValidator
from typing import Annotated



class FileMetadata(BaseModel):
    name: str
    extension: str
    size: int
    source: str

class AudioFileMetadata(FileMetadata):
    genre: str
    author: str


class FileResponse(BaseModel):
    content: Annotated[
        bytes,
        PlainSerializer(lambda x: list(bytes(x))),
        PlainValidator(bytes),
    ]
    metadata: FileMetadata