> **Historical audit.** This report predates the 2026-09-30 review. Its checkboxes describe the earlier preparation process, not independent evidence of the current repository state or successful model execution. See [the current review](PORTFOLIO_REVIEW.md) and [reproduction guide](REPRODUCIBILITY.md).

# Notebook audit before GitHub upload

Audited notebooks:

- `00_data_preparation.ipynb`
- `01_logit_benchmark.ipynb`
- `03_ebm_pipeline.ipynb`
- `04_bilstm_pipeline.ipynb`

The audit was static. The notebooks were not executed end-to-end because the raw input dataset `firmy_dataset.csv` and the generated `data_*.csv` files were not available in the working directory. The review focused on consistency between markdown descriptions and code cells, syntax validity, portability of file paths, output clearing, and GitHub readiness.

## Overall assessment

The notebooks are methodologically coherent and suitable for a reproducible research repository after minor documentation and portability adjustments. The main issues in the original versions were:

1. inconsistent version references such as `v5`, `v7`, and `v8`,
2. hardcoded local Windows paths,
3. markdown cells that described slightly different logic than the corresponding code,
4. a mismatch in the BiLSTM notebook between the architecture description and the implemented model,
5. an EBM export-name mismatch where the markdown referenced `ebm_v7_results.pkl`, while the original code primarily saved `results_ebm.pkl` and later `ebm_v5_results.pkl`.

The GitHub-ready notebook versions address these issues by standardizing path handling, clarifying markdown descriptions, and aligning export names with the actual code.

## 00_data_preparation.ipynb

### Status

The notebook is broadly consistent. The markdown description matches the code for loading data, computing financial ratios, applying the SME/activity filter, winsorization, lag/difference feature construction, and exporting model-ready datasets.

### Adjustments made

| Location | Issue | Adjustment |
|---|---|---|
| Class-imbalance section | The markdown suggested fixed class-imbalance handling choices for all downstream models. | The text was clarified: exported CSV files are not resampled; class imbalance is handled inside the model-specific notebooks. |
| Changelog section | The original wording was tied to an internal version history. | Replaced with general GitHub preparation notes. |

## 01_logit_benchmark.ipynb

### Status

The methodological description of the logistic benchmark is consistent with the implemented code: out-of-time split, literature-driven candidate variables, VIF filtering for continuous variables, full-rank checks, Logit-1 screening, iterative Logit-2 refitting, diagnostics, and export.

### Adjustments made

| Location | Issue | Adjustment |
|---|---|---|
| Introductory pipeline description | The markdown implied that missing ratios are recomputed from raw accounting items. | Clarified that existing engineered ratios from notebook 00 are preserved, missing required columns are created when possible, and remaining missing values are imputed from the training sample. |
| Data paths | The original code used a hardcoded local Windows path. | Replaced with environment-aware path handling using `DATA_DIR`. |
| Load-data description | The markdown overstated the ratio-filling step. | Reworded to match the code more precisely. |

## 03_ebm_pipeline.ipynb

### Status

The EBM notebook has a sound methodological structure but required several markdown and export-name corrections.

### Adjustments made

| Location | Issue | Adjustment |
|---|---|---|
| Introductory section | Export names were not fully aligned with the code. | The extended payload is saved as `ebm_v7_results.pkl`, with `ebm_v5_results.pkl` retained as a compatibility alias. |
| Optuna description | The markdown listed parameters not optimized by the code. | The text now lists the actual optimized parameters: `max_bins`, `learning_rate`, `interactions`, `max_leaves`, and `min_samples_leaf`. |
| Platt calibration | The markdown referred to validation log-odds. | Clarified that calibration is fitted on raw validation probabilities. |
| Top-k analysis | The markdown listed only selected cutoffs. | Updated to match the implemented cutoffs: 0.5%, 1%, 2%, 5%, and 10%. |
| Path handling | The extended payload used a local output path. | Replaced with portable path handling. |

## 04_bilstm_pipeline.ipynb

### Status

The BiLSTM notebook required the largest documentation correction because the original markdown did not fully reflect the implemented v8 architecture.

### Adjustments made

| Location | Issue | Adjustment |
|---|---|---|
| Architecture description | The markdown did not fully match the implemented model. | Updated to reflect the v8 model structure, including sequence length, industry embedding, static branch, recurrent layers, focal loss, balanced batches, and ensemble setup. |
| SHAP interpretation | The notebook needed clearer documentation of the interpretability step. | Added a clearer SHAP-oriented methodological description. |
| Path handling | Local or environment-specific path assumptions were clarified. | The notebook now uses `BASE_DIR` and can run locally or in Colab with fewer manual edits. |

## Final GitHub readiness checklist

- [x] Notebook markdown descriptions aligned with code logic.
- [x] Hardcoded local paths replaced or documented through environment variables.
- [x] Notebook outputs cleared.
- [x] Execution counts cleared.
- [x] Code cells passed static syntax checks.
- [x] Repository-level documentation added.
- [x] `.gitignore` excludes raw data, derived datasets, model artefacts, and large outputs.
- [x] MIT License added for code, notebooks, and documentation.
- [x] Data and generated artefacts explicitly excluded from the license scope.
