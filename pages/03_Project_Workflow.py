import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import altair as alt
import matplotlib
import re

st.set_page_config( page_title="Project Workflow", page_icon="🌟")
st.write("If you're starting a new project, here's a workflow you can use",
         "to build a robust, tidy Python project.")
st.write("Remember to use `git` to version control all your work.")
st.header("Part One: your Python package")

brainstorm_md = """
- What's the main purpose of the code?
- What sort of inputs will it take?
    - What format or data type will these be?
- What sort of output will it produce?
- Who is going to use it?
- Where is it going to be used?
    - A local desktop machine?
    - A HPC system?
- What submodules or functions do you predict you'll need?
- What should you call your package?
"""


export_pip_version_numbers = """
# Extract installed pip packages
pip_packages=$(conda env export | grep -A9999 ".*- pip:" | grep -v "^prefix: ")

# Export conda environment without builds, and append pip packages
conda env export --from-history | grep -v "^prefix: " > new-environment.yml
echo "$pip_packages" >> new-environment.yml
"""

export_pip_no_version_numbers = """
# Extract installed pip packages
pip_packages=$(conda env export | grep -A9999 ".*- pip:" | grep -v "^prefix: " | cut -f1 -d"=")

# Export conda environment without builds, and append pip packages
conda env export --from-history | grep -v "^prefix: " > new-environment.yml
echo "$pip_packages" >> new-environment.yml
"""

st.subheader("1. Brainstorm and gather requirements")
with st.expander("What does your code need to do?"):
    st.write(brainstorm_md)
st.subheader("2. Create package repository and directory structure")
with st.expander("Use a basic Python package template"):
    st.write("You can use the Python Project Template (GitHub): [bit.ly/python-template](https://bit.ly/python-template)")
    st.write("##### 1. Choose your package/repository name")
    project_name = st.text_input("Enter your package name (lowercase letters and underscores only!):", "example_package")
    project_name = re.sub('\s+', '_', project_name)
    project_name = re.sub('-', '_', project_name)

    repo_name = re.sub('_', '-', project_name)
    st.write(f"Your package name: `{project_name}`. If this doesn't look right, please change your input!")

    st.write(f"##### 2. Create a git repository called `{repo_name}`")
    
    st.write(f"You can create `{repo_name}` on GitHub and then clone this new repository to your local machine, or you can create it locally (using `mkdir {repo_name}`, `cd {repo_name}`, and `git init`).")

    st.write(f"##### 3. Create a tidy folder structure")

    folder_structure = f"""
    {repo_name}/
    ├── src/  
    │   └── {project_name}/     
    │       ├── __init__.py      Makes the folder a package.
    │       └── source.py        An example module containing source code.
    ├── tests/
    |   ├── __init__.py          Sets up the test suite.
    │   └── test_source.py       A file containing tests for the code in source.py.
    ├── README.md                README with information about the project.
    ├── pyproject.toml           Metadata about the project and its dependencies.
    ├── environment.yml          Your development environment (or requirements.txt)
    └── CITATION.cff             Citation file that makes it easy for people to cite you!

    """

    str_chunk = f"""
mkdir tests
touch tests/__init__.py
echo -e 'import sys\nsys.path.append("src")' > tests/__init__.py
mkdir src/
mkdir src/{project_name}/
touch pyproject.toml
touch environment.yml
touch README.md
touch CITATION.cff
touch src/{project_name}/__init__.py
touch src/{project_name}/source.py
"""

    st.write(f"If `{repo_name}` is the root directory of your project, you might want a project structure that looks something like this:")

    st.code(folder_structure, language='text')

    st.write(f'To recreate the structure above, `cd` into your project directory (`{repo_name}`) and run the following commands (by copying and pasting the block below into the terminal):')
    st.code(str_chunk, language='bash')


