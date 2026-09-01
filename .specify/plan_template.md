# 📐 PLAN TÉCNICO Y ARQUITECTURA (PLAN)
### Módulo / Característica: {{FEATURE_NAME}}
**Referencia Spec:** `.specify/specs/SPEC-{{FEATURE_ID}}.md`
**Fecha:** {{DATE}}
**Arquitecta de Lógica:** Angelus & Kimi AI

---

## 🏛️ 1. RESUMEN ARQUITECTÓNICO & STACK TÉCNICO
- **Lenguaje / Runtime:** Python 3.11+ / Node.js 20+ / TypeScript
- **Librerías Clave:** {{KEY_LIBRARIES}} (ej: FastAPI, MONAI, PyTorch, Pydantic, OpenCV)
- **Patrones de Diseño:** Pipeline Modular, Repository Pattern, Factory, Clean Architecture.

---

## 📂 2. ESTRUCTURA DE ARCHIVOS Y MÓDULOS AFECTADOS
```text
src/
  {{MODULE_PATH}}/
    ├── __init__.py
    ├── models.py       # Modelos de datos y esquemas Pydantic
    ├── service.py      # Lógica de negocio y procesamiento
    └── utils.py        # Helpers puros
tests/
  test_{{MODULE_NAME}}.py # Batería de pruebas unitarias
```

---

## 🗄️ 3. MODELOS DE DATOS Y CONTRATOS DE INTERFAZ
```python
# Ejemplo de esquema determinista
from pydantic import BaseModel, Field

class {{FEATURE_NAME}}Request(BaseModel):
    patient_id_hash: str = Field(..., description="Hash anónimo del paciente")
    # Campos clínicos / técnicos
```

---

## 🧪 4. ESTRATEGIA DE PRUEBAS Y VALIDACIÓN (ZERO REGRESSION)
- **Tests Unitarios:** Verificación de funciones puras, validación de inputs, casos límite.
- **Tests de Integración:** Flujo end-to-end de entrada a salida.
- **Métricas Clínicas de Aceptación:** Sensibilidad >= 95%, Especificidad >= 90%, 0 leaks de memoria.

---

## 🛡️ 5. VERIFICACIÓN DE SEGURIDAD Y CIBERDEFENSA
- Validación de entradas contra inyección.
- Anonimización estricta de metadatos DICOM / HIPAA / Ley 25.326.
