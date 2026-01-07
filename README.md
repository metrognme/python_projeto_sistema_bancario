# 🏦 Sistema Bancário com Python

Este é um projeto prático desenvolvido para consolidar os fundamentos da linguagem **Python**. O objetivo é criar um sistema bancário simples que evolui à medida que novos conceitos de programação são aprendidos e aplicados.

## 📌 Sobre o Projeto
O sistema permite realizar operações bancárias básicas através de um menu interativo no terminal. O projeto foca em lógica de programação, estruturas de repetição, condicionais e manipulação de dados.

### 🚀 Funcionalidades Atuais
* **Depósito:** Permite adicionar valores ao saldo da conta.
* **Saque:** Realiza retiradas respeitando um limite fixo por transação e um número máximo de saques diários.
* **Extrato:** Lista todas as movimentações realizadas de forma organizada e exibe o saldo atual formatado.
* **Tratamento de Erros:** Validação de entradas com `try/except` para evitar que o programa feche ao receber caracteres inválidos.

## 🛠️ Tecnologias Utilizadas
* **Python 3**
* **Git & GitHub** (Versionamento de código)

## 📖 O que aprendi até agora
Nesta fase inicial, implementei conceitos essenciais como:
1.  **Variáveis e Tipos de Dados:** Uso de `float` para valores monetários e `list` para armazenar o histórico de transações.
2.  **Estruturas de Repetição:** Utilização do `while True` para manter o sistema em execução até que o usuário decida sair.
3.  **Estruturas Condicionais:** Lógica de `if/elif/else` para controle de fluxo do menu e validações de regras de negócio (saldo insuficiente, limite excedido).
4.  **Manipulação de Strings:** Uso de **f-strings** para formatação de moeda (duas casas decimais) e o método `.join()` para transformar a lista de histórico em um extrato legível.
5.  **Tratamento de Exceções:** Implementação de `try/except` para tratar o erro `ValueError` quando o usuário digita textos em campos numéricos.

## 🔧 Como rodar o projeto
1.  Certifique-se de ter o Python instalado em sua máquina.
2.  Clone o repositório:
    ```bash
    git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
    ```
3.  Navegue até a pasta do projeto:
    ```bash
    cd nome-do-repositorio
    ```
4.  Execute o arquivo:
    ```bash
    python banco_python.py
    ```

## 📈 Próximos Passos (Roadmap)
Pretendo evoluir este sistema aplicando os seguintes tópicos futuros:
- [x] Modularização do código usando **Funções**.
- [x] Criação de um sistema de cadastro de clientes e contas (Dicionários).
- [ ] Persistência de dados em arquivos `.txt` ou `.json`.
- [ ] Aplicação de conceitos de **Programação Orientada a Objetos (POO)**.

---
**Desenvolvido por Christopher** 
