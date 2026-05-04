# Outputs directory

This directory is reserved for local model outputs, figures, diagnostics, and trained-model artefacts. Generated outputs are ignored by default and should not be committed to GitHub unless they are small, anonymized, and intended for publication.

Typical generated outputs include:

| File or directory | Origin |
|---|---|
| `logit_v7_results.pkl` | logistic-regression results payload |
| `logit_v7_results.json` | compact logistic-regression results export |
| `results_ebm.pkl` | base EBM results payload |
| `ebm_v7_results.pkl` | extended EBM results payload |
| `ebm_v5_results.pkl` | compatibility alias for EBM results |
| `ebm_results.png` | EBM visual outputs |
| `ebm_shape_functions.png` | selected EBM shape functions |
| `bilstm_v7_results.pkl` | compatible BiLSTM results export |
| `bilstm_v8/` | BiLSTM models, checkpoints, and auxiliary outputs |

If selected outputs are published, prefer final figures or compact tables rather than full `.pkl`, `.h5`, `.keras`, or checkpoint files.

## Licensing note

Generated artefacts may contain information derived from the raw dataset. They are not automatically covered by the repository MIT License and should be reviewed before publication.
