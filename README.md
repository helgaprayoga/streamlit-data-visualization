# Streamlit Data Visualization Dashboard

Project ini berisi beberapa aplikasi sederhana berbasis Streamlit untuk mempelajari visualisasi data, pengolahan dataset, caching, progress bar, dan session state.

## Fitur

- Visualisasi lokasi toko Indomaret dan Alfamart di Jakarta Selatan.
- Visualisasi data Uber pickups dalam bentuk grafik dan peta.
- Contoh penggunaan `st.cache_data` untuk perhitungan dan pembacaan data.
- Contoh progress bar untuk proses yang berjalan lama.
- Contoh session state dan callback pada form Streamlit.

## Struktur Project

```text
.
├── data_apps.py
├── indomaret_alfamart_location_visualisation.py
├── Data_Alfamart Indomaret_South Jakarta.csv
├── mbg-data.csv
└── multipage/
    ├── main_page.py
    └── pages/
        ├── caching.py
        ├── progress_bar.py
        └── session_callback.py
```

## Persyaratan

- Python 3.10 atau versi yang lebih baru.
- Koneksi internet untuk aplikasi yang mengambil data dari URL eksternal.
- Package Python: Streamlit, Pandas, dan NumPy.

## Instalasi

Buat dan aktifkan virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependency:

```powershell
pip install streamlit pandas numpy
```

## Menjalankan Aplikasi

Jalankan salah satu perintah berikut dari root project.

### Visualisasi Lokasi Toko

```powershell
streamlit run indomaret_alfamart_location_visualisation.py
```

Aplikasi ini membaca file `Data_Alfamart Indomaret_South Jakarta.csv`, menampilkan lokasi toko pada peta, dan menyediakan filter berdasarkan rating.

### Visualisasi Uber Pickups

```powershell
streamlit run data_apps.py
```

Aplikasi ini mengambil dataset Uber pickups dari URL eksternal, kemudian menampilkan data mentah, jumlah pickup per jam, dan peta lokasi pickup.

### Aplikasi Multipage

```powershell
streamlit run multipage/main_page.py
```

Aplikasi multipage berisi contoh:

- Caching dan pembersihan data CSV.
- Progress bar untuk simulasi proses panjang.
- Session state dan callback pada form.

## Catatan

- Folder virtual environment dan file cache Python sebaiknya tidak di-commit ke repository.
- Tekan `Ctrl+C` pada terminal untuk menghentikan aplikasi.
