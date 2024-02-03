import zipfile


def extract_archive(sourcepath, destpath):
    with zipfile.ZipFile(sourcepath, 'r') as archive:
        archive.extractall(destpath)


if __name__ == '__main__':
    extract_archive('E:\projects_20apps\compressed.zip', 'E:\projects_20apps\files')
