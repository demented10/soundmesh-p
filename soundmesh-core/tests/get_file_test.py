import pytest
from utils.file_storage_manager import LocalStorage
import logging




def test_local_storage(caplog):
    test_local_storage = LocalStorage()
    test_file_path = "tests/testfile.md"
    test_file_response= test_local_storage.get_file(test_file_path)
    print(type(test_file_response))
    assert test_file_response.metadata.name == "testfile.md"