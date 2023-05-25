import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data pengaduan dan aspirasi
data = pd.read_csv('data_pengaduan.csv')

# Menampilkan judul dan deskripsi dashboard
st.title('Dashboard Laporan Pengaduan dan Aspirasi Masyarakat Jayapura')
st.write('Ini adalah dashboard yang menampilkan laporan pengaduan dan aspirasi masyarakat Jayapura.')

# Menampilkan data pengaduan
st.subheader('Data Pengaduan')
st.dataframe(data)

# Menampilkan grafik atau visualisasi
st.subheader('Visualisasi Data')

# Visualisasi Jumlah Pengaduan per Kategori
st.subheader('Jumlah Pengaduan per Kategori')
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='Kategori Pengaduan')
plt.xlabel('Kategori Pengaduan')
plt.ylabel('Jumlah Pengaduan')
plt.xticks(rotation=45)
plt.tight_layout()  # Mengatur tata letak plot
st.pyplot(plt.gcf())  # Menampilkan plot menggunakan st.pyplot()

# Menampilkan filter atau opsi pemilihan
st.sidebar.subheader('Filter Data')
kategori_filter = st.sidebar.selectbox('Filter berdasarkan Kategori', ['Semua'] + list(data['Kategori Pengaduan'].unique()))
if kategori_filter != 'Semua':
    filtered_data = data[data['Kategori Pengaduan'] == kategori_filter]
else:
    filtered_data = data

# Menampilkan statistik atau ringkasan data
st.sidebar.subheader('Statistik Data')
st.sidebar.write('Jumlah Pengaduan:', len(filtered_data))
st.sidebar.write('Jumlah Kategori:', len(filtered_data['Kategori Pengaduan'].unique()))

# Menampilkan laporan individu
st.subheader('Laporan Individu')
selected_index = st.selectbox('Pilih nomor laporan', list(filtered_data.index))
selected_report = filtered_data.loc[selected_index]
st.write('Isi Pengaduan:', selected_report['Isi Pengaduan'])
st.write('Kategori Pengaduan:', selected_report['Kategori Pengaduan'])
st.write('Tanggal Pengaduan:', selected_report['Tanggal Pengaduan'])

# Formulir Pengaduan Baru
st.subheader('Pengaduan Baru')
pengaduan = st.text_area('Isi Pengaduan')
kategori = st.selectbox('Kategori Pengaduan', ['Korupsi', 'Lingkungan', 'Infrastruktur', 'Pendidikan', 'Kesehatan'])
button_submit = st.button('Submit')

# Simpan pengaduan baru ke dalam DataFrame
if button_submit:
    new_data = pd.DataFrame({'Isi Pengaduan': [pengaduan],
                             'Kategori Pengaduan': [kategori],
                             'Tanggal Pengaduan': [str(pd.to_datetime('today').date())]})  # Menggunakan tanggal hari ini
    data = pd.concat([data, new_data], ignore_index=True)
    data.to_csv('data_pengaduan.csv', index=False)  # Menyimpan data ke file CSV
    st.success('Pengaduan berhasil disimpan.')

# Menampilkan data pengaduan yang diperbarui
st.subheader('Data Pengaduan (Diperbarui)')
st.dataframe(data)
