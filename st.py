import streamlit as st
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from dateutil.relativedelta import relativedelta

data = pd.read_csv('data_merged.csv')
data['Date'] = pd.to_datetime(data['Date'])

st.set_page_config(
    page_title="Gas Natural",
    page_icon="✅",
    layout="wide",
)
st.title("Datos en tiempo real Gas Natural")
column_to_plot = st.selectbox("Selecciona una columna de datos para ver su evolucion a lo largo del tiempo", data.columns)
fig, ax = plt.subplots()
ax.plot(data["Date"], data[column_to_plot])
ax.set_xlabel("Date")
ax.set_ylabel(column_to_plot)
st.pyplot(fig)

# Set default date range values
default_start_date = data["Date"].min()
default_end_date = data["Date"].max()

# Create a date range selection widget
date_range = st.date_input("Selecciona un rango de fechas", value=(default_start_date.date(), default_end_date.date()))

# Convert date_range values to pandas Timestamps
start_date = pd.Timestamp(date_range[0])
end_date = pd.Timestamp(date_range[1])

# Filter your dataframe by the selected date range
data = data[(data["Date"] >= start_date) & (data["Date"] <= end_date)]

st.table(data)

