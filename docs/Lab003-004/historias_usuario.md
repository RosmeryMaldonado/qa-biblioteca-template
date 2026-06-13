# Historias de Usuario y Criterios de Aceptación
## Sistema Biblioteca Universitaria Inteligente (BUI)

---

# HU-01 — Registrar Libro

**Como** bibliotecario

**Quiero** registrar nuevos libros en el sistema

**Para** incorporarlos al catálogo de la biblioteca.

## Criterios de aceptación

### CA-01
El ISBN debe ser único dentro del catálogo.

### CA-02
El título del libro es obligatorio.

### CA-03
Debe registrarse la cantidad de ejemplares disponibles.

### CA-04
No se permiten cantidades negativas de ejemplares.

### CA-05
El libro debe quedar disponible para consultas y búsquedas.

---

# HU-02 — Buscar Libro

**Como** usuario

**Quiero** buscar libros por diferentes criterios

**Para** conocer su disponibilidad.

## Criterios de aceptación

### CA-01
Debe permitir búsquedas por título.

### CA-02
Debe permitir búsquedas por autor.

### CA-03
Debe mostrar la cantidad de ejemplares disponibles.

### CA-04
Si el libro no existe, debe informar que no se encontraron resultados.

### CA-05
La búsqueda no debe modificar la información almacenada del libro.

---

# HU-03 — Solicitar Préstamo

**Como** usuario

**Quiero** solicitar el préstamo de un libro

**Para** poder utilizarlo temporalmente.

## Criterios de aceptación

### CA-01
Debe existir al menos un ejemplar disponible.

### CA-02
Los usuarios bloqueados no pueden solicitar préstamos.

### CA-03
Los usuarios con multas pendientes no pueden solicitar préstamos.

### CA-04
El préstamo debe registrarse en el historial del usuario.

### CA-05
La cantidad de ejemplares disponibles debe disminuir.

### CA-06
Un usuario no puede tener más de tres préstamos activos.

---

# HU-04 — Devolver Libro

**Como** usuario

**Quiero** devolver un libro prestado

**Para** finalizar el préstamo.

## Criterios de aceptación

### CA-01
La devolución debe registrarse correctamente.

### CA-02
La cantidad de ejemplares disponibles debe incrementarse.

### CA-03
Si existe retraso en la devolución, debe generarse una multa.

### CA-04
La devolución debe registrarse en el historial del usuario.

### CA-05
El préstamo debe cambiar a estado devuelto.

---

# HU-05 — Reservar Libro

**Como** usuario

**Quiero** reservar un libro

**Para** obtenerlo cuando esté disponible.

## Criterios de aceptación

### CA-01
Solo se puede reservar un libro sin ejemplares disponibles.

### CA-02
La reserva debe registrarse correctamente.

### CA-03
No se permiten reservas duplicadas para un mismo usuario y libro.

### CA-04
Debe registrarse la fecha de reserva.

### CA-05
El sistema debe mantener la lista de usuarios en espera.

---

# HU-06 — Bloquear Usuario

**Como** bibliotecario

**Quiero** bloquear usuarios

**Para** restringir operaciones cuando incumplen las políticas de la biblioteca.

## Criterios de aceptación

### CA-01
El estado del usuario debe cambiar a bloqueado.

### CA-02
Un usuario bloqueado no puede solicitar préstamos.

### CA-03
Un usuario bloqueado no puede realizar reservas.

### CA-04
El bloqueo debe registrarse en el historial.

### CA-05
Debe conservarse la fecha del bloqueo.

---

# HU-07 — Consultar Historial

**Como** usuario

**Quiero** consultar mi historial de operaciones

**Para** revisar mis actividades dentro de la biblioteca.

## Criterios de aceptación

### CA-01
Deben mostrarse los préstamos realizados.

### CA-02
Deben mostrarse las devoluciones realizadas.

### CA-03
Deben mostrarse las reservas realizadas.

### CA-04
Deben mostrarse las multas registradas.

### CA-05
La información debe mostrarse en orden cronológico.

### CA-06
Debe mantenerse trazabilidad de todas las operaciones realizadas.