dev_env_md = f"""
#### 1. Create your environment yml file

In `{repo_name}/environment.yml`, add the following content (replacing the dependencies with
those you need for your specific project):

```yml
name: {repo_name}-dev

dependencies:
# These dependencies are very useful for packaging and testing your code
  - python=3.12
  - pytest
  - setuptools
  - blackd
  - isort
# Remove these/replace these ones:
  - numpy
  - matplotlib
  - pandas
```
#### 2. Create your env from the yml file

You can now create the conda environment `{repo_name}-dev`:

```bash
conda env create --file environment.yml
```

#### 3. Export your env exactly

At a future point in time (for example, after completing benchmarking, when creating a release etc.) you may want to export your exact conda env, including every dependency and version. This can be done using the `export` command (changing `env-record.yml` to a filename of your choosing):

```bash
conda env export > env-record.yml
```

This file will contain the exact versions of all your dependencies (including pip dependencies, and build information) which is a useful record, but isn't user-friendly when it comes to rebuilding/reproducing an environment. See the notes below on environment files and distributing code to see alternative export methods.

"""

pseudocode_md = """
Pseudocode can look different for different people, and can include scribbling notes on a piece of paper, or saving text files in your repository. 

Usually, I create my `.py` file where I plan on putting my code, and I use this to write my pseudocode as comments. Say I want to write a Python file with simple functions for calculating and converting diffusivity, heat capacity, density and conductivity; I might include notes like this:

```python
# Module with simple functions to convert between diffusivity,
# heat capacity, density and conductivity
# Reminder: Thermal diffusivity is the thermal conductivity divided
# by density and specific heat capacity at constant pressure. 

# Function to calculate diffusivity
# Inputs/args: density, heat cap, pressure, conductivity
# Outputs/returns: diffusivity

# Function to calculate conductivity
# Inputs/args: density, heat cap, pressure, diffusivity
# Outputs/returns: conductivity

# etc...
```

I might then start to flesh out how to do the calculation (note that this is more useful in more complex calculations, where there are multiple steps and the maths is less obvious):

```python
# Module with simple functions to convert between diffusivity,
# heat capacity, density and conductivity
# Reminder: Thermal diffusivity is the thermal conductivity divided
# by density and specific heat capacity at constant pressure. 

# Function to calculate diffusivity
# Inputs/args: density, heat cap, conductivity
# diff = cond / (heat_cap * density)
# Outputs/returns: diffusivity

# Function to calculate conductivity
# Inputs/args: density, heat cap, diffusivity
# cond = diff * heat_cap * density
# Outputs/returns: conductivity

# etc...
```

I then have a pretty straightforward blueprint to convert into actual Python code.

```python
# Module with simple functions to convert between diffusivity,
# heat capacity, density and conductivity
# Reminder: Thermal diffusivity is the thermal conductivity divided
# by density and specific heat capacity at constant pressure. 

# Function to calculate diffusivity
# Inputs/args: density, heat cap, conductivity
def diffusivity_calc(density, heat_cap, cond):
    diff = cond / (heat_cap * density)
    return diff
# Outputs/returns: diffusivity

# Function to calculate conductivity
# Inputs/args: density, heat cap, diffusivity
def conductivity_calc(density, heat_cap, diff):
    cond = diff * heat_cap * density
    return cond
# Outputs/returns: conductivity

# etc...
```

"""

testing_md = """
### Using `pytest`

The[`pytest`](https://docs.pytest.org/en/7.1.x/explanation/anatomy.html#test-anatomy) documentation suggests that each test has four parts:

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

- You can use a basic assert statement to check if output is identical, eg. `assert one == 1`.
- For floating point numbers of values where tolerance is required, you can use the `pytest.approx()` function -- see [documentation here](https://docs.pytest.org/en/latest/reference/reference.html#pytest.approx); remember that this will require an import statement like `from pytest import approx` at the beginning of your test script. You can define tolerance to suit your approach.
- The `math` library also includes a `isclose()` function -- see [documentation here](https://docs.python.org/3/library/math.html#math.isclose).
- The `numpy.testing` module contains many different assert statements for arrays -- see [documentation here](https://numpy.org/doc/stable/reference/routines.testing.html).

> First, sketch pseudocode for your tests.
> 
> - If given a specific input, what specific output do you expect?
> - What are some weird, edge cases that might trip your code up?
> - How might you separate out code-testing vs. scientific validation?
> - Are you matching integers with `==`, or will you have to include tolerances?
> - Do you need to import any external libraries into your test script, like `pytest` or `numpy`?
> 
> Run your tests. Can you break your code so a test fails?
"""

