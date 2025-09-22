from abc import ABC, abstractmethod
from .models import FileResponse
from pathlib import Path
from typing import Optional
class FileStorage(ABC):

    @abstractmethod
    def get_file(self, path: str) -> Optional[FileResponse]:
        pass

    @abstractmethod
    def get_audiofile(self, path: str) -> Optional[FileResponse]:
        pass