import shutil
import os

def save():
    shutil.copy('results/model.pkl', 'results/final_model.pkl')
    shutil.copy('results/metrics.json', 'results/final_metrics.json')
