# mlproject

A minimal machine learning project skeleton built to run locally.

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

## Run

- Ingest data and split into train/test:
  ```powershell
  python -m src.components.data_ingestion
  ```

- Run the training pipeline:
  ```powershell
  python -m src.pipeline.train_pipeline
  ```

## Notes

- Package name: `mlproject`
- Version: `0.0.1`
- Author: Devashish
- Requirements: `pandas`, `numpy`, `seaborn`, `scikit-learn`

## Output

- Artifacts are written to the `artifacts/` directory.
- Logs are written to `src/logs` when running `src/logger.py`.
