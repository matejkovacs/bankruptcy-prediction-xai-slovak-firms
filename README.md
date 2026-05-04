[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20029429.svg)](https://doi.org/10.5281/zenodo.20029429)

# Bankruptcy Prediction with Explainable AI

This repository contains the reproducible research pipeline for a diploma thesis focused on predicting the failure of Slovak firms using three model classes:

1. a transparent econometric logistic-regression benchmark,
2. an Explainable Boosting Machine (EBM),
3. a sequential BiLSTM model with post-hoc SHAP interpretation.

The purpose of the repository is to make the empirical workflow reproducible without publishing the underlying raw financial dataset.

## Repository structure

```text
.
├── 00_data_preparation.ipynb        # data preparation and model-ready CSV exports
├── 01_logit_benchmark.ipynb         # strict econometric logistic-regression benchmark
├── 03_ebm_pipeline.ipynb            # Explainable Boosting Machine pipeline
├── 04_bilstm_pipeline.ipynb         # BiLSTM + focal loss + SHAP pipeline
├── data/README.md                   # expected input data and generated datasets
├── outputs/README.md                # local output artefacts and ignored files
├── docs/                            # reproducibility notes and notebook audit report
├── requirements.txt                 # Python dependencies for pip
├── environment.yml                  # optional conda environment
├── .env.example                     # example environment-variable configuration
├── .gitignore                       # files intentionally excluded from Git
├── .gitattributes                   # line-ending normalization
└── LICENSE                          # MIT License for code and notebooks
```

## Notebook execution order

Run the notebooks in the following order:

1. `00_data_preparation.ipynb`  
   Loads the raw firm-year panel, creates financial ratios, non-financial features, macroeconomic controls, SME/activity filters, winsorized variables, lag/difference features, and model-specific CSV exports.

2. `01_logit_benchmark.ipynb`  
   Uses `data_logit_strict.csv` and estimates the transparent econometric logistic-regression benchmark.

3. `03_ebm_pipeline.ipynb`  
   Uses `data_ebm.csv` and estimates the Explainable Boosting Machine, including sampling-strategy comparison, hyperparameter tuning, Platt calibration, top-k analysis, and model interpretation.

4. `04_bilstm_pipeline.ipynb`  
   Uses `data_rnn.csv`, builds the sequential firm-year panel, trains the BiLSTM model with focal loss and balanced batches, and produces SHAP-based interpretation outputs.

## Input data

The raw dataset is **not included** in this repository.

Before running the pipeline, place the raw input file in the repository root or configure the path through environment variables:

```text
firmy_dataset.csv
```

The expected input is a firm-year panel covering Slovak firms, accounting variables, firm identifiers, year, target variable, industry information, legal form, firm age information, and other variables required to compute the financial ratios used in the notebooks. See `data/README.md` for details.

## Generated files

The notebooks generate intermediate datasets and model artefacts such as:

```text
data_logit.csv
data_logit_strict.csv
data_ebm.csv
data_rnn.csv
logit_v7_results.pkl
logit_v7_results.json
results_ebm.pkl
ebm_v7_results.pkl
ebm_v5_results.pkl
bilstm_v7_results.pkl
bilstm_v8/
```

These files are intentionally excluded through `.gitignore`, because they are derived from the raw data, can be large, and are not required as source files for the public repository.

## Environment setup

### Option A: pip

```bash
python -m venv .venv
source .venv/bin/activate      # Linux/macOS
# .venv\Scripts\activate       # Windows
pip install --upgrade pip
pip install -r requirements.txt
```

### Option B: conda

```bash
conda env create -f environment.yml
conda activate bankruptcy-xai
```

## Configuration

The notebooks are prepared to work from the repository root. If the data files are stored elsewhere, set the environment variables shown in `.env.example`:

```bash
DATA_DIR=/path/to/data
BASE_DIR=/path/to/data_and_outputs
```

## Reproducibility notes

The empirical workflow uses an out-of-time split:

| Dataset split | Years |
|---|---:|
| Train | 2013–2016 |
| Validation | 2017 |
| Test | 2018–2019 |

The main random seed is `42`. Some deep-learning steps may still show minor numerical differences across CPU/GPU environments.

Further reproducibility details are provided in `docs/REPRODUCIBILITY.md`.

## Data availability

The raw financial dataset is not part of this repository. The repository only contains source code, notebooks, and documentation needed to reproduce the empirical pipeline if the user has legitimate access to the required input data.

## License

The source code, notebooks, and documentation in this repository are released under the MIT License. See `LICENSE`.

The raw financial dataset, generated model artefacts, exported CSV files, trained model checkpoints, and any third-party data sources are **not included** in this repository and are **not covered** by the MIT License unless explicitly stated by their respective owners.

## Academic use

This repository is intended as a reproducibility package for academic research. The models and outputs are not intended to be used as standalone financial, legal, or investment advice.

## Citation

If you use this repository, please cite it as:

Kovacs, M. (2026). *XAI Pipelines for Bankruptcy Prediction of Slovak Firms* (Version 1.0.0) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.20029429
