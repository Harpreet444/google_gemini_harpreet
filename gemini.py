# Streamlite front end
# google-generativeai to access LLM model
# python-dotenv to load environment variable

from PIL import Image
from dotenv import load_dotenv as ld
ld()   # loading environment variable

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

# function for loading model and get response

def model_response(input,img):
  if input!="" and img!= None:
   model = genai.GenerativeModel("gemini-pro-vision")
   response = model.generate_content([input,img])
   return response.text

  elif input!="" and img == None:
     model = genai.GenerativeModel("gemini-pro")
     response =  model.generate_content(input)
     return response.text
  
  elif input=="" and img != None:
    model = genai.GenerativeModel("gemini-pro-vision")
    response =  model.generate_content(img)
    return response.text
  
  else:
    return "No Input Provided"

# Starting streamlit 

st.set_page_config(page_title="Gemini pro vision")
st.header("Gemini application")
input=st.text_input("Question: ",key = "input")

image = st.file_uploader("Choose Image File:",type=["jpg","jpeg","png"])
img =""

if image is not None:
    img = Image.open(image)
    st.image(img,caption="Uploaded image",use_column_width=True)

else:
  img = None
  
submit = st.button("Ask the question")
    
## on click action
if submit and img == None and input == "":
  response = model_response(input,img)
  st.subheader("Response :")
  st.write(response)

elif submit and img != None:
    response = model_response(input,img)
    st.subheader("Model Used: gemini-pro-vision")    
    st.subheader("Response :")
    st.write(response)
    
elif submit and img == None:
    response = model_response(input,None)
    st.subheader("Model Used: gemini-pro")
    st.subheader("Response :")
    st.write(response)