import json

# Create a proper Jupyter notebook structure
notebook_content = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["# Financial News Sentiment Analysis - Task 1: EDA\n", "## Exploratory Data Analysis of FNSPID Dataset"]
        },
        {
            "cell_type": "code", 
            "metadata": {},
            "source": ["# Import required libraries\nimport pandas as pd\nimport numpy as np\nimport matplotlib.pyplot as plt\nimport seaborn as sns\nimport warnings\nwarnings.filterwarnings('ignore')\n\nprint(\"🚀 Starting Task 1: Exploratory Data Analysis\")"],
            "execution_count": None
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python", 
            "name": "python3"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 4
}

# Save the notebook
with open('notebooks/01_eda.ipynb', 'w') as f:
    json.dump(notebook_content, f, indent=2)

print('✅ Notebook created successfully: notebooks/01_eda.ipynb')
