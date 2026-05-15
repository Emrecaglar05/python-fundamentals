import streamlit as st
import sqlite3
import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
from datetime import datetime
import pandas as pd
import time


# --- SAYFA AYARLARI ---
st.set_page_config(page_title="AI Radar Final", page_icon="📡", layout="wide")

# --- VERİTABANI KURULUMU (OTOMATİK) ---
def init_db():
    conn = sqlite3.connect("ai_radar_final.db")
    cursor = conn.cursor()
    # Tablo yoksa oluştur (Hatanın çözümü burası)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS news (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            link TEXT,
            source TEXT,
            category TEXT,
            image_url TEXT,
            found_date TEXT,
            UNIQUE(link) 
        )
    ''')
    conn.commit()
    conn.close()

# --- YARDIMCI FONKSİYONLAR ---
def ceviri_yap(text):
    if not text: return ""
    try:
        return GoogleTranslator(source='auto', target='tr').translate(text)
    except:
        return text

def veri_ekle(title, link, source, category, image_url):
    conn = sqlite3.connect("ai_radar_final.db")
    cursor = conn.cursor()
    try:
        today = datetime.now().strftime("%d-%m %H:%M")
        cursor.execute(
            "INSERT INTO news (title, link, source, category, image_url, found_date) VALUES (?, ?, ?, ?, ?, ?)", 
            (title, link, source, category, image_url, today)
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

# --- VERİ ÇEKME FONKSİYONLARI ---
def tara_ve_guncelle():
    headers = {"User-Agent": "Mozilla/5.0"}
    st.toast("Veriler taranıyor... Lütfen bekleyin.", icon="⏳")
    
    # 1. SHIFTDELETE
    try:
        soup = BeautifulSoup(requests.get("https://shiftdelete.net/tag/yapay-zeka", headers=headers).text, "html.parser")
        cards = soup.find_all("div", class_="td_module_10")
        if not cards: cards = soup.find_all(['h3', 'h2'])
        
        for card in cards[:3]:
            a = card.find("a")
            img = card.find("img")
            if a and "shiftdelete" in a['href']:
                resim = img['src'] if img else "https://shiftdelete.net/wp-content/uploads/2023/01/sdn-logo.png"
                veri_ekle(a.text.strip(), a['href'], "ShiftDelete", "Haber", resim)
    except: pass

    # 2. HUGGING FACE
    try:
        soup = BeautifulSoup(requests.get("https://huggingface.co/papers", headers=headers).text, "html.parser")
        articles = soup.find_all("h3")
        for art in articles[:3]:
            a = art.find("a")
            if a:
                baslik = ceviri_yap(a.text.strip())
                link = "https://huggingface.co" + a['href']
                veri_ekle(baslik, link, "Hugging Face", "Model", "https://huggingface.co/front/assets/huggingface_logo-noborder.svg")
    except: pass

    # 3. GITHUB
    try:
        soup = BeautifulSoup(requests.get("https://github.com/trending/python?since=daily", headers=headers).text, "html.parser")
        rows = soup.find_all("article", class_="Box-row")
        for row in rows[:3]:
            h2 = row.find("h2")
            a = h2.find("a")
            p = row.find("p")
            if a:
                desc = ceviri_yap(p.text.strip()) if p else "Açıklama yok"
                baslik = f"{a.text.strip().replace(' ', '')}: {desc}"
                link = "https://github.com" + a['href']
                veri_ekle(baslik, link, "GitHub", "Kod", "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png")
    except: pass

# --- ARAYÜZ ---
init_db() # Veritabanını başlat

st.title("🚀 AI Radar Final: Canlı Takip Merkezi")

col1, col2 = st.columns([3, 1])
with col1:
    st.markdown("Veriler otomatik olarak veritabanına kaydedilir ve gösterilir.")
with col2:
    if st.button("🔄 Şimdi Tara ve Yenile", type="primary"):
        tara_ve_guncelle()
        st.rerun()

# Verileri Getir
conn = sqlite3.connect("ai_radar_final.db")
df = pd.read_sql("SELECT * FROM news ORDER BY id DESC", conn)
conn.close()

if df.empty:
    st.info("Henüz veritabanı boş. İlk tarama başlatılıyor...")
    tara_ve_guncelle()
    st.rerun()
else:
    # İstatistik
    st.metric("Toplam İçerik", len(df))
    st.divider()
    
    # 3 Kolonlu Izgara
    cols = st.columns(3)
    for i, row in df.iterrows():
        col = cols[i % 3]
        with col:
            with st.container(border=True):
                if row['image_url']:
                    st.image(row['image_url'], use_container_width=True)
                st.subheader(row['source'])
                st.markdown(f"**{row['title']}**")
                st.caption(f"📅 {row['found_date']} | 🏷️ {row['category']}")
                st.link_button("Kaynağa Git", row['link'])