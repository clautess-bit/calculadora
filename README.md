# Calculadora em Python

## Descrição

Este projeto consiste em uma calculadora desenvolvida em Python, capaz de realizar operações matemáticas básicas entre dois números informados pelo usuário.

As operações disponíveis são:

* Soma (+)
* Subtração (-)
* Multiplicação (*)
* Divisão (/)

O programa permanece em execução até que o usuário escolha encerrá-lo.

## Arquivos do Projeto

* `calculadora.py` → Código-fonte da calculadora.
* `executar.sh` → Arquivo executável para iniciar o programa em sistemas Linux.

## Como executar o arquivo .sh

1. Abra o terminal Linux.
2. Acesse a pasta onde os arquivos estão armazenados.
3. Conceda permissão de execução ao arquivo:

```bash
chmod +x executar.sh
```

4. Execute o programa:

```bash
./executar.sh
```

## Explicação do Código Python

O programa utiliza uma estrutura de repetição (`while True`) para manter a calculadora em funcionamento até que o usuário decida sair.

Durante cada execução:

1. O usuário informa o primeiro número.
2. Escolhe a operação matemática desejada.
3. Informa o segundo número.
4. O programa realiza o cálculo utilizando estruturas condicionais (`if`, `elif` e `else`).
5. O resultado é exibido na tela.
6. O usuário escolhe se deseja realizar uma nova operação.

Além disso, o código possui tratamento para divisão por zero, exibindo uma mensagem de erro quando o segundo número informado for igual a zero.

## Autor

Projeto desenvolvido para atividade acadêmica da disciplina de Linux e Programação.
