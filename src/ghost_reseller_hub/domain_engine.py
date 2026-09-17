# -*- coding: utf-8 -*-
"""
Motor de Dominio Modular: ghost_reseller_hub
Dominio: educacion_ciencias_cognitivas_ia
Investigador: Rafael 'Rafa' Perez & Angelus AGI
Tarea: [T05] Fixtures Sintéticos y Mocks desacoplados de APIs externas
"""

import math
import hashlib
from typing import Dict, Any, List, Optional

def process_domain_payload(data: Dict[str, Any]) -> Dict[str, Any]:
    """Procesa datos nucleares del dominio con validación de tipos."""
    val = float(data.get('valor_base', 1.0))
    transformed = math.sqrt(abs(val)) * 1.61803398875
    checksum = hashlib.sha256(str(transformed).encode()).hexdigest()[:12]
    return {
        'status': 'OK',
        'paquete': 'ghost_reseller_hub',
        'dominio': 'educacion_ciencias_cognitivas_ia',
        'valor_transformado': transformed,
        'checksum_silicio': checksum
    }

def generate_synthetic_reseller_cognitive_curriculum_fixture(
    seed: int = 42,
    num_students: int = 25,
    curriculum_level: str = "advanced_cognitive_ai_edtech",
    include_product_catalog: bool = True
) -> Dict[str, Any]:
    """
    [T05] Genera un fixture sintético determinista de plataforma educativa,
    modelado cognitivo y gestión de conocimiento científico avanzado.
    Desacoplado 100% de APIs externas, gateways de pago remotos o servicios cloud.

    Modela:
      - Estructura curricular en 5 módulos cognitivos ontológicos.
      - Cohorte de aprendices sintéticos con métricas de asimilación conceptual,
        retención mnémica y rendimiento en resolución de problemas generados vía PRNG LCG.
      - Mocks de catálogo de conocimiento/herramientas educativas de silicio (AI & Dev Tools).
      - Resumen estadístico agregado (promedio de maestría, tasa de finalización).
      - Firma criptográfica determinista SHA-256 de 64 caracteres.
    """
    if num_students <= 0:
        raise ValueError("El número de estudiantes/aprendices debe ser estrictamente positivo.")

    # PRNG determinista LCG (Linear Congruential Generator) para reproducibilidad absoluta en CPU
    a_param = 1664525
    c_param = 1013904223
    m_param = 2**32
    current_state = seed & 0xFFFFFFFF

    cognitive_modules = [
        {"module_id": "COG-01", "name": "Ontología del Conocimiento & Grafos Conceptuales", "hours": 12, "weight": 0.15},
        {"module_id": "COG-02", "name": "Modelado Cognitivo & Métricas de Carga Mental", "hours": 18, "weight": 0.20},
        {"module_id": "COG-03", "name": "Arquitecturas LLM/Agentes en Educación Científica", "hours": 24, "weight": 0.25},
        {"module_id": "COG-04", "name": "Sistemas de Distribución Educativa & Licenciamiento Ético", "hours": 16, "weight": 0.20},
        {"module_id": "COG-05", "name": "Metacognición AGI, Evaluación Dinámica & Memoria Persistente", "hours": 20, "weight": 0.20}
    ]

    cohort_records: List[Dict[str, Any]] = []
    mastery_scores: List[float] = []
    retention_scores: List[float] = []

    for idx in range(1, num_students + 1):
        current_state = (a_param * current_state + c_param) % m_param
        u1 = (current_state + 1) / (m_param + 1)

        current_state = (a_param * current_state + c_param) % m_param
        u2 = (current_state + 1) / (m_param + 1)

        # Métricas cognitivas sintéticas:
        # Puntuación de maestría conceptual: [0.60, 0.99]
        mastery = round(0.60 + (u1 * 0.39), 4)
        # Índice de retención mnémica: [0.65, 0.98]
        retention = round(0.65 + (u2 * 0.33), 4)
        progress_pct = round(50.0 + ((u1 + u2) * 25.0), 2)

        mastery_scores.append(mastery)
        retention_scores.append(retention)

        learner_hash = hashlib.md5(f"LEARNER-{seed}-{idx}".encode()).hexdigest()[:8]
        cohort_records.append({
            "learner_id": f"GHOST-COG-{learner_hash}",
            "completed_modules": min(5, int(2 + (u1 * 4))),
            "overall_progress_pct": progress_pct,
            "cognitive_mastery_score": mastery,
            "knowledge_retention_index": retention,
            "status": "mastered" if mastery >= 0.85 else ("proficient" if mastery >= 0.70 else "in_training")
        })

    mean_mastery = sum(mastery_scores) / len(mastery_scores) if mastery_scores else 0.0
    mean_retention = sum(retention_scores) / len(retention_scores) if retention_scores else 0.0

    catalog_spec: Optional[List[Dict[str, Any]]] = None
    if include_product_catalog:
        catalog_spec = [
            {
                "product_id": "EDU-AI-GEMINI-18M",
                "title": "Google Gemini Pro Educational Node",
                "domain_category": "ai_cognitive_computing",
                "tier": "researcher",
                "offline_mock_tokens_k": 2048,
                "status": "ready"
            },
            {
                "product_id": "EDU-DEV-REPLIT-CORE",
                "title": "Cloud Dev Sandbox & Agentic Engine",
                "domain_category": "educational_coding",
                "tier": "student",
                "offline_mock_tokens_k": 512,
                "status": "ready"
            },
            {
                "product_id": "EDU-DS-NEURAL-CANVA",
                "title": "Visual Cognitive Design Suite",
                "domain_category": "knowledge_visualization",
                "tier": "educator",
                "offline_mock_tokens_k": 256,
                "status": "ready"
            }
        ]

    signature_raw = (
        f"{seed}:{num_students}:{curriculum_level}:{mean_mastery:.4f}:"
        f"{mean_retention:.4f}:{len(cognitive_modules)}"
    )
    fixture_hash = hashlib.sha256(signature_raw.encode("utf-8")).hexdigest()

    return {
        "fixture_version": "1.0.0",
        "environment": "synthetic_ghost_reseller_hub_cognitive_suite",
        "domain": "educacion_ciencias_cognitivas_ia",
        "seed": seed,
        "parameters": {
            "num_students": num_students,
            "curriculum_level": curriculum_level,
            "total_modules": len(cognitive_modules),
            "include_product_catalog": include_product_catalog
        },
        "curriculum_structure": cognitive_modules,
        "cohort_performance_summary": {
            "mean_cognitive_mastery": round(mean_mastery, 4),
            "mean_knowledge_retention": round(mean_retention, 4),
            "mastered_ratio": round(
                sum(1 for s in cohort_records if s["status"] == "mastered") / num_students, 4
            )
        },
        "educational_catalog": catalog_spec,
        "sample_cohort": cohort_records[:5],
        "total_cohort_count": len(cohort_records),
        "sha256_fingerprint": fixture_hash
    }

