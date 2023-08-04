import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_echarts import st_echarts
from streamlit_echarts import st_pyecharts

# Add a title and intro text
st.title('Novus Vote - Mando PreCampaña')
st.title('Votación en Bogotá por localidades para Alcaldía 2019 Vs Presidencial Uribismo 2018')
def render_basic_radar():
    option = {
        "title": {"text": "Previo Votación 🗳️"},
        "legend": {"data": ["Rodrigo Hernandez", "Top2.2019", "Top3.2019"]},
        "radar": {
            "indicator": [
                {"name": "Norte", "max": 10000},
                {"name": "Sur", "max": 10000},
                {"name": "Oriente", "max": 10000},
                {"name": "Occidente", "max": 10000},
                {"name": "Centro", "max": 10000},
            ]
        },
        "series": [
            {
                "name": "Votos por Zonas",
                "type": "radar",
                "data": [
                    {
                        "value": [5500, 5789, 8450, 5500, 7500],
                        "name": "Rodrigo Hernandez",
                    },
                    {
                        "value": [3500, 4500, 2500, 3500, 7000],
                        "name": "Top2.2019",
                    },
                    {
                        "value": [3000, 1500, 2000, 1800, 3000],
                        "name": "Top3.2019",
                    },
                ],
            }
        ],
    }
    st_echarts(option, height="500px")
ST_RADAR_DEMOS = {
    "Radar: Basic Radar": (
        render_basic_radar,
        "https://echarts.apache.org/examples/en/editor.html?c=radar",
    ),
}
render_basic_radar()
