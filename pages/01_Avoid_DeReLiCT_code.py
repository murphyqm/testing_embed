import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import altair as alt
import matplotlib

st.set_page_config(page_title="DeReLiCT Code", page_icon="🌺")

hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

st.title("Applying the FAIR principles to your code: DeReLiCT!")
st.write("Basic steps to help avoid total code collapse. Add some scaffolding to your scientific code with the",
         "**DeReLiCT** acronym: **De**pendencies, **Re**pository, **Li**cense, **C**itation, **T**esting.")

st.write("*Note that the examples given are specific to Python, but similar methods/approaches/tools can be used for/applied to projects using different languages.*")

font_css = """
<style>
button[data-baseweb="tab"] > div[data-testid="stMarkdownContainer"] > p {
  font-size: 24px;
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

tablist = ["\u2001  **De**  \u2001", "\u2001 **Re** \u2001", "\u2001 **Li** \u2001", "\u2001 **C** \u2001", "\u2001 **T** \u2001", "\u2001 More! \u2001"]



tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(tablist)

md_dependencies = """
## Dependencies

> Dependencies are the versions of different packages/modules that your code depends on, for example the version of Python you are using, and any libraries you have to import, like `matplotlib`, `scipy`, `tensorflow` etc.

Dependencies are an important thing to keep track of when building scientific code. How many different external libraries does your code depend on? What versions of these libraries does it need? How do you install and update these different libraries?

### Package management

In Python, there are lots of different ways to install and manage packages and dependencies. These different tools generally invovle using virtual environments
in order to keep the dependencies for different projects separate and tidy.
Some package installation and management tools include:

