# transmit_data

Transmit data using protocol buffers.

Objectives

- transmit data from one function to another
- use protocol buffers as the format to transmit the data
- serialize and deserialize the data
- use a class that takes care of the transmission of the data
- your cmake must have options
  -- run in gcc and clangd
  -- run in C++14 and C++17
  -- run in debug and release mode checked
  -- install the library
  -- remember not to use globbing as a rule

  -- install library in other folder
  -- make sure it works on application
  -- make sure it works when compiling the whole project and installing it

## Requirements

### Building process

- The project shall be built in GCC
- The project shall be built in clang
- The project shall be built in debug mode
- The project shall be built in release mode
- It must be possible to build the libraries independently of the examples
- It must be possible to build the examples in isolation
- It must be possible to build the libraries and examples
- It shall be possible to install the libraries
- It shall be possible to execute the examples by referencing the installed libraries
- it shall be possible to execute the examples by referencing the uninstalled project

### CI

- There must be a CI job validating the building process
- There must be a CI job validating building the project with GCC in debug mode
- There must be a CI job validating building the project with GCC in release mode
- There must be a CI job validating building the project with clang in debug mode
- There must be a CI job validating building the project with clang in release mode
- There must be a CI job validating building the project with all different compilers using the same environment
- There must be a CI job validating building the application examples with GCC in debug mode
- There must be a CI job validating building the application examples with GCC in release mode
- There must be a CI job validating running the application examples with GCC in debug mode
- There must be a CI job validating running the application examples with GCC in release mode
- There must be a CI job validating building the application examples with GCC in debug mode **using the installed library**
- There must be a CI job validating building the application examples with GCC in release mode **using the installed library**
- There must be a CI job validating running the application examples with GCC in debug mode **using the installed library**
- There must be a CI job validating running the application examples with GCC in release mode **using the installed library**
