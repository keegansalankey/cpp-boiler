import sys
import os
import re
import shutil
import fileinput

def insert_project_name(name, location):
    with fileinput.FileInput(location, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('<<replace_me>>', name), end='')

if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv)

    # TODO: print usage instructions at some point 
    if (argc != 3):
        print("ERROR: Please enter two arguments")
        exit(1)

    template_type, project_name = argv[1], argv[2]

    ####################################################################################################
    #                                                                                                  # 
    # Thoughts on how to make this work outside of the cpp-boiler directory:                           #
    #                                                                                                  #
    #   1) Store working directory in variable to know where to create project                         #
    #   2) Get home directory path and then append path to the cpp-b:oiler directory                   #
    #   3) Change directory to home directory                                                          #
    #   3) Should be able to copy between those two                                                    #
    #                                                                                                  #
    # NOTE: This issue is resolved, but I will leave this here for future understanding                #
    #                                                                                                  #
    ####################################################################################################

    # Getting path of this file as it is executed
    boiler_path = os.path.dirname(os.path.realpath(__file__))

    # Getting path to working directory where execution is happening
    target_path = os.getcwd() + '/'

    # verify that template type exists by scanning through directory and append '/' if so
    with os.scandir(boiler_path + "/templates/") as templates:
        for template in templates:
            if template.is_dir() and template.name == template_type:
                template_type += "/"

    # using regex to check if template_type was appended
    check = re.compile('\w*/')
    if not check.match(template_type):
        print("ERROR: {} is not an existing template type".format(template_type))
        exit(1)


    template_path = boiler_path + "/templates/" + template_type
    project_path = target_path + project_name + "/"

    # Checking if project is already to made to prevent overwriting
    if os.path.isdir(project_path):
        print("ERROR: {} already exists in this directory".format(project_name))
        exit(1)

    shutil.copytree(template_path, project_path)

    insert_project_name(project_name, project_path + "CMakeLists.txt")
    if os.path.exists(project_path + "CMakeLists.txt.bak"):
        os.remove(project_path + "CMakeLists.txt.bak")

    insert_project_name(project_name, project_path + "build.sh")
    if os.path.exists(project_path + "build.sh.bak"):
        os.remove(project_path + "build.sh.bak")

    if os.path.exists(project_path + "build/"):
        shutil.rmtree(project_path + "build/")
