import streamlit as st
import os
from dotenv import load_dotenv
from gpt3_text_generator import GPT3TextGenerator

load_dotenv()

gpt3_api_key = os.getenv("GPT3_API_KEY")

gpt3_generator = GPT3TextGenerator(gpt3_api_key)

st.title("GPT-3 Text Generator")

st.write("""

GPT-3 is a language model that uses deep learning to produce human-like text.

It was created by OpenAI, you can read more about it here: https://openai.com/blog/gpt-3/

This text generator uses the GPT-3 API to generate text.

You can generate text by entering a prompt below.

""")

prompt = st.text_input("Prompt")

if prompt:
    result = gpt3_generator.generate(prompt)
    st.write(result)
""")

st.markdown(prompt)

st.markdown("""
## Output
""")

st.markdown("""gpt_j.generate(prompt, temperature=temperature, top_p=top_p)""")
