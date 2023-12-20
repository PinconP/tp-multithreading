#ifndef MINION_H
#define MINION_H

#include <Eigen/Dense>
#include <nlohmann/json.hpp>

class Minion {
 private:
  Eigen::MatrixXd a;
  Eigen::VectorXd b;
  Eigen::VectorXd x;
  int id;

 public:
  Minion();
  bool init();
  void work();
  void executeTasks();
};

#endif  // MINION_H
