import os
from langchain.llms import OpenAI
from constants import openai_key
import streamlit as st

openai_key=os.getenv("OPENAI_API_KEY")

st.title("Book Recommendation")
llms=OpenAI(temperature=0.6)

input_text=st.text_input("Enter What you want")
if input_text:
    st.write(llms(input_text))