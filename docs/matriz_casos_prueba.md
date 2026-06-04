# Matriz de Casos de Prueba
## Sistema Biblioteca Universitaria Inteligente (BUI)

---

# HU-01 — Registrar Libro

| ID Caso | CA | Escenario | Entrada | Resultado esperado | Tipo |
|----------|----------|----------|----------|----------|----------|
| CP-001 | CA-01 | Registrar libro con ISBN único | ISBN001 | Libro registrado correctamente | Positiva |
| CP-002 | CA-01 | Registrar libro con ISBN duplicado | ISBN001 repetido | Operación rechazada | Negativa |
| CP-003 | CA-02 | Registrar libro con título válido | Python Básico | Libro registrado correctamente | Positiva |
| CP-004 | CA-02 | Registrar libro sin título | "" | Operación rechazada | Negativa |
| CP-005 | CA-04 | Registrar ejemplares negativos | -1 | Operación rechazada | Negativa |
| CP-006 | CA-04 | Registrar ejemplares igual a cero | 0 | Operación permitida | Positiva |
| CP-007 | CA-05 | Buscar libro recién registrado | ISBN001 | Libro encontrado | Positiva |

---

# HU-02 — Buscar Libro

| ID Caso | CA | Escenario | Entrada | Resultado esperado | Tipo |
|----------|----------|----------|----------|----------|----------|
| CP-008 | CA-01 | Buscar libro por título existente | Python | Coincidencia encontrada | Positiva |
| CP-009 | CA-01 | Buscar libro por título inexistente | Astronomía | Sin resultados | Negativa |
| CP-010 | CA-02 | Buscar libro por autor existente | Autor A | Coincidencia encontrada | Positiva |
| CP-011 | CA-02 | Buscar libro por autor inexistente | Autor X | Sin resultados | Negativa |
| CP-012 | CA-03 | Consultar disponibilidad | Libro con 3 ejemplares | Mostrar stock disponible | Positiva |
| CP-013 | CA-05 | Verificar que búsqueda no modifica datos | Buscar libro existente | Información permanece igual | Positiva |

---

# HU-03 — Solicitar Préstamo

| ID Caso | CA | Escenario | Entrada | Resultado esperado | Tipo |
|----------|----------|----------|----------|----------|----------|
| CP-014 | CA-01 | Solicitar préstamo con stock disponible | 1 ejemplar | Préstamo aprobado | Positiva |
| CP-015 | CA-01 | Solicitar préstamo sin stock | 0 ejemplares | Operación rechazada | Negativa |
| CP-016 | CA-02 | Usuario activo solicita préstamo | bloqueado=False | Préstamo aprobado | Positiva |
| CP-017 | CA-02 | Usuario bloqueado solicita préstamo | bloqueado=True | Operación rechazada | Negativa |
| CP-018 | CA-03 | Usuario sin multas solicita préstamo | multas=0 | Préstamo aprobado | Positiva |
| CP-019 | CA-03 | Usuario con multa pendiente solicita préstamo | multa impaga | Operación rechazada | Negativa |
| CP-020 | CA-04 | Registrar préstamo en historial | préstamo válido | Historial actualizado | Positiva |
| CP-021 | CA-05 | Disminuir stock después del préstamo | stock=2 | stock=1 | Positiva |
| CP-022 | CA-06 | Usuario con 2 préstamos activos | prestamos=2 | Préstamo aprobado | Positiva |
| CP-023 | CA-06 | Usuario con 3 préstamos activos | prestamos=3 | Operación rechazada | Negativa |

---

# HU-04 — Devolver Libro

| ID Caso | CA | Escenario | Entrada | Resultado esperado | Tipo |
|----------|----------|----------|----------|----------|----------|
| CP-024 | CA-01 | Registrar devolución válida | préstamo activo | Devolución registrada | Positiva |
| CP-025 | CA-02 | Incrementar stock | stock=1 | stock=2 | Positiva |
| CP-026 | CA-03 | Devolución sin retraso | 0 días | Sin multa | Positiva |
| CP-027 | CA-03 | Devolución con retraso | 2 días | Multa generada | Positiva |
| CP-028 | CA-04 | Registrar devolución en historial | devolución válida | Historial actualizado | Positiva |
| CP-029 | CA-05 | Cambiar estado a devuelto | devuelto=False | devuelto=True | Positiva |

---

# HU-05 — Reservar Libro

| ID Caso | CA | Escenario | Entrada | Resultado esperado | Tipo |
|----------|----------|----------|----------|----------|----------|
| CP-030 | CA-01 | Reservar libro sin stock | 0 ejemplares | Reserva registrada | Positiva |
| CP-031 | CA-01 | Reservar libro con stock disponible | 2 ejemplares | Operación rechazada | Negativa |
| CP-032 | CA-02 | Registrar reserva correctamente | usuario válido | Reserva almacenada | Positiva |
| CP-033 | CA-03 | Reserva duplicada | mismo usuario | Operación rechazada | Negativa |
| CP-034 | CA-04 | Registrar fecha de reserva | reserva válida | Fecha almacenada | Positiva |
| CP-035 | CA-05 | Mantener orden de lista de espera | varios usuarios | Orden conservado | Positiva |

---

# HU-06 — Bloquear Usuario

| ID Caso | CA | Escenario | Entrada | Resultado esperado | Tipo |
|----------|----------|----------|----------|----------|----------|
| CP-036 | CA-01 | Bloquear usuario activo | bloqueado=False | bloqueado=True | Positiva |
| CP-037 | CA-02 | Usuario bloqueado intenta préstamo | bloqueado=True | Operación rechazada | Negativa |
| CP-038 | CA-03 | Usuario bloqueado intenta reserva | bloqueado=True | Operación rechazada | Negativa |
| CP-039 | CA-04 | Registrar bloqueo en historial | bloqueo válido | Historial actualizado | Positiva |
| CP-040 | CA-05 | Registrar fecha de bloqueo | bloqueo válido | Fecha almacenada | Positiva |

---

# HU-07 — Consultar Historial

| ID Caso | CA | Escenario | Entrada | Resultado esperado | Tipo |
|----------|----------|----------|----------|----------|----------|
| CP-041 | CA-01 | Consultar historial con préstamos | historial existente | Mostrar préstamos | Positiva |
| CP-042 | CA-02 | Consultar historial con devoluciones | historial existente | Mostrar devoluciones | Positiva |
| CP-043 | CA-03 | Consultar historial con reservas | historial existente | Mostrar reservas | Positiva |
| CP-044 | CA-04 | Consultar historial con multas | historial existente | Mostrar multas | Positiva |
| CP-045 | CA-05 | Verificar orden cronológico | múltiples eventos | Mostrar orden correcto | Positiva |
| CP-046 | CA-06 | Verificar trazabilidad completa | historial completo | Mostrar todas las operaciones | Positiva |

---

# Resumen

| Métrica | Cantidad |
|----------|----------|
| Historias de Usuario | 7 |
| Criterios de aceptación | 37 |
| Casos de prueba | 46 |
| Casos positivos | 31 |
| Casos negativos | 15 |

## Observación

Los casos de prueba fueron diseñados a partir de las clases de equivalencia y valores límite identificados para cada criterio de aceptación. Estos casos servirán como base para la construcción de la matriz de trazabilidad y la evaluación de cobertura de pruebas.