docs_md = """
Like everything in Python, there are multiple different ways of doing things, and multiple different formats that documentation can be written in.

1. Write a useful README file with information on the name and aim of the project, the authors, installation instructions, and a basic example of how to use the code.
2. Write docstrings for your functions...
    - You can use an IDE plugin like Autodocstring to build a docstring tempalte for your function
    - Read the [official docstring guidance here](https://peps.python.org/pep-0257/)
    - Follow one of the official layout guides such as [Google](https://google.github.io/styleguide/pyguide.html) or [NumPy](https://numpydoc.readthedocs.io/en/latest/format.html)
3. You can also build a documentation website on GitHub pages using [mkdocs](https://arctraining.github.io/swd3-notes/session3/); this will automatically pull the information you have provided in your docstrings to create an API reference.
"""

toml_1_md = """
In order to generate a quick template toml file, fill in the following details:
"""

toml_2_md ="""
This file contains metadata about your project, such as the name, version, and author. It also specifies the required Python version and any dependencies your project may have. You might need to add to this, or change/add dependencies. We have added a specific version of `numpy` to demonstrate the syntax; please delete this is not needed. You can find more information about the `pyproject.toml` file [here](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html).
""" 
packaging_md = """
Because you have a `pyproject.toml` file and a well-organised directory structure, you can build your Python package. This means you can created pre-compiled binaries for your project.

Create a new environment from the terminal called build-env:

```bash
conda create --name build-env python=3.12
```

Activate the new environment:
```bash
conda activate build-env
```

Install `build` with `pip`:
```bash
python3 -m pip install --upgrade build
```

Then to create a `dist` folder with the installable `tar.gz` and `whl` files run build:
```bash
python3 -m build
```

When you create a new release on GitHub, you can upload these files to allow people to `pip install` using the release url (see example workflow below).

To install the package locally and test it, you can use `pip`:
```bash
python3 -m pip install --editable . # to install an editable version that will update when you change the source code

python3 -m pip install . # to install in non-editable format
```

You can then open Python and try importing your package and seeing if it works!

### Manual binary upload in a GitHub release

One possible workflow for generating a release for your code that includes installable binaries is detailed below.

1. Test your code locally using `pytest` and check that your docs build and are up to date.
2. Do a local install with `python3 -m pip install .` and try loading your package to check that it works.
3. Build your package locally with `python3 -m build`.
4. Push all your changes to the main branch (the `dist` and `build` files won't be included because of the `.gitignore` file).
5. Create a new release on your latest commit, and use the section *Attach binaries by dropping them here or selecting them* to upload both zipped files in the `dist` folder. Upload these individually instead of uploading the `dist` folder.
6. Once your release is published, you can point people to install your package with the following snippet (with the URL updated to the URL of your `tar.gz` file associated with the release):

        python -m pip install https://github.com/YOUR-USERNAME/YOUR-REPO-NAME/releases/download/YOUR-VERSION-NAME/PACKAGENAME-VERSION.tar.gz

But it would be nice if we could do this a little more automatically...
"""

