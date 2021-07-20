import os


def renameFiles():
    prefix = input("Copy prefix here: ")

    originals = os.listdir()

    for filename in originals:
        newName = filename.replace(prefix, "")
        os.rename(filename, newName)


renameFiles()
