# Streamlit front end
# google-generativeai to access LLM model
# python-dotenv to load environment variables

from PIL import Image
import streamlit as st
import google.generativeai as genai

# Configure API key from secrets
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Function for loading the model and getting a response
def model_response(input, img):
    if input != "" and img is not None:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content([input, img])
        return response.text

    elif input != "" and img is None:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(input)
        return response.text

    elif input == "" and img is not None:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(img)
        return response.text

    else:
        return "No Input Provided"

# Streamlit app setup
st.set_page_config(page_title="Gemini Pro Vision")
st.header("Gemini Application")

# User input for question
input = st.text_input("Question:", key="input")

# File uploader for image input
image = st.file_uploader("Choose Image File:", type=["jpg", "jpeg", "png"])
img = None

# Display uploaded image
if image is not None:
    img = Image.open(image)
    st.image(img, caption="Uploaded image", use_column_width=True)

# Button to submit the question and image
submit = st.button("Ask the question")

# On button click action
if submit and img is None and input == "":
    response = model_response(input, img)
    st.subheader("Response:")
    st.write(response)

elif submit and img is not None:
    response = model_response(input, img)
    st.code("Model Used: gemini-1.5-flash")
    st.subheader("Response:")
    st.write(response)

elif submit and img is None:
    response = model_response(input, None)
    st.code("Model Used: gemini-pro")
    st.subheader("Response:")
    st.write(response)
