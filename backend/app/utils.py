import logging
import requests
import json

from app import settings


async def calculate_hash(data: str):
    url = settings.hash_service

    if url == "":
        return

    response_data = json.dumps({"data": data})

    response = requests.post(f"{url}/hash", data=response_data)
    assert response.status_code == 201
    return response.json()
