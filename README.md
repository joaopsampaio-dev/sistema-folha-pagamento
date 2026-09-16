#  Sistema de Folha de Pagamento (OOP em Python)

Um sistema de folha de pagamento executado via terminal, desenvolvido em **Python** para demonstrar a aplicação prática de conceitos sólidos de **Programação Orientada a Objetos (POO)**.

##  Objetivo do Projeto

Este projeto foi criado para simular o cálculo de salários de diferentes tipos de funcionários dentro de uma empresa, aplicando regras de negócio específicas para cada modalidade de contratação. 

O grande foco aqui não é apenas o resultado matemático, mas sim a **arquitetura do código**, garantindo que ele seja escalável, limpo e de fácil manutenção.

##  Conceitos Técnicos Aplicados

Este script faz uso intensivo de POO, destacando:

*   **Classes Abstratas (`ABC`):** A classe base `Funcionario` atua como um contrato, impedindo que seja instanciada diretamente e obrigando as classes filhas a implementarem seus próprios métodos.
*   **Herança:** Criação de subclasses (`FuncionarioHorista`, `FuncionarioClt`, `Gerente`) que herdam atributos da superclasse mãe, evitando repetição de código.
*   **Polimorfismo:** O método `calcular_salario()` se comporta de maneira diferente e específica dependendo do tipo de funcionário instanciado, sem que o sistema principal precise saber qual é o tipo exato do funcionário na hora de gerar a folha.
*   **Encapsulamento e Tipagem:** Uso de *Type Hints* (`-> float`, `-> None`) para tornar o código mais previsível e documentado.

##  Como Executar

Certifique-se de ter o Python 3 instalado na sua máquina.

1. Clone este repositório:
   ```bash
   git clone [https://github.com/joaopsampaio-dev/sistema-folha-pagamento.git](https://github.com/joaopsampaio-dev/sistema-folha-pagamento.git)
