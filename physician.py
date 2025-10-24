import streamlit as st, pandas as pd, numpy as np, plotly.graph_objects as go
from pathlib import Path

st.markdown("## Physician")

# Mock patient record (demo only)
left, right = st.columns([2,1])
with left:
    st.markdown("**Patient ID:** P-000118")
    st.markdown("**Name:** John Doe")
    st.markdown("**Age:** 45")
    st.markdown("**Gender:** Male")
    st.markdown("**Cancer family history:** Yes")
with right:
    st.markdown("**Last visit:** 2024‑10‑10")
    st.markdown("**Region:** Riyadh")
    st.markdown("**Comorbidities:** Diabetes, Hypertension")

# Simple composite risk (demo)
risk = 0.58
fig = go.Figure(go.Indicator(mode="gauge+number", value=round(risk*100,1),
    number={"suffix":"%","font":{"size":32}},
    gauge={
        "axis":{"range":[0,100]},
        "bar":{"color":"#19A7B8"},
        "steps":[{"range":[0,50],"color":"#E6F9FC"},{"range":[50,70],"color":"#BFEAF2"},{"range":[70,100],"color":"#FDB3B3"}],
        "threshold":{"line":{"color":"#ff4d4f","width":4},"thickness":0.75,"value":round(risk*100,1)}
    }
))
fig.update_layout(height=320, margin=dict(l=10,r=10,t=10,b=10))
st.plotly_chart(fig, use_container_width=True)

if risk>=0.7:
    st.error("High risk detected for cancer. Recommend immediate screening.", icon="⚠️")
elif risk>=0.5:
    st.warning("Moderate risk. Consider targeted screening and follow‑up.", icon="⚠️")
else:
    st.success("Low risk. Continue routine monitoring.", icon="✅")