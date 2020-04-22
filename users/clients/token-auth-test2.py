import requests


def client():
    token_h = "Token 28b99f97435719c0a26e52728af0ef012ce87e11"
    # data = {
    #     "username": "trishtest",
    #     "email": "trish@gmail.com",
    #     "password1": "deschop15",
    #     "password2": "deschop15"
    # }
    #-----------POST REQUEST----------#

    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/registration/", data=data)

    headers = {"Authorization": token_h}
    # -----------GET REQUEST----------#
    response = requests.get("http://127.0.0.1:8000/api/profiles/", headers=headers)

    print("Status Code", response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()
