# Matriz de Trazabilidad

## Objetivo

Relacionar historias de usuario, criterios de aceptación, casos de prueba, resultados y defectos encontrados durante el análisis QA.

---

## Ejemplo desarrollado

Historia revisada:

HU-03 — Solicitar Préstamo

Criterio de aceptación:

CA-02 — Usuarios bloqueados no pueden solicitar préstamos.

Caso de prueba asociado:

CP-014 — Usuario bloqueado solicita préstamo.

Resultado del análisis:

El método `prestar_libro()` no valida si el usuario se encuentra bloqueado antes de registrar el préstamo.

Defecto identificado:

El sistema permite préstamos a usuarios bloqueados.

Registro en matriz:

| N° | HU | CA | Escenario | CP | Descripción Caso | Resultado | Defecto | Estado |
|----|----|----|-----------|----|------------------|-----------|----------|---------|
| 1 | HU-03 | CA-02 | Usuario bloqueado solicita préstamo | CP-014 | Verificar que usuarios bloqueados no puedan solicitar préstamos | FAIL | DEF-01 | Abierto |

---

## Actividad

Completar la matriz de trazabilidad para las demás historias de usuario y criterios de aceptación.

| N° | HU | CA | Escenario | CP | Descripción Caso | Resultado | Defecto | Estado |
|----|----|----|-----------|----|------------------|-----------|----------|---------|
| 1 | HU-03 | CA-02 | Usuario bloqueado solicita préstamo | CP-014 | Verificar que usuarios bloqueados no puedan solicitar préstamos | FAIL | DEF-01 | Abierto |
| 2 | | | | | | | | |
| 3 | | | | | | | | |
| 4 | | | | | | | | |
| 5 | | | | | | | | |