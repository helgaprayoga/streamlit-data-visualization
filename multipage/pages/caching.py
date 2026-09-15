import time

import pandas as pd
import streamlit as st


DATA_URL = (
    "https://raw.githubusercontent.com/wsuryaningrat/"
    "mbg-food-poisoning-data/refs/heads/main/data/mbg-data.csv"
)


@st.cache_data
def my_slow_function(arg1, arg2):
    """Contoh fungsi lambat yang hasilnya disimpan oleh Streamlit."""
    time.sleep(2)
    return arg1 + arg2


@st.cache_data(persist=True)
def fetch_and_clean_data(url):
    """Membaca CSV dari URL, lalu membersihkan dan mengubah tipe datanya."""
    data = pd.read_csv(url, sep=";")
    data.columns = data.columns.str.strip().str.lower().str.replace(" ", "_", regex=False)
    data["tanggal_kasus"] = pd.to_datetime(data["tanggal_kasus"], errors="coerce")
    data["tanggal_update"] = pd.to_datetime(data["tanggal_update"], errors="coerce")
    data["jumlah_kasus"] = pd.to_numeric(data["jumlah_kasus"], errors="coerce")
    data = data.dropna()
    return data


st.title("Demo Streamlit Caching")
st.write("Contoh penggunaan `st.cache_data` pada dua fungsi sederhana.")

st.header("1. Caching")
arg1 = st.number_input("Angka pertama", value=10, step=1)
arg2 = st.number_input("Angka kedua", value=5, step=1)

if st.button("Hitung penjumlahan"):
    start_time = time.perf_counter()
    result = my_slow_function(arg1, arg2)
    elapsed_time = time.perf_counter() - start_time
    st.success(f"Hasil: {result}")
    st.caption(f"Waktu proses: {elapsed_time:.2f} detik")
    st.info("Klik lagi dengan angka yang sama untuk melihat hasil dari cache.")


st.header("2. Membaca dan membersihkan CSV")
st.write("Sumber data: `mbg-data.csv` dari GitHub")

if st.button("Ambil dan bersihkan data"):
    cleaned_data = fetch_and_clean_data(DATA_URL)
    st.success("File CSV berhasil dibaca dan dibersihkan.")
    st.write(f"Jumlah baris setelah dibersihkan: {len(cleaned_data)}")
    st.dataframe(cleaned_data, use_container_width=True)
