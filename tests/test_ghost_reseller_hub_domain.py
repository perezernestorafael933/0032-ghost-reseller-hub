# -*- coding: utf-8 -*-
"""
Suite de Pruebas de Dominio y Fixtures Sintéticos: ghost_reseller_hub
Tarea [T05]: Entornos de datos sintéticos desacoplados de APIs externas.
Dominio: educacion_ciencias_cognitivas_ia
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'src'))

try:
    from ghost_reseller_hub.domain_engine import (
        process_domain_payload,
        generate_synthetic_reseller_cognitive_curriculum_fixture,
        generate_synthetic_reseller_distribution_mock,
        validate_synthetic_reseller_fixture,
        execute_verification_cycle
    )
except ImportError:
    import importlib.util
    p = Path(__file__).resolve().parent.parent / 'src' / 'ghost_reseller_hub' / 'domain_engine.py'
    spec = importlib.util.spec_from_file_location('domain_engine', str(p))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    process_domain_payload = mod.process_domain_payload
    generate_synthetic_reseller_cognitive_curriculum_fixture = mod.generate_synthetic_reseller_cognitive_curriculum_fixture
    generate_synthetic_reseller_distribution_mock = mod.generate_synthetic_reseller_distribution_mock
    validate_synthetic_reseller_fixture = mod.validate_synthetic_reseller_fixture
    execute_verification_cycle = mod.execute_verification_cycle

def test_domain_engine_basic():
    assert execute_verification_cycle() is True

def test_domain_engine_payload():
    res = process_domain_payload({'valor_base': 9.0})
    assert res['status'] == 'OK'
    assert res['valor_transformado'] > 0
    assert len(res['checksum_silicio']) == 12

def test_generate_synthetic_reseller_cognitive_curriculum_fixture_structure():
    fixture = generate_synthetic_reseller_cognitive_curriculum_fixture(
        seed=101,
        num_students=35,
        curriculum_level="advanced_cognitive_ai_edtech",
        include_product_catalog=True
    )
    assert fixture["fixture_version"] == "1.0.0"
    assert fixture["environment"] == "synthetic_ghost_reseller_hub_cognitive_suite"
    assert fixture["domain"] == "educacion_ciencias_cognitivas_ia"
    assert fixture["seed"] == 101
    assert fixture["parameters"]["num_students"] == 35
    assert fixture["parameters"]["total_modules"] == 5
    assert fixture["total_cohort_count"] == 35
    assert len(fixture["sample_cohort"]) == 5
    assert len(fixture["curriculum_structure"]) == 5
    assert fixture["educational_catalog"] is not None
    assert len(fixture["educational_catalog"]) == 3
    assert len(fixture["sha256_fingerprint"]) == 64
    assert validate_synthetic_reseller_fixture(fixture) is True

def test_generate_synthetic_reseller_fixture_reproducibility():
    f1 = generate_synthetic_reseller_cognitive_curriculum_fixture(seed=777, num_students=20)
    f2 = generate_synthetic_reseller_cognitive_curriculum_fixture(seed=777, num_students=20)
    assert f1["sha256_fingerprint"] == f2["sha256_fingerprint"]
    assert f1["cohort_performance_summary"]["mean_cognitive_mastery"] == f2["cohort_performance_summary"]["mean_cognitive_mastery"]
    assert f1["cohort_performance_summary"]["mean_knowledge_retention"] == f2["cohort_performance_summary"]["mean_knowledge_retention"]

def test_generate_synthetic_reseller_distribution_mock():
    mock = generate_synthetic_reseller_distribution_mock(
        order_id="ORD-EDU-9922",
        product_tier="researcher",
        requested_units=2
    )
    assert mock["order_id"] == "ORD-EDU-9922"
    assert mock["product_tier"] == "researcher"
    assert mock["requested_units"] == 2
    assert mock["mock_cost_usdt"] == 11.00
    assert mock["allocated_cloud_quota_mb"] == 1024
    assert mock["mock_source"] == "offline_ghost_reseller_hub_stub"
    assert len(mock["sha256_mock_signature"]) == 16

def test_validate_synthetic_reseller_fixture_edge_cases():
    valid_f = generate_synthetic_reseller_cognitive_curriculum_fixture(seed=55, num_students=15)
    assert validate_synthetic_reseller_fixture(valid_f) is True

    # Mutación inválida
    invalid_f = dict(valid_f)
    invalid_f["parameters"] = {"num_students": -5}
    assert validate_synthetic_reseller_fixture(invalid_f) is False

if __name__ == "__main__":
    test_domain_engine_basic()
    test_domain_engine_payload()
    test_generate_synthetic_reseller_cognitive_curriculum_fixture_structure()
    test_generate_synthetic_reseller_fixture_reproducibility()
    test_generate_synthetic_reseller_distribution_mock()
    test_validate_synthetic_reseller_fixture_edge_cases()
    print("[SUCCESS] ALL_T05_SYNTHETIC_FIXTURE_TESTS_PASSED_100%")
