#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>

#include "Minion.h"

TEST_CASE("Minion Work - Linear System Solver", "[work]") {
  Minion minion;

  // Set up a known linear system (A and b)
  Eigen::MatrixXd A(2, 2);
  Eigen::VectorXd b(2);
  A << 4, 2, 1, 3;
  b << 10, 5;

  // You'll need to add methods to set A and b in Minion
  minion.setA(A);
  minion.setB(b);

  // Known solution for the system
  Eigen::VectorXd expected_solution(2);
  expected_solution << 2, 1;

  // Call work to compute the solution
  minion.work();

  // Verify the solution
  Eigen::VectorXd computed_solution =
      minion.getX();  // Assuming getX() is available to retrieve x

  // Compare the computed solution with the expected solution
  REQUIRE(computed_solution.isApprox(
      expected_solution,
      1e-6));  // Using a tolerance for floating point comparison
}
