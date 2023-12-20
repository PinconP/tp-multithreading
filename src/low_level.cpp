#include <cpr/cpr.h>

#include <iostream>
#include <nlohmann/json.hpp>

int main() {
  cpr::Response r = cpr::Get(cpr::Url{"http://localhost:8000"});

  // Vérifier si la requête a réussi
  if (r.status_code == 200) {
    // Parser la réponse en un objet JSON
    nlohmann::json jsonResponse = nlohmann::json::parse(r.text);

    // Afficher l'objet JSON
    std::cout << "Response JSON:\n" << jsonResponse.dump(4) << std::endl;
  } else {
    std::cout << "Failed to get response, status code: " << r.status_code
              << std::endl;
  }

  return 0;
}
