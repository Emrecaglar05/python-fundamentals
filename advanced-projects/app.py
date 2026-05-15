import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="AI Radar", page_icon="📡", layout="wide")

st.title("📡 AI Radar: Yapay Zeka Gündemi")
st.markdown("*Öğrenciler ve Geliştiriciler için Gerçek Zamanlı Takip Sistemi*")

def get_data():
    conn = sqlite3.connect("ai_radar.db")
    df = pd.read_sql("SELECT * FROM news ORDER BY id DESC", conn)
    conn.close()
    return df

try:
    df = get_data()
    
    # --- YAN MENÜ (Filtreler) ---
    st.sidebar.header("Filtreleme")
    
    # Kaynak Filtresi
    kaynaklar = ["Tümü"] + list(df['source'].unique())
    secilen_kaynak = st.sidebar.selectbox("Kaynak Seç:", kaynaklar)
    
    # Kategori Filtresi
    kategoriler = ["Tümü"] + list(df['category'].unique())
    secilen_kategori = st.sidebar.selectbox("Kategori Seç:", kategoriler)

    # Veriyi Filtrele
    if secilen_kaynak != "Tümü":
        df = df[df['source'] == secilen_kaynak]
    if secilen_kategori != "Tümü":
        df = df[df['category'] == secilen_kategori]

    # --- ANA EKRAN (Kartlar) ---
    st.info(f"Şu an veritabanında {len(df)} adet güncel içerik var.")

    # Haberleri 2 kolon halinde göster
    col1, col2 = st.columns(2)
    
    for index, row in df.iterrows():
        # Kolon değişimi (biri sağa biri sola)
        with col1 if index % 2 == 0 else col2:
            with st.container(border=True):
                st.markdown(f"### {row['title']}")
                
                # Etiketler
                st.caption(f"📅 {row['found_date']} | 🔗 {row['source']} | 🏷️ {row['category']}")
                
                st.link_button("Habere Git", row['link'])

except Exception as e:
    st.error("Veri çekilemedi. Lütfen önce main.py'yi çalıştırın.")
    st.write(e)