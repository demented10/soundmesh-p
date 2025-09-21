from abc import ABC, abstractmethod
from .models import FileResponse

class FileStorage(ABC):

    @abstractmethod
    def get_file(self, file_path: str) -> FileResponse:
        pass