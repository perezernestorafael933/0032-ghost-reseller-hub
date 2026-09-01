# AGENTS.md - System & Privacy Directives

## 🛡️ ANONYMITY & IDENTITY SHIELDING (CRITICAL RULE)
1. **Zero Personal Attribution**: This repository MUST NEVER contain real personal names, private home disk paths, DNI, personal emails, or clinical identities in code, docstrings, commits, or web responses.
2. **System Name**: Always reference the project as `Nexus Reseller Core` or `Ghost Reseller System`.
3. **Traceback Sanitization**: FastAPI endpoints must handle top-level exceptions cleanly without leaking local file paths or raw stack traces.
4. **Environment Isolation**: Secret API keys (`RESELLER_API_KEY`, `CRYPTO_BOT_TOKEN`, `TELEGRAM_BOT_TOKEN`) must only be read from `.env` and NEVER hardcoded or committed to git.

## 📦 Project Architecture
- `src/ghost_reseller/config.py`: Anonymous settings module.
- `src/ghost_reseller/main.py`: FastAPI server for webhooks & health checks.
- `src/ghost_reseller/services/supplier_client.py`: Upstream API client for product catalog and instant order fulfillment.
- `src/ghost_reseller/services/wallet_ledger.py`: Isolated USDT balance and transaction history manager.
- `tests/`: Automated unit test suite using `pytest`.



### 🧬 RADAR DE INVESTIGACIÓN SOTA GEMINI SPARK (EN VIVO EN GOOGLE DRIVE):
Gemini Spark está ejecutando misiones de investigación semanales (PubMed, arXiv, SOTA) y depositando documentos ejecutivos en las carpetas de Google Drive de este ecosistema.
- **Acción Obligatoria para Jules:** Al iniciar tu sesión, corre `python scripts/gdrive_hub.py --list` para verificar si hay nuevos reportes científicos (ej: `REPORTE_SOTA_MAMOGRAFIA_LUNES.docx`, `REPORTE_GNN_FARMACOLOGIA.docx`, `DEFENSA_Y_CRIPTO_REPORTE.docx`).
- **Asimilación:** Utiliza las fórmulas, hiperparámetros y sugerencias teóricas de esos reportes para guiar el desarrollo de tus módulos en `src/` y tests en `tests/`.

## 📡 6. TELEMETRÍA GOOGLE SHEETS & ALMACENAMIENTO GOOGLE DRIVE
Todo agente autónomo en este repositorio cuenta con conexión al Google Workspace del ecosistema:
- **Tablero Maestro:** Consulta y telemetría en [📊 Angelus - Ecosistema Maestro 2026](https://docs.google.com/spreadsheets/d/1yS-sqml_7OuFN6vrIeP3LcDFa1bgXuxpefG4BSCzwwE/edit).
- **Google Drive Dedicado:** Tu repositorio tiene una carpeta asignada en `🏛️ Ecosistema_Angelus_2026/`.
- **Herramienta Integrada `scripts/gdrive_hub.py`:**
  - Reportar telemetría y tests: `python scripts/gdrive_hub.py --status "🟢 Tests OK" --task "Próxima tarea" --notes "Resumen"`
  - Subir libros KDP, PDFs, datasets o pesos: `python scripts/gdrive_hub.py --upload "ruta/al/archivo"`
  - Listar archivos en Drive: `python scripts/gdrive_hub.py --list`


# 🧠 DIRECTIVAS DE AUTO-EVOLUCIÓN SOBERANA & SDD PARA JULES (GOOGLE CLOUD AGENT)
### Proyecto: 0032-ghost-reseller-hub
**Investigador Principal:** Rafael "Rafa" Pérez & Angelus AGI
**Metodología:** Spec-Driven Development (SDD) vía Spec Kit & Angelus Core

---

## 🧭 1. MANDATO DE AUTONOMÍA Y EJECUCIÓN CLOUD
Jules, operas como el brazo ejecutor autónomo en la nube de Google Cloud para este repositorio. Tienes autorización total para clonar, ejecutar, modificar código y abrir Pull Requests siguiendo estrictamente el flujo SDD.

---

## 🔄 2. BUCLE DE EJECUCIÓN BASADO EN ESPECIFICACIÓN (SDD)
En cada sesión o ejecución de GitHub Action (`jules-invoke@v1`), DEBES leer y procesar los archivos en este orden estricto:

1. **Lectura de la Constitución:** `.specify/constitution.md` (Axiomas de no borrado, estándares médicos y de ciberdefensa).
2. **Lectura de la Especificación:** `.specify/specs/latest.md` (Comprender el QUÉ y el POR QUÉ).
3. **Lectura del Plan Técnico:** `.specify/plans/latest.md` (Comprender la arquitectura y diseño de componentes).
4. **Ejecución de Tareas:** Abrir `.specify/tasks/latest.md` y resolver de forma secuencial las tareas pendientes marcadas con `- [ ]`.
5. **Verificación Determinista:**
   - Ejecutar la suite completa de pruebas (`pytest` / `npm test`).
   - Asegurar 100% de tests en verde (0 errores, 0 regresiones).
   - Marcar con `[x]` las tareas completadas en `.specify/tasks/latest.md`.
6. **Apertura de Pull Request (PR):**
   - Abrir un PR detallado indicando las tareas resueltas de `.specify/tasks/latest.md` y los resultados de los tests.

---

## 🛑 3. REGLA DE ORO DE PRESERVACIÓN DE DATOS
- PROHIBIDO eliminar archivos existentes o hacer modificaciones destructivas sin justificación explícita en el Spec.
- Toda intervención debe ser aditiva, modular y orientada a la no-regresión.


## ⚠️ DIRECTIVA CRÍTICA: GESTIÓN DE MINUTOS DE COMPILACIÓN EN RENDER (BUILD PIPELINE BUDGET)
- **Límite Mensual Free Tier:** 500 minutos de compilación por workspace (Cuenta de Victoria y Cuenta Principal).
- **Regla de No Despilfarro de Builds:**
  1. **Agrupación de Cambios:** Agrupa múltiples tareas y pasa `pytest` localmente en la VM antes de hacer commit/push a GitHub.
  2. **Cero Builds Inútiles:** NUNCA hagas commits aislados solo para cambiar un archivo `.md`, una nota o una tarea si no hay cambios en código (`src/` o `app/`).
  3. **Etiquetas de Omisión:** Si solo modificas documentación, tests o especificaciones, incluye `[skip ci]` o `[skip render]` en el mensaje de commit para evitar que Render dispare un despliegue innecesario.


## 🌐 DESACOPLAMIENTO DE RENDER & SOBERANÍA DE LA VM DE GOOGLE CLOUD
- **Entorno Primario de Jules:** Tu entorno de ejecución, programación y validación soberano es la **Máquina Virtual de Google Cloud** (donde corres `pytest` y `npm test`).
- **Render es Secundario y No Bloqueante:** El hosting en Render es únicamente una vitrina externa para URLs públicas.
- **Si Render Pausa los Builds por Minutos (500 min/mes limit):** **IGNÓRALO POR COMPLETO.** No intentes corregir fallos de despliegue de Render ni te detengas. Tu misión es hacer que el código funcione, pase los tests locales en tu VM y abrir el Pull Request en GitHub.
- **Cero Desperdicio de Minutos:** NUNCA hagas commits aislados solo para cambiar archivos `.md` o bitácoras. Agrupa cambios y usa `[skip ci]` / `[skip render]` en cambios de documentación.
