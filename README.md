# 🛒 Testando um E-commerce na prática

Projeto de testes funcionais em uma aplicação de e-commerce, desenvolvido como portfólio de QA Junior.

🎯 Objetivo

Praticar testes de software em uma aplicação real, criando casos de teste,
executando cenários, registrando evidências e documentando bugs encontrados
durante os testes.

🧪 O que eu testei

- Login com credenciais válidas
- Login com senha inválida
- Adição de produto ao carrinho
- Remoção de produto do carrinho
- Processo de checkout
- Validação de campos obrigatórios
- Finalização da compra
- Registro de evidências dos testes
- Identificação e documentação de bugs

📊 Resultado dos testes

- Login com credenciais válidas — PASSOU
- Login com senha inválida — PASSOU
- Adição de produto ao carrinho — PASSOU
- Remoção de produto do carrinho — PASSOU
- Checkout com dados válidos — PASSOU
- Validação de campos obrigatórios — PASSOU

Durante os testes, encontrei alguns comportamentos que foram registrados para análise como possíveis bugs.

🌐 Aplicação testada

- Sauce Labs Swag Labs
- Tipo: E-commerce
- Testes realizados: Funcionais

📝 Casos de teste

- TC001 — Login com credenciais válidas
- TC002 — Login com senha inválida
- TC003 — Adicionar produto ao carrinho
- TC004 — Remover produto do carrinho
- TC005 — Finalizar compra (Checkout)

✅ Resultados dos testes

| Caso | Cenário | Status |
|---|---|---|
| TC001 | Login com credenciais válidas | ✅ PASSOU |
| TC002 | Login com senha inválida | ✅ PASSOU |
| TC003 | Adicionar produto ao carrinho | ✅ PASSOU |
| TC004 | Remover produto do carrinho | ✅ PASSOU |
| TC005 | Finalizar compra | ✅ PASSOU |

## 🐛 Problema encontrado

Durante os testes, encontrei um problema na validação do campo ZIP/Postal Code no checkout.

- BUG-001 — Campo ZIP/Postal Code aceita formato inválido
- Severidade: Baixa
- Prioridade: Média

## 📸 Evidências

Aqui está uma evidência de um dos testes realizados no checkout.

![Evidência do checkout](evidence/TC005-checkout.png)

📁 Estrutura do projeto

```text
qa-ecommerce-testing/
├── bug-reports/
├── evidence/
├── test-cases/
├── test-plan/
└── README.md
