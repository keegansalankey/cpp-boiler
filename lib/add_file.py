import sys
import os
import shutil
import lib.utilities as utilities

def add_class(name, boiler_path):
   
    # Declaring strings for pathing
    boiler_path = boiler_path + "/templates/_generic/"
    class_h_string = "generic_class.h"
    class_cpp_string = "generic_class.cpp"

    # Replacement strings for files
    file_name_string = name.capitalize()
    macro_name_string = name.upper()
    
    # Path where files are intended to be created
    target_path = os.getcwd() + "/"

    # if include directory is included, file is created there and cmake file is updated, otherwise file is created
    # in the current working directory
    if os.path.isdir(include_path := target_path + "include/"):
        shutil.copyfile(boiler_path + class_h_string, file_path := include_path + file_name_string + ".h")
        utilities.remove_from_file(target_path + "CMakeLists.txt", "#H_REMOVE_ME_")
    else:
        shutil.copyfile(boiler_path + class_h_string, file_path := target_path + file_name_string + ".h")
    
    # Generatng custom text for files through marker replacement
    utilities.insert_project_name(file_name_string, file_path)
    utilities.insert_project_name(macro_name_string, file_path, "<<REPLACE_ME>>" )
    
    # Same process as above for .cpp file instead
    if os.path.isdir(src_path := target_path + "src/"):
        shutil.copyfile(boiler_path + class_cpp_string, file_path := src_path + file_name_string + ".cpp")
        utilities.remove_from_file(target_path + "CMakeLists.txt", "#CPP_REMOVE_ME_")
    else:
        shutil.copyfile(boiler_path + class_cpp_string, file_path := target_path + file_name_string + ".cpp")

    utilities.insert_project_name(file_name_string, file_path)


def add_header(name, boiler_path):
    
    # Similar deal as above except different template is used and only a .h file is created
    boiler_path = boiler_path + "/templates/_generic/"
    header_h_string = "generic_header.h"
    file_name_string = name.capitalize()
    macro_name_string = name.upper()

    target_path = os.getcwd() + "/"
    
    if os.path.isdir(include_path := target_path + "include/"):
        shutil.copyfile(boiler_path + header_h_string, file_path := include_path + file_name_string + ".h")
        utilities.remove_from_file(target_path + "CMakeLists.txt", "#H_REMOVE_ME_")
    else:
        shutil.copyfile(boiler_path + header_h_string, file_path := target_path + file_name_string + ".h")

    utilities.insert_project_name(macro_name_string, file_path, "<<REPLACE_ME>>")
