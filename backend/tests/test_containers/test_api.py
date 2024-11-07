import pytest
from httpx import AsyncClient
from testcontainers.core.utils import logging

from tests.hash_service import HashService


@pytest.mark.asyncio()
async def test_empty_rows(client: AsyncClient) -> None:
    response = await client.get("/large_data/")
    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.asyncio()
async def test_post_one_large_data(client: AsyncClient) -> None:
    large_data = {"big_data": "test"}
    response = await client.post("/large_data/", json=large_data)
    assert response.status_code == 201
    # if we don't have hash service the hash field is empty
    assert response.text == ""


@pytest.mark.asyncio()
async def test_post_one_large_data_with_hash_service(
    client: AsyncClient, hash_service: HashService
) -> None:
    large_data = {"big_data": "test"}
    logging.warning(hash_service.get_logs())
    response = await client.post("/large_data/", json=large_data)
    assert response.status_code == 201
    logging.warning(hash_service.get_logs())
    # if we don't have hash service the hash field is empty
    assert response.text == ""
