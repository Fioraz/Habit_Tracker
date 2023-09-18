import requests
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv('v/.gitignore')
TOKEN = os.getenv("TOKEN")
USERNAME = "fiora"
GRAPH_ID = "graph1"


# <<<<---- CREATE USER ACCOUNT ---->>>>

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


# <<<<---- CREATE GRAPH ---->>>>

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Self-studying Graph",
    "unit": "Hours",
    "type": "int",
    "color": "momiji",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


# <<<<---- CREATE PIXELS ---->>>>

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(year=2023, month=9, day=15)

pixel_input = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "2",
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_input, headers=headers)
print(response.text)


# <<<<---- UPDATE PIXELS ---->>>>

date_to_update = datetime(year=2023, month=9, day=16)

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_to_update.strftime('%Y%m%d')}"

update_info = {
    "quantity": "3"
}

# response = requests.put(url=pixel_update_endpoint, json=update_info, headers=headers)
# print(response.text)


# <<<<---- DELETE PIXELS ---->>>>

date_to_delete = datetime(year=2023, month=9, day=15)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_to_delete.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
