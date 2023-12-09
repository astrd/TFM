import streamlit as st
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from dateutil.relativedelta import relativedelta

data = pd.read_csv('data_merged.csv')
data['Date'] = pd.to_datetime(data['Date'])

st.set_page_config(
    page_title="Real-Time NG predictor",
    page_icon="✅",
    layout="wide",
)
st.title("Real-Time / Live Data Science Dashboard")


# Set default date range values
default_start_date = data["Date"].min()
default_end_date = data["Date"].max()

# Create a date range selection widget
date_range = st.date_input("Select a date range", value=(default_start_date.date(), default_end_date.date()))

# Convert date_range values to pandas Timestamps
start_date = pd.Timestamp(date_range[0])
end_date = pd.Timestamp(date_range[1])

# Filter your dataframe by the selected date range
data = data[(data["Date"] >= start_date) & (data["Date"] <= end_date)]

st.table(data)
# Create a line plot with "Date" on the horizontal axis and a selected column on the vertical axis
column_to_plot = st.selectbox("Select a column to plot against Date", data.columns)
fig, ax = plt.subplots()
ax.plot(data["Date"], data[column_to_plot])
ax.set_xlabel("Date")
ax.set_ylabel(column_to_plot)
st.pyplot(fig)
st.write('Hello world!')
