# Bankruptcy Prediction with Explainable AI

**An empirical comparison of econometric, interpretable machine-learning and deep-learning approaches on Slovak firm data.**

[Key results](docs/RESULTS.md) · [Read the thesis](Diplomova_praca.pdf) · [Explore the notebooks](notebooks/README.md) · [Reproduce the workflow](docs/REPRODUCIBILITY.md) · [Slovenský prehľad](docs/PREHLAD_SK.md)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20029429.svg)](https://doi.org/10.5281/zenodo.20029429)
[![Code license: MIT](https://img.shields.io/badge/code_license-MIT-blue.svg)](LICENSE)

## Research question

How do logistic regression, an Explainable Boosting Machine (EBM), and a bidirectional LSTM compare when identifying firm failure from financial statements and firm histories?

This diploma-thesis project connects financial feature engineering, rare-event classification, chronological evaluation, probability calibration, and model interpretation. It examines both predictive ranking and how a model's predictions can be explained.

**Author:** Matej Kovács · **Institution:** University of Economics in Bratislava (EUBA), Faculty of National Economy, Department of Finance · **Year:** 2026

**Thesis:** *Metódy vysvetliteľnej umelej inteligencie v modelovaní zlyhania firiem na Slovensku*  
**Supervisor:** doc. Mgr. Marek Káčer, PhD.

## Key results from the thesis

**EBM captures 52.6% of future failures in the highest-risk 5% of the ranked population.** The thesis identifies it as the best overall balance of predictive performance and interpretability among the three approaches studied.

| EBM metric | Reported result, test 2018–2019 |
|---|---:|
| ROC-AUC | **0.882** |
| PR-AUC | **0.028** |
| KS statistic | **0.611** |
| Failure capture in top 5% | **52.6%** |

Source: the author's [abstract and conclusion](docs/THESIS_EXCERPTS.md). These are thesis-reported values, not a new reproduction run. The notebooks use average precision for the metric labeled PR-AUC. [Results and interpretation](docs/RESULTS.md) explain the evaluation scope and available evidence.

The project highlights a practical research finding: a directly interpretable nonlinear model can be more useful than a more complex neural model for these accounting data. BiLSTM contributes insight into the timing of risk signals; the abstract reports no statistically significant performance improvement over logistic regression.

## Project at a glance

| Dimension | Implementation |
|---|---|
| Data | Slovak Register of Financial Statements; firm-year panel, 2011–2019 |
| Target | Entry into bankruptcy or restructuring in the following period, as defined in the thesis |
| Preparation | Accounting ratios, firm characteristics, industry indicators, macroeconomic controls, lag and difference features |
| Training | 2013–2016 |
| Validation | 2017 |
| Test | 2018–2019 |
| Model families | Logistic regression · EBM · BiLSTM |
| Evaluation | ROC-AUC, average precision, calibration, threshold metrics and top-k capture |
| Interpretation | Logit coefficients · EBM shape functions and interactions · BiLSTM SHAP analysis |
| Public materials | Four source notebooks, thesis PDF, reported-results summary, environment specifications and documentation |

## Three complementary approaches

| Model | Role | Implemented techniques | Interpretation |
|---|---|---|---|
| **Logistic regression** | Econometric benchmark | Feature screening, collinearity and rank checks, model diagnostics | Coefficients and odds ratios |
| **EBM** | Interpretable nonlinear model | Sampling-strategy comparison, Optuna tuning, sigmoid calibration on validation probabilities | Additive shape functions and pairwise interactions |
| **BiLSTM** | Model of firm histories | Four-step windows, two recurrent layers, industry embedding, temporal attention, focal loss, balanced batches, five-seed ensemble and isotonic calibration | SHAP for a separately retrained explanatory model |

The SHAP analysis concerns the single-seed explanatory model; it is not a direct explanation of the complete calibrated ensemble. Details and evaluation caveats are in the [methodology guide](docs/METHODOLOGY.md).

## Explore the evidence

- **Start with the [results summary](docs/RESULTS.md)** for reported performance, a model comparison and an explanation of the top-5% finding.
- **Read the [thesis PDF](Diplomova_praca.pdf)** for the academic narrative and full empirical discussion.
- **Read the [notebooks](notebooks/README.md)** to inspect preprocessing, model fitting and evaluation code.
- **Use the [data specification](data/README.md)** and [reproduction guide](docs/REPRODUCIBILITY.md) to prepare a local run with authorized data.

The public notebooks have cleared outputs. The supplied thesis excerpts support the EBM headline values and qualitative model comparison; exact Logit/BiLSTM scores, full uncertainty estimates and result figures are not included in those excerpts. The [results summary](docs/RESULTS.md) preserves these distinctions.

## Workflow

```mermaid
flowchart TD
    A["Firm-year panel"] --> B["Preparation and feature engineering"]
    B --> C["Logistic regression"]
    B --> D["Explainable Boosting Machine"]
    B --> E["BiLSTM firm histories"]
    C --> F["Chronological evaluation and interpretation"]
    D --> F
    E --> F
```

| Order | Notebook | Main input |
|---|---|---|
| 1 | [Data preparation](notebooks/00_data_preparation.ipynb) | `firmy_dataset.csv` |
| 2 | [Logistic benchmark](notebooks/01_logit_benchmark.ipynb) | `data_logit_strict.csv` |
| 3 | [EBM pipeline](notebooks/03_ebm_pipeline.ipynb) | `data_ebm.csv` |
| 4 | [BiLSTM pipeline](notebooks/04_bilstm_pipeline.ipynb) | `data_rnn.csv` |

Run preparation first; the three model notebooks then use its exports independently. Notebook numbering preserves the original research sequence; there is no required notebook `02` in this package.

## Get started

Source data are not distributed. Reading the thesis, code and documentation requires no local setup.

To run the notebooks with authorized data, clone the repository and create an environment:

```bash
git clone https://github.com/matejkovacs/bankruptcy-prediction-xai-slovak-firms.git
cd bankruptcy-prediction-xai-slovak-firms
python -m venv .venv
```

Activate the environment:

| Platform | Command |
|---|---|
| Windows PowerShell | `.venv\Scripts\Activate.ps1` |
| Linux / macOS | `source .venv/bin/activate` |

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m jupyterlab
```

Place `firmy_dataset.csv` in the repository root, then open the notebooks in the order above. Alternatively, export `DATA_DIR` before launching Jupyter. BiLSTM also supports `BASE_DIR`. See [configuration and environment limitations](docs/REPRODUCIBILITY.md).

The dependency files specify version ranges, not a verified lockfile. Installing the environment alone does not establish that the thesis results have been reproduced.

## Repository guide

| Location | Contents |
|---|---|
| [Diplomova_praca.pdf](Diplomova_praca.pdf) | Thesis |
| [notebooks/](notebooks/) | Research implementation |
| [data/README.md](data/README.md) | Source format and derived datasets |
| [docs/RESULTS.md](docs/RESULTS.md) | Thesis-reported metrics, findings and explainability comparison |
| [docs/thesis_reported_metrics.json](docs/thesis_reported_metrics.json) | Machine-readable values with provenance |
| [docs/](docs/) | Source excerpts, methodology, reproduction instructions and review notes |
| [outputs/README.md](outputs/README.md) | Generated artifact inventory |
| [requirements.txt](requirements.txt) / [environment.yml](environment.yml) | pip / conda environment specifications |
| [.env.example](.env.example) | Configuration reference; not automatically loaded |
| [CITATION.cff](CITATION.cff) | Machine-readable software citation |

## Reuse and citation

The repository's existing [MIT license](LICENSE) covers the code, notebooks and documentation as described in this package. Raw data, derived datasets and model artifacts are not distributed under that license. See the [data notes](data/README.md).

For the archived software version, use the existing citation:

> Kovacs, M. (2026). *XAI Pipelines for Bankruptcy Prediction of Slovak Firms* (Version 1.0.0) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.20029429

The GitHub default branch may contain later maintenance changes. Record the exact commit when referring to a particular implementation. This is a research project; deployment performance has not been established.
