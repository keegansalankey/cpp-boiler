import sys
import os
import re
import shutil
import fileinput
import lib.utilities as utilities

###### NOTE: Currently under refactor as CLI module is being programmed to reduce functionality in this module


def create(argv, boiler_path):
    argc = len(argv)


    # TODO: print usage instructions at some point 
    if (argc != 2):
        print("ERROR: Please enter two arguments")
        exit(1)

    template_type, project_name = argv[0], argv[1]

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
    # boiler_path = os.path.dirname(os.path.realpath(__file__))

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

    utilities.insert_project_name(project_name, project_path + "CMakeLists.txt")

    utilities.insert_project_name(project_name, project_path + "build.sh")

    # Cleaning up any artifacts from testing builds of actual templates
    if os.path.exists(project_path + "build/"):
        shutil.rmtree(project_path + "build/")

