import streamlit as st
import os

st.write("Testing")

foo = os.environ.get("OPENAI")

st.write(foo)
