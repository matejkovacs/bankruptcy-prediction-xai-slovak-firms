# Methodology and interpretation

This guide describes the published implementation. It is not a claim that the current GitHub notebooks exactly reproduce every table in the thesis; that requires a thesis-to-run reconciliation.

## Mapping the research workflow

| Research component | Implementation | Evidence to retain from a run |
|---|---|---|
| Accounting data preparation | Notebook 00: ratios, firm controls, macro controls, filters, train-period winsorization | Input provenance, feature definitions, population counts |
| Econometric benchmark | Notebook 01: collinearity/rank checks, feature screening and refitting | Final coefficients, diagnostics, selected variables |
| Nonlinear interpretable model | Notebook 03: imbalance strategy selection, Optuna, calibration | Selected strategy, hyperparameters, shape functions, interactions |
| Sequential model | Notebook 04: history windows, recurrent architecture, ensemble | Seeds, selected ensemble, learning history, evaluation |
| Explainability | Logit coefficients; EBM terms; BiLSTM gradient SHAP | Exact model, feature space, explained sample and background sample |

## Evaluation protocol

The code splits observations by year: training 2013–2016, validation 2017 and test 2018–2019. Firms can appear in more than one period; this evaluates future observations within the panel, not a firm-disjoint generalization experiment.

The notebooks label `average_precision_score` as PR-AUC in several places. Report it explicitly as **average precision (AP)** when exporting a comparison table, so it is not confused with trapezoidal area under the precision–recall curve.

Ranking metrics, threshold metrics, probability calibration and top-k capture address different questions. Document whether each score uses raw or calibrated probabilities and how its threshold was chosen.

## Checks for reproducing the reported model ranking

1. **Align the evaluation population.** Sequence-history filtering can change which observations reach BiLSTM. Compare matched `(id, rok)` rows and report the sample size and positive count for each model.
2. **Confirm the operational prediction horizon.** The supplied thesis abstract defines failure as entry into bankruptcy or restructuring in the following period. The code consumes an existing `target`; the exact period length, event-date matching and label-construction procedure still need to be recorded from the original data/methodology.
3. **Check information availability.** Year splits alone do not prove the absence of look-ahead effects. Establish when financial statements and annual macro indicators were available.
4. **Keep test results out of model selection.** The notebooks display test metrics for multiple candidates. Selection is described in terms of validation metrics; preserve a record demonstrating that test inspection did not drive subsequent tuning.
5. **Account for validation reuse.** Hyperparameter selection, calibration and threshold setting reuse 2017 observations. Document this limitation; a future extension can use separate calibration data or chronological cross-fitting.
6. **Check panel-aware uncertainty.** Firm-year observations are dependent within firms. The current row-based bootstrap should not be presented as a firm-cluster bootstrap. Overlapping individual confidence intervals are not a paired test of a model difference.
7. **Treat missing-value encoding accurately.** EBM inputs replace missing entries with numeric `-999`. This is a sentinel, not automatically a native missing-value category. Its fitted behavior should be inspected.
8. **Check calendar gaps.** Row shifts within a firm are previous observations; without checking year differences, they are not necessarily one- or two-calendar-year lags.

## Explaining predictions

- Logit coefficients and odds ratios describe associations conditional on the fitted specification.
- EBM shape functions and interactions explain additive model terms. Calibration adds another transformation to the output.
- BiLSTM SHAP is computed for an additional single-seed explanatory model with a one-hot industry wrapper. It should not be described as an exact explanation of the five-seed isotonic-calibrated ensemble.
- These explanations do not establish causal effects.

## Results and remaining evidence

The [results page](RESULTS.md) now includes the thesis-reported EBM metrics and a Table 19-based explainability comparison. A complete reproduction package should additionally record model/version, sample size, positive count, calibration state, ROC-AUC, AP, Brier score and a common top-k capture rate for all three models. Add the original PR curve, an EBM shape-function example and a clearly labeled SHAP figure. Reference the exact thesis table/page and producing commit for each item.

The source excerpts establish what the thesis reports; they do not establish a fresh model run. Table 19's reference to an EBM five-seed ensemble differs from the published code's five-seed feature-stability assessment. See the [implementation distinctions](RESULTS.md#implementation-distinctions) before describing either model's ensemble or explanations.
