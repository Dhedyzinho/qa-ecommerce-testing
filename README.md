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

## 📊 Resultado dos testes

- Login com credenciais válidas — PASSOU
- Login com senha inválida — PASSOU
- Adicionar produto ao carrinho — PASSOU
- Remover produto do carrinho — PASSOU
- Finalizar compra (Checkout) — PASSOU
- Login com campos vazios — PASSOU
- Adicionar mais de um produto ao carrinho — PASSOU
- Verificar quantidade de produtos no carrinho — PASSOU
- Validar campos obrigatórios no checkout — PASSOU
- Cancelar checkout — PASSOU

## 🤖 Automação dos testes

Além dos testes manuais, automatizei os 10 casos de teste usando Python e Playwright.

As automações cobrem os principais fluxos do e-commerce, como login, carrinho e checkout.

Os testes podem ser encontrados na pasta `automacao` e as evidências geradas ficam na pasta `evidence`.

### Tecnologias utilizadas

- Python
- Playwright
- Git e GitHub

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
- TC006 — Login com campos vazios
- TC007 — Adicionar mais de um produto ao carrinho
- TC008 — Verificar quantidade de produtos no carrinho
- TC009 — Validar campos obrigatórios no checkout
- TC010 — Cancelar checkout

✅ Resultados dos testes

| Caso | Cenário | Status |
|---|---|---|
| TC001 | Login com credenciais válidas | ✅ PASSOU |
| TC002 | Login com senha inválida | ✅ PASSOU |
| TC003 | Adicionar produto ao carrinho | ✅ PASSOU |
| TC004 | Remover produto do carrinho | ✅ PASSOU |
| TC005 | Finalizar compra | ✅ PASSOU |
| TC006 | Login com campos vazios | ✅ PASSOU |
| TC007 | Adicionar mais de um produto ao carrinho | ✅ PASSOU |
| TC008 | Verificar quantidade de produtos no carrinho | ✅ PASSOU |
| TC009 | Validar campos obrigatórios no checkout | ✅ PASSOU |
| TC010 | Cancelar checkout | ✅ PASSOU |

## 🐛 Problemas encontrados

Durante os testes, encontrei alguns comportamentos que merecem atenção.

### BUG-001 — Campo ZIP/Postal Code aceita formato inválido

- Severidade: Baixa
- Prioridade: Média

O sistema permite avançar no checkout mesmo quando o ZIP/Postal Code informado está em um formato inválido.

### BUG-002 — Checkout pode ser finalizado sem produtos

- Severidade: Média
- Prioridade: Alta

Durante um teste exploratório, foi possível finalizar o checkout com o carrinho vazio, gerando um pedido com total de $0.00.

## 📸 Evidências

Aqui está uma evidência de um dos testes realizados no checkout.

![Evidência do checkout](evidence/TC005-checkout.png)

📁 Estrutura do projeto

```text
qa-ecommerce-testing/
├── automacao/
│   ├── test_login.py
│   ├── test_login_invalido.py
│   ├── test_adicionar_produto.py
│   ├── test_remover_produto.py
│   ├── test_checkout.py
│   ├── test_login_campos_vazios.py
│   ├── test_adicionar_varios_produtos.py
│   ├── test_quantidade_carrinho.py
│   ├── test_checkout_campo_obrigatorio.py
│   └── test_cancelar_checkout.py
├── evidence/
├── casos-de-teste/
├── problemas-encontrados/
├── plano-de-testes/
├── testes-checkout.md
├── testes-login.md
├── testes-exploratorios.md
└── README.md
