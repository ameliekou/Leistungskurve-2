# Leistungskurve-2

- Diese Streamlit-App analysiert Leistungsdaten von Aktivitäten und erstellt eine interaktive Visualisierung der "Best Effort" Leistung über verschiedene Zeitintervalle. Die App nutzt Plotly zur Erstellung der Visualisierungen und ermöglicht es Benutzern, Leistungsdaten aus einer CSV-Datei zu analysieren.


## Erforderliche Bibliotheken installieren:
- numpy
- pandas
- streamlit
- plotly.express
- plotly.graph_objects


## Visualisierung
- Die App visualisiert die Daten mit Plotly Express. Die X-Achse zeigt die Zeitintervalle in Minuten und Sekunden, während die Y-Achse die Leistung in Watt anzeigt. Die X-Achse wird logarithmisch skaliert, um die unterschiedlichen Zeitintervalle besser darzustellen.


