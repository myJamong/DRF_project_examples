import requests


def main():
    response = requests.get("http://www.google.com") # 200
    # response = requests.get("http://www.google.com/random") # 404
    print("Status Code: {0}".format(response.status_code))
    print("Headers: {0}".format(response.headers))
    print("Content-Type: {0}".format(response.headers['Content-Type']))
    print("Content: {0}".format(response.text))


if __name__ == "__main__":
    main()
