# 📋 LISTA DE TAREAS ACCIONABLES (TASKS)
### Módulo / Característica: {{FEATURE_NAME}}
**Referencia Spec:** `.specify/specs/SPEC-{{FEATURE_ID}}.md`
**Referencia Plan:** `.specify/plans/SPEC-{{FEATURE_ID}}_plan.md`
**Fecha:** {{DATE}}
**Estado de Ejecución:** PENDING | IN_PROGRESS | COMPLETED

---

## 🎯 TAREAS ATÓMICAS Y ORDEN DE EJECUCIÓN

<!-- Tareas para ejecución local por Nova/Angelus o Cloud por Jules -->

- [ ] **Fase 1: Modelos y Contratos de Datos**
  - [ ] 1.1 Crear archivo `src/{{MODULE_PATH}}/models.py` con esquemas Pydantic y tipado estricto.
  - [ ] 1.2 Escribir pruebas de validación de modelos en `tests/test_{{MODULE_NAME}}_models.py`.
  - [ ] 1.3 Verificar que las pruebas de modelos pasen (`pytest tests/test_{{MODULE_NAME}}_models.py`).

- [ ] **Fase 2: Lógica Central y Algoritmos**
  - [ ] 2.1 Implementar `src/{{MODULE_PATH}}/service.py` con el pipeline principal.
  - [ ] 2.2 Integrar manejo de excepciones y casos límite según el Spec.
  - [ ] 2.3 Escribir tests unitarios exhaustivos en `tests/test_{{MODULE_NAME}}_service.py`.
  - [ ] 2.4 Verificar que las pruebas pasen al 100%.

- [ ] **Fase 3: Integración, APIs y Conectores**
  - [ ] 3.1 Exponer endpoints en `src/api/` o CLI commands en `src/cli/`.
  - [ ] 3.2 Escribir tests de integración end-to-end.
  - [ ] 3.3 Validar que no existan regresiones en toda la suite de tests (`pytest`).

- [ ] **Fase 4: Documentación y Convergencia**
  - [ ] 4.1 Documentar uso y ejemplos en `docs/` o `README.md`.
  - [ ] 4.2 Validar cumplimiento total de los Criterios de Aceptación del Spec.
  - [ ] 4.3 Marcar Spec como COMPLETED.
