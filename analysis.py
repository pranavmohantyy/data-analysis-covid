import pandas as pd

def load_data():
    df = pd.read_csv("owid-covid-data.csv")
    print(df.info())
    print(df.isnull().sum())

if __name__ == "__main__":
    load_data()