# Thesis source excerpts

Source: author-supplied text from the abstract, Table 19 and conclusion, provided on 2026-09-30. This is a selected text record for tracing the portfolio summary, not a transcription of the entire PDF. Formatting has been normalized. Page numbers and the complete numerical model-comparison table were not supplied.

## Bibliographic information

**KOVÁCS, Matej (2026).** *Metódy vysvetliteľnej umelej inteligencie v modelovaní zlyhania firiem na Slovensku.*

Ekonomická univerzita v Bratislave, Národohospodárska fakulta, Katedra financií. Vedúci záverečnej práce: doc. Mgr. Marek Káčer, PhD. Bratislava: NHF EU.

## Abstract — original Slovak text

Diplomová práca sa zaoberá využitím metód vysvetliteľnej umelej inteligencie pri predikcii zlyhania slovenských podnikov. Cieľom práce je empiricky posúdiť, či moderné prístupy XAI dokážu zlepšiť diskriminačnú schopnosť a interpretovateľnosť predikčných modelov v porovnaní s tradičnou logistickou regresiou. Analýza vychádza z účtovných údajov slovenských podnikov z Registra účtovných závierok za obdobie rokov 2011 až 2019. Zlyhanie podniku je definované ako vstup do konkurzu alebo reštrukturalizácie v nasledujúcom období. Výskumná časť porovnáva tri modelové prístupy: logistickú regresiu ako transparentný ekonometrický benchmark, Explainable Boosting Machine ako vnútorne interpretovateľný nelineárny model a sekvenčný model BiLSTM doplnený o SHAP vysvetlenia. Modely sú hodnotené na testovacom období rokov 2018 až 2019 pomocou metrík ROC-AUC, PR-AUC, KS štatistiky, Brierovho skóre a top-k capture analýzy. Výsledky ukazujú, že najvyššiu diskriminačnú schopnosť dosahuje model EBM s hodnotou ROC-AUC 0,882, PR-AUC 0,028 a KS štatistikou 0,611. EBM zároveň v horných 5 % najrizikovejších podnikov zachytáva viac ako polovicu budúcich zlyhaní. BiLSTM prináša dodatočnú hodnotu najmä v časovej interpretácii rizikových signálov, no jeho výkonnosť nie je štatisticky významne vyššia než výkonnosť logistickej regresie. Práca dospieva k záveru, že vysvetliteľné nelineárne modely môžu pri predikcii zlyhania slovenských podnikov priniesť lepší kompromis medzi predikčnou výkonnosťou, transparentnosťou a praktickou využiteľnosťou než tradičné lineárne modely.

**Kľúčové slová:** zlyhanie podnikov, vysvetliteľná umelá inteligencia, Explainable Boosting Machine, logistická regresia, BiLSTM, SHAP, kreditné riziko, predikčné modelovanie.

## Conclusion — selected original passages

> Najvyššiu výkonnosť dosiahol model EBM, ktorý na testovacom období rokov 2018 až 2019 dosiahol ROC-AUC 0,882, PR-AUC 0,028 a KS štatistiku 0,611. Zároveň v horných 5 % najrizikovejších podnikov zachytil 52,6 % všetkých budúcich zlyhaní.

> Logistická regresia síce dosiahla nižšiu výkonnosť, no potvrdila význam transparentného a ekonomicky interpretovateľného benchmarku. BiLSTM priniesol pridanú hodnotu najmä pri interpretácii časového vývoja rizikových signálov, avšak jeho celková diskriminačná schopnosť neprekonala EBM.

> Tento model poskytol najlepší kompromis medzi predikčnou výkonnosťou, interpretovateľnosťou a praktickou použiteľnosťou.

> Medzi hlavné obmedzenia práce patrí viazanosť výsledkov na slovenské podnikové dáta a testovacie obdobie 2018 až 2019, ktoré nezachytáva neskoršie krízové šoky. Budúci výskum by mal overiť stabilitu modelov na dlhšom časovom horizonte a v krízových obdobiach.

## Table 19 — selected source rows

The following rows preserve the supplied table's descriptions. An implementation-aware English comparison and notes on the five-seed distinction appear in [RESULTS.md](RESULTS.md).

| Vlastnosť | Logit | BiLSTM | EBM |
|---|---|---|---|
| Typ interpretovateľnosti | Intrinsická | Post-hoc (SHAP) | Intrinsická |
| Linearita | Lineárna (log-odds) | Nelineárna (LSTM) | Nelineárna (shape fn.) |
| Interakcie medzi premennými | Manuálny cross-term | Implicitne cez stav LSTM | Automatické párové (8 inter.) |
| Temporálna dynamika | Nie | Áno (seq_len=4, T-2 dominantný) | Nie |
| Globálny prehľad | Odds ratio, CI | SHAP feature importance | Shape funkcie fⱼ(xⱼ) |
| Lokálne vysvetlenie | Aditívne skóre | SHAP waterfall / lokálny príklad | Aditívny lokálny profil |
| Interpretácia nelinearít | Nie | Obmedzená (black-box LSTM) | Áno (tvar shape funkcie) |
| Stabilita vysvetlení | Vysoká | Stredná (závislosť od seedu) | Vysoká (ensemble 5 seedov) |

The source table also contains an auditability row. The portfolio comparison focuses on the model's inspectable mechanisms and makes no regulatory-certification claim.

## Evidence boundaries

These excerpts support the reported EBM numbers and the thesis's qualitative conclusions. They do not provide Logit/BiLSTM metric values, Brier scores, test population counts, calibration state of the reported scores, confidence intervals, p-values, or the original producing commit. The abstract's statistical-significance statement is attributed to the thesis and has not been independently re-tested.
