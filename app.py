from dotenv import load_dotenv as ld
ld()   # loading environment variable

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

# function for loading model and get response
model = genai.GenerativeModel("gemini-pro")
def model_response(qus):
   response =  model.generate_content(qus)
   return response.text
   

# Starting streamlit 

st.set_page_config(page_title="QNA")
st.header("Gemini pro model")
input=st.text_input("Question: ",key = "input")
submit = st.button("Ask the question")

## on click action
if submit:
    response = model_response(input)
    st.subheader("Response :")
    st.write(response)