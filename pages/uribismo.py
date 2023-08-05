import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_echarts import st_echarts
from streamlit_echarts import st_pyecharts

# Add a title and intro text
st.title('Novus Vote 🗳️ Mando PreCampaña')
st.title('Votación histrórica en Bogotá por localidades')
st.header('Votos Uribistas al Congreso y Presidencia 2018')
def render_basic_radar():
    option = {
        "title": {"text": "🗳️"},
        "legend": {"data": ["CD_Cámara_2018", "CD_Senado_2018", "CD_Presi_2018_1", "CD_Presi_2018_2"]},
        "radar": {
            "indicator": [
                {"name": "Usaquén", "max": 142000},
                {"name": "Chapinero", "max": 142000},
                {"name": "SantaFé", "max": 142000},
                {"name": "SanCristobal", "max": 142000},
                {"name": "Usme", "max": 142000},
                {"name": "Tunjuelito", "max": 142000},
                {"name": "Bosa", "max": 142000},
                {"name": "Kennedy", "max": 142000},
                {"name": "Fontibon", "max": 142000},
                {"name": "Engativá", "max": 142000},
                {"name": "Suba", "max": 142000},
                {"name": "BarriosUnidos", "max": 142000},
                {"name": "Teusaquillo", "max": 142000},
                {"name": "Mártires", "max": 142000},
                {"name": "A.Nariño", "max": 142000},
                {"name": "PuenteAranda", "max": 142000},
                {"name": "Candelaria", "max": 142000},
                {"name": "RafaelUribe", "max": 142000},
                {"name": "C.Bolivar", "max": 142000},
                {"name": "Sumapaz", "max": 142000},
            ]
        },
        "series": [
            {
                "name": "Votos por Zonas",
                "type": "radar",
                "data": [
                    {
                        "value": [41805, 16516, 3910, 10960, 8972, 7507, 16577, 32557, 14405, 33250, 50312, 11049, 12849, 4926, 6157, 13816, 1934, 12890, 17193, 20],
                        "name": "CD_Cámara_2018",
                    },
                    {
                        "value": [49000, 19427, 4611, 13228, 10880, 9156, 20217, 39371, 17536, 40024, 59549, 13251, 15500, 5809, 7469, 16524, 2272, 15375, 20168, 44],
                        "name": "CD_Senado_2018",
                    },
                    {
                        "value": [52074, 19291, 7167, 22504, 21263, 14697, 35214, 62239, 23970, 54691, 71106, 15821, 16495, 9196, 11073, 23476, 3367, 25318, 38290, 156],
                        "name": "CD_Presi_2018_1",
                    },
                    {
                        "value": [93918, 32843, 14102, 47474, 42737, 29908, 71009, 125169, 47346, 113650, 141800, 31327, 31295, 16813, 21321, 45782, 6591, 50580, 75825, 256],
                        "name": "CD_Presi_2018_2",
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


st.header('Votos Aspirantes Alcaldía Bog 2019')
