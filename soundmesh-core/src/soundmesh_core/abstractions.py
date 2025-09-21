from abc import ABC, abstractmethod
from .models import FileResponse
from pathlib import Path
class FileStorage(ABC):

    @abstractmethod
    def get_file(self, path: str) -> FileResponse:
        pass