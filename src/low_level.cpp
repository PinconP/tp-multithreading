#include <cpr/cpr.h>

#include <Eigen/Dense>
#include <chrono>
#include <iostream>
#include <nlohmann/json.hpp>

class Minion {
 private:
  Eigen::MatrixXd a;
  Eigen::VectorXd b;
  Eigen::VectorXd x;
  int id;

 public:
  Minion() : id(-1) {}

  bool init() {
    cpr::Response r = cpr::Get(cpr::Url{"http://localhost:8000"});
    if (r.status_code != 200) {
      return false;
    }

    nlohmann::json jsonResponse = nlohmann::json::parse(r.text);
    id = jsonResponse["identifier"];
    int size = jsonResponse["size"];
    a.resize(size, size);
    b.resize(size);
    x.resize(size);

    for (int i = 0; i < size; ++i) {
      for (int j = 0; j < size; ++j) {
        a(i, j) = jsonResponse["a"][i][j];
      }
      b(i) = jsonResponse["b"][i];
    }

    return true;
  }

  void work() {
    auto start = std::chrono::high_resolution_clock::now();
    x = a.colPivHouseholderQr().solve(b);
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end - start;
    double time = elapsed.count();
    std::cout << "Time taken: " << time << " seconds\n";
  }

  void executeTasks() {
    while (init()) {
      work();
    }
  }
};

int main() {
  Minion minion;
  minion.executeTasks();

  return 0;
}
