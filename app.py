import streamlit as st
import pandas as pd
import plotly.express as px

# Sayfa başlığı ve ayarı
st.set_page_config(page_title="Aclind & Acto Dashboard", layout="wide")
st.title("📊 Aclind & Acto | Veriye Dayalı Strateji Panosu")

# Açıklama bölümü
st.markdown(
    """
    İki marka, iki pazar: Türkiye ve Almanya'daki ürün trendlerini karşılaştırmak için interaktif analiz aracı.  
    **Aclind** kozmetik temelli; **Acto** ise medikal ürünleri temsil eder.
    """
)

# JSON verisini oku
import json
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Filtre seçimi
kategori = st.radio("Kategoriye Göre Filtrele:", ["Tüm Ürünler", "Aclind", "Acto"], horizontal=True)
if kategori != "Tüm Ürünler":
    df = df[df["category"] == kategori]

# Plotly grafik
fig = px.bar(
    df,
    y="product",
    x=["tr", "de"],
    orientation="h",
    barmode="group",
    labels={"value": "Trend Skoru", "variable": "Pazar"},
    color_discrete_map={"tr": "#3498db", "de": "#1abc9c"},
    height=500,
)

fig.update_layout(
    xaxis_title="Trend Skoru (0-100)",
    yaxis_title="Ürünler",
    legend_title="Pazar",
    yaxis=dict(autorange="reversed")
)

st.plotly_chart(fig, use_container_width=True)

