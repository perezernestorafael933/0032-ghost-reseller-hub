# 🏛️ ARQUITECTURA Y ESTADO VIGENTE DEL CÓDIGO: `0032-ghost-reseller-hub`
### Investigador Principal: Rafael "Rafa" Pérez & Angelus AGI
**Fecha de Actualización:** 10 de Septiembre de 2026 | **Estándar:** Open Spec v2.0 (PyPI Modular)

> [!CAUTION]
> **MANDATO DE NO-RECONSTRUCCIÓN (CONTINUIDAD INCREMENTAL OBLIGATORIA):**
> Este repositorio contiene módulos previamente desarrollados y validados. Queda **ESTRICTAMENTE PROHIBIDO** reescribir, recrear desde cero o reemplazar con archivos temporales las funciones que ya están implementadas. Todo nuevo desarrollo debe importar y extender directamente estos componentes.

---

## 📦 1. MÓDULOS Y ARCHIVOS YA IMPLEMENTADOS (BASE REAL EN DISCO - NO RECONSTRUIR)

- `/app/__init__.py`: Componente funcional activo.
- `/app/main.py`: Componente funcional activo.
- `/despliegues_multicloud/huggingface/app.py`: Componente funcional activo.
- `/despliegues_multicloud/huggingface_stealth/private_dataset/bot_core.py`: Componente funcional activo.
- `/despliegues_multicloud/huggingface_stealth/public_space/app.py`: Componente funcional activo.
- `/despliegues_multicloud/pella/app_pella.py`: Componente funcional activo.
- `/despliegues_multicloud/pella/bot.py`: Componente funcional activo.
- `/despliegues_multicloud/pella/main.py`: Componente funcional activo.
- `/despliegues_multicloud/pythonanywhere/flask_app.py`: Componente funcional activo.
- `/despliegues_multicloud/telebothost/bot_telebothost.py`: Componente funcional activo.
- `/main.py`: Componente funcional activo.
- `/scripts/check_live_products.py`: Componente funcional activo.
- `/scripts/deploy_render_github.py`: Componente funcional activo.
- `/scripts/gdrive_hub.py`: Componente funcional activo.
- `/src/ghost_reseller/config.py`: Componente funcional activo.
- `/src/ghost_reseller/main.py`: Componente funcional activo.
- `/src/ghost_reseller/services/gas_database.py`: Componente funcional activo.
- `/src/ghost_reseller/services/multi_supplier_manager.py`: Componente funcional activo.
- `/src/ghost_reseller/services/supplier_client.py`: Componente funcional activo.
- `/src/ghost_reseller/services/wallet_ledger.py`: Componente funcional activo.
- `/src/ghost_reseller/services/web3_wallet.py`: Componente funcional activo.
- `/src/ghost_reseller/telegram_bot.py`: Componente funcional activo.

---

## 🔧 2. CÓMO CONSUMIR E IMPORTAR COMO PAQUETE MODULAR PYPI

Este repositorio está configurado como biblioteca PEP 621 (`pyproject.toml`).
Para instalar en modo desarrollo:
```bash
pip install -e .
```
Las importaciones deben realizarse desde los paquetes existentes:
- `from app import ...`

---

## 🚀 3. DIRECTRICES DE EXTENSIÓN INCREMENTAL
1. **Inspección Previa:** Consultar las clases y funciones en los archivos de la sección 1.
2. **Cero Duplicación:** Si ya existe un cálculo o función de preprocesamiento, úsala directamente.
3. **Tests sin GPU y sin DB Remota:** Todos los tests deben usar las funciones existentes con datos sintéticos en `tests/conftest.py`.

[VINCIT_OMNIA_VERITAS]