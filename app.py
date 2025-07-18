import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Veriler
data = [
    {"category": "Aclind", "product": "Leke Karşıtı Krem", "tr": 45, "de": 48},
    {"category": "Aclind", "product": "Yaşlanma Karşıtı Krem", "tr": 22, "de": 54},
    {"category": "Aclind", "product": "Florürsüz Diş Macunu", "tr": 45, "de": 63},
    {"category": "Aclind", "product": "Kadın Parfümü", "tr": 70, "de": 22},
    {"category": "Aclind", "product": "Yüksek Korumalı Güneş Kremi", "tr": 75, "de": 65},
    {"category": "Aclind", "product": "Ağız Bakım Paketi", "tr": 70, "de": 55},
    {"category": "Acto", "product": "El Dezenfektanı", "tr": 60, "de": 85},
    {"category": "Acto", "product": "Yüzey Dezenfektanı", "tr": 50, "de": 80}
]

df = pd.DataFrame(data)

# Sayfa yapılandırması
st.set_page_config(layout="wide", page_title="Aclind & Acto | Strateji Panosu")
st.title("📊 Aclind & Acto | Veriye Dayalı Strateji Panosu")

st.markdown(
    "İki marka, iki pazar: Türkiye ve Almanya'daki ürün trendlerini karşılaştırmak için interaktif analiz aracı. "
    "**Aclind** kozmetik temelli; **Acto** ise medikal ürünleri temsil eder."
)

# Kategori filtresi
segment = st.radio("Kategoriye Göre Filtrele:", ["Tüm Ürünler", "Aclind", "Acto"], horizontal=True)

# Filtrelenmiş veri
if segment == "Aclind":
    df_plot = df[df["category"] == "Aclind"]
elif segment == "Acto":
    df_plot = df[df["category"] == "Acto"]
else:
    df_plot = df.copy()

# Grafik
st.subheader("TR vs DE Trend Skorları")
fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.35
x = range(len(df_plot))
ax.barh([i + bar_width for i in x], df_plot["tr"], height=bar_width, label="TR", color="#3498db")
ax.barh(x, df_plot["de"], height=bar_width, label="DE", color="#1abc9c")

ax.set_yticks([i + bar_width / 2 for i in x])
ax.set_yticklabels(df_plot["product"])
ax.invert_yaxis()
ax.set_xlabel("Trend Skoru (0–100)")
ax.legend()
st.pyplot(fig)
