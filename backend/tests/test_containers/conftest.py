from collections.abc import AsyncGenerator, Generator
from typing import Any
import logging

import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from testcontainers.postgres import PostgresContainer, os

from app.main import create_app
from tests.hash_service import HashService


@pytest.fixture(scope="function", autouse=True)
def database_container_setup() -> Generator[PostgresContainer, Any, Any]:
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
    ) as client:
        yield client


@pytest.fixture()
def hash_service() -> Generator[HashService, Any, Any]:
    with HashService("hash_calculator-server", host="0.0.0.0").with_name(
        "hash_service"
    ) as hash:
        yield hash
