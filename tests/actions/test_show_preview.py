from pro_filer.actions.main_actions import show_preview  # NOQA


def test_show_preview_no_context(capsys):
    context = {"all_files": [], "all_dirs": []}
    show_preview(context)
    message = capsys.readouterr()
    assert message.out == 'Found 0 files and 0 directories\n'


def test_show_preview_with_context(capsys):
    context = {
        'all_files': ['file1', 'file2', 'file3', 'file4', 'file5', 'file6'],
        'all_dirs': ['dir1', 'dir2', 'dir3', 'dir4', 'dir5', 'dir6']
    }
    right_message = '''Found 6 files and 6 directories
First 5 files: ['file1', 'file2', 'file3', 'file4', 'file5']
First 5 directories: ['dir1', 'dir2', 'dir3', 'dir4', 'dir5']\n'''
    show_preview(context)
    message = capsys.readouterr()
    assert message.out == right_message
