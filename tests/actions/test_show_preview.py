from pro_filer.actions.main_actions import show_preview  # NOQA


def test_show_preview_no_context(capsys):
    context = {"all_files": [], "all_dirs": []}
    show_preview(context)
    message = capsys.readouterr()
    assert message.out == 'Found 0 files and 0 directories\n'
