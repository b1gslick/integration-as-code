import logging

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio()
async def test_get_all_rows(client: AsyncClient) -> None:
    data = await client.get("/large_data/")
    logging.warning(data)
