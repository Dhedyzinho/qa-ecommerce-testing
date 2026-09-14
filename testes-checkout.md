# Testes de Checkout

## Objetivo

Validar o preenchimento dos dados e a finalização de uma compra.

## TC001 — Checkout com dados válidos

**Objetivo:** Validar a finalização de uma compra utilizando dados válidos.

**Pré-condição:**

- Usuário autenticado.
- Produto adicionado ao carrinho.

**Dados de teste:**

- First Name: `Wesley`
- Last Name: `QA`
- ZIP/Postal Code: `20000-000`

**Passos:**

1. Acessar o carrinho.
2. Clicar em **Checkout**.
3. Preencher os dados solicitados.
4. Clicar em **Continue**.
5. Conferir o resumo do pedido.
6. Clicar em **Finish**.

**Resultado esperado:**

A compra deve ser finalizada e o sistema deve apresentar uma confirmação do pedido.

**Resultado obtido:**

A compra foi finalizada com sucesso e a tela de confirmação foi apresentada.

**Status:** ✅ PASSOU

---

## TC002 — Checkout sem preencher o First Name

**Objetivo:** Validar a obrigatoriedade do campo First Name.

**Passos:**

1. Acessar o carrinho.
2. Clicar em **Checkout**.
3. Deixar o campo First Name vazio.
4. Preencher os demais campos.
5. Clicar em **Continue**.

**Resultado esperado:**

O sistema deve impedir o avanço e apresentar uma mensagem informando que o First Name é obrigatório.

**Resultado obtido:**

O sistema apresentou a mensagem de erro e impediu o avanço.

**Status:** ✅ PASSOU

---

## TC003 — Checkout sem preencher o Last Name

**Objetivo:** Validar a obrigatoriedade do campo Last Name.

**Passos:**

1. Acessar o carrinho.
2. Clicar em **Checkout**.
3. Preencher o First Name.
4. Deixar o Last Name vazio.
5. Preencher o ZIP/Postal Code.
6. Clicar em **Continue**.

**Resultado esperado:**

O sistema deve impedir o avanço e apresentar uma mensagem informando que o Last Name é obrigatório.

**Resultado obtido:**

O sistema apresentou a mensagem de erro e impediu o avanço.

**Status:** ✅ PASSOU
