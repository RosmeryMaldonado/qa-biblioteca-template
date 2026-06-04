from datetime import date


class Prestamo:
    """Representa un préstamo realizado por un usuario."""

    def __init__(self, codigo_usuario, isbn):
        self.codigo_usuario = codigo_usuario
        self.isbn = isbn
        self.fecha_prestamo = date.today()
        self.fecha_devolucion = None
        self.devuelto = False

    def devolver(self):
        self.fecha_devolucion = date.today()
        self.devuelto = True