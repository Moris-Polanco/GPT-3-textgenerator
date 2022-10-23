import streamlit as st
import gpt-2

st.title("GPT-2 Text Generator")

st.markdown("""
This is a text generator powered by [GPT-2](https://github.com/openai/gpt-2-output-dataset)
""")

st.sidebar.title("GPT-2 Text Generator")

st.sidebar.markdown("""
This is a text generator powered by [GPT-2](https://github.com/openai/gpt-2-output-dataset)
""")

st.sidebar.markdown("""
## Input
""")

prompt = st.sidebar.text_area("Enter your prompt", "")

st.sidebar.markdown("""
## Options
""")

temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7)

top_p = st.sidebar.slider("Top P", 0.0, 1.0, 0.9)

st.sidebar.markdown("""
## Output
""")

st.markdown("""
## Input
""")

st.markdown(prompt)

st.markdown("""
## Output
""")

st.markdown(gpt_j.generate(prompt, temperature=temperature, top_p=top_p))
