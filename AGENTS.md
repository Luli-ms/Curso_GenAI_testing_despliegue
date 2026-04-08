# AGENTS.md

## Propósito del proyecto

Este repositorio acompaña la sesión 4 del curso de IA generativa de U-Tad. El objetivo no es solo escribir código, sino practicar cómo usar agentes para:

- generar y revisar tests unitarios e integración;
- trabajar con una base de datos SQLite real en pruebas;
- preparar un pipeline de CI con GitHub Actions;
- detectar cuándo una propuesta de IA parece válida pero no cubre bien el problema.

La referencia funcional y pedagógica está en [README.md](./README.md).

## Estado actual del repo

- Proyecto Python pequeño con código en `src/sesion_4/`.
- Módulos con implementación real:
  - `src/sesion_4/time_utils.py`
  - `src/sesion_4/task_repository.py`
- Hay archivos todavía vacíos o incompletos:
  - `src/sesion_4/main.py`
  - `tests/test_main.py`
  - `pyproject.toml`
  - `.github/workflows/ci.yml`
- Existen carpetas preparadas para tests:
  - `tests/unit`
  - `tests/integration`

## Regla general para agentes

Prioriza cambios pequeños, verificables y alineados con el laboratorio actual. No conviertas este repo en una aplicación más grande de lo necesario.

Antes de modificar código:

1. Lee `README.md` para entender qué laboratorio está guiando el trabajo.
2. Revisa los módulos afectados y los tests relacionados.
3. Mantén el alcance ajustado al pedido del usuario.

## Convenciones de trabajo

- Usa Python estándar y soluciones simples.
- Mantén el código claro y didáctico; este repo tiene intención formativa.
- Prefiere `pytest` para cualquier nueva prueba.
- En tests, usa Arrange-Act-Assert y `pytest.mark.parametrize` cuando ayude a reducir duplicación.
- No añadas dependencias nuevas sin una razón clara.
- No introduzcas ORMs, frameworks web ni capas de abstracción innecesarias.

## Estructura relevante

- `src/sesion_4/time_utils.py`
  - Utilidades de tiempo y validación de turnos.
  - Punto delicado: duraciones negativas y turnos que cruzan medianoche.
- `src/sesion_4/task_repository.py`
  - Acceso SQLite básico.
  - Punto delicado: validación de títulos/estados y aislamiento entre bases temporales en tests.
- `tests/unit/`
  - Lugar preferido para tests unitarios nuevos.
- `tests/integration/`
  - Lugar preferido para pruebas de integración con SQLite real.
- `.github/workflows/ci.yml`
  - Pipeline esperado para ejecutar tests en push y pull request.

## Qué se espera por tipo de tarea

### Si el usuario pide tests unitarios

- Céntrate en `src/sesion_4/time_utils.py` salvo que el usuario indique otro módulo.
- Cubre:
  - casos normales;
  - casos borde;
  - inputs inválidos;
  - turnos que cruzan medianoche;
  - duraciones negativas o incoherentes.
- No modifiques el código productivo si el encargo es solo generar o revisar tests.

### Si el usuario pide integración

- Usa SQLite real con un archivo temporal por test.
- No uses mocks.
- Verifica inserción y lectura reales.
- Comprueba aislamiento entre tests.
- Guarda estas pruebas en `tests/integration/`.

### Si el usuario pide reglas de negocio

En `task_repository.py`, revisa como mínimo:

- títulos vacíos;
- estados no válidos;
- filtrado correcto por estado.

Si faltan validaciones, primero decide si el usuario pidió solo tests o también cambios en código productivo.

### Si el usuario pide CI

- Limita el workflow a lo esencial.
- El pipeline debería:
  - ejecutarse en `push` y `pull_request`;
  - instalar Python y dependencias;
  - lanzar `pytest`;
  - fallar si falla cualquier test.

No añadas pasos decorativos o despliegues.

## Comandos útiles

Si el entorno ya tiene `pytest` disponible:

```bash
pytest
pytest tests/unit
pytest tests/integration
pytest -q
```

Si hace falta inspeccionar rápido la estructura:

```bash
rg --files
```

## Criterios de calidad

Un cambio está bien encaminado si:

- el código sigue siendo fácil de leer para alumnado;
- los tests detectan fallos reales y no solo cubren líneas;
- no se añade complejidad accidental;
- los cambios respetan el alcance del laboratorio.

## Límites importantes

- No asumas que el repo está completamente configurado: ahora mismo hay varios archivos vacíos.
- No asumas que existe un flujo Git operativo en esta carpeta hasta que el usuario lo configure; en el estado actual, `git status` falla porque no hay repositorio inicializado aquí.
- No reestructures carpetas sin necesidad.
- No cambies nombres públicos de funciones existentes salvo petición explícita.

## Entregables esperados de un agente

Cuando completes una tarea en este proyecto:

- explica brevemente qué cambiaste;
- indica qué pruebas ejecutaste, si pudiste ejecutarlas;
- señala cualquier hueco pendiente, por ejemplo si `pyproject.toml` o el workflow aún no están definidos.
