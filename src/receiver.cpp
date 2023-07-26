#include "receiver.hpp"

void Receiver::receive() { 
  #ifndef NDEBUG
  std::cout << "DEBUG: ready to receive!" << std::endl;
  #else 
  std::cout << "RELEASE: ready to receive" << std::endl;
  #endif 
  #ifdef __clang__
  std::cout << "CLANG: ready to receive" << std::endl;
  #else
  std::cout << "GCC: ready to receive" << std::endl;
  #endif
}