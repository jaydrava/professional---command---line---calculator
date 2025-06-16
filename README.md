

# Command-Line Calculator Professional Edition

## Project Description
This is a robust command-line calculator application designed for seamless user interaction.
It supports the four foundamental arithemetic operations with a live REPL interface, comprehensive error handling, and command history.

## Core Capabilities
- Interactiove REPL loo for continuous calculations
- Operations: Addition (+), Subtraction (-), Multiplication (*), Division(/)
- Input Checks and graceful recovery from invalid inputs
- Implements both LBYL and EAFP error handling strategies
- Calculation history tracking and special user commands (*'help', ' history', 'exit'*)
- Modular architecture with a CalculationFactory design pattern

## Getting Started
### Clone the repository
```bash
git clone <repository-url>
cd <project-directory>
```
## Setup Your environment
#### create virtual environment and activate it.

```bash
python -m venv venv
venv\Scripts\activate # mac source venv/bin/activate
```
### Install required packages
```bash
pip install -r requirements.txt
```
### How to Use
python -m app.calculator

## Testing your code
pytest --cov=app tests/

## Additional Info
This project follows clean coding standards and DRY principles to ensure maintainability and extensibility.

Made with Python 🐍

```bash
name: Python application

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python 3.x
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pytest pytest-cov
    - name: Run tests with coverage
      run: |
        pytest --cov=app tests/
    - name: Check coverage
      run: |
        coverage report --fail-under=100
```