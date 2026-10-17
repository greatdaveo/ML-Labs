# ML Labs

This is where I keep the notebooks and exercises I work through while learning data analysis, machine learning, and NLP. Most of the examples use datasets in the repo and Python libraries like pandas, NumPy, and scikit-learn.

## What's here

- `DA-Basics/` has notebooks on NumPy, pandas, reading data, and plotting.
- `EDA/` contains a few exploratory data analysis notebooks, including examples with flight prices, Google Play Store data, and wine quality.
- `LinearRegression/`, `LogisticRegression/`, `KNearestNeighbour/`, `DecisionTree/`, `RandomForest/`, and `NaiveBayesTheorem/` cover different machine learning algorithms.
- `feature-engineering/` has examples of cleaning data, encoding categories, and handling imbalanced datasets.
- `NLP/` covers text preprocessing and techniques like bag-of-words, TF-IDF, and Word2Vec.
- `database/` and `logger/` contain some SQLite and Python logging exercises.

These are learning materials, so the notebooks are meant to be opened and run individually rather than as one application. Some use relative paths to data files, so it's best to start Jupyter from the repository root. A few notebooks may also need extra packages beyond the main requirements.

## Getting started

Clone the repo and create a virtual environment:

```bash
git clone https://github.com/greatdaveo/ML-Labs.git
cd ML-Labs
python3 -m venv .venv
source .venv/bin/activate
```

On Windows, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

Install the main dependencies:

```bash
python -m pip install -r requirements.txt
```

If JupyterLab isn't already installed in your environment, install it and start it from the repository folder:

```bash
python -m pip install jupyterlab
jupyter lab
```
