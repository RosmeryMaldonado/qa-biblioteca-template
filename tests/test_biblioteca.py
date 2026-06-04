import pytest

from src.biblioteca import Biblioteca


def test_registrar_usuario():
    biblioteca = Biblioteca()

    usuario = biblioteca.registrar_usuario("U001", "Ana Torres")

    assert usuario.codigo == "U001"
    assert usuario.nombre == "Ana Torres"
    assert usuario.bloqueado is False


def test_registrar_libro():
    biblioteca = Biblioteca()

    libro = biblioteca.registrar_libro(
        "ISBN001",
        "Introducción a Python",
        "Autor A",
        3
    )

    assert libro.isbn == "ISBN001"
    assert libro.titulo == "Introducción a Python"
    assert libro.ejemplares == 3


def test_buscar_libro_por_titulo():
    biblioteca = Biblioteca()
    biblioteca.registrar_libro(
        "ISBN001",
        "Introducción a Python",
        "Autor A",
        3
    )

    resultados = biblioteca.buscar_libro("Python")

    assert len(resultados) == 1
    assert resultados[0].isbn == "ISBN001"


def test_prestar_libro_disminuye_stock():
    biblioteca = Biblioteca()
    biblioteca.registrar_usuario("U001", "Ana Torres")
    biblioteca.registrar_libro(
        "ISBN001",
        "Introducción a Python",
        "Autor A",
        3
    )

    biblioteca.prestar_libro("U001", "ISBN001")

    assert biblioteca.libros["ISBN001"].ejemplares == 2
    assert biblioteca.usuarios["U001"].prestamos_activos == 1


def test_bloquear_usuario():
    biblioteca = Biblioteca()
    biblioteca.registrar_usuario("U001", "Ana Torres")

    biblioteca.bloquear_usuario("U001")

    assert biblioteca.usuarios["U001"].bloqueado is True