[![Build Python application](https://github.com/abulgher/pypiprivatizer/actions/workflows/python-app.yml/badge.svg)](https://github.com/abulgher/pypiprivatizer/actions/workflows/python-app.yml)
[![Upload Python Package](https://github.com/abulgher/pypiprivatizer/actions/workflows/publish-python.yml/badge.svg)](https://github.com/abulgher/pypiprivatizer/actions/workflows/publish-python.yml)

# pypiprivatizer
A python tool to download PyPI packages and create the local structure to run a private index

This tool is totally based on pip.

The user needs to provide via the command line a requirement file and the tool will invoke pip to download all the packages required. Moreover the user can select a directory where the packages will be moved in order to mimick the required structure of the PyPI index.
