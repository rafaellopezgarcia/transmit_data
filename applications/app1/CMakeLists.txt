project(app1
        VERSION 1.0.0
        DESCRIPTION "application to showcase the functionalities of the com library"
        LANGUAGES CXX)
        
add_executable(app1)
target_sources(app1 PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/main.cpp)
target_link_libraries(app1 com)