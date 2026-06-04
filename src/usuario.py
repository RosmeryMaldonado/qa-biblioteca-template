class Usuario:
    """Representa a un usuario de la biblioteca."""

    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
        self.bloqueado = False
        self.fecha_bloqueo = None
        self.multas = []
        self.prestamos_activos = 0
        self.historial = []