from soundmesh_core.abstractions import FileStorage, FileResponse
import os
import structlog

class LocalStorage(FileStorage):
    def get_file(path: str) -> FileResponse:
        logger =structlog.get_logger()
        try:
            logger.info("Start loading file from local storage")
        except Exception:
            logger.error("Failed to load from local storage")
            

class MinioStorage(FileStorage):
    def get_file(path: str) -> FileResponse:
        logger =structlog.get_logger()
        try:
            logger.info("Start loading file from minio storage")
        except Exception:
            logger.error("Failed to load from minio storage")
            