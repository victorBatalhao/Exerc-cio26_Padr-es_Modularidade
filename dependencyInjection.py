from abc import ABC, abstractmethod

# Interface
class BancoDeDados(ABC):
    @abstractmethod
    def conectar(self):
        pass

    @abstractmethod
    def desconectar(self):
        pass


# Implementações concretas
class MySQLBancoDeDados(BancoDeDados):
    def conectar(self):
        print("Conectando ao banco de dados MySQL...")

    def desconectar(self):
        print("Desconectando do banco de dados MySQL...")


class PostgreSQLBancoDeDados(BancoDeDados):
    def conectar(self):
        print("Conectando ao banco de dados PostgreSQL...")

    def desconectar(self):
        print("Desconectando do banco de dados PostgreSQL...")


# Classe principal que usa injeção de dependência
class Biblioteca:
    def __init__(self, banco: BancoDeDados):
        self.banco = banco
        self.livros = []

    def adicionar_livro(self, livro):
        self.banco.conectar()
        self.livros.append(livro)
        print(f"Livro '{livro}' adicionado.")
        self.banco.desconectar()

    def remover_livro(self, livro):
        self.banco.conectar()
        if livro in self.livros:
            self.livros.remove(livro)
            print(f"Livro '{livro}' removido.")
        else:
            print(f"Livro '{livro}' não encontrado.")
        self.banco.desconectar()

if __name__ == "__main__":
    mysql_db = MySQLBancoDeDados()
    postgres_db = PostgreSQLBancoDeDados()

    biblioteca_mysql = Biblioteca(mysql_db)
    biblioteca_pg = Biblioteca(postgres_db)

    biblioteca_mysql.adicionar_livro("O Senhor dos Anéis")
    biblioteca_pg.adicionar_livro("Dom Casmurro")

    biblioteca_mysql.remover_livro("O Senhor dos Anéis")
