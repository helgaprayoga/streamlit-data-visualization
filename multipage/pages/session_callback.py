import streamlit as st


if "last_result" not in st.session_state:
    st.session_state.last_result = None

if "calculation_count" not in st.session_state:
    st.session_state.calculation_count = 0


def form_callback():
    """Mengolah input form dan menyimpan hasilnya ke session state."""
    st.session_state.last_result = (
        st.session_state.form_arg1 + st.session_state.form_arg2
    )
    st.session_state.calculation_count += 1


st.header("3. Session State dan Callback")
st.write("Nilai di bawah tetap tersimpan selama session browser ini aktif.")

with st.form(key="calculation_form"):
    st.number_input("Angka pertama", value=2, step=1, key="form_arg1")
    st.number_input("Angka kedua", value=3, step=1, key="form_arg2")
    st.slider("Nilai slider", 0, 10, 5, key="my_slider")
    st.checkbox("Aktifkan pilihan", key="my_checkbox")
    st.form_submit_button("Jalankan callback", on_click=form_callback)

if st.session_state.last_result is not None:
    st.success(f"Hasil callback: {st.session_state.last_result}")
    st.write(f"Slider: {st.session_state.my_slider}")
    st.write(f"Checkbox: {st.session_state.my_checkbox}")
    st.write(f"Callback dijalankan: {st.session_state.calculation_count} kali")
