from soundmesh_core.abstractions import FileStorage, FileResponse
from pathlib import Path
import structlog

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
                    with file_path.open(mode="rb") as f:
                        file_content = f.read()
                        logger.info(f"File {f.name} readed, len is {len(file_content)}")
                        file_metadata = {"name": file_path.name}
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
            