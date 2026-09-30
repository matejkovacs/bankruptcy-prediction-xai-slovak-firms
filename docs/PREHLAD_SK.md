# Predikcia zlyhania slovenských podnikov pomocou vysvetliteľnej AI

Projekt k diplomovej práci porovnáva tri prístupy: logistickú regresiu, Explainable Boosting Machine a sekvenčný model BiLSTM. Spája spracovanie účtovných dát, modelovanie zriedkavých udalostí a interpretáciu predikcií.

[Výsledky](RESULTS.md) · [Diplomová práca](../Diplomova_praca.pdf) · [Notebooky](../notebooks/README.md) · [Návod na spustenie](REPRODUCIBILITY.md)

## Hlavné výsledky diplomovej práce

Na testovacom období **2018–2019** dosiahol EBM tieto výsledky:

| Metrika | Hodnota |
|---|---:|
| ROC-AUC | **0,882** |
| PR-AUC | **0,028** |
| KS štatistika | **0,611** |
| Zachytené zlyhania v najrizikovejších 5 % | **52,6 %** |

Zdrojom je [abstrakt a záver dodaný autorom](THESIS_EXCERPTS.md). Ide o výsledky uvedené v diplomovej práci, nie o nový výpočet.

EBM podľa záveru práce poskytol najlepší kompromis medzi výkonnosťou a interpretovateľnosťou. Logistická regresia zostáva transparentným ekonometrickým benchmarkom. BiLSTM priniesol poznatky o časovom vývoji rizikových signálov; abstrakt neuvádza štatisticky významné zlepšenie oproti logistickej regresii.

Zachytenie 52,6 % zlyhaní pri výbere 5 % zodpovedá približne **10,5-násobnému zachyteniu oproti náhodnému výberu** rovnakého podielu. Je to odvodený pomer zo zaokrúhlených hodnôt, nie presnosť predikcií.

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

Začni [prehľadom výsledkov](RESULTS.md), potom si pozri plnú prácu a implementáciu v notebookoch. Výskum vychádza z Registra účtovných závierok; zlyhanie znamená vstup do konkurzu alebo reštrukturalizácie v nasledujúcom období. Presná dĺžka horizontu nie je v dodaných úryvkoch uvedená.

Verejné notebooky majú vymazané výstupy a zdrojový dataset nie je súčasťou repozitára. Dodané úryvky neobsahujú číselné výsledky Logitu a BiLSTM, Brierove skóre, úplné intervaly spoľahlivosti ani finálne grafy. Výsledky sú viazané na slovenské dáta a obdobie 2018–2019; stabilita počas neskorších kríz je témou pre nadväzujúci výskum.

Metodické podmienky porovnávania modelov a hranice interpretácie sú uvedené v [metodickom prehľade](METHODOLOGY.md). Úspešná inštalácia balíkov ani statická kontrola kódu nenahrádzajú reprodukciu výsledkov na pôvodných dátach.
