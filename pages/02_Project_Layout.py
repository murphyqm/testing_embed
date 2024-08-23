import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib

st.set_page_config( page_title="Project Layout", page_icon="🍃")

hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

st.title('Project layout and organisation')

st.write("Having had a dig into each of the **DeReLiCT** headings, let's now look at one way of organising your work.")

md_layout_01 = """
- One thing that always confused me was the best way to keep all my work tidy
- In general, my work involved:
	1. Building some form of numerical model that was somewhat generic/modular.
    2. Applying that model to specific parameters and testing various inputs/outputs.
- I tended to bump into a few questions or problems that I didn't see an obvious solution to:
	- I want to keep my codebase nice and tidy and comprehensible, but I also tend to produce lots and lots of analysis scripts, notebooks and figures as I analyse my results;
    - I want to compare my models to analytical cases to check their validity, again producing lots of various outputs, figures etc.;
    - I don't want to accidentally modify some of my numerical model code when trying to analyse my results at a later stage;
    - I want to update my core code, fix some problems and add some functionality; how do I keep track of what results I produced with which version of my code?
    - Other people would probably be able to use my model, or adapt it for their own projects, but they won't want to sift through all my iterative work in the meantime.
"""
st.write(md_layout_01)

st.header("Two-repository project layout")

font_css = """
<style>
button[data-baseweb="tab"] > div[data-testid="stMarkdownContainer"] > p {
  font-size: 18px;
}
</style>
"""

st.markdown("""
<style>

	.stTabs [data-baseweb="tab-list"] {
		gap: 2px;
    }

	.stTabs [data-baseweb="tab"] {
		height: 50px;
        white-space: pre-wrap;
		background-color: #F0F2F6;
		border-radius: 4px 4px 0px 0px;
		gap: 1px;
		padding-top: 10px;
		padding-bottom: 10px;
    }

	.stTabs [aria-selected="true"] {
  		background-color: #FFFFFF;
	}

</style>""", unsafe_allow_html=True)

st.write(font_css, unsafe_allow_html=True)

tablist = ["\u2001  **Why?**  \u2001","\u2001  **Package repo**  \u2001", "\u2001 **Application repo** \u2001", "\u2001 **Alternatives** \u2001"]

tab0, tab1, tab2, tab3 = st.tabs(tablist)

with tab0:
    md_why_01 = """
    This example specifically is for Python based projects; however, a similar approach of splitting your model code and analysis code can be applied to other languages too.

    One organisation method I have found useful is splitting my code into two seaparate repositories:
    - A "package" repository, where my code is in the form of a tidy standard Python package
    - An "application" repository where I use/apply the Python package and test it, with Jupyter notebooks, etc. 
    """
    st.write(md_why_01)

with tab1:
    md_package_repo = """
    #### Repository 1: the numerical model as a Python package

    ```text
    planet-evolution/            The package git repository
    ├── src/  
    │   └── planet_evolution/     
    │       ├── __init__.py      Makes the folder a package.
    │       └── source.py        An example module containing source code.
    ├── tests/
    |   ├── __init__.py          Sets up the test suite.
    │   └── test_source.py       A file containing tests for the code in source.py.
    ├── README.md                README with information about the project.
    ├── docs                     Package documentation
    ├── pyproject.toml           Allows me to install this as a package
    ├── LICENSE                  License text to allow for reuse
    └── CITATION.cff             Citation file that makes it easy for people to cite you!
    ```

    This model can be installed as a package, cited in your research, and reused in a later project.
    """

    st.write(md_package_repo)

with tab2:
    md_app_repo = """
    #### Repository 2: my scientific analysis

    ```bash
    pallasite-parent-body-evolution/    The project git repository
    ├── LICENSE
    ├── README.md
    ├── env.yml or requirements.txt     The libraries I need for analysis (including planet_evolution!)
    ├── data                            I usually load in large data from storage elsewhere
    │   ├── interim                     But sometimes do keep small summary datafiles in the repository
    │   ├── processed
    │   └── raw
    ├── docs                            Notes on analysis, process etc.
    ├── notebooks                       Jupyter notebooks used for analysis
    ├── reports                         For a manuscript source, e.g., LaTeX, Markdown, etc., or any project reports
    │   └── figures                     Figures for the manuscript or reports
    ├── src                             Source code for this project
    │   ├── data                        Scripts and programs to process data
    │   ├── tools                       Any helper scripts go here
    │   └── visualization               Scripts for visualisation of your results, e.g., matplotlib, ggplot2 related.
    └── tests                           Test code for this project, benchmarking, comparison to analytical models
    ```

    This is the actual work for the scientific project - while others are unlikely to use this code as-is, it's public and citeable so that you can point to a specific version in your published paper and readers can reproduce your work with it if they wish.

    Adapted/modified from [mkrapp/cookiecutter-reproducible-science github](https://github.com/mkrapp/cookiecutter-reproducible-science)
    """
    st.write(md_app_repo)

with tab3:
    md_alternatives = """
    Of course, this is just one way of organising your work.

    Another option is to keep everything in the one repository, with your package in a `src/package_name` directory, and other scripts in a `analysis_scripts` directory in the same repository.

    You can also use a tool like [Cookiecutter](https://cookiecutter.readthedocs.io/en/stable/) to use a template to create your project structure; there are many different scientific computing templates available.

    Regardless, it's a good idea to keep your code well-organised with an intentional, sensible structure. Pick a project organisation scheme because it's sensible and will help you write better code and do better research, not because you've just ended up with files in certain folders.
    """
    st.write(md_alternatives)

st.markdown('<p style="text-align: center;">Copyright © 2024 Maeve Murphy Quinlan</p>', unsafe_allow_html=True)

md_quick_links = """
## Useful links

- Python Project Template (GitHub): [bit.ly/python-template](https://bit.ly/python-template)
- GitHub Discussions (for polls etc.): [bit.ly/gh_discussions](https://bit.ly/gh_discussions)
"""

with st.sidebar:
    st.write(md_quick_links)