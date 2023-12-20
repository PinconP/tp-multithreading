#include <cpr/cpr.h>

#include <Eigen/Dense>
#include <chrono>
#include <iostream>
#include <nlohmann/json.hpp>

class Minion {
 public:
  void work() {
    cpr::Response r = cpr::Get(cpr::Url{"http://localhost:8000"});
    // Vérifier si la requête a réussi
    if (r.status_code == 200) {
      // Parser la réponse en un objet JSON
      nlohmann::json jsonResponse = nlohmann::json::parse(r.text);

      int size =
          jsonResponse["size"];  // Utilisez la taille de 'a' dans le JSON
      Eigen::MatrixXd a(size, size);
      Eigen::VectorXd b(size);
      Eigen::VectorXd x(size);

      // Remplir la matrice 'a'
      for (int i = 0; i < size; ++i) {
        for (int j = 0; j < size; ++j) {
          a(i, j) = jsonResponse["a"][i][j];
        }
      }

      // Remplir le vecteur 'b'
      for (int i = 0; i < size; ++i) {
        b(i) = jsonResponse["b"][i];
      }

      auto start = std::chrono::high_resolution_clock::now();

      x = a.colPivHouseholderQr().solve(b);

      auto end = std::chrono::high_resolution_clock::now();
      std::chrono::duration<double> elapsed = end - start;
      double time = elapsed.count();
      std::cout << "Time taken: " << time << " seconds\n";
    }
  }
};

int main() {
  Minion minion;
  minion.work();

  return 0;
}
