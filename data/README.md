# Data directory

This directory documents the expected input files and generated datasets. The actual data files are not included in the repository.

## Expected raw input

Before running `00_data_preparation.ipynb`, the following raw input file must be available either in the repository root or in the directory specified by `DATA_DIR`:

```text
firmy_dataset.csv
```

The notebook expects a firm-year panel for the period 2011–2019. The dataset should contain at least:

- firm identifier `id`,
- observation year `rok`,
- binary target variable `target`,
- industry code/category `sk_nace`,
- number of employees,
- legal form,
- firm incorporation date,
- accounting items from the balance sheet and profit-and-loss statement needed to compute the financial ratios.

## Generated model-ready datasets

`00_data_preparation.ipynb` exports the following derived datasets:

| File | Purpose |
|---|---|
| `data_logit.csv` | input dataset for logistic regression |
| `data_logit_strict.csv` | strict/alias input for the logistic benchmark |
| `data_ebm.csv` | input dataset for the Explainable Boosting Machine |
| `data_rnn.csv` | input dataset for the BiLSTM sequence model |
| `logit_train_medians.pkl` | training medians used for logit-dataset imputation |
| `rnn_train_medians.pkl` | training medians used for RNN-dataset imputation |

These files are generated from the raw input data and are therefore excluded from Git through `.gitignore`.

## Data licensing note

The MIT License in this repository applies only to the source code, notebooks, and documentation. It does not apply to the raw dataset or to generated data files derived from it.
