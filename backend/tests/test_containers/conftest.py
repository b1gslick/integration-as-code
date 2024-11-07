from collections.abc import AsyncGenerator, Generator
from typing import Any
import logging

import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from testcontainers.postgres import PostgresContainer, os

from app.main import create_app


@pytest.fixture(scope="module", autouse=True)
def database_container_setup() -> Generator[PostgresContainer, Any, Any]:
    logging.warning("start")
    with PostgresContainer(
        "postgres:16-alpine",
        port=5432,
        username="postgres",
        password="postgres",  # noqa: S106
        dbname="postgres",
        driver="postgresql",
    ).with_bind_ports(
        5432,
        5432,
    ) as pg:
        yield pg


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
