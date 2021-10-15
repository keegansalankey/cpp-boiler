import fileinput
import os

def insert_project_name(name, location, replace_string="<<replace_me>>"):
    with fileinput.FileInput(location, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace(replace_string, name), end='')

    if os.path.exists(location + ".bak"):
        os.remove(location + ".bak")


def remove_from_file(location, remove_string):
    with fileinput.FileInput(location, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace(remove_string, ''), end='')

    if os.path.exists(location + ".bak"):
        os.remove(location + ".bak")
