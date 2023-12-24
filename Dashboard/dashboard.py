import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Streamlit page configuration - must be the first command
st.set_page_config(page_title='Air Quality Analysis Dashboard', layout='wide')

# Function to load data with the new caching command
@st.cache_data
def load_data():
    data = pd.read_csv('AirQuality_datahari.csv')
    data['tanggal'] = pd.to_datetime(data['tanggal'])  # Ensure 'tanggal' is datetime
    return data

# Load the data
datapilih = load_data()

# Streamlit title
st.title('Dashboard Analisis Kualitas Udara')

# AQI Time Series Plot
st.subheader('Tingkat Kualitas Udara Seiring Waktu')
fig, ax = plt.subplots(figsize=(20, 8))

# Plotting
ax.plot(datapilih['tanggal'], datapilih['AQI'], label='AQI', color='blue')
ax.fill_between(datapilih['tanggal'], 0, 50, color='green', alpha=0.3, label='Good (0-50)')
ax.fill_between(datapilih['tanggal'], 51, 100, color='yellow', alpha=0.3, label='Moderate (51-100)')
ax.fill_between(datapilih['tanggal'], 101, 150, color='orange', alpha=0.3, label='Unhealthy for Sensitive Groups (101-150)')
ax.fill_between(datapilih['tanggal'], 151, 200, color='red', alpha=0.3, label='Unhealthy (151-200)')
ax.fill_between(datapilih['tanggal'], 201, 300, color='purple', alpha=0.3, label='Very Unhealthy (201-300)')
ax.fill_between(datapilih['tanggal'], 301, 500, color='maroon', alpha=0.3, label='Hazardous (301-500)')

# Labels and Title
ax.set_xlabel('Bulan')
ax.set_ylabel('Indeks Kualitas Udara (AQI)')
ax.set_title('Tingkat Kualitas Udara Seiring Waktu')
ax.legend()

st.pyplot(fig)
datacorr= datapilih.drop(columns= 'Kategori_Udara')
# Correlation Matrix Heatmap
st.subheader('Hubungan Indikator lain terhadap Polusi Udara')
correlation_matrix = datacorr.corr()
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
ax.set_title('Matriks Korelasi', fontsize=15)
ax.tick_params(axis='x', rotation=45)
ax.tick_params(axis='y', rotation=45)
st.pyplot(fig)
