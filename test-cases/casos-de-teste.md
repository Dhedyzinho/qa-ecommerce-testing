# Casos de Teste — E-commerce

## TC001 — Login com credenciais válidas

**Objetivo:** Validar o acesso de um usuário com credenciais válidas.

**Pré-condição:**
- Usuário cadastrado na aplicação.
- Aplicação disponível.

**Dados de teste:**
- Usuário: `standard_user`
- Senha: `secret_sauce`

**Passos:**
1. Acessar a aplicação.
2. Informar o usuário `standard_user`.
3. Informar a senha `secret_sauce`.
4. Clicar no botão **Login**.

**Resultado esperado:**
O usuário deve ser direcionado para a página de produtos.

**Resultado obtido:** O usuário foi direcionado corretamente para a página de produtos.

**Status:** ✅ PASSOU



---

## TC002 — Login com senha inválida

**Objetivo:** Validar o comportamento do sistema ao informar uma senha incorreta.

**Pré-condição:**
- Aplicação disponível.

**Dados de teste:**
- Usuário: `standard_user`
- Senha: `senha_incorreta`

**Passos:**
1. Acessar a aplicação.
2. Informar o usuário `standard_user`.
3. Informar uma senha incorreta.
4. Clicar no botão **Login**.

**Resultado esperado:**
O sistema deve impedir o acesso e apresentar uma mensagem informando que as credenciais são inválidas.

**Resultado obtido:** O acesso foi bloqueado e uma mensagem de erro foi apresentada.

**Status:** ✅ PASSOU

---

## TC003 — Adicionar produto ao carrinho

**Objetivo:** Validar a inclusão de um produto no carrinho.

**Pré-condição:**
- Usuário autenticado.
- Página de produtos aberta.

**Passos:**
1. Selecionar um produto.
2. Clicar no botão **Add to cart**.
3. Acessar o carrinho.

**Resultado esperado:**
O produto selecionado deve aparecer no carrinho com nome e preço corretos.

**Resultado obtido:** O Sauce Labs Backpack foi adicionado corretamente ao carrinho.

**Status:** ✅ PASSOU

---

## TC004 — Remover produto do carrinho

**Objetivo:** Validar a remoção de um produto do carrinho.

**Pré-condição:**
- Usuário autenticado.
- Produto adicionado ao carrinho.

**Passos:**
1. Acessar o carrinho.
2. Localizar o produto.
3. Clicar no botão **Remove**.

**Resultado esperado:**
O produto deve ser removido do carrinho.

**Resultado obtido:** O produto foi removido corretamente e o carrinho ficou vazio.

**Status:** ✅ PASSOU


---

## TC005 — Finalizar compra com dados válidos

**Objetivo:** Validar a conclusão de uma compra utilizando dados válidos.

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

**Resultado obtido:** A compra foi finalizada com sucesso e a tela de confirmação do pedido foi apresentada.

**Status:** ✅ PASSOU
