
from abc import ABC, abstractmethod


class Funcionario(ABC):
    

    def __init__(self, nome: str, id_funcionario: int):
        self.nome = nome
        self.id_funcionario = id_funcionario

    @abstractmethod
    def calcular_salario(self) -> float:
        
        pass

    def exibir_contracheque(self) -> None:
        salario = self.calcular_salario()
        print(f"{self.id_funcionario:<5}{self.nome:<20}"
              f"{self.__class__.__name__:<19}R$ {salario:>10,.2f}")


class FuncionarioHorista(Funcionario):
    

    def __init__(self, nome, id_funcionario, horas_trabalhadas, valor_hora):
        super().__init__(nome, id_funcionario)  
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def calcular_salario(self) -> float:
        return self.horas_trabalhadas * self.valor_hora


class FuncionarioClt(Funcionario):
    

    def __init__(self, nome, id_funcionario, salario_fixo):
        super().__init__(nome, id_funcionario)
        self.salario_fixo = salario_fixo

    def calcular_salario(self) -> float:
        return self.salario_fixo


class Gerente(Funcionario):
    

    def __init__(self, nome, id_funcionario, salario_fixo, bonus):
        super().__init__(nome, id_funcionario)
        self.salario_fixo = salario_fixo
        self.bonus = bonus

    def calcular_salario(self) -> float:
        return self.salario_fixo + self.bonus


class SistemaFolhaPagamento:
    

    def __init__(self):
        self._funcionarios = []

    def cadastrar(self, funcionario: Funcionario) -> None:
        self._funcionarios.append(funcionario)

    def gerar_folha(self) -> None:
        largura = 57
        print("=" * largura)
        print("FOLHA DE PAGAMENTO".center(largura))
        print("=" * largura)
        print(f"{'ID':<5}{'Nome':<20}{'Cargo':<19}{'Salário':>13}")
        print("-" * largura)

        total = 0.0
        for funcionario in self._funcionarios:
            funcionario.exibir_contracheque()
            total += funcionario.calcular_salario()

        print("-" * largura)
        print(f"Total da folha: R$ {total:,.2f}")


if __name__ == "__main__":
    sistema = SistemaFolhaPagamento()

    sistema.cadastrar(FuncionarioHorista(
        "Carlos Silva", 1, horas_trabalhadas=160, valor_hora=25.50))
    sistema.cadastrar(FuncionarioClt(
        "Ana Souza", 2, salario_fixo=3500.00))
    sistema.cadastrar(Gerente(
        "Marina Costa", 3, salario_fixo=6000.00, bonus=1500.00))

    sistema.gerar_folha()