def generate_synthetic_reseller_distribution_mock(
    order_id: str = "ORD-EDU-8821",
    product_tier: str = "researcher",
    requested_units: int = 1
) -> Dict[str, Any]:
    """
    [T05] Genera un mock determinista de distribución y licenciamiento educativo
    desacoplado de pasarelas de pago externas, APIs de proveedores remotos y contratos Web3.
    """
    signature_base = f"{order_id}:{product_tier}:{requested_units}"
    order_hash = hashlib.sha256(signature_base.encode("utf-8")).hexdigest()

    base_costs = {
        "student": 1.50,
        "educator": 3.00,
        "researcher": 5.50
    }
    unit_cost = base_costs.get(product_tier, 2.50)
    total_cost = round(unit_cost * requested_units, 2)
    allocated_quota_mb = (requested_units * 512)

    return {
        "mock_id": f"MOCK-DIST-{order_hash[:8]}",
        "order_id": order_id,
        "product_tier": product_tier,
        "requested_units": requested_units,
        "mock_cost_usdt": total_cost,
        "allocated_cloud_quota_mb": allocated_quota_mb,
        "activation_token": f"ACT-MOCK-{order_hash[8:24].upper()}",
        "mock_source": "offline_ghost_reseller_hub_stub",
        "sha256_mock_signature": order_hash[:16]
    }

