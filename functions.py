import numpy as np


zeit_werte = [1, 2, 5, 10, 20, 30, 60, 120, 300, 600, 1200, 1800]


def best_effort(df):
    Leistungskurve = []
    df_cleaned = df.dropna(subset = ["PowerOriginal"])

    for intervall in zeit_werte:
        rolling_mean = df_cleaned["PowerOriginal"].rolling(window=intervall).mean()
        max_durchschnitt = rolling_mean.max()
        Leistungskurve.append(max_durchschnitt)

    return zeit_werte, Leistungskurve