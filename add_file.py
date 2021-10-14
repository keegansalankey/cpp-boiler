import sys
import os
import shutil
import utilities

def add_class(name):

    class_h_string = "generic_class.h"
    class_cpp_string = "generic_class.cpp"
    file_name_string = name.capitalize()
    macro_name_string = name.upper()

    boiler_path = os.path.dirname(os.path.realpath(__file__)) + "/templates/_generic/"
    target_path = os.getcwd() + "/"

    if os.path.isdir(include_path := target_path + "include/"):
        shutil.copyfile(boiler_path + class_h_string, file_path := include_path + file_name_string + ".h")
    else:
        shutil.copyfile(boiler_path + class_h_string, file_path := target_path + file_name_string + ".h")

    utilities.insert_project_name(file_name_string, file_path)
    utilities.insert_project_name(macro_name_string, file_path, "<<REPLACE_ME>>" )

    if os.path.isdir(src_path := target_path + "src/"):
        shutil.copyfile(boiler_path + class_cpp_string, file_path := src_path + file_name_string + ".cpp")
    else:
        shutil.copyfile(boiler_path + class_cpp_string, file_path := target_path + file_name_string + ".cpp")

    utilities.insert_project_name(file_name_string, file_path)



def add_header(name):
    
    header_h_string = "generic_header.h"
    file_name_string = name.capitalize()
    macro_name_string = name.upper()

    boiler_path = os.path.dirname(os.path.realpath(__file__)) + "/templates/_generic/"
    target_path = os.getcwd() + "/"

    if os.path.isdir(include_path := target_path + "include/"):
        shutil.copyfile(boiler_path + header_h_string, file_path := include_path + file_name_string + ".h")
    else:
        shutil.copyfile(boiler_path + header_h_string, file_path := target_path + file_name_string + ".h")

    utilities.insert_project_name(macro_name_string, file_path, "<<REPLACE_ME>>")
