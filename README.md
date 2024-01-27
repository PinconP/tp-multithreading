# Multithreading

![GitHub language count](https://img.shields.io/github/languages/count/PinconP/tp-multithreading)
![GitHub last commit](https://img.shields.io/github/last-commit/PinconP/tp-multithreading)
[![codecov](https://codecov.io/gh/PinconP/tp-multithreading/graph/badge.svg?token=XN361JU1D1)](https://codecov.io/gh/PinconP/tp-multithreading)
![Build Status](https://app.travis-ci.com/PinconP/tp-multithreading.svg?branch=main)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/6d6b3dda03a7462da8d6054a633f69f2)](https://app.codacy.com/gh/PinconP/tp-multithreading/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Introduction

This framework, written in Python and C++, is designed for efficient execution of distributed tasks using parallel processing. It features a Master-Slave architecture where the Master delegates tasks and Slave nodes execute them. It leverages Python's multiprocessing library to facilitate concurrent task processing, offering an intuitive approach to managing workload distribution among multiple processors.

## Main Features

- **Master-Slave Structure:** Optimized for distributing tasks in a parallel computing environment.
- **Parallel Processing:** Employs Python's multiprocessing features for simultaneous task processing.
- **Task Handling:** Includes classes for task assignment, result aggregation, and inter-node communication.
- **Sample Code:** Comes with sample code for Master, Slave, and Task classes.
- **Comprehensive Testing:** Incorporates unit tests to guarantee the integrity and performance of key functions.

## Setup Guide

### Requirements

- Python 3.x

### Setting Up

Execute the `venv_install.sh` script from the project's base directory:

```bash
./setup/venv_install.sh
```

### Uninstalling

Execute the `venv_uninstall.sh` script from the project's base directory:

```bash
./setup/venv_uninstall.sh
```

## License

This software is provided under the MIT License. Refer to the [LICENSE](LICENSE) file for more information.

## Benchmarking

For a matrix size of 4000, the following results were observed:

- Resolution in Python took approximately 9.3 seconds.

- Using the `colPivHouseholderQr` function in C++, it took about 12.5 seconds.

- The `lu` function in C++ completed the task in roughly 1.8 seconds.

These outcomes were recorded on my personal computer and may vary on different systems.

### PC Specifications

For reference, here are the specifications of the computer used for benchmarking:

- **CPU:** Intel Core i7-11800H @ 2.30GHz

- **RAM:** 16GB DDR4 @ 3200MHz

- **OS:** Ubuntu 20.04.1 LTS

- **GPU:** NVIDIA GeForce RTX 3070 Laptop GPU
