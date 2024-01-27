cmake_minimum_required(VERSION 3.14)

set(PROJECT_NAME "low_level")
project(${PROJECT_NAME})

option(CPR_ENABLE_SSL "" OFF)

include(FetchContent)
FetchContent_Declare(
  Catch2
  GIT_REPOSITORY https://github.com/catchorg/Catch2.git
  GIT_TAG v3.4.0 # or a later release
)
FetchContent_Declare(
  json
  DOWNLOAD_EXTRACT_TIMESTAMP OFF
  URL "https://github.com/nlohmann/json/releases/download/v3.11.2/json.tar.xz")
FetchContent_Declare(
  cpr
  DOWNLOAD_EXTRACT_TIMESTAMP OFF
  URL "https://github.com/libcpr/cpr/archive/refs/tags/1.10.5.tar.gz")
FetchContent_Declare(
  eigen
  DOWNLOAD_EXTRACT_TIMESTAMP OFF
  URL "https://gitlab.com/libeigen/eigen/-/archive/3.4.0/eigen-3.4.0.tar.gz")
FetchContent_MakeAvailable(json eigen cpr Catch2)

add_executable(${PROJECT_NAME} ${PROJECT_NAME}.cpp)
target_link_libraries(${PROJECT_NAME} nlohmann_json::nlohmann_json cpr::cpr
                      Eigen3::Eigen Catch2::Catch2WithMain)
