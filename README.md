# Proyecto Parcial CI/CD Python

Este proyecto demuestra una canalización (pipeline) de CI con Python, flake8, pytest y cobertura de código usando GitHub Actions.
La idea es mostrar cómo automatizar el análisis estático, las pruebas y la validación de cobertura dentro de un workflow sencillo.

## Requisitos previos
Antes de ejecutar el proyecto necesitas tener instalado:

Python 3.11 o superior

pip actualizado

Docker (solo si vas a usar act para ejecutar GitHub Actions de forma local)

## Instalación de dependencias
```
Desde la raíz del proyecto:
```
```cmd
pip install -r requirements.txt
```

## Ejecutar el linter (flake8)
```cmd
flake8 src tests
```
```
Esto revisa errores de estilo, nombres mal usados y algunas prácticas inseguras.
```
## Ejecutar pruebas unitarias
```cmd
pytest -q
```

## Ejecutar pruebas con cobertura y verificar umbral
```cmd
pytest --cov=src --cov-report=term-missing --cov-fail-under=80
```
Si la cobertura es menor al 80% el proceso saldrá con código distinto de cero (fallará).

## Ver reporte XML de cobertura (opcional)
```cmd
coverage xml
```

## Configuración de Coverage
El archivo `.coveragerc` define:
- `source = src` para medir solo el código productivo.
- `omit = tests/*`para excluir las pruebas
- `fail_under = 80` como umbral mínimo de cobertura

## Pipeline CI (GitHub Actions)
Archivo: `.github/workflows/ci-quality.yml`
Etapas:
1. Checkout del repositorio.
2. Setup Python (versión 3.11).
3. Instalación de dependencias.
4. Ejecución de flake8 para análisis estático.
5. Ejecución de pytest (rápida sin cobertura).
6. Ejecución de pytest con cobertura y validación de umbral.
7. Generación de reporte XML (opcional).

La ejecución falla inmediatamente si alguna etapa retorna código de salida distinto de cero.

## Ejecutar el workflow localmente con `act`
### ¿Qué es `act`?
`act` es una herramienta que permite simular la ejecución de GitHub Actions en tu máquina usando contenedores Docker. Facilita probar workflows sin necesidad de hacer push a GitHub.

### Requisitos
- Docker instalado y funcionando.
- `act` instalado (ver instrucciones en https://github.com/nektos/act).

### Comando para ejecutar este workflow
Desde la raíz del repositorio:
```cmd
act -W .github\workflows\ci-quality.yml
```
Esto levantará contenedores y ejecutará los mismos pasos definidos para `push` y `pull_request`.

## Estructura
```
mi-proyecto/
  src/
    calculator.py
  tests/
    test_add_subtract.py
    test_mean.py
  .coveragerc
  .flake8
  requirements.txt
  README.md
  RESPUESTAS.md
  .github/workflows/ci-quality.yml
```

## Extender el proyecto
- Agrega más funciones a `calculator.py`.
- Añade nuevas pruebas siguiendo el patrón `test_*.py`.
- Si lo deseas, ajusta reglas de estilo dentro de `.flake8`.

## Licencia
Uso académico para el parcial CI/CD.
