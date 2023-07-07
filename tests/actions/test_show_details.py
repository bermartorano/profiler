import os
from datetime import date
from pro_filer.actions.main_actions import show_details  # NOQA


def test_show_details(capsys):
    context = {'base_path': "this/file/do_not_exist.py"}
    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == "File 'do_not_exist.py' does not exist\n"


def test_show_details_file_with_ext(capsys, tmp_path):
    mock_file_path = tmp_path / "mocked_file.txt"
    mock_file_path.touch()
    file_name = 'mocked_file.txt'
    file_size = os.path.getsize(mock_file_path)
    file_type = 'file'
    file_extension = '.txt'
    file_last_mod = date.today()

    message = f'''File name: {file_name}
File size in bytes: {file_size}
File type: {file_type}
File extension: {file_extension}
Last modified date: {file_last_mod}
'''
    context = {'base_path': f'{mock_file_path}'}
    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == message


def test_show_details_file_with_no_ext(capsys, tmp_path):
    mock_file_path = tmp_path / "mocked_file"
    mock_file_path.touch()
    file_name = 'mocked_file'
    file_size = os.path.getsize(mock_file_path)
    file_type = 'file'
    file_extension = '[no extension]'
    file_last_mod = date.today()

    message = f'''File name: {file_name}
File size in bytes: {file_size}
File type: {file_type}
File extension: {file_extension}
Last modified date: {file_last_mod}
'''
    context = {'base_path': f'{mock_file_path}'}
    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == message
