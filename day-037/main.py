import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "dfdsf3dfdhgjsdsfs3fff3",
    "username": "rafa_qwerty",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
    
}

response = requests.get(url=pixela_endpoint, json=user_params)

print(response.text)