def validate_synthetic_reseller_fixture(fixture: Dict[str, Any]) -> bool:
    """
    [T05] Valida la integridad estructural, tipos e invariantes de un fixture sintético educativo y cognitivo.
    Verifica firma hash SHA-256 de 64 caracteres, rangos [0.0, 1.0] de métricas y coherencia en conteos.
    """
    required_keys = [
        "fixture_version", "environment", "domain", "seed",
        "parameters", "curriculum_structure", "cohort_performance_summary",
        "sample_cohort", "total_cohort_count", "sha256_fingerprint"
    ]
    for k in required_keys:
        if k not in fixture:
            return False

    params = fixture["parameters"]
    summary = fixture["cohort_performance_summary"]

    if params["num_students"] <= 0:
        return False
    if fixture["total_cohort_count"] != params["num_students"]:
        return False
    if not (0.0 <= summary["mean_cognitive_mastery"] <= 1.0):
        return False
    if not (0.0 <= summary["mean_knowledge_retention"] <= 1.0):
        return False
    if not (0.0 <= summary["mastered_ratio"] <= 1.0):
        return False
    if len(fixture["sha256_fingerprint"]) != 64:
        return False

    return True

def calculate_cognitive_load_index(
    task_intrinsic_complexity: float,
    extraneous_distraction_factor: float,
    germane_effort_investment: float,
    prior_domain_knowledge: float = 0.5
) -> Dict[str, Any]:
    """
    [T11] Modela la carga cognitiva basándose en la Teoría de Carga Cognitiva de Sweller.
    - Carga Intrínseca: complejidad del material / conocimiento previo.
    - Carga Extraña: interferencias, ruido, falta de ergonomía cognitiva.
    - Carga Pertinente (Germane): esfuerzo dedicado a la construcción de esquemas mentales.
    - Carga Cognitiva Total: combinación ponderada acotada en [0.0, 1.0].
    """
    if not (0.0 <= task_intrinsic_complexity <= 1.0):
        raise ValueError("task_intrinsic_complexity debe estar en el rango [0.0, 1.0]")
    if not (0.0 <= extraneous_distraction_factor <= 1.0):
        raise ValueError("extraneous_distraction_factor debe estar en el rango [0.0, 1.0]")
    if not (0.0 <= germane_effort_investment <= 1.0):
        raise ValueError("germane_effort_investment debe estar en el rango [0.0, 1.0]")
    
    clamped_prior = max(0.05, min(1.0, prior_domain_knowledge))
    
    # La carga intrínseca efectiva se amortigua con el conocimiento previo del estudiante
    effective_intrinsic = task_intrinsic_complexity * (1.0 - (0.5 * clamped_prior))
    effective_extraneous = extraneous_distraction_factor * 0.8
    effective_germane = germane_effort_investment * 0.6
    
    raw_total_load = (0.5 * effective_intrinsic) + (0.35 * effective_extraneous) + (0.15 * effective_germane)
    total_cognitive_load = round(min(1.0, max(0.0, raw_total_load)), 4)
    
    if total_cognitive_load >= 0.80:
        overload_status = "CRITICAL_OVERLOAD"
    elif total_cognitive_load >= 0.65:
        overload_status = "HIGH_STRAIN"
    elif total_cognitive_load >= 0.35:
        overload_status = "OPTIMAL_FLOW"
    else:
        overload_status = "UNDER_STIMULATED"
        
    return {
        "task_intrinsic_complexity": round(task_intrinsic_complexity, 4),
        "effective_intrinsic_load": round(effective_intrinsic, 4),
        "effective_extraneous_load": round(effective_extraneous, 4),
        "effective_germane_load": round(effective_germane, 4),
        "total_cognitive_load_index": total_cognitive_load,
        "overload_status": overload_status,
        "is_overloaded": total_cognitive_load >= 0.65
    }

