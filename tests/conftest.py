"""Pytest fixtures"""
import pytest
from unittest.mock import AsyncMock
import httpx

@pytest.fixture
def mock_httpx_client():
    """Mock httpx.AsyncClient"""
    client = AsyncMock(spec=httpx.AsyncClient)
    return client

@pytest.fixture
def sample_providers():
    """Sample provider configuration"""
    return {
        "deepseek": {
            "name": "DeepSeek",
            "endpoint": "https://api.deepseek.com/v1/chat/completions",
            "env_key": "DEEPSEEK_API_KEY",
            "model": "deepseek-chat",
            "auth_type": "bearer",
            "color": "green",
            "icon": "🟢"
        }
    }

@pytest.fixture
def sample_api_keys():
    """Sample API keys"""
    return {"deepseek": "sk-test-key"}
