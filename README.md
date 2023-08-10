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

- [T008:0004] The project shall be built in GCC
- [T008:0005] The project shall be built in clang
- [T008:0006] The project shall be built in debug mode
- [T008:0007] The project shall be built in release mode
- [T008:0008] It must be possible to build the libraries independently of the examples
- [T008:0009] It must be possible to build the examples in isolation
- [T008:000a] It must be possible to build the libraries and examples
- [T008:000b] It shall be possible to install the libraries
- [T008:000c] It shall be possible to execute the examples by referencing the installed libraries
- [T008:000d] it shall be possible to execute the examples by referencing the uninstalled project

### CI

- [W009:000e] There must be a CI job validating the building process
- [W009:000f] There must be a CI job validating building the project with GCC in debug mode
- [W009:0010] There must be a CI job validating building the project with GCC in release mode
- [W009:0011] There must be a CI job validating building the project with clang in debug mode
- [W009:0012] There must be a CI job validating building the project with clang in release mode
- [W009:0013] There must be a CI job validating building the project with all different compilers using the same environment
- [W009:0014] There must be a CI job validating building the application examples with GCC in debug mode
- [W009:0015] There must be a CI job validating building the application examples with GCC in release mode
- [W009:0016] There must be a CI job validating running the application examples with GCC in debug mode
- [W009:0017] There must be a CI job validating running the application examples with GCC in release mode
- [W009:0018] There must be a CI job validating building the application examples with GCC in debug mode **using the installed library**
- [W009:0019] There must be a CI job validating building the application examples with GCC in release mode **using the installed library**
- [W009:001a] There must be a CI job validating running the application examples with GCC in debug mode **using the installed library**
- [W009:001b] There must be a CI job validating running the application examples with GCC in release mode **using the installed library**
