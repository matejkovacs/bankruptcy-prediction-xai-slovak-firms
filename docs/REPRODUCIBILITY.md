# Reproducibility notes

## 1. Running the pipeline from a clean environment

1. Create a Python environment using either `requirements.txt` or `environment.yml`.
2. Place `firmy_dataset.csv` in the repository root, or set the `DATA_DIR` environment variable.
3. Run the notebooks in the following order:
   - `00_data_preparation.ipynb`,
   - `01_logit_benchmark.ipynb`,
   - `03_ebm_pipeline.ipynb`,
   - `04_bilstm_pipeline.ipynb`.

## 2. Out-of-time split

All models use the same out-of-time validation design:

| Split | Years |
|---|---:|
| Train | 2013–2016 |
| Validation | 2017 |
| Test | 2018–2019 |

This split prevents look-ahead bias by ensuring that future observations do not enter training or hyperparameter selection.

## 3. Imputation and winsorization

- Winsorization thresholds are computed only from the training years.
- Missing values are handled separately for each model-specific dataset.
- The EBM dataset uses the technical value `-999` for missing values.
- The BiLSTM dataset first converts infinite values to `NaN` and then applies training-median imputation, with fallback values where necessary.

## 4. Random seeds

The main random seed is `42`. The BiLSTM pipeline uses a multi-seed ensemble. Small numerical differences may occur across hardware backends, TensorFlow versions, and CPU/GPU settings.

## 5. Large artefacts

CSV datasets, pickle payloads, trained models, checkpoints, SHAP outputs, and generated figures are treated as derived artefacts rather than source code. They are ignored through `.gitignore`.

## 6. License and data scope

The MIT License applies to the repository code, notebooks, and documentation. It does not apply to the raw financial dataset, generated datasets, model artefacts, or third-party data sources.
