import streamlit as st
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from dateutil.relativedelta import relativedelta

data = pd.read_csv('final_data_merge.csv')
data['Date'] = pd.to_datetime(data['Date'])

st.set_page_config(
    page_title="Gas Natural",
    page_icon="✅"
)
st.title("Datos en tiempo real Gas Natural")
column_to_plot = st.selectbox("Selecciona una columna de datos para ver su evolucion a lo largo del tiempo", data.columns)
fig, ax = plt.subplots()
ax.plot(data["Date"], data[column_to_plot])
ax.set_xlabel("Date")
ax.set_ylabel(column_to_plot)
st.pyplot(fig)


# Scatter Plot with column selection
st.subheader("Diagrama de dispersión")

# Select x and y columns using selectbox
scatter_x = st.selectbox("Selecciona una columna para el eje X", data.columns, index=0)
scatter_y = st.selectbox("Selecciona una columna para el eje Y", data.columns, index=1)

# Plotting the scatter plot based on selected columns
fig, ax = plt.subplots()
sns.scatterplot(data=data, x=scatter_x, y=scatter_y)
ax.set_xlabel(scatter_x)
ax.set_ylabel(scatter_y)
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

