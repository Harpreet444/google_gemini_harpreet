# Gemini Pro Vision - LLM and Image Analysis Application

This project is a Streamlit application that integrates Google’s Generative AI model (Gemini Pro Vision) for processing both text and image inputs. It demonstrates how to interact with the LLM (Large Language Model) using the `google-generativeai` library and load environment variables using Streamlit's `secrets` management.

## Features

- **Natural Language Input**: Ask questions in English and get responses from the Gemini Pro model.
- **Image Input**: Upload an image for analysis by the Gemini Pro Vision model.
- **Dual Processing**: The app supports processing either text, images, or both using the appropriate models.
- **Secure API Keys**: Environment variables are loaded securely via Streamlit's secrets feature.

## Prerequisites

1. Python 3.x
2. Streamlit
3. [Google Generative AI](https://developers.generativeai.google)
4. Python-Dotenv (for local environment variable loading)
5. PIL (Pillow for image processing)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/gemini-pro-vision-app.git
    cd gemini-pro-vision-app
    ```

2. Install the required dependencies:
    ```bash
    pip install streamlit google-generativeai pillow
    ```

3. Set up your environment:
    - Store your **Google Generative AI** API key in `secrets.toml` as follows:
      ```toml
      [secrets]
      GOOGLE_API_KEY = "your-google-api-key"
      ```

## Running the Application

To run the Streamlit application, execute the following command:

```bash
streamlit run app.py