def detect_mental_fatigue_and_strain(
    session_duration_minutes: float,
    consecutive_high_difficulty_tasks: int,
    reaction_time_latency_ms: float,
    baseline_reaction_time_ms: float = 350.0,
    error_rate_drift: float = 0.05
) -> Dict[str, Any]:
    """
    [T11] Detecta fatiga mental y agotamiento neurocognitivo acumulado:
    - Duración acumulada de la sesión continua.
    - Número de tareas consecutivas de alta dificultad sin descanso.
    - Desviación / latencia en el tiempo de reacción frente a la línea base.
    - Deriva en la tasa de errores del estudiante.
    Retorna índice de fatiga [0.0, 1.0] y nivel de agotamiento.
    """
    if session_duration_minutes < 0.0:
        raise ValueError("session_duration_minutes no puede ser negativo")
    if consecutive_high_difficulty_tasks < 0:
        raise ValueError("consecutive_high_difficulty_tasks no puede ser negativo")
        
    # Factor de duración: función sigmoidal saturando a partir de 90-120 minutos
    duration_factor = 1.0 / (1.0 + math.exp(-0.04 * (session_duration_minutes - 75.0)))
    
    # Factor de tareas intensas consecutivas: saturación progresiva
    task_strain_factor = min(1.0, consecutive_high_difficulty_tasks * 0.15)
    
    # Desviación de latencia de reacción: enlentecimiento psicomotor por fatiga
    baseline = max(100.0, baseline_reaction_time_ms)
    latency_ratio = max(0.5, reaction_time_latency_ms / baseline)
    latency_penalty = min(1.0, max(0.0, (latency_ratio - 1.0) * 0.8)) if latency_ratio > 1.0 else 0.0
    
    # Deriva de error
    error_penalty = min(1.0, max(0.0, error_rate_drift * 1.5))
    
    # Índice de fatiga mental ponderado
    raw_fatigue = (0.35 * duration_factor) + (0.25 * task_strain_factor) + (0.25 * latency_penalty) + (0.15 * error_penalty)
    fatigue_index = round(min(1.0, max(0.0, raw_fatigue)), 4)
    
    if fatigue_index >= 0.75:
        fatigue_level = "EXHAUSTION"
    elif fatigue_index >= 0.50:
        fatigue_level = "MODERATE_FATIGUE"
    elif fatigue_index >= 0.25:
        fatigue_level = "MILD_FATIGUE"
    else:
        fatigue_level = "ALERT_REFRESHED"
        
    return {
        "session_duration_minutes": float(session_duration_minutes),
        "duration_strain_factor": round(duration_factor, 4),
        "consecutive_tasks": consecutive_high_difficulty_tasks,
        "task_strain_factor": round(task_strain_factor, 4),
        "latency_drift_ratio": round(latency_ratio, 4),
        "mental_fatigue_index": fatigue_index,
        "fatigue_level": fatigue_level,
        "requires_intervention": fatigue_index >= 0.50
    }

def adapt_dynamic_study_pacing(
    cognitive_load_result: Dict[str, Any],
    fatigue_result: Dict[str, Any],
    nominal_block_duration_min: int = 45,
    nominal_difficulty: float = 0.7
) -> Dict[str, Any]:
    """
    [T11] Adapta dinámicamente el ritmo de estudio (pacing), la duración de bloques,
    los descansos requeridos y la dificultad sugerida para prevenir el burnout y la sobrecarga.
    Retorna recomendaciones pedagógicas en tiempo real y firma SHA-256 del plan adaptativo.
    """
    cog_load = float(cognitive_load_result.get("total_cognitive_load_index", 0.5))
    fatigue = float(fatigue_result.get("mental_fatigue_index", 0.3))
    
    # Estrés neurocognitivo compuesto
    composite_stress = round(min(1.0, (0.55 * cog_load) + (0.45 * fatigue)), 4)
    
    # Adaptación de duración de bloque: reducción progresiva si hay sobrecarga
    if composite_stress >= 0.75:
        pacing_mode = "MANDATORY_BREAK"
        recommended_block_min = max(15, int(nominal_block_duration_min * 0.4))
        recommended_break_min = 20
        adapted_difficulty = max(0.2, round(nominal_difficulty * 0.5, 2))
        intervention_action = "HALT_IMMEDIATE: Pausa activa obligatoria de 20 min y rehidratación."
    elif composite_stress >= 0.55:
        pacing_mode = "DE-ESCALATION"
        recommended_block_min = max(20, int(nominal_block_duration_min * 0.7))
        recommended_break_min = 10
        adapted_difficulty = max(0.35, round(nominal_difficulty * 0.75, 2))
        intervention_action = "ADAPT_MICRO: Desescalar dificultad a casos de consolidación conceptual."
    elif composite_stress >= 0.30:
        pacing_mode = "STEADY_PROGRESS"
        recommended_block_min = nominal_block_duration_min
        recommended_break_min = 5
        adapted_difficulty = nominal_difficulty
        intervention_action = "MAINTAIN_FLOW: Ritmo de asimilación óptimo en zona de desarrollo próximo."
    else:
        pacing_mode = "ACCELERATED_CHALLENGE"
        recommended_block_min = min(60, int(nominal_block_duration_min * 1.2))
        recommended_break_min = 5
        adapted_difficulty = min(1.0, round(nominal_difficulty * 1.15, 2))
        intervention_action = "BOOST_STIMULUS: Capacidad cognitiva plena, introducir casos clínicos de alta complejidad."
        
    fingerprint_raw = f"{composite_stress}:{pacing_mode}:{recommended_block_min}:{recommended_break_min}:{adapted_difficulty}"
    plan_signature = hashlib.sha256(fingerprint_raw.encode("utf-8")).hexdigest()
    
    return {
        "pacing_mode": pacing_mode,
        "composite_stress_index": composite_stress,
        "original_nominal_block_min": nominal_block_duration_min,
        "recommended_block_duration_min": recommended_block_min,
        "recommended_break_duration_min": recommended_break_min,
        "adapted_content_difficulty": adapted_difficulty,
        "intervention_action": intervention_action,
        "plan_sha256_fingerprint": plan_signature
    }

