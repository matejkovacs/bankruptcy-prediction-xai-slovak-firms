# Source data and file format

Raw data are not included. The [thesis abstract](../docs/THESIS_EXCERPTS.md) identifies the source as Slovakia's Register of Financial Statements (Register účtovných závierok), covering 2011–2019. Use an authorized copy of the original source panel; a generic export may not match its construction or schema.

## Parser contract

Notebook 00 reads `firmy_dataset.csv` with:

- comma delimiter (the pandas default);
- **three leading rows skipped** using `skiprows=3`;
- **48 positional columns**, assigned the names below;
- attempted encodings: UTF-8 with BOM, UTF-8, CP1250, Latin-1.

A CSV with one ordinary header row will lose observations under this parser. Adapt the import explicitly for a different format. Confirm the delimiter, column order, units and number of skipped rows before fitting models.

| Position | Column |
|---|---|
| 1 | `id` |
| 2 | `rok` |
| 3 | `target` |
| 4 | `sk_nace` |
| 5 | `pocet_zamestnancov` |
| 6 | `pravna_forma` |
| 7 | `celkove_aktiva` |
| 8 | `dlhodoby_nehmotny_majetok` |
| 9 | `dlhodoby_hmotny_majetok` |
| 10 | `obezne_aktiva` |
| 11 | `zasoby` |
| 12 | `obchodne_pohladavky` |
| 13 | `peniaze` |
| 14 | `vlastne_imanie` |
| 15 | `zakladne_imanie` |
| 16 | `nerozdeleny_zisk` |
| 17 | `celkove_zavazky` |
| 18 | `dlhodobe_zavazky` |
| 19 | `dlhodobe_obch_zavazky` |
| 20 | `dlhodobe_danove_dlhy` |
| 21 | `kratkodobe_zavazky` |
| 22 | `obchodne_zavazky` |
| 23 | `kratkodobe_danove_dlhy` |
| 24 | `kratkodobe_financne_vypomoci` |
| 25 | `bankove_uvery_dlhodobe` |
| 26 | `bankove_uvery_kratkodobe` |
| 27 | `celkove_trzby` |
| 28 | `trzby_spolu` |
| 29 | `odpisy` |
| 30 | `vysledok_hospodarenia_z_hospodarskej_cinnosti` |
| 31 | `trzby_z_predaja_cennych_papierov_a_podielov` |
| 32 | `predane_cenne_papiere_a_podiely` |
| 33 | `vynosy_z_dhodobeho_financneho_majetku` |
| 34 | `vynosy_z_kratkodobeho_financneho_majetku` |
| 35 | `naklady_na_kratkodoby_financny_majetok` |
| 36 | `vynosy_z_precenenia_cennych_papierov_a_vynosy_z_derivatovych_operacii` |
| 37 | `naklady_na_precenenie_cennych_papierov_a_naklady_na_derivatove_operacie` |
| 38 | `tvorba_a_zauctovanie_opravnych_poloziek_k_financnemu_majetku` |
| 39 | `vynosove_uroky` |
| 40 | `nakladove_uroky` |
| 41 | `kurzove_zisky` |
| 42 | `kurzove_straty` |
| 43 | `ostatne_vynosy_z_financnej_cinnosti` |
| 44 | `ostatne_naklady_na_financnu_cinnost` |
| 45 | `celkove_dane` |
| 46 | `ebt` |
| 47 | `cisty_zisk_strata` |
| 48 | `datum_vzniku` |

The import treats `id`, `sk_nace`, `pravna_forma` and `datum_vzniku` as text-like fields and coerces other fields to numeric. Later code may cast identifiers to integers. Verify identifier compatibility, unique `(id, rok)` pairs, valid years and binary targets before execution. Industry handling in notebook 00 expects textual category names.

The thesis defines failure as entry into bankruptcy or restructuring in the following period. The source supplies `target`; the excerpts do not specify the exact period length, event-date matching or label-construction procedure. Record these operational details from the original data/methodology before reproduction.

## Generated datasets

| File | Consumer |
|---|---|
| `data_logit.csv` / `data_logit_strict.csv` | Logistic-regression benchmark; compatibility exports |
| `data_ebm.csv` | EBM |
| `data_rnn.csv` | BiLSTM |
| `logit_train_medians.pkl` | Logit preparation provenance |
| `rnn_train_medians.pkl` | RNN preparation provenance |

Files are written to `DATA_DIR`, defaulting locally to the repository root. These derived files are ignored by Git.

The repository's MIT license does not grant rights to the source dataset or generated data. Record source provenance and access terms independently.
