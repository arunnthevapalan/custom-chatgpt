# Custom ChatGPT

A custom ChatGPT-like web application using OpenAI API, Python, and Streamlit.

## Overview
This project is a simple ChatGPT-like application built with Streamlit and OpenAI's API. It provides an interactive chat interface where users can enter prompts and receive AI-generated responses using the `gpt-4o` model.

## Features
- Interactive chat interface powered by Streamlit.
- Uses OpenAI's GPT-4o model for responses.
- Secure API key input for accessing OpenAI API.
- Maintains chat history within a session.

## Prerequisites
To run this project, ensure you have:
- Python 3.8 or higher installed
- An OpenAI API key

## Installation
Clone the repository and install the required dependencies:

```sh
pip install -r requirements.txt
```

## Usage
Run the Streamlit application with the following command:

```sh
streamlit run app.py
```

Once the app is running:
1. Enter your OpenAI API key when prompted.
2. Type your message in the chat input field.
3. Receive AI-generated responses in real time.

## Files
- `README.md` : Documentation for the project.
- `app.py` : Main script containing the Streamlit chat application.
- `requirements.txt` : List of dependencies required for the project.

## Acknowledgements
- [OpenAI](https://openai.com/) for providing the API.
- [Streamlit](https://streamlit.io/) for the interactive UI framework.

