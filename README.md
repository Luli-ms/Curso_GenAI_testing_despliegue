# Sesión 4 - Curso IA generativa U-Tad

## Laboratorio 1

### Objetivo
Tener un entorno profesional funcional antes de escribir un solo test:

- VS Code configurado para uso con agentes
- IA activa
- Repo clonado

### Herramientas:
- Visual Studio Code
- Extensión VS Code Gemini Code Assist
- Python 3
- PIP 3
- pytest
- Cuenta de Gemini
- Cuenta de GitHub

## Laboratorio 2
### Objetivo
Ser capaz de:

- Generar tests útiles con IA
- Detectar casos borde
- Entender cuándo un test está mal aunque pase
- Usar la IA como herramienta, no como piloto automático

### Prompt 1:
Genera tests unitarios en pytest para este módulo.
Incluye:
- casos normales
- casos borde
- inputs inválidos
Usa el patrón Arrange-Act-Assert y parametrización.
No modifiques el código original.

**Ejecutar test:** pytest

### Prompt 2:
Revisa los tests generados y añade casos que cubran:
- turnos que cruzan medianoche
- inputs inválidos (horas incorrectas)
- casos donde la duración sea negativa
Asegúrate de que los tests detecten errores reales.

### Prompt 3:
Refactoriza los tests para que usen parametrización en pytest y evita duplicación de código.

## Laboratorio 3

### Objetivo
Aprender a usar IA generativa para:

- crear pruebas de integración reales
- distinguir unit tests de integration tests
- validar comportamiento sobre una base de datos
- detectar errores que en unit tests no aparecen

Aquí ya no estamos probando solo funciones aisladas.
Aquí probamos cómo se comporta el sistema al guardar y recuperar datos.

### Prompt 1:
Genera pruebas de integración en pytest para este módulo.
Requisitos:
- usa una base de datos SQLite temporal para cada test
- no uses mocks
- comprueba inserción y lectura real de datos
- incluye casos normales
- guarda el archivo en tests/integration/test_task_repository.py

**Ejecutar test:** pytest tests/integration

### Prompt 2:
Revisa las pruebas de integración generadas y añade casos que validen reglas de negocio.
Incluye pruebas para:
- impedir títulos vacíos
- impedir estados no válidos
- comprobar que solo se devuelven tareas del estado solicitado
- mantener aislamiento entre tests usando una base de datos temporal distinta en cada prueba
No modifiques aún el código productivo.

## Laboratorio 4

### Objetivo
Ser capaz de:

- usar IA para generar un pipeline CI
- ejecutar tests automáticamente en GitHub
- interpretar fallos de CI
- iterar hasta que el pipeline pase

### Prompt 1:

Genera un workflow de GitHub Actions para un proyecto Python que:
- se ejecute en cada push y pull request
- instale dependencias
- ejecute pytest
- falle si algún test falla

**Primer push**
Crear repositorio remoto y hacer push

### Prompt 2
Este es el error del pipeline de GitHub Actions:
[pegar error]

Dime qué lo está causando y cómo solucionarlo.