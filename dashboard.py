import streamlit as st, pandas as pd, plotly.express as px
from pathlib import Path

st.markdown("## Dashboard")
data_dir = Path("data")

def kpi(label, value):
    st.markdown('<div class="baqa-card">', unsafe_allow_html=True)
    st.markdown(f'<div class="kpi-big">{value}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="kpi-sub">{label}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Choropleth map
nat_file = data_dir/"summary_premature_by_nationality.csv"
if nat_file.exists():
    df = pd.read_csv(nat_file)
    cols = {c.lower(): c for c in df.columns}
    country_col = next((cols[k] for k in cols if k in ["country","nationality","location","iso3","iso"]), None)
    value_col = next((cols[k] for k in cols if k in ["cases","count","premature","value","deaths","incidence"]), None)
    c1,c2 = st.columns([2.2,1])
    if country_col and value_col:
        with c1:
            if country_col.lower() in ["iso3","iso"]:
                fig = px.choropleth(df, locations=country_col, color=value_col, color_continuous_scale="Blues")
            else:
                fig = px.choropleth(df, locations=country_col, locationmode="country names", color=value_col, color_continuous_scale="Blues")
            fig.update_layout(height=520, margin=dict(l=0,r=0,t=0,b=0))
            st.plotly_chart(fig, use_container_width=True)
        with c2:
            kpi("Total (sum)", f"{int(df[value_col].sum()):,}")
            for _,row in df.sort_values(value_col, ascending=False).head(3).iterrows():
                st.metric(str(row[country_col]), int(row[value_col]))
else:
    st.info("Upload data/summary_premature_by_nationality.csv to show the map.")

reg_file = data_dir/"summary_premature_by_region.csv"
if reg_file.exists():
    df = pd.read_csv(reg_file)
    cols = {c.lower(): c for c in df.columns}
    region = next((cols[k] for k in cols if k in ["region","area","province"]), None)
    prem   = next((c for c in df.columns if "Premature" in c or "premature" in c), None)
    nonp   = next((c for c in df.columns if "Non" in c and "remature" in c), None)
    if region and prem and nonp:
        st.markdown("### Premature vs Non‑premature by Region")
        mdf = df.melt(id_vars=[region], value_vars=[prem,nonp], var_name="Category", value_name="Count")
        fig = px.bar(mdf, x=region, y="Count", color="Category", barmode="group", color_discrete_sequence=px.colors.sequential.Blues)
        fig.update_layout(height=420, margin=dict(l=0,r=0,t=10,b=0))
        st.plotly_chart(fig, use_container_width=True)