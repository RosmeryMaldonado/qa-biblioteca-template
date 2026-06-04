# Biblioteca Universitaria Inteligente (BUI)

## Descripción

Este repositorio contiene el proyecto desarrollado durante el curso de **Pruebas y Aseguramiento de Calidad de Software**.

El sistema simula la gestión de una biblioteca universitaria y será utilizado para aplicar técnicas de:

- Revisión estática
- Diseño de casos de prueba
- Trazabilidad
- Gestión de defectos
- Cobertura de pruebas
- Automatización de pruebas
- Integración continua
- Métricas de calidad

---

## Estructura del proyecto

```text
src/
tests/
docs/
.github/workflows/
```

### src/

Contiene la implementación del sistema.

### tests/

Contiene las pruebas automatizadas.

### docs/

Contiene los artefactos de calidad desarrollados durante el curso.

---

## Herramientas utilizadas

- Git
- GitHub
- GitHub Classroom
- Pytest
- Pytest-Cov
- Flake8
- Pylint
- SonarQube
- SonarScanner

---

## Comandos útiles

### Ejecutar pruebas

```bash
pytest
```

### Ejecutar pruebas con cobertura

```bash
pytest --cov=src --cov-report=xml
```

### Ejecutar análisis de estilo

```bash
flake8 src tests --max-line-length=100
```

### Ejecutar análisis con SonarQube

```bash
sonar-scanner
```

---

## Artefactos de Calidad

Durante el desarrollo del curso se utilizarán los siguientes artefactos:

```text
docs/
├── historias_usuario.md
├── checklist_calidad.md
├── equivalencia_valores_limite.md
├── matriz_casos_prueba.md
├── matriz_trazabilidad.md
├── registro_defectos.md
├── analisis_cobertura.md
└── informe_trazabilidad_cobertura.md
```

---

## Entregables

Los entregables de cada laboratorio serán indicados mediante Google Classroom y deberán ser desarrollados dentro de este mismo repositorio.

Se evaluará:

- Calidad de los artefactos generados.
- Diseño de pruebas.
- Gestión de defectos.
- Cobertura de pruebas.
- Calidad del código.
- Historial de commits.
- Cumplimiento de los criterios de aceptación.

---

## Objetivo del Proyecto

Aplicar de manera progresiva los conceptos y técnicas de aseguramiento de calidad de software sobre un sistema realista, permitiendo evidenciar la relación entre requisitos, pruebas, defectos, cobertura y calidad del producto software.