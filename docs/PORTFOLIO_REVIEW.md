# Repository review — 2026-09-30

Review baseline: commit `1878e78f7a5216af427640e639c2c6b1b7bf138e`.

## Confirmed strengths

- Four substantial notebooks covering preparation, econometric modeling, interpretable ML and sequence learning.
- Chronological split implemented across model notebooks.
- Thesis PDF, software citation metadata and an existing code license.
- Calibration, rare-event evaluation and explainability are present in code.

## Maintenance changes

- Replaced an inaccurate root-level file listing with working notebook links and a research-oriented project overview.
- Added missing ignore rules, environment-variable reference and line-ending configuration.
- Made preparation and EBM honor `DATA_DIR`; made local notebook paths work from the root or notebook directory; gave BiLSTM a `DATA_DIR` fallback.
- Added a precise source-file format description, model-to-method mapping and Slovak overview.
- Added lightweight notebook compilation/output checks.
- Replaced an unconditional EBM superiority statement with a requirement for an aligned, verified comparison.
- Marked the older upload audit as historical rather than treating its checklist as current evidence.

## Verification scope and remaining work

The maintenance review inspected repository metadata, documentation and all four notebook sources. It did not have an executable local Python environment, source data or readable thesis text. The repository's PDF was located, but its content could not be retrieved for comparison with the attachment. No empirical performance values or thesis-page mappings were independently verified.

The dependency files remain broad ranges; environment compatibility and end-to-end execution remain unverified. The new automated check compiles cells without training models.

Before presenting the project as a fully reproduced thesis result, add verified aggregate metrics and figures, reconcile them to thesis tables/pages and an exact run, preserve a tested environment, and resolve the evaluation questions in [METHODOLOGY.md](METHODOLOGY.md).

## GitHub presentation settings

At review time the repository was public and had a useful description, but no topics or homepage. The main branch was unprotected. These settings were inspected; this maintenance change does not modify account or repository administration.

Suggested topics: `bankruptcy-prediction`, `explainable-ai`, `machine-learning`, `econometrics`, `interpretml`, `lstm`, `shap`, `slovakia`, `masters-thesis`.

Pin this repository on the author's profile. A suitable profile bio is: “Data analytics & machine learning | Financial data, econometrics and explainable AI | Slovakia”. Add a portfolio or professional-profile URL only when supplied by the author. Consider branch protection once an automated check is confirmed working.
