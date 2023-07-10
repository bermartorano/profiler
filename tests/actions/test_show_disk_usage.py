import os
from pro_filer.actions.main_actions import show_disk_usage  # NOQA


def test_show_disk_usage_empty_context(capsys):
    context = {'all_files': []}
    show_disk_usage(context)
    captured = capsys.readouterr()
    assert captured.out == 'Total size: 0\n'


def test_show_disk_usage_with_context(capsys, tmp_path):
    mock_dir = tmp_path
    mock_file_1 = mock_dir / 'mock_file_1.txt'
    mock_file_2 = mock_dir / 'mock_file_2.txt'

    mock_file_1.touch()
    mock_file_2.touch()

    with open(mock_file_1, 'w') as file1:
        file1.write('este é o primeiro arquivo de teste\n')
    with open(mock_file_2, 'w') as file2:
        file2.write('este é o segundo arquivo de teste\nCom duas linhas\n')

    file1_size = os.path.getsize(mock_file_1)
    file2_size = os.path.getsize(mock_file_2)
    total_size = file1_size + file2_size
    file_2_percent = int(file2_size/total_size * 100)
    file_1_percent = int(file1_size/total_size * 100)
    file1_prnt = '/tmp/pytest-of-bernardo/pyt...age_with_cont0/mock_file_1.txt'
    file2_prnt = '/tmp/pytest-of-bernardo/pyt...age_with_cont0/mock_file_2.txt'

    context = {'all_files': [f'{mock_file_1}', f'{mock_file_2}']}
    show_disk_usage(context)
    captured = capsys.readouterr()
    right_message = f''''{file2_prnt}':        {file2_size} ({file_2_percent}%)
'{file1_prnt}':        {file1_size} ({file_1_percent}%)
Total size: {total_size}
'''

    assert right_message == captured.out
