# cpp-boiler
**NOTE:** This project is currently waiting to be further expanded/revised, but basic functionality has been achieved.  
  
This project is intended to generate a boiler-plate c++ project with a default build system and package management. It can also be utilized to generate
boiler plate code for class header/project files and generic headers.

## Dependencies
1. Currently only functions with [Python 3.10](https://www.python.org/downloads/release/python-3100/) (I was excited to utilize pattern matching). Functionality with all python will be implemented eventually.
2. [Conan](https://conan.io/) will be utilized for package managment and dependency installation for generated projects.
3. [CMake](https://cmake.org/) is the default build system that will be generated with projects.

## Usage
I currently have this project stored in my `$HOME` directory (most likely only functional on linux machines for the time being).
I then have an executable in `$HOME/bin/` directory named `boiler-cpp`. The contents of the executable are as follows:
```
#!/bin/bash 
python3.10 ~/cpp-boiler/main.py $@
```
Currently, there are two separate functionalities, with the first being project creation:
```
python3 path/to/make_project.py --create template project_name
```
Or, alternatively, for project creation with a `$HOME/bin/` executable:
```
boiler-cpp --create template_type project_name
```
## Future Plans
1. Implement another template for boiler-plate [openGL](https://www.opengl.org//) code.
2. Add to functionality for add boiler-plate code files to already established projects (i.e. adding classes with header and project files).
3. Add scripts for debugging to templates.
4. Add more robust usage instructions to CLI.
 
