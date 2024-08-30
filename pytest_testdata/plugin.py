import os
from pathlib import Path

import pytest
from filez import file

DEFAULT_TESTDATA_DIR = './data'


class TestData(object):
    def __init__(self, testdata_dir: Path):
        self.testdata_dir = testdata_dir

    def get_file(self, file_name):
        file_obj = self.testdata_dir / file_name
        if file_obj.is_file():
            return file_obj

    def read(self, file_name):
        file_obj = self.get_file(file_name)
        if file_obj.is_file():
            return file_obj.read_text()

    def read_bytes(self, file_name):
        file_obj = self.get_file(file_name)
        if file_obj.is_file():
            return file_obj.read_bytes()

    def load(self, file_name, **kwargs):
        file_obj = self.get_file(file_name)
        if file_obj.is_file():
            return file.load(file_obj.absolute(), **kwargs)


def pytest_addoption(parser):
    parser.addoption("--testdata-dir", action="store", help="set testdata dir path")
    parser.addini('testdata_dir', help="set testdata dir path")


@pytest.fixture
def testdata_dir(request):
    config = request.config
    testdata_dir = config.getoption('--testdata-dir') or config.getini('testdata_dir') or DEFAULT_TESTDATA_DIR
    if testdata_dir and testdata_dir.startswith('.'):
        testdata_dir = os.path.abspath(os.path.join(config.rootdir, testdata_dir))

    return Path(testdata_dir)


@pytest.fixture()
def testdata(testdata_dir):
    return TestData(testdata_dir)
