import requests

def main():
    payloads = {"base": "USD", "symbols": "GBP"}
    response = requests.get("https://api.exchangeratesapi.io/latest", params=payloads)

    if response.status_code != 200:
        print("Status Code: {}".format(response.status_code))
        raise Exception("There was an Error!")

    data = response.json()
    print("JSON data: {}".format(data))


if __name__ == "__main__":
    main()