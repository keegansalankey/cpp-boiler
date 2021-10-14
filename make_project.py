import sys
import os
import re
import shutil

if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv)
    
    # Add function to print usage instructions at some point 
    if (argc != 3):
        print("ERROR: Please enter two arguments")
        exit(1)
    
    template_type, project_name = argv[1], argv[2]

    # verify that template type exists by scanning through directory
    with os.scandir("templates/") as templates:
        for template in templates:
            if template.is_dir() and template.name == template_type:
                template_type += "/"
                print(template_type)
    
    # usig regex to check if template_type was appended
    check = re.compile('\w*/')
    if not check.match(template_type):
        print("ERROR: {} is not an existing template type".format(template_type))
        exit(1)
                
    
    template_path = "templates/" + template_type
    project_path = "./" + project_name + "/"
    if os.path.isdir(project_path):
        print("ERROR: {} already exists in this directory".format(project_name))
        exit(1)

    shutil.copytree(template_path, project_path)
