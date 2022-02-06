import requests


def client():
    #credentials = {"username": "admin", "password": "1234"}
    #response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/", data=credentials)

    token_h = "Token 7009ee799d8f33adb7157a538da8a1e51acaf5d6"
    headers = {"Authorization": token_h}
    response = requests.get("http://127.0.0.1:8000/api/profiles/", headers=headers)

    print("Status Code: {}".format(response.status_code))
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()
