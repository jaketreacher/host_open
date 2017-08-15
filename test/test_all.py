import pytest
import json
import os
from host_open import client
from host_open import arg_handler

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
    result = client.get_synced_folders()
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

    converted, invalid = client.convert_filepaths(filepaths, folders)

    assert converted == expected

@pytest.mark.parametrize('data, expected', [
    (['-p', '3800', '--log', 'critial', 'file.py', 'folder/awesome.txt'],
        (50, 3800, ['file.py', 'folder/awesome.txt'])),
    (['file1.py', 'file2.py', 'file3.py'],
        (30, arg_handler.default_port, ['file1.py', 'file2.py', 'file3.py']))
])
def test_parse_client(data, expected):
    # level, port, files
    results = arg_handler.parse_client(data)
    assert results == expected


@pytest.mark.parametrize('data, expected', [
    (['subl', '--port', '3800', '--log', 'debug'], ('subl', 10, 3800)),
    (['subl'], ('subl', 40 ,arg_handler.default_port)),
])
def test_parse_server(data, expected):
    # app, level, port
    results = arg_handler.parse_server(data)
    assert results == expected
