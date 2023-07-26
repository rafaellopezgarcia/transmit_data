cmake_minimum_required(VERSION 3.10)
set(version 1.0.0)
project(transmit_data
        VERSION ${version}
        DESCRIPTION "transmit data among processes using protocol buffers"
        LANGUAGES CXX)

include(CMakePackageConfigHelpers)

option(ADD_EXAMPLES "Build examples" ON)
set(PROJECT_CXX_STANDARD 98 CACHE STRING "The C++ standard for this project")       
set(CMAKE_CXX_STANDARD ${PROJECT_CXX_STANDARD})
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

set(CMAKE_DEBUG_POSTFIX _deb)
add_compile_options(-Wall -Wextra -Wpedantic)
find_package (Threads)

set(COM_PUBLIC_HEADERS ${CMAKE_CURRENT_SOURCE_DIR}/include/receiver.hpp)
add_library(com STATIC)
target_sources(com PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/src/receiver.cpp)
target_include_directories(com PUBLIC "$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>"
                                      "$<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>/com/include")
set_target_properties(com PROPERTIES PUBLIC_HEADER ${COM_PUBLIC_HEADERS})


add_executable(playground)
set_target_properties(playground PROPERTIES DEBUG_POSTFIX ${CMAKE_DEBUG_POSTFIX})

target_sources(playground PRIVATE src/main.cpp)
target_link_libraries (playground ${CMAKE_THREAD_LIBS_INIT})
target_link_libraries(playground com)

if(CMAKE_COMPILER_IS_GNUCXX MATCHES 1)
  install(TARGETS com EXPORT comTargets
                      ARCHIVE DESTINATION "${CMAKE_INSTALL_LIBDIR}/com"
                      LIBRARY DESTINATION "${CMAKE_INSTALL_LIBDIR}/com"
                      PUBLIC_HEADER DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}/com/include"
                      RUNTIME DESTINATION "${CMAKE_INSTALL_BINDIR}/com/"
         )

  install(EXPORT comTargets
         FILE comTargets.cmake
         NAMESPACE com::
         DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/comTargets)
endif()

if (CMAKE_CXX_COMPILER_ID STREQUAL "Clang")
  install(TARGETS com EXPORT comTargets
                      ARCHIVE DESTINATION "${CMAKE_INSTALL_LIBDIR}/com/clang"
                      LIBRARY DESTINATION "${CMAKE_INSTALL_LIBDIR}/com/clang"
                      PUBLIC_HEADER DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}/com/include"
                      RUNTIME DESTINATION "${CMAKE_INSTALL_BINDIR}/com/clang"
         )

  install(EXPORT comTargets
          FILE comTargetsClang.cmake
          NAMESPACE com::
          DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/comTargets)

endif()

# Generate package configuration file
configure_package_config_file(${CMAKE_CURRENT_SOURCE_DIR}/Config.cmake.in
                              "${CMAKE_CURRENT_BINARY_DIR}/comTargetsConfig.cmake"
                              INSTALL_DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/comTargets
)

# Install the generated configuration files
install(FILES
        "${CMAKE_CURRENT_BINARY_DIR}/comTargetsConfig.cmake"
        "${CMAKE_CURRENT_BINARY_DIR}/comTargetsConfigVersion.cmake"
        DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/comTargets)

# Generate the version file for the config file
write_basic_package_version_file("${CMAKE_CURRENT_BINARY_DIR}/comTargetsConfigVersion.cmake"
                                  VERSION "${version}"
                                  COMPATIBILITY AnyNewerVersion)

if(ADD_EXAMPLES)
  message("adding examples")
  add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/applications)
endif(ADD_EXAMPLES)