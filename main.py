import requests

def fetch_data(option):
    url = f"https://swapi.mimo.dev/api/{option}/"
    data = []
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print(len(data))
        return data

    except requests.HTTPError as e:
        print(f"An HTTP error occurred: {e}")
        return None
    
option = input("What Star Wars data would you like to explore? ").strip().lower()
data = fetch_data(option)

if data:
    for datas in data:
        print(datas["name"])
else:
    print("Unable to download data")
