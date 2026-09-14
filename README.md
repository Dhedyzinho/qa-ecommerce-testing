# 🛒 Testando um E-commerce na prática

Projeto de testes funcionais em uma aplicação de e-commerce, desenvolvido como portfólio de QA Junior.

## Objetivo

Praticar testes de software em uma aplicação real, criando casos de teste, executando cenários, registrando evidências e documentando bugs encontrados durante os testes.

## O que eu testei

- Login com credenciais válidas
- Login com senha inválida
- Adição de produto ao carrinho
- Remoção de produto do carrinho
- Processo de checkout
- Validação de campos obrigatórios
- Finalização da compra
- Registro de evidências dos testes
- Identificação e documentação de bugs

Praticar testes de software em uma aplicação real, criando casos de teste, executando cenários, registrando evidências e documentando bugs encontrados durante os testes.

## Aplicação testada

- Sauce Labs Swag Labs
- Tipo: E-commerce
- Testes realizados: Funcionais

## Casos de teste

- TC001 — Login com credenciais válidas
- TC002 — Login com senha inválida
- TC003 — Adicionar produto ao carrinho
- TC004 — Remover produto do carrinho
- TC005 — Finalizar compra (Checkout)

## Resultado dos testes

| Caso | Cenário | Status |
|---|---|---|
| TC001 | Login com credenciais válidas | ✅ PASSOU |
| TC002 | Login com senha inválida | ✅ PASSOU |
| TC003 | Adicionar produto ao carrinho | ✅ PASSOU |
| TC004 | Remover produto do carrinho | ✅ PASSOU |
| TC005 | Finalizar compra | ✅ PASSOU |

## Bug Report

Durante os testes foi identificado um problema relacionado à validação do campo ZIP/Postal Code no checkout.

- BUG-001 — Validação do campo ZIP/Postal Code
- Severidade: Baixa
- Prioridade: Média

## Evidências

As evidências dos testes estão organizadas na pasta `evidence`.

## Estrutura do projeto

```text
qa-ecommerce-testing/
├── bug-reports/
├── evidence/
├── test-cases/
├── test-plan/
└── README.md
