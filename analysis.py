import pandas as pd
import matplotlib.pyplot as plt

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


def calculate_death_rate(df):
    df["death_rate"] = df["total_deaths"] / df["total_cases"] * 100
    return df


def plot_death_rate(df):
    plt.figure(figsize=(10, 5))
    plt.plot(df["date"], df["death_rate"], label="Death Rate (%)")
    plt.title("COVID-19 Death Rate Over Time")
    plt.xlabel("Date")
    plt.ylabel("Death Rate (%)")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()