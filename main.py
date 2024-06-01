import streamlit as st
import pandas as pd
import functions as chart

def main():
    df = pd.read_csv("activities/activity.csv")
    fig, Leistungskurve = chart.create_chart(df)

    st.plotly_chart(fig)
    st.write("Best Effort: ", Leistungskurve)

if __name__ == "__main__":
    main()