automated_md = """
## Basic testing workflow

First, let's set up an automated testing suite using one of GitHub's Workflow Templates:

1. From your repository main page, select the "Actions" tab in the top banner.
2. Select "New Workflow".
3. Search for "Python application" and select *Configure* for the action called *Python application* (note: after the course, have a look through the "Python package" workflow and see what's different).
4. Read through the action file; it should work as-is. One small change for convience is under this section:

        on:
            push:
                branches: [ "main" ]
            pull_request:
                branches: [ "main" ]

    add the line:

        on:
            push:
                branches: [ "main" ]
            pull_request:
                branches: [ "main" ]
            workflow_dispatch:
    
    This will allow you to manually run the action which can be very useful!

## Packaging workflow

Another workflow that I frequently use is this build and packaging workflow:

```yml
# This workflow will install python dependencies and build the package
# It will then add the binaries to a specified release
# This action does not run automatically

name: Build package and release

on:
  workflow_dispatch:

jobs:
  build:

    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        python-version: ["3.12"]

    steps:
    - uses: actions/checkout@v4
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v5
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        python -m pip install flake8 pytest
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    - name: Lint with flake8
      run: |
        # stop the build if there are Python syntax errors or undefined names
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
        flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
    - name: Test with pytest
      run: |
        pytest
    - name: Install pypa/build
      run: >-
        python3 -m
        pip install
        build
        --user
    - name: Build a binary wheel and a source tarball
      run: python3 -m build --sdist --wheel --outdir dist/
    - name: Release with Notes
      uses: softprops/action-gh-release@v2
      with:
        files: dist/*
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

To use this workflow, you need to create a GitHub release; then manually run with workflow. You will be asked to pick the commit to run the workflow on: select your recently created release tag. This will add your Python `whl` and `tar.gz` to the release (instead of you manually having to build and upload these as detailed before).

## Documentation workflow

The steps to build your docs shown above require you to run `TZ=UTC mkdocs gh-deploy` after you make changes to your documentation. You might instead want to edit locally, test that the website looks correct using the `serve` option, and then deploy the website online only when changes are merged into the main branch. You can add the following workflow `yml` file to the folder `.github/workflows` in order to do this:

``` yaml
# Workflow to automatically deploy mkdocs website when changes are pushed to main
name: mkdocs-action
on:
  push:
    branches:
      - main  # the workflow will run when you push changes to the main branch
  workflow_dispatch:  # you can also manually trigger the workflow for a different branch
permissions:
  contents: write
jobs:
  deploy:
    runs-on: ubuntu-latest  # the action runs on a virtual ubuntu machine
    steps:
      - uses: actions/checkout@v4
      - name: Configure Git Credentials  # this figures out the permissions
        run: |
          git config user.name github-actions[bot]
          git config user.email 41898282+github-actions[bot]@users.noreply.github.com
      - uses: actions/setup-python@v5
        with:
          python-version: 3.x
      - run: echo "cache_id=$(date --utc '+%V')" >> $GITHUB_ENV 
      - uses: actions/cache@v4
        with:
          key: mkdocs-material-${{ env.cache_id }}
          path: .cache
          restore-keys: |
            mkdocs-material-
      - run: pip install \  # install any required mkdocs packages or plugins
              mkdocs-material \
              mkdocs  # you will have to add additional packages if you pip installed any extra features
      - run: mkdocs gh-deploy --force  # make mkdocs deploy even if there already exists content on the gh-pages branch
```

"""

st.subheader("3. Create a dev env")
with st.expander("Create a conda environment for development"):
    st.write(dev_env_md)
with st.expander("More detail on balancing `env.yml` files for development and `pyproject.toml` files for distributing code"):
    st.subheader("Managing dependencies")
    st.write("While developing your code, you may need other external Python packages, for example `numpy`, `matplotlib.pyplot`, or `scipy`. These are **dependencies**.",
    "While developing your code, you can use the dependency manager of your choice, such as `conda`, and then export your dependencies",
    "to an `environment.yml` file or a `requirements.txt` file.",
    "You can then add these dependencies to your `pyproject.toml` file when you are ready to share the code.")
    st.subheader("Example workflow using `conda`")
    st.write("When writing your code, you should work in a virtual environment, in this case using conda.",
    "First you should create an environment with the version of Python you need, and any initial packages you know you will require.")
    st.code("conda create -n ENV-NAME python=3.12 numpy", language="bash")
    st.write("Then, as needed, you can add packages (with the environment active):")
    st.code("conda install pytest", language="bash")
    st.write("When you are ready to package/release the code, you can export all your environments to an `environment.yml` file:")
    st.code("conda env export --from-history > environment.yml # again, from inside the activated env", language="bash")
    st.write("You can modify this file and remove packages that you were just using for development (for example, `pytest`).",
    "You should test the environment works and you code can run by installing the env (you may need to change it's name):")
    st.code("conda env create -f environment.yml", language="bash")
    st.write("if you have installed packages with pip from inside your conda env, you will need to add a few steps to add these requirements.",
    "[ekiwi111](https://github.com/conda/conda/issues/9628#issuecomment-1608913117) on GitHub provides the following code snippet:")
    st.code(export_pip_version_numbers, language="bash")
    st.write("For more flexibility in pip package versions, we can modify this to cut the pip version numbers out:")
    st.code(export_pip_no_version_numbers, language="bash")
    
