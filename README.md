# cpp-boiler
**NOTE:** This project is currently waiting to be further expanded/revised, but basic functionality has been achieved.  
  
This project is intended to generate a boiler-plate C++ project with a default build system and package management. It can also be utilized to generate
boiler plate code for class header/project files and generic headers.

## Dependencies
1. Currently only functions with [Python 3.10](https://www.python.org/downloads/release/python-3100/) (I was excited to utilize pattern matching). Functionality with all python will be implemented eventually.
2. [Conan](https://conan.io/) will be utilized for package managment and dependency installation for generated projects.
3. [CMake](https://cmake.org/) is the default build system that will be generated with projects.

## Usage
Projects created with this tool will have the following directory tree architechture:
```
project
├── build/
├── build.sh
├── CMakeLists.txt
├── conanfile.txt
├── include
├── main.cpp
├── resources
└── src
```
The `include` and `src` directories are intended to contain `.h` and `.cpp` files, respecively. The `resources` directories is intended to contain any external files being read such as text or images. The `build` directory will not be created until `build.sh` has been executed.

### My personal configuration
I currently have this project stored in my `$HOME` directory (most likely only functional on linux machines for the time being).
I then have an executable in my `$HOME/bin/` directory named `boiler-cpp`. The contents of the executable are as follows:
```
#!/bin/bash 
python3.10 ~/cpp-boiler/main.py $@
```
### Creating a new project
To create a project `project_name` in your current working directory using template type `basic`:
```
$ python3.10 path/to/cpp_boiler/main.py --create basic project_name
```
Or, alternatively, for project creation with a `$HOME/bin/` executable:
```
$ boiler-cpp --create basic project_name
```
### Adding additional files
Navigate to the project directory for which you would like to add additional files. To create a new class named `MyClass` with both a header (`.h`) and project (`.cpp`) file, execute the following:
```
$ python3.10 path/to/cpp_boiler/main.py --add -c MyClass
```
The header file will either be placed in a `/include/` directory within the project, if such a directory exists, or will default to being placed in the current working directory. Likewise the project file will be placed in a `/src/` directory, if such a directory exists, or will default to being placed in the current working directory. The created files will already have generated text for macro definitions, `class` declarations, constructors, and `#include` statements.  
  
**NOTE:** By changing the `-c` flag to `-h`, a generic header (`.h`) will be generated.
## Future Plans
1. Implement another template for boiler-plate [openGL](https://www.opengl.org//) code.
2. Add to functionality for add boiler-plate code files to already established projects (i.e. adding classes with header and project files).
3. Add scripts for debugging to templates.
4. Add more robust usage instructions to CLI.
5. Update CMake file of project so newly created files are included
 
