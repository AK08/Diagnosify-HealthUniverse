import streamlit as st

st.write("Testing")

foo = os.environ.get("OPENAI")

st.write(foo)
