import pytest


@pytest.mark.asyncio()
async def test_just_for_ci() -> None:
    assert 2 == 2


@pytest.mark.asyncio()
async def test_just_for_ci_2() -> None:
    assert 1 == 1
