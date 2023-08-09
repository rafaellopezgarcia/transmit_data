cmake_minimum_required(VERSION 3.10)
project(app1
        VERSION 1.0.0
        DESCRIPTION "application to showcase the functionalities of the com library"
        LANGUAGES CXX)

set(CMAKE_DEBUG_POSTFIX _deb)

if("${CMAKE_SOURCE_DIR}" STREQUAL "${PROJECT_SOURCE_DIR}")

list(APPEND CMAKE_PREFIX_PATH "$ENV{HOME}/cmake/comTargets/")

find_package(comTargets 1.0.0 EXACT)    
add_executable(app1)
target_sources(app1 PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/main.cpp)
target_link_libraries(app1 PRIVATE com::com)
else()
  message("Building application as part of a bigger project")
  add_executable(app1)
  target_sources(app1 PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/main.cpp)
  target_link_libraries(app1 PRIVATE com)
endif()

set_target_properties(app1 PROPERTIES DEBUG_POSTFIX ${CMAKE_DEBUG_POSTFIX})

if(CMAKE_COMPILER_IS_GNUCXX MATCHES 1)
  install(TARGETS app1 ARCHIVE DESTINATION "${CMAKE_INSTALL_LIBDIR}/com"
                      LIBRARY DESTINATION "${CMAKE_INSTALL_LIBDIR}/com"
                      PUBLIC_HEADER DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}/com/include"
                      RUNTIME DESTINATION "${CMAKE_INSTALL_BINDIR}/com"
  )
else()
  install(TARGETS app1 ARCHIVE DESTINATION "${CMAKE_INSTALL_LIBDIR}/com/clang"
                      LIBRARY DESTINATION "${CMAKE_INSTALL_LIBDIR}/com/clang"
                      PUBLIC_HEADER DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}/com/include"
                      RUNTIME DESTINATION "${CMAKE_INSTALL_BINDIR}/com/clang"
  )
endif()