import pandas as pd
from utils import db_connect

engine = db_connect()


engine
if engine:
    print("Conexión exitosa")

data = pd.read_csv('https://raw.githubusercontent.com/4GeeksAcademy/decision-tree-project-tutorial/main/diabetes.csv')
data.to_sql('tabla diabetes', engine, if_exists='replace', index=False)