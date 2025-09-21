import pytest
from infrastructure.file_storage_manager import LocalStorage

def test_passing():
    test_local_storage = LocalStorage()

    assert test_local_storage.get_file() == None