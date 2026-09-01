# 📝 ESPECIFICACIÓN FUNCIONAL (SPEC)
### Módulo / Característica: {{FEATURE_NAME}}
**Fecha:** {{DATE}}
**Estado:** DRAFT | APPROVED | IN_PROGRESS | COMPLETED
**ID de Spec:** `SPEC-{{FEATURE_ID}}`

---

## 🎯 1. OBJETIVO Y JUSTIFICACIÓN (QUÉ Y POR QUÉ)
- **Problema que resuelve:** {{PROBLEM_DESCRIPTION}}
- **Propósito y valor:** {{PURPOSE_AND_VALUE}}
- **Impacto Clínico / Técnico:** {{CLINICAL_OR_TECH_IMPACT}}

---

## 👤 2. HISTORIAS DE USUARIO Y CASOS DE USO
- **Como** {{USER_ROLE}} (ej: Radiólogo / Investigador / Operador de Ciberdefensa)
- **Quiero** {{DESIRED_CAPABILITY}}
- **Para que** {{BENEFIT_OUTCOME}}

---

## 📥 3. ENTRADAS, SALIDAS Y CONTRATO DE DATOS
- **Entradas Esperadas:**
  - Tipos de datos, formatos (DICOM, PNG, JSON, FASTQ, etc.), rangos válidos.
- **Salidas Producidas:**
  - Estructura de respuesta, esquemas JSON, artefactos generados.
- **Invariantes del Dominio:**
  - Reglas que NUNCA deben romperse (ej: métricas BI-RADS válidas entre 0 y 6, hashes SHA-256 inalterados).

---

## ⚠️ 4. CASOS LÍMITE Y MANEJO DE EXCEPCIONES
- Datos corruptos o nulos.
- Caídas de red o timeouts en APIs remotas.
- Errores de concurrencia o recursos insuficientes.

---

## ✅ 5. CRITERIOS DE ACEPTACIÓN
- [ ] Criterio 1: {{ACCEPTANCE_1}}
- [ ] Criterio 2: {{ACCEPTANCE_2}}
- [ ] Criterio 3: Cobertura de tests unitarios >= 90% con 0 regresiones.
