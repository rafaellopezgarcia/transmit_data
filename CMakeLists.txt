cmake_minimum_required(VERSION 3.10)
project(transmit_data
        VERSION 1.0.0
        DESCRIPTION "transmit data among processes using protocol buffers"
        LANGUAGES CXX)
        
find_package (Threads)
add_executable(playground)
target_sources(playground PRIVATE src/main.cpp)
target_link_libraries (playground ${CMAKE_THREAD_LIBS_INIT})