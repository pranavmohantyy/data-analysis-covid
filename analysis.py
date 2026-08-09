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


def calculate_vaccination_rate(df):
    df["vaccination_rate"] = df["total_vaccinations"] / df["population"] * 100
    return df


def plot_vaccination_rate(df):
    top_countries = df.groupby("location").last().nlargest(5, "vaccination_rate")
    plt.bar(top_countries.index, top_countries["vaccination_rate"])
    plt.title("Top 5 Countries by Vaccination Rate")
    plt.xlabel("Country")
    plt.ylabel("Vaccination Rate (%)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()