import pytest
from soundmesh_core.infrastructure.file_storage_manager import LocalStorage
import logging




def test_local_storage_text():
    test_local_storage = LocalStorage()
    test_file_path = "tests/testfile.md"
    test_file_response= test_local_storage.get_file(test_file_path)
    print(type(test_file_response))
    assert test_file_response.metadata.name == "testfile.md"

def test_local_storage_mp3():
    test_local_storage = LocalStorage()
    test_file_path = "tests/test.mp3"
    test_file_response= test_local_storage.get_file(test_file_path)
    print(type(test_file_response))
    assert test_file_response.metadata.name == "test.mp3"
    assert test_file_response.metadata.extension == ".mp3"