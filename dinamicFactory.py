from abc import ABC, abstractmethod

# Interface
class MetodoPagamento(ABC):
    @abstractmethod
    def processar_pagamento(self, valor: float):
        pass


# Implementações concretas
class CartaoCredito(MetodoPagamento):
    def processar_pagamento(self, valor: float):
        print(f"Pagamento de R${valor:.2f} processado via Cartão de Crédito.")


class Paypal(MetodoPagamento):
    def processar_pagamento(self, valor: float):
        print(f"Pagamento de R${valor:.2f} processado via PayPal.")


class TransferenciaBancaria(MetodoPagamento):
    def processar_pagamento(self, valor: float):
        print(f"Pagamento de R${valor:.2f} processado via Transferência Bancária.")


# Fábrica dinâmica
class FabricaPagamentoDinamica:
    _metodos = {}

    @classmethod
    def registrar_metodo(cls, nome: str, classe_metodo):
        cls._metodos[nome] = classe_metodo

    @classmethod
    def criar_metodo(cls, nome: str) -> MetodoPagamento:
        metodo = cls._metodos.get(nome)
        if not metodo:
            raise ValueError(f"Método de pagamento '{nome}' não encontrado!")
        return metodo()

if __name__ == "__main__":
    # Registrar métodos
    FabricaPagamentoDinamica.registrar_metodo("cartao", CartaoCredito)
    FabricaPagamentoDinamica.registrar_metodo("paypal", Paypal)
    FabricaPagamentoDinamica.registrar_metodo("transferencia", TransferenciaBancaria)

    # Criar métodos dinamicamente
    pagamentos = [
        ("cartao", 120.50),
        ("paypal", 250.00),
        ("transferencia", 980.90),
    ]

    for tipo, valor in pagamentos:
        metodo = FabricaPagamentoDinamica.criar_metodo(tipo)
        metodo.processar_pagamento(valor)
