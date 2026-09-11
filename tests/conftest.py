import pytest

@pytest.fixture
def mock_synthetic_payload():
    return {
        "status": "ready",
        "sample_id": "MOCK-001",
        "values": [0.1, 0.4, 0.9, 0.2]
    }
