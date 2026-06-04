class Multa:
    """Representa una multa generada por devolución tardía."""

    def __init__(self, monto, motivo):
        self.monto = monto
        self.motivo = motivo
        self.pagada = False

    def pagar(self):
        self.pagada = True