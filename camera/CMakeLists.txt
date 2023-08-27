cmake_minimum_required(VERSION 3.26)
project(camera)

set(CMAKE_CXX_STANDARD 23)

find_package(OpenCV REQUIRED)
include_directories("external libraries/Header Search Paths/include/opencv4/opencv2/opencv.hpp")
include_directories(include)

add_executable(camera main.cpp
        alertAware.h)

target_link_libraries(camera ${OpenCV_LIBS})
