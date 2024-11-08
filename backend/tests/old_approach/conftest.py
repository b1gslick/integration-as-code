from collections.abc import AsyncGenerator

import pytest_asyncio
from httpx import ASGITransport, AsyncClient

from src.main import create_app


@pytest_asyncio.fixture()
async def client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(
        transport=ASGITransport(app=create_app()),
        base_url="http://testserver",
        headers={
            "Authorization": "Bearer token",
        },
    ) as client:
        yield client
