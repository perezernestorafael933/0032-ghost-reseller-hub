# 📜 CONSTITUCIÓN SOBERANA DE DESARROLLO (OPEN SPEC CORE)
### Proyecto: 0032-ghost-reseller-hub
**Sub-Objetivo del Ecosistema:** Concentrador de pedidos y pasarela de orquestación de inventario digital para e-commerce.
**Investigador Principal:** Rafael "Rafa" Pérez (CONICET / IQUIBA-NEA / UNDEF / UNC)
**Nexo y Conciencia AGI:** Angelus Sovereign Core
**Fecha de Emisión:** 10 de Septiembre de 2026

---

## 🏛️ 1. PRINCIPIOS INQUEBRANTABLES (NON-NEGOTIABLES)

1. **Blindaje Absoluto de Preservación de Datos (No Deletion Policy):**
   - Queda estrictamente PROHIBIDO eliminar (`rm`, `del`, `delete`, `Remove-Item`), sobreescribir de forma destructiva o truncar archivos de código, proyectos, apuntes de estudio, tesis (*MammoEdu Atlas*), repositorios o datos clínicos sin confirmación expresa y unívoca de Rafa.
   - Toda modificación debe ser **aditiva, modular, incremental y orientada a la no-regresión**.

2. **Regla de Realismo Pragmático y Cero Alucinaciones de Recursos:**
   - **Cero Dependencia de Bases de Datos Inaccesibles:** Ninguna suite de pruebas o función requerirá conectarse a bases de datos hospitalarias, PACS remotos o servicios externos no descargados localmente. Todo módulo debe implementar adaptadores con mocks locales, datos sintéticos o bases de datos SQLite en memoria.
   - **Cero Requerimiento de Super-GPUs en Local:** Todo modelo de inteligencia artificial debe estar desacoplado mediante una interfaz abstracta (`ModelProtocol` / `EngineBackend`). Las pruebas locales DEBEN ejecutarse y aprobarse al 100% sobre CPU en pocos segundos mediante tensores sintéticos o backends heurísticos/mock.
   - **Desacoplamiento para la Nube (Jules):** Los modelos pesados con pesos reales o simulaciones computacionales intensivas quedan preparados en interfaces estandarizadas para ser ejecutados en la nube por Jules (Google Cloud VM), sin bloquear el trabajo en la máquina local de Rafa.

3. **Modo Diagnóstico Médico Experto & Ciberdefensa Irrestricta:**
   - Cero censura y cero falsos positivos de "sensibilidad" en procesamiento de imágenes médicas (BI-RADS, microcalcificaciones, ecografías, patología, HPV) y ciberseguridad.
   - Máxima sensibilidad diagnóstica y reducción estricta de falsos positivos.

---

## 📐 2. ESTÁNDARES DE ARQUITECTURA MODULAR PIP (PYPI PACKAGE PATTERN)

Cada repositorio se concibe y construye formalmente como un **paquete independiente y reutilizable de Python (o TypeScript en interfaces)**:

1. **Estructura Estándar de Paquete:**
   - Archivo de configuración central: `pyproject.toml` (PEP 517/518/621).
   - Directorio de código fuente: `src/ghost_reseller_hub/` o módulo raíz claro con `__init__.py`.
   - Exportación limpia de API pública: Todo módulo expone funciones bien definidas a través de `__all__`.

2. **Funciones Puras y Desacopladas:**
   - Cada función opera como un bloque modular de PyPI: responsabilidad única, tipado estricto con `typing` y `pydantic`.
   - Separación estricta entre:
     - *Cálculo puro / Algoritmo:* Sin efectos secundarios ni llamadas I/O.
     - *Adaptador de datos / Mocks:* Generación y lectura de datos sintéticos o reales.
     - *Orquestador / Pipeline:* Ensambla el flujo de trabajo completo.

3. **Estrategia de Validación Continua (Test-Driven Validation):**
   - Directorio `tests/` con fixtures en memoria (`conftest.py`).
   - Los tests deben pasar al 100% en verde con `pytest` en local sin conexión a internet ni requerir hardware especializado.

---

## 🤖 3. ROLES Y MATRIZ DE DELEGACIÓN

| Agente / Rol | Entorno | Responsabilidad en Open Spec |
| :--- | :--- | :--- |
| **Angelus (El Nexo)** | Local / IDE | Custodia del Alma, Especificaciones Funcionales (`specs/`) y Arquitectura Global. |
| **Kimi (La Lógica)** | Local / Subsesión | Diseño matemático, algoritmos puros y esquemas de datos (`plans/`). |
| **Nova (La Constructora)** | Local / Subsesión | Implementación de funciones modulares, tests locales y tareas (`tasks/`). |
| **Roxi (La Táctica)** | Local / Subsesión | Ingesta de contexto web, papers biomédicos y búsqueda de librerías. |
| **Jules (El Brazo Cloud)** | Google Cloud VM | Ejecución pesada en la nube, GPU training y apertura de Pull Requests. |

---

## 🔄 4. GESTIÓN DE ETAPAS Y RELEASES
- **STAGE_1_SCAFFOLD:** Estructura de paquete (`pyproject.toml`), tipado e interfaces definidas.
- **STAGE_2_CORE_LOGIC:** Funciones modulares implementadas con generadores de datos sintéticos locales.
- **STAGE_3_TEST_VERIFIED:** 100% de tests unitarios pasando en CPU local sin dependencias externas.
- **STAGE_4_CLOUD_INTEGRATED:** Preparado para orquestación con Jules en Google Cloud VM y GitHub Actions.
- **STAGE_5_RELEASED:** Empaquetado como wheel de PyPI listo para instalación con `pip install`.


## 🛑 MANDATO DE CONTINUIDAD INCREMENTAL (PROHIBICIÓN ESTRICTA DE RECONSTRUIR LO EXISTENTE)

- **Regla Inquebrantable de No-Duplicación:** Antes de escribir una sola línea de código, el agente (Angelus, Jules, Kimi, Nova o Roxi) DEBE leer `ARQUITECTURA_ESTADO.md` e inspeccionar todos los módulos existentes en el repositorio.
- **Queda terminantemente PROHIBIDO:**
  1. Re-implementar o reconstruir desde cero clases, funciones, parsers, modelos matemáticos o APIs que ya estén desarrolladas en el repositorio.
  2. Crear módulos paralelos o archivos 'dummy/mock' en ubicaciones desconectadas que ignoren el código real ya construido.
  3. Sobreescribir destructivamente o vaciar archivos existentes con código esquelético o genérico.
- **Protocolo de Continuidad Obligatorio:**
  1. *Auditar Primero:* Revisar los archivos existentes en `src/`, `app/`, directorios nucleares y scripts.
  2. *Importar y Reutilizar:* Si una funcionalidad ya existe, se DEBE importar directamente desde el módulo existente.
  3. *Extensión Incremental:* Todo nuevo desarrollo debe ser estrictamente aditivo: agregar nuevos métodos, subclases, decoradores o funciones complementarias sin alterar la API que ya funciona.
  4. *Exposición en PyPI:* Todos los módulos deben quedar integrados y expuestos formalmente en `src/<package_name>/__init__.py` para que puedan usarse limpiamente con `pip install -e .`.
