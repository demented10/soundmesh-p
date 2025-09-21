from soundmesh_core.abstractions import FileResponse, FileStorage
from pathlib import Path
import structlog
import sys
class LocalStorage(FileStorage): 
    def get_file(self, path: str) -> FileResponse:
        logger = structlog.get_logger()
        file_path = Path(path)
        try:
            logger.info(f"Start loading file from local storage")
            if(file_path.exists()):
                logger.info(f"File {file_path} is exists")
                if(file_path.is_file()):
                    logger.info(f"File {file_path.absolute} is not path")
                    file_content = file_path.read_bytes()
                    logger.info(f"File {file_path.name} readed, len is {len(file_content)}")
                    file_metadata = {"name": file_path.name, "extension": file_path.suffix, "size": sys.getsizeof(file_content)}
                    file_response = {"content" : file_content, "metadata": file_metadata}
                    return FileResponse(**file_response)
                else:
                    logger.info(f"File {file_path.absolute} is not file")
            else:
                logger.info(f"File is not exists")

        except Exception:
            logger.error("Failed to load from local storage", Exception)
            

class MinioStorage(FileStorage):
    def get_file(self, path: str) -> FileResponse:
        logger =structlog.get_logger()
        try:
            logger.info("Start loading file from minio storage")
        except Exception:
            logger.error("Failed to load from minio storage")
            