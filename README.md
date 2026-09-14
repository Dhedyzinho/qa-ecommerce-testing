# 🛒 Testando um E-commerce na prática

Projeto de testes funcionais em uma aplicação de e-commerce, desenvolvido como portfólio de QA Junior.

## Objetivo

Demonstrar conhecimentos em testes manuais, elaboração de casos de teste, execução de cenários, registro de evidências e reporte de bugs.

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
