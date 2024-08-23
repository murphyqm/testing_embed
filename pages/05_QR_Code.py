import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import altair as alt
import matplotlib

st.set_page_config(page_title="Sustainable Software Development", page_icon="✨")

# with open( ".streamlit/style.css" ) as css:
#     st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

st.image("assets/cover_2.png")

md_intro="""
*As part of the NFFDy 2024 Summer School*  

#### Access this page at software-dev.streamlit.app or scan this:
"""

st.write(md_intro)
st.image("assets/streamlit.png")

st.divider()
gh_discussions="""


### GitHub Discussions

#### Access the GitHub Discussions board at [bit.ly/gh_discussions](https://bit.ly/gh_discussions) or scan this:
"""
st.write(gh_discussions)
st.image("assets/gh_discussions.png")


st.markdown('<p style="text-align: center;">Copyright © 2024 Maeve Murphy Quinlan</p>', unsafe_allow_html=True)


md_quick_links = """
## Useful links

- Python Project Template (GitHub): [bit.ly/python-template](https://bit.ly/python-template)
- GitHub Discussions (for polls etc.): [bit.ly/gh_discussions](https://bit.ly/gh_discussions)
"""

with st.sidebar:
    st.write(md_quick_links)