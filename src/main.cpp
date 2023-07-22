#include <chrono>
#include <iostream>
#include <thread>
#include "receiver.hpp"

/*template<typename DataType>
class Transmitter {
public:
  void Send(DataType data) {
    
  }
};

template<typename DataType>
class Receiver {
public:
  DataType Receive() {

  }
};

void ping() {
  std::cout << "this is ping and sends data to pong" << std::endl;
  Transmitter<int> transmitter;
  transmitter.Send(34);
}

template <typename DataType>
void pong()  {
  using namespace std::chrono_literals;
  std::cout << "this is pong and receives data from ping" << std::endl;
  while(true) {
    std::cout << "checking if there is data" << std::endl;
    std::this_thread::sleep_for(300ms);
  }
}
*/

int main() {
  /*
  std::cout << "transmit data" << std::endl;
  auto a =432;
  std::cout << a << std::endl;
  //std::thread t1(pong<int>);
  //ping();
  //t1.join();
  */
  Receiver r;
  r.receive();
  return 0;
}