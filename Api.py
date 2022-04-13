from flask import Flask, jsonify
import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB

app = Flask(__name__)

@app.route('/')
def main():
    return "api is calling"

@app.route('/Working')
def Parse():