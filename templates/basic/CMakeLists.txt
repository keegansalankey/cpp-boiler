cmake_minimum_required(VERSION 3.10)

#Set up project
project(
  <<replace_me>> 
  VERSION 1.0
  )

include_directories( include/)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

################ UNCOMMENT WHEN FILES ARE ADDED TO SRC AND INCLUDE DIRECTORIES  #####################

#file(GLOB SRC_FILES ${PROJECT_SOURCE_DIR}/src/*.cpp)
#add_library(source_files ${SRC_FILES})

#file(GLOB INC_FILES ${PROJECT_SOURCE_DIR}/include/*.h)
#add_library(include_files ${INC_FILES})

####################################################################################################

#Set executable
add_executable(${PROJECT_NAME}     
  main.cpp
  )

#Set C++17
target_compile_features(${PROJECT_NAME} PUBLIC cxx_std_17)
set_target_properties(${PROJECT_NAME} PROPERTIES CXX_EXTENSIONS OFF)

######################## UNCOMMENT AFTER ADDING HEADER FILES TO INCLUDE ###########################
#set_target_properties(include_files PROPERTIES LINKER_LANGUAGE CXX)


#Set flags
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

if(MSVC)
  set(CMAKE_CXX_FLAGS_RELEASE "/O2")
  set(CMAKE_CXX_FLAGS_RELEASE "/Ox")
  target_compile_options(${PROJECT_NAME} PRIVATE 
    /W4)
else()
  target_compile_options(${PROJECT_NAME} PRIVATE 
    -Wall -Wextra -pedantic)		
endif()


#Finally
target_link_libraries(${PROJECT_NAME} 
  ${CONAN_LIBS}
  ##### UNCOMMENT WHEN FILES ARE ADDED TO SRC AND INCLUDE DIRECTORIES #####
  #include_files
  #source_files
  #########################################################################
  )
