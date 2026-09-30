# Research notebooks

| Order | Notebook | Purpose |
|---|---|---|
| 1 | [00_data_preparation.ipynb](00_data_preparation.ipynb) | Load the source panel, engineer features and export model inputs |
| 2 | [01_logit_benchmark.ipynb](01_logit_benchmark.ipynb) | Estimate and diagnose the logistic-regression benchmark |
| 3 | [03_ebm_pipeline.ipynb](03_ebm_pipeline.ipynb) | Compare imbalance strategies, tune and interpret EBM |
| 4 | [04_bilstm_pipeline.ipynb](04_bilstm_pipeline.ipynb) | Train sequence models, calibrate the ensemble and run single-model SHAP |

Run preparation first. The model notebooks can then be run independently. Numbering retains the research project's original names; no notebook 02 is needed.

Local defaults detect the repository root when the kernel starts in the repository or its `notebooks/` directory. Set an absolute `DATA_DIR` for another data location. BiLSTM uses `BASE_DIR` when set, otherwise `DATA_DIR`, otherwise its environment-specific default.

The source notebooks intentionally have no saved cell outputs. Read the [reproduction guide](../docs/REPRODUCIBILITY.md) before running, and the [methodology guide](../docs/METHODOLOGY.md) before interpreting comparisons. References inside notebooks to a downstream comparison/stacking notebook describe a separate research artifact that is not currently included here.

Code is covered by the repository [MIT license](../LICENSE). Source data and generated artifacts are outside the documented license scope.
