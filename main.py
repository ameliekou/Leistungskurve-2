import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

zeit_werte = [1, 2, 5, 10, 20, 30, 60, 120, 300, 600, 1200, 1800]


def best_effort(df):
    Leistungskurve = []
    df_cleaned = df.dropna(subset = ["PowerOriginal"])

    for intervall in zeit_werte:
        rolling_mean = df_cleaned["PowerOriginal"].rolling(window=intervall).mean()
        max_durchschnitt = rolling_mean.max()
        Leistungskurve.append(max_durchschnitt)

    return zeit_werte, Leistungskurve

df = pd.read_csv("activities/activity.csv")
t_end = len(df["PowerOriginal"])
df["Time in s"] = np.arange(0, t_end)


zeit_werte, Leistungskurve = best_effort(df)
fig = px.line(x=zeit_werte, y=Leistungskurve, title="Best Effort", log_x = True)
fig.update_xaxes(title_text="Zeit in Minuten:Sekunden")
fig.update_yaxes(title_text="Leistung in Watt")
fig.add_trace(go.Scatter(x=zeit_werte, y=Leistungskurve, mode="none"))  
fig.update_layout(xaxis=dict(tickmode = "array", tickvals = zeit_werte, ticktext = [f"{i//60}:{i%60}" for i in zeit_werte]))

st.plotly_chart(fig)
st.write("Best Effort: ", Leistungskurve)