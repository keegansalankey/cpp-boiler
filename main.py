# This currently only supports python3.10 because I wanted to utilize pattern-matching
# A more generic CLI parser will be implemented eventually for all python3 versions

import sys

if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv)

    req_version = (3,10)

    if (argc == 1):
        print("ERROR: Invalid usage") # replace with usage instruction eventually
        exit(0)

    if sys.version_info < req_version:
        print("ERROR: Only python3.10+ is currently supported. Currently using: python{}.{}".format(sys.version_info[0], sys.version_info[1]))
    else:
        import CLI
        CLI.parse(argv)

    
