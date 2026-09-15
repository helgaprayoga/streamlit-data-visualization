from pathlib import Path

import pandas as pd
import streamlit as st


st.set_page_config(page_title='Lokasi Indomaret dan Alfamart', layout='wide')
st.title('Visualisasi Lokasi Indomaret dan Alfamart')
st.write('Persebaran lokasi toko berdasarkan dataset Alfamart dan Indomaret.')

DATA_FILE = Path(__file__).with_name('Data_Alfamart Indomaret_South Jakarta.csv')


@st.cache_data
def load_data():
    data = pd.read_csv(DATA_FILE)

    numeric_columns = [
        'rating_tempat',
        'user_ratings_total',
        'latitude',
        'longitude',
    ]
    for column in numeric_columns:
        data[column] = pd.to_numeric(data[column], errors='coerce')

    # Membersihkan karakter encoding yang kadang muncul pada nama wilayah.
    data['nama_kelurahan'] = data['nama_kelurahan'].astype('string').str.replace(
        'Â', '', regex=False
    )
    data['store'] = data['store'].astype('string').str.strip()
    return data


required_columns = {
    'nama_tempat',
    'rating_tempat',
    'user_ratings_total',
    'latitude',
    'longitude',
    'alamat_tempat',
    'place_id',
    'store',
    'nama_kelurahan',
    'nama_kecamatan',
    'nama_kota',
}

try:
    data = load_data()
except (KeyError, pd.errors.ParserError, UnicodeDecodeError) as error:
    st.error(f'File CSV tidak sesuai format: {error}')
    st.stop()

missing_columns = required_columns.difference(data.columns)
if missing_columns:
    st.error('Kolom berikut tidak ditemukan: ' + ', '.join(sorted(missing_columns)))
    st.stop()

data = data.dropna(subset=['latitude', 'longitude', 'rating_tempat']).copy()

if data.empty:
    st.warning('Tidak ada data valid untuk ditampilkan.')
    st.stop()

with st.sidebar:
    st.header('Filter rating')
    rating_min = float(data['rating_tempat'].min())
    rating_max = float(data['rating_tempat'].max())
    rating_range = st.slider(
        'Pilih rating',
        min_value=0.0,
        max_value=5.0,
        value=(max(0.0, rating_min), min(5.0, rating_max)),
        step=0.1,
    )

filtered_data = data[
    data['rating_tempat'].between(rating_range[0], rating_range[1])
].copy()

if st.checkbox('Tampilkan raw data'):
    st.subheader('Raw data')
    st.dataframe(data, use_container_width=True, hide_index=True)

st.subheader('Lokasi toko pada peta')
st.map(filtered_data[['latitude', 'longitude']])

st.caption(f'{len(filtered_data)} dari {len(data)} lokasi ditampilkan.')
