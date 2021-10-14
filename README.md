# cpp-boiler
**NOTE:** This project is currently waiting to be further expanded/revised, but basic functionality has been achieved.  
    
This project is intended to be able to generate a new project with boiler-plate C++ in the users current working directory. The current plan is to include a [CMake](https://cmake.org/) build system and [Conan](https://conan.io/) dependency installation system with each template.


## Usage
I currently have this project stored in my `$HOME` directory (most likely only functional on linux machines for the time being).
I then have an executable in `$HOME/bin/` directory named `boiler-cpp`. The contents of the executable are as follows:
```
#!/bin/bash 
python3 ~/cpp-boiler/make_project.py $@
```
Currently, `make_project.py` only accepts two arguments, with the first being the template type (name of a directory from templates directory) and the second being the project name. Here is an example invocation:
```
python3 path/to/make_project.py template_type project_name
```
Or, alternatively with a `$HOME/bin/` executable:
```
boiler-cpp template_type project_name
```

## Future Plans
1. Implement another template for boiler-plate [openGL](https://www.opengl.org//) code.
2. Create functionality to add boiler-plate code files to already established projects (i.e. adding classes with header and project files).
3. Add scripts for debugging to templates.
 