- [Conda](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html)/[Mamba](https://mamba.readthedocs.io/en/latest/)
    - If using Conda/Mamba we recommend installing with [Miniforge](https://github.com/conda-forge/miniforge)
- [pip](https://packaging.python.org/en/latest/key_projects/#pip)
- [pixi](https://packaging.python.org/en/latest/key_projects/#pip)
- [Poetry](https://python-poetry.org/)

You can read more about Python package management tool recommendations [here](https://packaging.python.org/en/latest/guides/tool-recommendations/). The package management tool you use will vary depending on whether you want to build your code into a package itself, or are relying primarily on external libraries. Some of these package managers include entire workflows for building and publishing Python packages, while others focus on organising pre-existing packages.

Due to its widespread use in the research community, our examples are going to use
`conda` in conjunction with some other tools for package building.
"""

md_repository = """
"""

md_license = """

"""

md_citation = """
"""

md_testing = """
### Write initial tests

When we run through an example case, we are going to be using `pytest`, which is already installed in your `packaging-env`in your devcontainer. The[`pytest`](https://docs.pytest.org/en/7.1.x/explanation/anatomy.html#test-anatomy) documentation suggests that each test has four parts:

1. Arrange: you set the test up; you define variables/example data.
2. Act: you run the functions you want to test.
3. Assert: you check the answers to these functions are expected.
4. Clean-up: you wipe the board clean and delete any variables or outputs.

These tests will go into your `test` directory, in a Python file that begins with `test_`, and are essentially functions who's names also begin with `test_` - this means that `pytest` will be able to find and identify them as tests. Whew, the word "test" has almost lost meaning by now.

In practise, a test might look like this:

```python
def test_example(self):
    '''Test for the example function'''
    
    # Arrange
    test_variable_1 = 0
    test_variable_2 = 1
    expected_output = 7

    # Act
    output = your_function(test_variable_1, test_variable_2)

    # Assert
    assert output == expected_output

    # No cleanup needed
```

You can see that testing in Python depends heavily on [assert statements](https://realpython.com/python-assert-statement/).

- You can use a basic assert statement to check if output is identical, eg. `assert one == 1`.
- For floating point numbers of values where tolerance is required, you can use the `pytest.approx()` function -- see [documentation here](https://docs.pytest.org/en/latest/reference/reference.html#pytest.approx); remember that this will require an import statement like `from pytest import approx` at the beginning of your test script. You can define tolerance to suit your approach.
- The `math` library also includes a `isclose()` function -- see [documentation here](https://docs.python.org/3/library/math.html#math.isclose).
- The `numpy.testing` module contains many different assert statements for arrays -- see [documentation here](https://numpy.org/doc/stable/reference/routines.testing.html).

Once you've written your tests, you can run `pytest` from the conda env where it's installed, in the top-level directory (where your `src/` and `tests/` directories are). See details on [running `pytest` here](https://docs.pytest.org/en/7.1.x/how-to/usage.html#usage).

## Testing for Machine Learning

Machine learning testing can be complex due to the stochastic processes involved; however, good code writing practises and diligent unit testing can ensure that your code is behaving as intended.

### Make your code modular and break it into small functions

Making sure your code is made up of small simple functions that fit together in a modular way makes it far easier to write unit tests, and seaprates out any training/ML algorithms from easier-to-test code.

### Build unit tests for all your functions

In addition to your actual machine learning algorithms, you will presumably have multiple preprocessing and data cleaning stages, and other calculations before you train a model. Ensure that all these stages are covered by your unit testing suite. 

### Test your modelling functions

You should test that your modelling function produces the correct coefficients. In [this tutorial](https://medium.com/@ydmarinb/simplifying-unit-testing-in-machine-learning-with-python-df9b9c1a3300#:~:text=Unit%20tests%20are%20small%20tests,processing%20to%20model%20performance%20evaluation.), the author uses the `assert` statement in conjunction with the `hasattr` function to check that the model has actually been trained:

```python
def test_model_training():
    X, y = make_classification(n_samples=100, n_features=2, random_state=42)
    model = LogisticRegression(random_state=42)
    model.fit(X, y)
    assert hasattr(model, "coef_"), "The model should have attributes after training"
```
### Integration tests and example outputs

It's important to test that your model outputs results within specified bounds. This can be done by creating an example or model dataset that is expected when the model is trained with certain parameters and input data. Depending on your model, the example output may be coefficients or an entire data array (possibly saved as a csv file) that you are confident in: the results make scientific sense, compare favourable to existing analytical or numerical models, or are within a certain error envelope of a known result.

As machine learning algorithms usually produce a similar but non-identical output, you can set up your test in a number of ways to allow comparison of slightly differing results:
- Fix the random seed (if applicable) to allow for closer comparison;
- Use libraries such as `numpy.testing` to compare numbers and arrays with specified tolerances;
- Use post-processing functions in your library/package/workflow that reduce the data down to certain derived values to compare to example saved values (also ensure these post-processing functions have unit tests).

### Test your code as it will be used

Do not include argument flags like `"testing"` to alter the behaviour of your functions when running tests; this can lead to problematic behaviour being missed by your testing suite. If you feel you *must* do this in order to run your tests, you instead need to rewrite and reorganise your code so that robust and accurate tests can be run.

#### Further information and resources

- [Simplifying Unit Testing in Machine Learning with Python](https://medium.com/@ydmarinb/simplifying-unit-testing-in-machine-learning-with-python-df9b9c1a3300#:~:text=Unit%20tests%20are%20small%20tests,processing%20to%20model%20performance%20evaluation.)
- [How to unit test machine learning code](https://thenerdstation.medium.com/how-to-unit-test-machine-learning-code-57cf6fd81765)
- [How to test ML code](https://medium.com/marvelous-mlops/how-to-test-ml-code-f9483829c72a#:~:text=Most%20ML%20codebases%20typically%20include,ensure%20they%20operate%20as%20intended.)

## Remember that testing is essential and your code *is not scientific* if you do not test
"""

md_more = """
Please see our lecture material for [SWD3: Software Development Practises in Python](https://arctraining.github.io/swd3-notes/) for more information.

See also [FAIR Software](https://fair-software.nl/about/) for a slightly different approach to applying the FAIR principles to your code.
"""

with tab1:
    
    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vQF-shEdPlDcEvzPGuAkdgCsMTTPRQKB_b4YqbKhLzg8lBuCkDHYtBBbWmxrufmbK02FWqHEV7T0CP9/embed?start=false&loop=false&delayms=3000", height=450)
    st.write(md_dependencies)

with tab2:
    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vSMwoFMvL_BAK_-pdifK_8jVjJ_UAOfGsh5g-HFsTqrOZ6ZYVpXL179fFOJdsRs4n64Ns3rPjY0RJn8/embed?start=false&loop=false&delayms=3000", height=450)
    st.write(md_repository)

with tab3:
    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vQMdFqBQHJcOu0RTJgbB2XR2lm-tfyFZp8DkMePASLAqKoHxoPrZto-yH08fpni3xnNBlr3RsvH0sHs/embed?start=false&loop=false&delayms=3000", height=450)
    st.write(md_license)

with tab4:
    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vR5otqepCmH9BMwvglLRBW_X-CF_C4bJ-40lGPROcwdFSBPBoNaO950ZRHClsLXvOWOmLMitMx05EJI/embed?start=false&loop=false&delayms=3000", height=450)
    st.write(md_citation)

with tab5:
    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vTJiN_hYC28QSikHJxGdjGXy67W1fpdIv_L9pHB0CASDCHEOssrKHSaBHvbYlqPRFhKnC3ziHExXddn/embed?start=false&loop=false&delayms=3000", height=450)
    st.write(md_testing)

with tab6:
    st.write(md_more)

st.markdown('<p style="text-align: center;">Copyright © 2024 Maeve Murphy Quinlan</p>', unsafe_allow_html=True)

md_quick_links = """
## Useful links

- Python Project Template (GitHub): [bit.ly/python-template](https://bit.ly/python-template)
- GitHub Discussions (for polls etc.): [bit.ly/gh_discussions](https://bit.ly/gh_discussions)
"""

with st.sidebar:
    st.write(md_quick_links)