st.subheader("4. Write Pseudocode and code")
with st.expander("Use comments to draft your code"):
    st.write(pseudocode_md)
st.subheader("5. Write test suite")
with st.expander("Create a robust testing suite"):
    st.write(testing_md)
st.subheader("6. Write documentation")
with st.expander("Useful documentation is both human and machine readable"):
    st.write(docs_md)
with st.expander("Use this pregenerated template to create a `pyproject.toml` file"):
    st.write(toml_1_md)
    project_name_new = st.text_input(f"Enter the project name if `{project_name}` doesn't look correct:", project_name)
    author_name = st.text_input("Enter the author's full name:", "Author Full Name")

    author_email = st.text_input("Enter the author's email:", "authors_email@goes_here.ie")

    version = st.text_input("Enter the package version:", "0.1.0")

    description = st.text_input("Enter a very brief project description:", "A simple Python project")
    st.write("You can now copy and paste this into your `pyproject.toml` file:")

    toml_snippet = f"""
    [build-system]
    requires = ["setuptools>=61.0", "setuptools-scm"]
    build-backend = "setuptools.build_meta"

    [project]
    name = "{project_name_new}"
    description = "{description}"
    version = "0.0.1"
    readme = "README.md"
    authors = [
    {{ name="{author_name}", email="{author_email}" }},
    ]
    requires-python = ">=3.10"
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
    dependencies = [
        "numpy>=1.21.2",
    ]
    """
    st.code(toml_snippet, language='toml')
    st.write(toml_2_md)
with st.expander("Using `mkdocs` to create a docs website"):
    st.write("[Mkdocs](https://www.mkdocs.org/) is a simple and quick documentation building library that works well with GitHub and GitHub pages.")

    st.write("From the project folder (which holds you `pyproject.toml` file - note: you may want to build this file first then come back), from an environment with `mkdocs` and the required extra libraries installed",
    "(see the suggested env yml at the bottom of the page to install `mkdocs` and the required extensions), you can quickly set up your docs:")
    st.code("mkdocs new .", language="bash")
    st.write("This will both create a `docs/` folder, and a `mkdocs.yml` file. Add the following to the `mkdocs.yml` file:")

    mkdocs_snippet = f"""
    site_name: {project_name} Documentation

theme:
  name: "material"

plugins:
- mkdocstrings:
    handlers:
      python:
        paths: [src]  # search packages in the src folder

nav:
  - Index: index.md
    """
    st.code(mkdocs_snippet, language='yaml')
    st.write("Then, within the `docs/` folder, you can edit the file `index.md` (or add additional markdown files), and add the following snippets:")

    st.code(f"::: {project_name}")

    st.write(f"This will include any documentation you have added to the `__init__.py` file in your `src/{project_name}/` folder.")

    st.write("You can include your API reference by including the following snippet (updating `source` with whatever your python file in your package is called):")

    st.code(f"::: {project_name}.source")

    st.write("To preview your documentation, just run `TZ=UTC mkdocs serve` from the directory that contains the `mkdocs.yml`.",
    "The `TZ=UTC` command is due to a timezone bug that causes the build to fail if not included.",
    "When happy with your documentation, you can run `TZ=UTC mkdocs build` to create a folder of webpages, then `TZ=UTC mkdocs gh-deploy`",
    "to publish these docs to GitHub. Note that you will have to enable GitHub pages, and provide actions with write permissions on your repository.",
    "For more information, see [the wiki post here](https://github.com/murphyqm/python-project-template/wiki/mkdocs-workfow).")


    st.subheader("Mkdocs env")
    st.write("You can use the following env yml to install the required `mkdocs` packages to build the docs example above.")

    mkdocs_package = """
    name: mkdocs-env
channels:
  - defaults
dependencies:
  - python=3.12
  - pip
  - pip:
    - mkdocs
    - "mkdocstrings[python]"
    - mkdocs-material
    """
    st.code(mkdocs_package, language="yaml")
