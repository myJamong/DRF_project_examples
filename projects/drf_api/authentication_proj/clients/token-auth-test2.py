import requests


def client():
    # data = {
    #     "username": "resttest",
    #     "email": "test@rest.com",
    #     "password1": "changeme123",
    #     "password2": "changeme123"
    # }
    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/registration/", data=data)

    token_h = "Token 374efb512d8920253c5763e7beb70aaa3b886ee1"
    headers = {"Authorization": token_h}
    response = requests.get("http://127.0.0.1:8000/api/profiles/", headers=headers)

    print("Status Code: {}".format(response.status_code))
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()
