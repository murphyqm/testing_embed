import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import altair as alt
import matplotlib

st.set_page_config(page_title="Sustainable Software Development", page_icon="🌠")

# with open( ".streamlit/style.css" ) as css:
#     st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)


md_header="""
#### Testing embedding a PowerBI dashboard/report
"""
st.markdown(md_header)
components.iframe("https://app.powerbi.com/reportEmbed?reportId=83e4e471-55e2-4a86-8504-83ce0681fbc0&autoAuth=true&ctid=bdeaeda8-c81d-45ce-863e-5232a535b7cb", height=450)


