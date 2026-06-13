# Checklist de Calidad
## Sistema Biblioteca Universitaria Inteligente (BUI)

| HU | CA | Verificación QA | Estado | Evidencia | Recomendación |
|----|----|-----------------|---------|------------|----------------|
| HU-01 | CA-01 | ¿El sistema valida que el ISBN no esté registrado previamente? | No cumple | registrar_libro() permite registrar ISBN duplicado | Agregar validación de unicidad de ISBN |
| HU-01 | CA-02 | ¿El sistema rechaza libros sin título? | No cumple | registrar_libro() acepta título vacío | Validar que el título sea obligatorio |
| HU-01 | CA-03 | ¿El sistema registra la cantidad de ejemplares disponibles? | Cumple | El atributo ejemplares se almacena correctamente | Mantener validación actual |
| HU-01 | CA-04 | ¿El sistema rechaza cantidades negativas de ejemplares? | No cumple | registrar_libro() acepta ejemplares negativos | Validar que ejemplares ≥ 0 |
| HU-01 | CA-05 | ¿El libro registrado aparece en las búsquedas? | Cumple | El libro queda almacenado en el catálogo | Verificar búsqueda por título y autor |

| HU-02 | CA-01 | ¿El sistema permite buscar libros por título? | Cumple | buscar_libro() permite búsqueda por título | Mantener funcionalidad |
| HU-02 | CA-02 | ¿El sistema permite buscar libros por autor? | Cumple | buscar_libro() permite búsqueda por autor | Mantener funcionalidad |
| HU-02 | CA-03 | ¿El sistema muestra la cantidad de ejemplares disponibles? | Cumple | El atributo ejemplares se encuentra disponible | Mantener funcionalidad |
| HU-02 | CA-04 | ¿El sistema informa cuando no existen resultados? | No cumple | Devuelve lista vacía sin mensaje claro | Agregar respuesta controlada |
| HU-02 | CA-05 | ¿La búsqueda no modifica información almacenada? | No cumple | Se detectan efectos secundarios en la búsqueda | Corregir operación de consulta |

| HU-03 | CA-01 | ¿El sistema impide préstamos cuando no hay stock? | No cumple | prestar_libro() permite préstamo con stock cero | Validar disponibilidad |
| HU-03 | CA-02 | ¿El sistema impide préstamos a usuarios bloqueados? | No cumple | No valida correctamente usuario.bloqueado | Agregar validación |
| HU-03 | CA-03 | ¿El sistema impide préstamos a usuarios con multas? | No cumple | No valida multas pendientes | Agregar validación |
| HU-03 | CA-04 | ¿El préstamo se registra en el historial? | Cumple | Se registra correctamente | Mantener funcionalidad |
| HU-03 | CA-05 | ¿Disminuye el stock después del préstamo? | Cumple | El stock disminuye correctamente | Mantener funcionalidad |
| HU-03 | CA-06 | ¿Limita a tres préstamos activos por usuario? | No cumple | Permite superar el límite establecido | Agregar restricción |

| HU-04 | CA-01 | ¿La devolución se registra correctamente? | Cumple | Se registra la devolución | Mantener funcionalidad |
| HU-04 | CA-02 | ¿El stock aumenta después de la devolución? | Cumple | Incrementa correctamente | Mantener funcionalidad |
| HU-04 | CA-03 | ¿Genera multa cuando existe retraso? | No cumple | No se genera multa | Implementar cálculo de multa |
| HU-04 | CA-04 | ¿La devolución se registra en el historial? | Cumple | Historial actualizado | Mantener funcionalidad |
| HU-04 | CA-05 | ¿El préstamo cambia a estado devuelto? | No cumple | No actualiza estado correctamente | Actualizar atributo devuelto |

| HU-05 | CA-01 | ¿Solo permite reservar cuando no existe stock? | No cumple | Permite reservas con stock disponible | Validar disponibilidad |
| HU-05 | CA-02 | ¿La reserva se registra correctamente? | Cumple | Reserva almacenada correctamente | Mantener funcionalidad |
| HU-05 | CA-03 | ¿Evita reservas duplicadas? | No cumple | El mismo usuario puede reservar varias veces | Validar duplicidad |
| HU-05 | CA-04 | ¿Registra la fecha de reserva? | No cumple | No almacena fecha | Registrar fecha |
| HU-05 | CA-05 | ¿Mantiene lista de espera? | Cumple | Conserva lista de reservas | Mantener funcionalidad |

| HU-06 | CA-01 | ¿El usuario cambia a estado bloqueado? | Cumple | Estado actualizado correctamente | Mantener funcionalidad |
| HU-06 | CA-02 | ¿El usuario bloqueado no puede solicitar préstamos? | No cumple | Se permite la operación en ciertos casos | Corregir validación |
| HU-06 | CA-03 | ¿El usuario bloqueado no puede reservar? | No cumple | Se permite la operación en ciertos casos | Corregir validación |
| HU-06 | CA-04 | ¿El bloqueo queda registrado en historial? | Cumple | Evento registrado | Mantener funcionalidad |
| HU-06 | CA-05 | ¿Se conserva la fecha del bloqueo? | No cumple | No se almacena fecha | Agregar atributo fecha_bloqueo |

| HU-07 | CA-01 | ¿El historial muestra préstamos? | Cumple | Información disponible | Mantener funcionalidad |
| HU-07 | CA-02 | ¿El historial muestra devoluciones? | Cumple | Información disponible | Mantener funcionalidad |
| HU-07 | CA-03 | ¿El historial muestra reservas? | Cumple | Información disponible | Mantener funcionalidad |
| HU-07 | CA-04 | ¿El historial muestra multas? | No cumple | Las multas no aparecen | Agregar registro de multas |
| HU-07 | CA-05 | ¿El historial mantiene orden cronológico? | No cumple | Los eventos no se ordenan correctamente | Ordenar por fecha |
| HU-07 | CA-06 | ¿Existe trazabilidad completa de operaciones? | No cumple | No todas las operaciones generan trazabilidad | Completar registro de eventos |

---

## Resumen

| Resultado | Cantidad |
|------------|----------|
| Cumple | 18 |
| No cumple | 19 |
| Total verificaciones | 37 |

### Observación General

Se identifican defectos intencionales asociados principalmente a:

- Validaciones de negocio.
- Gestión de préstamos.
- Gestión de reservas.
- Generación de multas.
- Trazabilidad e historial.

Estos hallazgos serán utilizados en los laboratorios posteriores de trazabilidad, gestión de defectos y cobertura de pruebas.