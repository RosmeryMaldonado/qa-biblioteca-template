"""Módulo principal del sistema de biblioteca."""

from datetime import date

from src.libro import Libro
from src.usuario import Usuario
from src.prestamo import Prestamo


class Biblioteca:
    """Sistema de gestión de biblioteca universitaria."""

    def __init__(self):
        self.libros = {}
        self.usuarios = {}
        self.prestamos = []

    def registrar_libro(self, isbn, titulo, autor, ejemplares):
        """Registra un libro en el catálogo."""

        libro = Libro(
            isbn=isbn,
            titulo=titulo,
            autor=autor,
            ejemplares=ejemplares
        )

        self.libros[isbn] = libro

        return libro

    def registrar_usuario(self, codigo, nombre):
        """Registra un usuario."""

        usuario = Usuario(
            codigo=codigo,
            nombre=nombre
        )

        self.usuarios[codigo] = usuario

        return usuario

    def buscar_libro(self, texto):
        """Busca libros por título o autor."""

        resultados = []

        for libro in self.libros.values():

            if (
                texto.lower() in libro.titulo.lower()
                or texto.lower() in libro.autor.lower()
            ):

                libro.titulo = libro.titulo.strip()

                resultados.append(libro)

        return resultados
    
    def puede_prestar(self, codigo_usuario, isbn):
        """Valida si un usuario puede solicitar un préstamo."""

        usuario = self.usuarios[codigo_usuario]
        libro = self.libros[isbn]

        if usuario.bloqueado:
            return False

        if libro.ejemplares <= 0:
            return False

        return True


    def prestar_libro(self, codigo_usuario, isbn):
        """Registra un préstamo."""

        usuario = self.usuarios[codigo_usuario]
        libro = self.libros[isbn]

        prestamo = Prestamo(
            codigo_usuario=codigo_usuario,
            isbn=isbn
        )

        self.prestamos.append(prestamo)

        libro.ejemplares -= 1

        usuario.prestamos_activos += 1

        usuario.historial.append(
            {
                "tipo": "prestamo",
                "isbn": isbn,
                "fecha": date.today()
            }
        )

        return prestamo

    def devolver_libro(
        self,
        codigo_usuario,
        isbn,
        dias_retraso=0
    ):
        """Registra una devolución."""

        usuario = self.usuarios[codigo_usuario]
        libro = self.libros[isbn]

        libro.ejemplares += 1

        if usuario.prestamos_activos > 0:
            usuario.prestamos_activos -= 1

        usuario.historial.append(
            {
                "tipo": "devolucion",
                "isbn": isbn,
                "fecha": date.today(),
                "dias_retraso": dias_retraso
            }
        )

        return True

    def reservar_libro(self, codigo_usuario, isbn):
        """Registra una reserva."""

        usuario = self.usuarios[codigo_usuario]
        libro = self.libros[isbn]

        libro.reservas.append(codigo_usuario)

        usuario.historial.append(
            {
                "tipo": "reserva",
                "isbn": isbn
            }
        )

        return True

    def bloquear_usuario(self, codigo_usuario):
        """Bloquea un usuario."""

        usuario = self.usuarios[codigo_usuario]

        usuario.bloqueado = True

        usuario.historial.append(
            {
                "tipo": "bloqueo",
                "fecha": date.today()
            }
        )

        return True

    def consultar_historial(self, codigo_usuario):
        """Devuelve el historial de operaciones."""

        usuario = self.usuarios[codigo_usuario]

        return usuario.historial