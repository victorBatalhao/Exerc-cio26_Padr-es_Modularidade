from abc import ABC, abstractmethod

# Interface
class ServicoNotificacao(ABC):
    @abstractmethod
    def enviar_mensagem(self, mensagem: str):
        pass


# Implementações concretas
class EmailServico(ServicoNotificacao):
    def enviar_mensagem(self, mensagem: str):
        print(f"[E-MAIL] Enviando mensagem: {mensagem}")


class SmsServico(ServicoNotificacao):
    def enviar_mensagem(self, mensagem: str):
        print(f"[SMS] Enviando mensagem: {mensagem}")


class PushServico(ServicoNotificacao):
    def enviar_mensagem(self, mensagem: str):
        print(f"[PUSH] Enviando mensagem: {mensagem}")


# Service Locator
class ServiceLocator:
    _servicos = {}

    @classmethod
    def registrar_servico(cls, nome: str, servico: ServicoNotificacao):
        cls._servicos[nome] = servico

    @classmethod
    def obter_servico(cls, nome: str) -> ServicoNotificacao:
        servico = cls._servicos.get(nome)
        if not servico:
            raise ValueError(f"Serviço '{nome}' não encontrado!")
        return servico


# Classe que usa o Service Locator
class Notificador:
    def enviar(self, tipo: str, mensagem: str):
        servico = ServiceLocator.obter_servico(tipo)
        servico.enviar_mensagem(mensagem)

if __name__ == "__main__":
    # Registrar serviços
    ServiceLocator.registrar_servico("email", EmailServico())
    ServiceLocator.registrar_servico("sms", SmsServico())
    ServiceLocator.registrar_servico("push", PushServico())

    notificador = Notificador()

    notificador.enviar("email", "Seu pedido foi confirmado!")
    notificador.enviar("sms", "Código de verificação: 123456")
    notificador.enviar("push", "Você ganhou um bônus!")
