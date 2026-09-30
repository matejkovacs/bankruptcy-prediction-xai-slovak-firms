# Predikcia zlyhania slovenských podnikov pomocou vysvetliteľnej AI

Projekt k diplomovej práci porovnáva tri prístupy: logistickú regresiu, Explainable Boosting Machine a sekvenčný model BiLSTM. Spája spracovanie účtovných dát, modelovanie zriedkavých udalostí a interpretáciu predikcií.

[Diplomová práca](../Diplomova_praca.pdf) · [Notebooky](../notebooks/README.md) · [Návod na spustenie](REPRODUCIBILITY.md)

## Čo projekt ukazuje

| Oblasť | Implementácia |
|---|---|
| Dátová príprava | Finančné pomery, charakteristiky podnikov, odvetvia, makroekonomické premenné a historické príznaky |
| Ekonometria | Logistický benchmark, diagnostika kolinearity, koeficienty a odds ratios |
| Strojové učenie | EBM, výber stratégie pri nevyvážených triedach a optimalizácia hyperparametrov |
| Hlboké učenie | BiLSTM, embedding odvetvia, attention, focal loss a ensemble piatich behov |
| Hodnotenie | Časové rozdelenie, diskriminácia, kalibrácia a zachytenie zlyhaní medzi najrizikovejšími pozorovaniami |
| Vysvetliteľnosť | EBM shape functions a interakcie; SHAP samostatného vysvetľujúceho neurónového modelu |

Tréning používa roky **2013–2016**, validácia **2017** a test **2018–2019**.

## Ako projekt posudzovať

Najprv si pozri akademické výsledky v PDF, následne implementáciu v notebookoch. Verejné notebooky majú vymazané výstupy a zdrojový dataset nie je súčasťou repozitára. Samostatná overená výsledková tabuľka a finálne grafy zatiaľ nie sú zverejnené.

Metodické podmienky porovnávania modelov a hranice interpretácie sú uvedené v [metodickom prehľade](METHODOLOGY.md). Úspešná inštalácia balíkov ani statická kontrola kódu nenahrádzajú reprodukciu výsledkov na pôvodných dátach.
