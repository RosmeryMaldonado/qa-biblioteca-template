# Partición de Equivalencia y Valores Límite
## Sistema Biblioteca Universitaria Inteligente (BUI)

---

# HU-01 — Registrar Libro

## CA-01: El ISBN debe ser único

### Clases de equivalencia

| Condición | Clase | Tipo | Representante |
|------------|---------|---------|---------------|
| ISBN no registrado | ISBN válido | Válida | ISBN001 |
| ISBN ya registrado | ISBN duplicado | Inválida | ISBN001 repetido |

---

## CA-02: El título es obligatorio

### Clases de equivalencia

| Condición | Clase | Tipo | Representante |
|------------|---------|---------|---------------|
| Título no vacío | Título válido | Válida | Introducción a Python |
| Título vacío | Título inválido | Inválida | "" |

---

## CA-04: No se permiten cantidades negativas

### Clases de equivalencia

| Condición | Clase | Tipo | Representante |
|------------|---------|---------|---------------|
| Ejemplares ≥ 0 | Cantidad válida | Válida | 5 |
| Ejemplares < 0 | Cantidad inválida | Inválida | -1 |

### Valores límite

| Campo | Límite | Valor probado | Tipo |
|---------|---------|---------------|---------|
| ejemplares | 0 | -1 | Inválido |
| ejemplares | 0 | 0 | Válido |
| ejemplares | 0 | 1 | Válido |

---

# HU-02 — Buscar Libro

## CA-01: Buscar por título

### Clases de equivalencia

| Condición | Clase | Tipo | Representante |
|------------|---------|---------|---------------|
| Libro existente | Resultado encontrado | Válida | Python |
| Libro inexistente | Resultado vacío | Inválida | Astronomía |

---

## CA-02: Buscar por autor

### Clases de equivalencia

| Condición | Clase | Tipo | Representante |
|------------|---------|---------|---------------|
| Autor existente | Resultado encontrado | Válida | Autor A |
| Autor inexistente | Resultado vacío | Inválida | Autor X |

---

## CA-04: Libro inexistente

### Clases de equivalencia

| Condición | Clase | Tipo | Representante |
|------------|---------|---------|---------------|
| Coincidencias encontradas | Resultado válido | Válida | 1 libro |
| Sin coincidencias | Resultado vacío | Inválida | 0 libros |

---

# HU-03 — Solicitar Préstamo

## CA-01: Debe existir stock disponible

### Clases de equivalencia

| Condición | Clase | Tipo | Representante |
|------------|---------|---------|---------------|
| Stock disponible | Stock válido | Válida | 1 ejemplar |
| Sin stock | Stock inválido | Inválida | 0 ejemplares |

### Valores límite

| Campo | Límite | Valor probado | Tipo |
|---------|---------|---------------|---------|
| ejemplares | 1 | 0 | Inválido |
| ejemplares | 1 | 1 | Válido |

---

## CA-02: Usuario bloqueado

### Clases de equivalencia

| Condición | Clase | Tipo | Representante |
|------------|---------|---------|---------------|
| Usuario activo | Estado válido | Válida | bloqueado=False |
| Usuario bloqueado | Estado inválido | Inválida | bloqueado=True |

---

## CA-03: Usuario con multas

### Clases de equivalencia

| Condición | Clase | Tipo | Representante |
|------------|---------|---------|---------------|
| Sin multas pendientes | Estado válido | Válida | 0 multas |
| Con multas pendientes | Estado inválido | Inválida | multa impaga |

---

## CA-06: Máximo de préstamos activos

### Clases de equivalencia

| Condición | Clase | Tipo | Representante |
|------------|---------|---------|---------------|
| Menos de 3 préstamos | Cantidad válida | Válida | 2 |
| 3 o más préstamos | Cantidad inválida | Inválida | 3 |

### Valores límite

| Campo | Límite | Valor probado | Tipo |
|---------|---------|---------------|---------|
| prestamos_activos | 3 | 2 | Válido |
| prestamos_activos | 3 | 3 | Inválido |
| prestamos_activos | 3 | 4 | Inválido |

---

# HU-04 — Devolver Libro

## CA-03: Generar multa por retraso

### Clases de equivalencia

| Condición | Clase | Tipo | Representante |
|------------|---------|---------|---------------|
| Sin retraso | Devolución normal | Válida | 0 días |
| Con retraso | Devolución tardía | Válida con multa | 2 días |

### Valores límite

| Campo | Límite | Valor probado | Tipo |
|---------|---------|---------------|---------|
| dias_retraso | 0 | 0 | Sin multa |
| dias_retraso | 0 | 1 | Con multa |

---

## CA-05: Estado del préstamo

### Clases de equivalencia

| Condición | Clase | Tipo | Representante |
|------------|---------|---------|---------------|
| Préstamo activo | Estado válido | Válida | devuelto=False |
| Préstamo ya devuelto | Estado inválido | Inválida | devuelto=True |

---

# HU-05 — Reservar Libro

## CA-01: Solo reservar sin stock

### Clases de equivalencia

| Condición | Clase | Tipo | Representante |
|------------|---------|---------|---------------|
| Sin stock | Reserva válida | Válida | 0 ejemplares |
| Con stock | Reserva inválida | Inválida | 2 ejemplares |

### Valores límite

| Campo | Límite | Valor probado | Tipo |
|---------|---------|---------------|---------|
| ejemplares | 0 | 0 | Válido |
| ejemplares | 0 | 1 | Inválido |

---

## CA-03: Evitar reservas duplicadas

### Clases de equivalencia

| Condición | Clase | Tipo | Representante |
|------------|---------|---------|---------------|
| Usuario sin reserva previa | Reserva válida | Válida | U001 |
| Usuario con reserva previa | Reserva inválida | Inválida | U001 repetido |

---

# HU-06 — Bloquear Usuario

## CA-01: Cambiar estado

### Clases de equivalencia

| Condición | Clase | Tipo | Representante |
|------------|---------|---------|---------------|
| Usuario activo | Estado válido | Válida | bloqueado=False |
| Usuario ya bloqueado | Estado inválido | Inválida | bloqueado=True |

---

## CA-05: Registrar fecha de bloqueo

### Clases de equivalencia

| Condición | Clase | Tipo | Representante |
|------------|---------|---------|---------------|
| Fecha registrada | Registro válido | Válida | 2026-06-01 |
| Fecha inexistente | Registro inválido | Inválida | null |

---

# HU-07 — Consultar Historial

## CA-01 a CA-06

### Clases de equivalencia

| Condición | Clase | Tipo | Representante |
|------------|---------|---------|---------------|
| Historial con operaciones | Resultado válido | Válida | 10 registros |
| Historial vacío | Resultado válido | Válida | 0 registros |
| Historial incompleto | Resultado inválido | Inválida | faltan multas |

---

# Resumen

| Elemento | Cantidad |
|-----------|-----------|
| Historias de Usuario | 7 |
| Criterios de aceptación | 37 |
| Clases válidas | 20 |
| Clases inválidas | 16 |
| Valores límite identificados | 12 |

## Observación

Las clases de equivalencia y valores límite fueron identificadas a partir de las reglas de negocio definidas en las historias de usuario y servirán como base para la construcción de los casos de prueba funcionales.