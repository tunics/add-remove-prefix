import os


def renameFiles():
    prefix = input("Copy prefix here: ")

    originals = os.listdir()

    for filename in originals:
        newName = prefix + filename
        os.rename(filename, newName)


renameFiles()