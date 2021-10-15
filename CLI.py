import lib.make_project as make_project
import lib.add_file as add_file
import os

def parse(argv):
    # boiler_path is passed throughout program to keep the head of directory tree
    boiler_path = os.path.dirname(os.path.realpath(__file__))
    argc = len(argv)

    match argv:
        case [_, "--create", *objects]:
            match objects:
                case[template_type, project_name]:
                    # invoke call to make project here
                    make_project.create(objects, boiler_path)

        case [_, "--add", *objects]:
            match objects:
                case["-c", file_name]:
                    # -c flag indicates class creation
                    add_file.add_class(file_name, boiler_path)
                case["-h", file_name]:
                    # -h flag indicates creation of generic header
                    add_file.add_header(file_name, boiler_path)
                case _:
                    # print usage instructions
                    print("ERROR: Invalid usage of --add")


