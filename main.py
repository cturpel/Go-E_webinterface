import pandas as pd
import streamlit as st
import time
import plotly.express as px

url = "http://XXX.XXX.XXX.XXX/api/status?filter=ccp,ccn"


while True:
    df = pd.read_json(url)
    chart_data = pd.DataFrame(df)
    chart_data = chart_data.iloc[:5]
    st.title("Go-E Controller Data")
    figure = px.bar(x=chart_data["ccn"], y=chart_data["ccp"], labels={"x": "Datapoint", "y": "Wh"})
    st.plotly_chart(figure)
    time.sleep(2)
    st.rerun()
