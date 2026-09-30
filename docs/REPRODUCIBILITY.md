# Reproducing the workflow

## What this package provides

The repository provides the source implementation, thesis and a [summary of thesis-reported results](RESULTS.md) transcribed from author-supplied excerpts. Raw inputs, executed result notebooks, a tested dependency lockfile and a complete numerical comparison of all three models are not included. Full numerical reproduction therefore requires authorized data and a verified environment.

## 1. Prepare an environment

From the repository root, use the pip instructions in [README](../README.md), or:

```bash
conda env create -f environment.yml
conda activate bankruptcy-xai
python -m jupyterlab
```

The conda file selects Python 3.10. Dependency ranges are not a record of the exact thesis runtime. In particular, the BiLSTM uses Keras API features such as `LSTM(use_cudnn=False)`; the declared TensorFlow lower bound should not be treated as a verified compatibility guarantee. Validate the chosen TensorFlow/Keras combination before starting the expensive model search. After a successful run, preserve `python -m pip freeze` and hardware details with the run record.

## 2. Supply the source file

Place `firmy_dataset.csv` in the repository root, or set `DATA_DIR` to an absolute directory containing it. Follow the [input format](../data/README.md): a generic CSV with a single header row is not a drop-in replacement.

Default local path resolution works when the notebook kernel starts in the repository root or `notebooks/`. Launching Jupyter from the root does not by itself guarantee the kernel working directory.

Linux / macOS:

```bash
export DATA_DIR="/absolute/path/to/data"
python -m jupyterlab
```

Windows PowerShell:

```powershell
$env:DATA_DIR = "C:\path\to\data"
python -m jupyterlab
```

Set these variables before launching the kernel; restart an existing kernel after changes. `.env.example` is a reference, not an automatic configuration loader.

For BiLSTM, precedence is `BASE_DIR` → `DATA_DIR` → local repository root. In Colab, the final fallback remains `/content/drive/MyDrive/BILSTM` after mounting Drive. Use the same data directory across all four notebooks unless deliberately copying their inputs.

## 3. Execute in order

1. [00_data_preparation.ipynb](../notebooks/00_data_preparation.ipynb)
2. [01_logit_benchmark.ipynb](../notebooks/01_logit_benchmark.ipynb)
3. [03_ebm_pipeline.ipynb](../notebooks/03_ebm_pipeline.ipynb)
4. [04_bilstm_pipeline.ipynb](../notebooks/04_bilstm_pipeline.ipynb)

Use a fresh kernel for each notebook and run all cells in order. Preparation exports four CSV files; models consume their corresponding exports. Outputs are written beside inputs, with BiLSTM-specific files under `BASE_DIR/bilstm_v8/`. The repository `outputs/` directory is documentation and is not automatically used by every notebook.

## 4. Record the experiment

| Item | Record |
|---|---|
| Source | Exact Git commit and input-file checksum |
| Data | Provenance, target definition, horizon, extraction date and reporting availability |
| Population | Filters, row counts, unique firms and positives for every split/model |
| Runtime | Python, installed dependencies, operating system, CPU/GPU |
| Configuration | SME filter mode, features, hyperparameters and seeds |
| Evaluation | Raw/calibrated probabilities, thresholds, metrics and uncertainty method |

Split years are train **2013–2016**, validation **2017**, test **2018–2019**. The common seed is **42**; BiLSTM uses **42, 7, 1337, 2025, 99**. Hardware and dependency differences may change results.

Chronological splitting is only one part of leakage control. Confirm target timing and feature availability, and compare models on aligned firm-year observations. See [methodology](METHODOLOGY.md).

## 5. Public verification

The repository check compiles notebook code cells and verifies that saved outputs remain cleared. It does not execute models, validate dependency compatibility or certify the empirical results.

```bash
python scripts/check_notebooks.py
```

Derived data and models are excluded by [.gitignore](../.gitignore). Ignore rules protect future untracked files; they do not remove anything already committed. Publish only reviewed aggregate tables and figures with explicit provenance.
