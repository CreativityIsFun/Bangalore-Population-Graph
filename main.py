import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import openpyxl


st.set_page_config(page_title="Bangalore Population Survey Results")
st.header("Bangalore Population")
st.subheader("- from 1950 to 2022")


df = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols="A:B",
                   header=0)

st.dataframe(df)

bar_chart = px.bar(df, x='Year', y='Population')

st.plotly_chart(bar_chart)

image = Image.open("Images/Statistics.jpg")
st.image(image,
         caption="Designed by storyset /freepik.com",
         width = 500)


