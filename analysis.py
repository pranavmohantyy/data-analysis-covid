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


def calculate_rolling_average(df):
    df["rolling_7_day_avg"] = df["total_cases"].rolling(window=7).mean()
    return df


def plot_daily_new_cases(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df["date"], df["total_cases"], label="Daily Cases")
    plt.plot(df["date"], df["rolling_7_day_avg"], label="7-Day Rolling Average", color='orange')
    plt.xlabel("Date")
    plt.ylabel("Number of Cases")
    plt.title("Daily New Cases with 7-Day Average")
    plt.legend()
    plt.show()