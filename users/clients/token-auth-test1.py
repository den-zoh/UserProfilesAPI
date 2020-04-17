import requests


def client():
    token_h = "Token 341ca494fc62bf96c01d413eb13299baa7cfd4c2"
    # credentials = {"username": "trish", "password": "deschop15"}
    #
    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/", data=credentials)
    headers = {"Authorization": token_h}

    response = requests.get("http://127.0.0.1:8000/api/profiles/", headers=headers)

    print("Status Code", response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()
