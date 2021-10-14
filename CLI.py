import make_project
import add_file

def parse(argv):
    argc = len(argv)

    match argv:
        case [_, "--create", *objects]:
            match objects:
                case[template_type, project_name]:
                    # invoke call to make project here
                    make_project.create(objects)

        case [_, "--add", *objects]:
            match objects:
                case["-c", file_name]:
                    # -c flag indicates class creation
                    add_file.add_class(file_name)
                case["-h", file_name]:
                    # -h flag indicates creation of generic header
                    add_file.add_header(file_name)
                case _:
                    # print usage instructions
                    print("ERROR: Invalid usage of --add")


