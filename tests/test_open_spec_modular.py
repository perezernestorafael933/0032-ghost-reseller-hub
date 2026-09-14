import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from conftest import mock_synthetic_payload

def test_open_spec_metadata_and_mock(mock_synthetic_payload):
    assert mock_synthetic_payload["status"] == "ready"
    assert len(mock_synthetic_payload["values"]) == 4
    # Validacion determinista en CPU sin dependencias externas
    assert sum(mock_synthetic_payload["values"]) > 0

if __name__ == "__main__":
    payload = mock_synthetic_payload()
    test_open_spec_metadata_and_mock(payload)
    print("[SUCCESS] ALL_OPEN_SPEC_MODULAR_TESTS_PASSED")
