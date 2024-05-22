cmake_minimum_required(VERSION 3.10)
project(structurax)

add_subdirectory(feaplusplus)

find_package(pybind11 REQUIRED)

include_directories(${CMAKE_SOURCE_DIR}/FEAplusplus/feaplusplus/include)

add_library(pyfeaplusplus MODULE structurax/pyfeaplusplus.cpp)

target_link_libraries(pyfeaplusplus PRIVATE pybind11::module feaplusplus_src)

set_target_properties(pyfeaplusplus PROPERTIES PREFIX "${PYTHON_MODULE_PREFIX}"
                      SUFFIX "${PYTHON_MODULE_EXTENSION}")
