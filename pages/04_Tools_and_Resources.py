import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import altair as alt
import matplotlib

st.set_page_config(page_title="Tools and Resources", page_icon="👩‍🔧")

# with open( ".streamlit/style.css" ) as css:
#     st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

md_repro = """
> *Computational reproducibility is the principle that results produced with research software, such as data analysis, can be reproduced using the same methods and input data. This relies on workflows which are transparent and produce results consistently.*

<div style="text-align: right;">University of Manchester Office for Open Research</div>

<br>
<br>

- *Computational reproducibility*, [(University of Manchester Office for Open Research)](https://www.openresearch.manchester.ac.uk/resources/open-research-practices/computational-reproducibility/#:~:text=Computational%20reproducibility%20is%20the%20principle,transparent%20and%20produce%20results%20consistently.)
- *Tools and techniques for computational reproducibility* , [(Piccolo and Frampton, 2016)](https://doi.org/10.1186/s13742-016-0135-4)
- *The five pillars of computational reproducibility: bioinformatics and beyond*, [(Ziemann et al., 2023)](https://academic.oup.com/bib/article/24/6/bbad375/7326135)
    1. Literate programming
    2. Code version control and sharing
    3. Compute environment control
    4. Persistent data sharing
    5. Documentation
- *The role of metadata in reproducible computational research*, [(Leipzig et al., 2021)](https://www.sciencedirect.com/science/article/pii/S2666389921001707)
- *Ten Simple Rules for Reproducible Computational Research*, [(Sandve et al., 2013)](https://doi.org/10.1371/journal.pcbi.1003285)
    1. For Every Result, Keep Track of How It Was Produced
    2. Avoid Manual Data Manipulation Steps
    3. Archive the Exact Versions of All External Programs Used
    4. Version Control All Custom Scripts
    5. Record All Intermediate Results, When Possible in Standardized Formats
    6. For Analyses That Include Randomness, Note Underlying Random Seeds
    7. Always Store Raw Data behind Plots
    8. Generate Hierarchical Analysis Output, Allowing Layers of Increasing Detail to Be Inspected
    9. Connect Textual Statements to Underlying Results
    10. Provide Public Access to Scripts, Runs, and Results
"""

md_publishing = """
- *How to make your script ready for publication*, [(Schlauch & Haupt, 2021)](https://www.software.ac.uk/guide/how-make-your-script-ready-publication)
"""

st.header("References related to reproducibility in research computing")

st.write(md_repro, unsafe_allow_html=True)

st.header("References related to publishing your code")

st.write(md_publishing, unsafe_allow_html=True)

st.markdown('<p style="text-align: center;">Copyright © 2024 Maeve Murphy Quinlan</p>', unsafe_allow_html=True)

md_quick_links = """
## Useful links

- Python Project Template (GitHub): [bit.ly/python-template](https://bit.ly/python-template)
- GitHub Discussions (for polls etc.): [bit.ly/gh_discussions](https://bit.ly/gh_discussions)
"""

with st.sidebar:
    st.write(md_quick_links)