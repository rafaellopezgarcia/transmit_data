#include <iostream>
#include "receiver.hpp"

int main() {
  std::cout << "app1" << std::endl;
  Receiver r;
  r.receive();
  return 0;
}