def model_learner_fatigue_and_pacing_pipeline(
    task_intrinsic_complexity: float,
    extraneous_distraction_factor: float,
    germane_effort_investment: float,
    session_duration_minutes: float,
    consecutive_high_difficulty_tasks: int,
    reaction_time_latency_ms: float,
    prior_domain_knowledge: float = 0.5,
    baseline_reaction_time_ms: float = 350.0,
    error_rate_drift: float = 0.05,
    nominal_block_duration_min: int = 45,
    nominal_difficulty: float = 0.7
) -> Dict[str, Any]:
    """
    [T11] Pipeline integral de modelado cognitivo y prevención de fatiga mental.
    Ejecuta evaluación de carga cognitiva, detección de fatiga y cálculo de adaptación dinámica de ritmo.
    """
    cog_load = calculate_cognitive_load_index(
        task_intrinsic_complexity=task_intrinsic_complexity,
        extraneous_distraction_factor=extraneous_distraction_factor,
        germane_effort_investment=germane_effort_investment,
        prior_domain_knowledge=prior_domain_knowledge
    )
    
    fatigue = detect_mental_fatigue_and_strain(
        session_duration_minutes=session_duration_minutes,
        consecutive_high_difficulty_tasks=consecutive_high_difficulty_tasks,
        reaction_time_latency_ms=reaction_time_latency_ms,
        baseline_reaction_time_ms=baseline_reaction_time_ms,
        error_rate_drift=error_rate_drift
    )
    
    pacing = adapt_dynamic_study_pacing(
        cognitive_load_result=cog_load,
        fatigue_result=fatigue,
        nominal_block_duration_min=nominal_block_duration_min,
        nominal_difficulty=nominal_difficulty
    )
    
    return {
        "pipeline_version": "1.1.0",
        "domain": "educacion_ciencias_cognitivas_ia",
        "cognitive_load_assessment": cog_load,
        "fatigue_detection": fatigue,
        "study_pacing_adaptation": pacing,
        "status": "COMPLETED_OPTIMIZED"
    }

def execute_verification_cycle() -> bool:
    """Prueba determinista local sin dependencias externas verificando T01-T05 y T11."""
    res = process_domain_payload({'valor_base': 4.0})
    fixture = generate_synthetic_reseller_cognitive_curriculum_fixture(seed=123, num_students=20)
    dist_mock = generate_synthetic_reseller_distribution_mock(order_id="TEST-ORD-01")
    is_valid_fixture = validate_synthetic_reseller_fixture(fixture)
    
    # Verificación determinista de T11
    pipeline_res = model_learner_fatigue_and_pacing_pipeline(
        task_intrinsic_complexity=0.8,
        extraneous_distraction_factor=0.6,
        germane_effort_investment=0.7,
        session_duration_minutes=95.0,
        consecutive_high_difficulty_tasks=4,
        reaction_time_latency_ms=480.0
    )
    t11_valid = (
        pipeline_res["status"] == "COMPLETED_OPTIMIZED"
        and pipeline_res["cognitive_load_assessment"]["total_cognitive_load_index"] > 0
        and pipeline_res["fatigue_detection"]["mental_fatigue_index"] > 0
        and len(pipeline_res["study_pacing_adaptation"]["plan_sha256_fingerprint"]) == 64
    )

    return (
        res['valor_transformado'] > 0
        and len(res['checksum_silicio']) == 12
        and is_valid_fixture
        and dist_mock['mock_cost_usdt'] > 0
        and len(dist_mock['sha256_mock_signature']) == 16
        and t11_valid
    )

if __name__ == '__main__':
    print('Verificación de dominio:', execute_verification_cycle())

