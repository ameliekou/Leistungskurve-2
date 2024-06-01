import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

zeit_werte = [1, 2, 5, 10, 20, 30, 60, 120, 180, 300, 600, 1200, 1600]

def best_effort(df):
    Leistungskurve = []
    df_cleaned = df.dropna(subset=["PowerOriginal"])

    for intervall in zeit_werte:
        rolling_mean = df_cleaned["PowerOriginal"].rolling(window=intervall).mean()
        max_durchschnitt = rolling_mean.max()
        Leistungskurve.append(max_durchschnitt)

    return zeit_werte, Leistungskurve

def create_chart(df):
    zeit_werte, Leistungskurve = best_effort(df)
    fig = px.line(x=zeit_werte, y=Leistungskurve, title="Leistungskurve II", log_x=True)
    fig.update_xaxes(title_text="Zeit in Minuten:Sekunden")
    fig.update_yaxes(title_text="Leistung in Watt")
    fig.add_trace(go.Scatter(x=zeit_werte, y=Leistungskurve, mode="none"))
    fig.update_layout(
        xaxis=dict(
            tickmode="array",
            tickvals=zeit_werte,
            ticktext=[f"{i//60}:{i%60}" for i in zeit_werte],
            tickangle=45  # Rotate the x-axis labels
            
        )
    )
    return fig, Leistungskurve