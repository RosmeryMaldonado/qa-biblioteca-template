# Análisis de Cobertura

## Objetivo

Analizar la cobertura estructural del método `puede_prestar()` utilizando las técnicas de:

- Cobertura de sentencias
- Cobertura de decisiones
- Cobertura de caminos

---

# Cobertura de Sentencias

## Método analizado

```python
def puede_prestar(self, codigo_usuario, isbn):

    usuario = self.usuarios[codigo_usuario]
    libro = self.libros[isbn]

    if usuario.bloqueado:
        return False

    if libro.ejemplares <= 0:
        return False

    return True
```

## Ejemplo desarrollado

Casos utilizados:

- CP-012 — Préstamo con stock disponible.
- CP-013 — Préstamo sin stock.
- CP-014 — Usuario bloqueado solicita préstamo.

Tabla:

| Sentencia | Caso asociado | Cubierta |
|------------|------------|------------|
| usuario = self.usuarios[...] | CP-012, CP-013, CP-014 | Sí |
| libro = self.libros[...] | CP-012, CP-013, CP-014 | Sí |
| if usuario.bloqueado | CP-012, CP-014 | Sí |
| return False (1) | CP-014 | Sí |
| if libro.ejemplares <= 0 | CP-012, CP-013 | Sí |
| return False (2) | CP-013 | Sí |
| return True | CP-012 | Sí |

Resultado:

Cobertura de sentencias = 100%

---

# Cobertura de Decisiones

## Ejemplo desarrollado

| Decisión | Rama | Caso asociado | Cubierta |
|----------|----------|----------|----------|
| usuario.bloqueado | True | CP-014 | Sí |
| usuario.bloqueado | False | CP-012 | Sí |
| libro.ejemplares <= 0 | True | CP-013 | Sí |
| libro.ejemplares <= 0 | False | CP-012 | Sí |

Resultado:

Cobertura de decisiones = 100%

---

# Cobertura de Caminos

## Caminos identificados

| Camino | Descripción | Caso asociado |
|----------|----------|----------|
| P1 | Usuario bloqueado | CP-014 |
| P2 | Usuario activo sin stock | CP-013 |
| P3 | Usuario activo con stock disponible | CP-012 |

Resultado:

Cobertura de caminos = 100%

---

## Actividad

Analizar otros métodos del sistema e identificar:

- sentencias cubiertas,
- decisiones cubiertas,
- caminos identificados,

justificando cada resultado mediante casos de prueba existentes.