from soundmesh_core.abstractions import FileResponse, FileStorage
from soundmesh_core.models import FileMetadata
from pathlib import Path
from typing import Optional, Union
import structlog
import sys


class LocalStorage(FileStorage):
    def get_file(self, path: str) -> Optional[FileResponse]:
        logger = structlog.get_logger()
        file_path = Path(path)
        try:
            logger.info(f"Start loading file from local storage")
            if file_path.exists():
                logger.info(f"File {file_path} is exists")
                if file_path.is_file():
                    logger.info(f"File {file_path.absolute} is not path")
                    file_content = file_path.read_bytes()
                    logger.info(
                        f"File {file_path.name} readed, len is {len(file_content)}"
                    )
                    file_metadata = FileMetadata(
                        name= file_path.name,
                        extension= file_path.suffix,
                        size= sys.getsizeof(file_content),
                        source= "local"
                    )
                    return FileResponse(content=file_content, metadata=file_metadata)
                else:
                    logger.info(f"File {file_path.absolute} is not file")
                    return None
            else:
                logger.info(f"File is not exists")
                return None
        except Exception:
            logger.error("Failed to load from local storage", Exception)
            return None
    def get_audiofile(self, path):
        return super().get_audiofile(path)


class MinioStorage(FileStorage):
    def get_file(self, path: str) -> Optional[FileResponse]:
        logger = structlog.get_logger()
        try:
            logger.info("Start loading file from minio storage")
            return None
        except Exception:
            logger.error("Failed to load from minio storage")
            return None
