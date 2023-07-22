cmake_minimum_required(VERSION 3.10)
project(transmit_data
        VERSION 1.0.0
        DESCRIPTION "transmit data among processes using protocol buffers"
        LANGUAGES CXX)


set(PROJECT_CXX_STANDARD 98 CACHE STRING "The C++ standard for this project")       
set(CMAKE_CXX_STANDARD ${PROJECT_CXX_STANDARD})
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

set(CMAKE_DEBUG_POSTFIX _deb)
add_compile_options(-Wall -Wextra -Wpedantic)
find_package (Threads)


add_library(com STATIC)
target_sources(com PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/src/receiver.cpp)
target_include_directories(com PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include )

add_executable(playground)
set_target_properties(playground PROPERTIES DEBUG_POSTFIX ${CMAKE_DEBUG_POSTFIX})

target_sources(playground PRIVATE src/main.cpp)
target_link_libraries (playground ${CMAKE_THREAD_LIBS_INIT})
target_link_libraries(playground com)

if(CMAKE_COMPILER_IS_GNUCXX MATCHES 1)
  install(TARGETS playground DESTINATION lib)
endif()

add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/applications/app1)