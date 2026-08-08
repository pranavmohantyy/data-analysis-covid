import requests

def fetch_data():
    url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
    response = requests.get(url)
    with open("owid-covid-data.csv", "wb") as file:
        file.write(response.content)

if __name__ == "__main__":
    fetch_data()