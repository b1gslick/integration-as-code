import pytest
from httpx import AsyncClient

from tests.hash_service import HashService


@pytest.mark.asyncio()
async def test_empty_rows(client: AsyncClient) -> None:
    response = await client.get("/large_data/")
    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.asyncio()
async def test_post_one_large_data_with_hash_service(
    client: AsyncClient,
    hash_service: HashService,  # noqa: ARG001
) -> None:
    large_data = {"big_data": "test"}
    response = await client.post("/large_data/", json=large_data)
    assert response.status_code == 201
    assert (
        response.json()
        == "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"
    )
