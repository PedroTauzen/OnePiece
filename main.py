import pandas as pd

dataFrame = pd.read_csv('Characters.csv', encoding='latin1')
dataFrame.to_json('Character.json', orient='records', lines=True)
