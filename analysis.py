import pandas as pd

def load_data():
    df = pd.read_csv("owid-covid-data.csv")
    print(df.info())
    print(df.isnull().sum())
    return df


def filter_by_country(df, country):
    return df[df["location"] == country]


def filter_by_date_range(df, start_date, end_date):
    df["date"] = pd.to_datetime(df["date"])
    return df[(df["date"] >= start_date) & (df["date"] <= end_date)]


def compute_totals(df):
    total_cases = df["total_cases"].sum()
    total_deaths = df["total_deaths"].sum()
    total_vaccinations = df["total_vaccinations"].sum()
    return total_cases, total_deaths, total_vaccinations

if __name__ == "__main__":
    data = load_data()
    filtered_data = filter_by_country(data, "United States")
    totals = compute_totals(filtered_data)
    print(totals)