# Data Science Demo Pipeline

Dieses Projekt zeigt eine End-to-End Machine Learning Pipeline für die Rolle Data Scientist (ML & Advanced Analytics).

## Inhalt

- **data/**: simulierte DWH-Tabelle (`dwh_table.csv`)
- **output/**: ETL-Ausgabe, Vorhersagen, gespeichertes Modell, Dashboard und Plots
- **dags/**: Beispiel Airflow DAG für Orchestrierung
- **docs/**: zusätzliche Dokumentation

## Schritte im Workflow

1. **Datenextraktion** aus einem simulierten DWH-Export (CSV-Datei).
2. **ETL/Feature Engineering**: Handling von Missing Values, Lags, Rolling Means, Kalender-Features.
3. **Modelltraining & Backtesting**: Walk-Forward-Strategie mit RandomForestRegressor, Metriken (MAE, RMSE).
4. **Deployment-Artefakte**: Speichern von Modell, Predictions, Metriken.
5. **Dashboard**: Kleine HTML-Seite mit Metriken und Plots.
6. **Orchestrierung**: Beispielhafter Airflow DAG.

## Installation

```bash
pip install -r requirements.txt
```

## Ausführung

Die Hauptlogik ist in `pipeline_demo.py` (nicht enthalten in diesem Export). Für Reproduktion siehe Notebooks oder eigene Skripte.


