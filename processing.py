import numpy as np
import pandas as pd

names = ['class', 'id', 'object']

df = pd.read_csv('output.csv', sep = ',', names = names, header = None)