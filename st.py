import streamlit as st
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

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
sns.scatterplot(data=data, x=scatter_x, y=scatter_y, s=5))
ax.set_xlabel(scatter_x)
ax.set_ylabel(scatter_y)
st.pyplot(fig)


pred = pd.read_csv('predictions.csv')
pred['Date'] = pd.to_datetime(pred['Date'])



# Select a column for visualization
selected_pred = st.selectbox("Selecciona un modelo para ver su prediccion", pred.columns)
figi, ax = plt.subplots(figsize=(10, 6))  # Wider plot
ax.set_ylim(0, 7)  # Establecer el rango del eje y de 0 a 7

ax.plot(pred["Date"], pred[selected_pred])
ax.set_xlabel("Date")
ax.set_ylabel(selected_pred)
st.pyplot(figi)

fig, ax = plt.subplots(figsize=(14, 6))  # Wider plot
fig = px.line(pred, x='Date', y=pred.columns[1:])
fig.update_xaxes(title='Fecha')
fig.update_yaxes(title='Precios')
fig.update_layout(title='Predicciones de Gas Natural de Todos los Modelos', xaxis_rangeslider_visible=True)
fig.update_yaxes(title='Precios', range=[0, 7])  

st.plotly_chart(fig)

