import zipfile
import pathlib


def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, 'compressed.zip')

    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)  # extra folders are not created
            archive.write(filepath, arcname=filepath.name)  # arcname will only give the filename


if __name__ == '__main__':
    make_archive(filepaths=['cli.py', 'todos.txt'],
                 dest_dir='projects_20apps')
