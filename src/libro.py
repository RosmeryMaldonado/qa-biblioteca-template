class Libro:
    """Representa un libro dentro del catálogo de la biblioteca."""

    def __init__(self, isbn, titulo, autor, ejemplares):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.ejemplares = ejemplares
        self.reservas = []