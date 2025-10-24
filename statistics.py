import streamlit as st, pandas as pd, plotly.express as px
from pathlib import Path
st.markdown("## Statistics")
data_dir = Path("data")

co_file = data_dir/"summary_comorbidity_premature.csv"
if co_file.exists():
    st.markdown("### Premature death rate by comorbidity")
    df = pd.read_csv(co_file)
    if len(df.columns) >= 2:
        fig = px.bar(df, x=df.columns[0], y=df.columns[1], color=df.columns[1], color_continuous_scale="Blues")
        fig.update_layout(height=420, margin=dict(l=0,r=0,t=10,b=0))
        st.plotly_chart(fig, use_container_width=True)

top_file = data_dir/"summary_top_causes_per_region.csv"
if top_file.exists():
    st.markdown("### ICD‑10 cause groups across regions")
    df = pd.read_csv(top_file)
    cols = {c.lower(): c for c in df.columns}
    group = next((cols[k] for k in cols if k in ["group","icd10","icd-10","category"]), None)
    region = next((cols[k] for k in cols if k in ["region","area","province"]), None)
    value = next((cols[k] for k in cols if k in ["value","deaths","count"]), None)
    if group and region and value:
        fig = px.bar(df, x=value, y=group, color=region, orientation="h")
        fig.update_layout(height=520, margin=dict(l=0,r=0,t=10,b=0))
        st.plotly_chart(fig, use_container_width=True)