# mlproject

Nothing much.

## Setup

- Create the Conda environment:
  ```powershell
  conda env create -f environment.yml
  conda activate venv
  ```

- Install the package in editable mode if needed:
  ```powershell
  pip install -e .
  ```

## Notes

- Package name: `mlproject`
- Version: `0.0.1`
- Author: Devashish
- Requirements: `pandas`, `numpy`, `seaborn`

## Logging

- Logs are written to `src/logs` when running `src/logger.py`.
