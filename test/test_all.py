import pytest
import json
import os
from host_open.client import get_synced_folders, convert_filepaths
from host_open.arg_handler import parse_client

def mock_path(file):
    """ Gets files within the <project>/test/mock directory

    Args:
        file <str>

    Returns:
        <str>: absolute filepath
    """
    mock_fldr = os.path.join(
        os.path.dirname(
            os.path.abspath(__file__)
        ),
        'mock'
    )
    return os.path.join(mock_fldr, file)


def test_get_synced_folders(monkeypatch):
    def mockreturn(unused):
        data = open(mock_path('synced_folders'), 'r').read()
        return json.loads(data)
    monkeypatch.setattr(json, 'load', mockreturn)
    result = get_synced_folders()
    expected = [
        ('/.vagrant_info',
         '/Users/Jake/Programming/vagrant/' \
            'ubuntu/.vagrant/machines/default/virtualbox'),
        ('/home/ubuntu/Programming/code',
         '/Users/Jake/Programming/code'),
    ]

    assert sorted(result) == sorted(expected)

def test_convert_filepaths(monkeypatch):
    folders = [
        ('/home/ubuntu/Programming/code',
         '/Users/Jake/Programming/code'),
        ('/vagrant/myproject',
         '/Users/Jake/Programming/vagrant/myproject'),
    ]
    filepaths = [
        '/home/ubuntu/Programming/code/project1/file.py',
        '/home/ubuntu/privatedir/password.txt',
        '/vagrant/myproject/awesome.py'
    ]
    expected = [
        '/Users/Jake/Programming/code/project1/file.py',
        '/Users/Jake/Programming/vagrant/myproject/awesome.py'
    ]

    converted, invalid = convert_filepaths(filepaths, folders)

    assert converted == expected

@pytest.mark.parametrize('data, expected', [
    (['-p', '3800', '--log', 'critial', 'file.py', 'folder/awesome.txt'],
        (50, 3800, ['file.py', 'folder/awesome.txt'], None)),
    (['file1.py', 'file2.py', 'file3.py'],
        (20, 12345, ['file1.py', 'file2.py', 'file3.py'], None))
])
def test_parse_client(data, expected):
    # level, port, files, flags
    results = parse_client(data)
    assert results == expected