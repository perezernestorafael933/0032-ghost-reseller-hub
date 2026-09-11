# 📋 TAREAS ATÓMICAS Y CHECKLIST DE MVP (OPEN SPEC)
### Paquete: `ghost-reseller-hub` | Repositorio: `0032-ghost-reseller-hub`
**Estado Actual:** STAGE_2_CORE_LOGIC

---

## 📌 CHECKLIST DE ENTREGABLES MÍNIMOS VIABLES (MVP):

- [x] **T1. Estandarización Open Spec:** Creación de `.specify/` con constitución, manifiesto y especificaciones.
- [x] **T2. Arquitectura de Paquete PyPI:** Configuración de `pyproject.toml` con metadatos y dependencias desacopladas.
- [x] **T3. Funciones Modulares Puras:** Definición de funciones nucleares con tipado fuerte y exportación en `__init__.py`.
- [x] **T4. Fixtures y Mocks Locales:** Implementación de datos sintéticos para evitar depender de bases de datos externas.
- [x] **T5. Suite de Pruebas Unitarias:** Creación y verificación de tests en `tests/` ejecutables en CPU con `pytest`.
- [ ] **T6. Integración con Jules Cloud:** Conexión con VM de Google Cloud para tareas de cómputo intensivo o GPU real.
- [ ] **T7. Publicación de Release:** Compilación de wheel (`uv build`) y generación de release `v0.1.0-mvp`.