st.subheader("7. Build package with `pyproject.toml`")
with st.expander("Create a `pip` installable package"):
    st.write(packaging_md)
st.subheader("8. Build automated workflows")
with st.expander("Work smarter, not harder"):
    st.write(automated_md)

record_deps = """
While you want your package dependencies to be loose to allow for flexible use with other packages, you also want a record of your exact environment before we create a build, including every dependency and version. This can be done using the `export` command (changing `env-record.yml` to a filename of your choosing):

```bash
conda env export > env-record.yml
```

This file will contain the exact versions of all your dependencies (including pip dependencies, and build information) which is a useful record, but isn't user-friendly when it comes to rebuilding/reproducing an environment. See the notes above (under "create a dev env") on environment files and distributing code to see alternative export methods.
"""
st.subheader("9. Export/record dev env/dependencies")
with st.expander("Record exact versions of packages used for reproducibility and transparency"):
    st.write(record_deps)
st.subheader("10. Create a release on GitHub, with a DOI")
with st.expander("Ensure your Zenodo/GitHub Integration is set up"):
    st.write("Creating a release on GitHub is as easy as clicking 'Draft new release'",
             "from your repository release page.",
             "If you haven't already, build a [CFF file](https://citation-file-format.github.io/) in your repository for easy citation",
             "(and to automatically pull in your project's metadata). ")
st.divider()
st.header("Part Two: using the package for research")
st.subheader("11. Create project repository and directory structure")
st.write("See our Project Layout page for some ideas on how to organise this.")
st.subheader("12. Create a research env with the new package")
st.write("You can create an environment in your preferred package manager; and pip install your package:")
st.code("python -m pip install https://github.com/YOUR-USERNAME/YOUR-REPO-NAME/releases/download/YOUR-VERSION-NAME/PACKAGENAME-VERSION.tar.gz")
st.write("You can also build a conda env from a file (`environment.yml`):")
my_env_md = """
name: my-research-env

dependencies:
# Whatever packages you need for your project
  - python=3.12
  - numpy
  - matplotlib
  - pandas
  - pip
  - pip:
    - https://github.com/YOUR-USERNAME/YOUR-REPO-NAME/releases/download/YOUR-VERSION-NAME/PACKAGENAME-VERSION.tar.gz
"""
st.code(my_env_md)
st.write("You can then build the package:")

st.code("conda env create --file environment.yml")

st.subheader("13. Do analysis/research work")
st.write("Easy as that!")
st.write("You may bounce back and forth, adding new features to your package and creating a new release,",
         "and then updating your package in your research environment.")
st.subheader("14. Export/record research env")
st.write("You can follow the exact same steps detailed for your development environment above.")
st.subheader("15. Create release with DOI")
st.write("Again, you'll want to authorise Zenodo for this repository.",
         "The main difference between a release here vs. in your package repository",
         "is that there are no build files to include in this release.")

st.markdown('<p style="text-align: center;">Copyright © 2024 Maeve Murphy Quinlan</p>', unsafe_allow_html=True)


md_quick_links = """
## Useful links

- Python Project Template (GitHub): [bit.ly/python-template](https://bit.ly/python-template)
- GitHub Discussions (for polls etc.): [bit.ly/gh_discussions](https://bit.ly/gh_discussions)
"""

with st.sidebar:
    st.write(md_quick_links)