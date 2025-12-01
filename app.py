import google.generativeai as genai
import os
import pandas as pd
import json
import streamlit as st

api_key = st.text_input("Input your Gemini api key here")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash-lite")








st.button("Rerun")
# The title of your web application
st.title('My First Streamlit App')
# A header for a section
st.header('Hello, Streamlit World!')
# The 'magic' write command can handle almost anything
st.write(" ")
# Display text formatted with Markdown
st.markdown('### Streamlit makes development **easy** and')             




