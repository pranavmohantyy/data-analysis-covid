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


def summary_stats(df):
    peak_daily_cases = df["new_cases"].max()
    total_deaths = df["total_deaths"].sum()
    vaccination_rate = df["total_vaccinations"].max() / df["population"].max() * 100
    print(f"Peak Daily Cases: {peak_daily_cases}")
    print(f"Total Deaths: {total_deaths}")
    print(f"Vaccination Rate: {vaccination_rate:.2f}%")