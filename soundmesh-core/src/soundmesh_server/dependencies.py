from soundmesh_core.infrastructure.file_storage_manager import LocalStorage

def get_file_storage() -> LocalStorage:
    return LocalStorage()