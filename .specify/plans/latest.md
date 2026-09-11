# 📐 PLAN TÉCNICO Y ARQUITECTURA MODULAR PIP
### Paquete: `ghost-reseller-hub` | Repositorio: `0032-ghost-reseller-hub`
**Cluster:** Automatización & Finanzas
**Estado:** STAGE_2_CORE_LOGIC

---

## 🏗️ 1. ARQUITECTURA DE PAQUETE PYPI

```
0032-ghost-reseller-hub/
├── .specify/
│   ├── constitution.md
│   ├── open_spec.json
│   ├── specs/latest.md
│   ├── plans/latest.md
│   └── tasks/latest.md
├── pyproject.toml
├── src/
│   └── ghost_reseller_hub/
│       ├── __init__.py       # Exportación pública (__all__)
│       ├── core.py           # Funciones puras de cálculo
│       ├── adapters.py       # Mocks de datos y lectura local
│       └── pipeline.py       # Orquestador del flujo
└── tests/
    ├── conftest.py           # Fixtures sintéticas en memoria
    └── test_core.py          # Pruebas en CPU deterministas
```

---

## 🔧 2. DESACOPLAMIENTO DE RECURSOS
- **Cálculo Local:** Optimizado para NumPy / PyTorch CPU / SQLite.
- **Cómputo en la Nube:** Interfaz `CloudBackend` lista para ser invocada por Jules en la VM de Google Cloud.
