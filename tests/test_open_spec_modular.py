def test_open_spec_metadata_and_mock(mock_synthetic_payload):
    assert mock_synthetic_payload["status"] == "ready"
    assert len(mock_synthetic_payload["values"]) == 4
    # Validacion determinista en CPU sin dependencias externas
    assert sum(mock_synthetic_payload["values"]) > 0
