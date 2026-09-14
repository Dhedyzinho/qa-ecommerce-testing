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

## TC006
Título: Login com campos vazios

Objetivo:
Verificar se o sistema impede o login quando os campos obrigatórios não são preenchidos.

Pré-condição:
Estar na tela de login.

Passos:
1. Acessar a página de login.
2. Não preencher o campo de usuário.
3. Não preencher o campo de senha.
4. Clicar em "Login".

Resultado esperado:
O sistema deve impedir o login e apresentar uma mensagem informando que os campos obrigatórios precisam ser preenchidos.

Resultado obtido:
O sistema impediu o login e apresentou a mensagem "Epic sadface: Username is required".

Status:
✅ PASSOU

## TC007

**Título:** Adicionar mais de um produto ao carrinho

**Objetivo:**

Verificar se o sistema permite adicionar mais de um produto ao carrinho e mantém os produtos selecionados corretamente.

**Pré-condição:**

Estar logado na aplicação.

**Passos:**

1. Acessar a página de produtos.
2. Adicionar um produto ao carrinho.
3. Voltar para a lista de produtos.
4. Adicionar um segundo produto ao carrinho.
5. Acessar o carrinho.

**Resultado esperado:**

Os dois produtos adicionados devem aparecer no carrinho corretamente.

Resultado obtido:

Os três produtos adicionados foram exibidos corretamente no carrinho, cada um com quantidade 1.

Status:

✅ PASSOU

## TC008

**Título:** Verificar quantidade de produtos no carrinho

**Objetivo:**

Verificar como a aplicação apresenta a quantidade dos produtos adicionados ao carrinho.

**Pré-condição:**

Estar logado na aplicação e ter um produto no carrinho.

**Passos:**

1. Acessar a página de produtos.
2. Adicionar um produto ao carrinho.
3. Acessar o carrinho.
4. Verificar o campo de quantidade apresentado para o produto.

**Resultado esperado:**

O produto deve aparecer no carrinho com a quantidade apresentada corretamente.

**Resultado obtido:**

O produto foi apresentado no carrinho com a quantidade 1. O campo de quantidade não permite edição direta.

**Status:**

✅ PASSOU

## TC009

**Título:** Validar campos obrigatórios no checkout

**Objetivo:**

Verificar se o sistema impede o usuário de continuar a compra quando um dos campos obrigatórios do checkout não é preenchido.

**Pré-condição:**

Estar logado na aplicação e ter pelo menos um produto no carrinho.

**Passos:**

1. Acessar a página de produtos.
2. Adicionar um produto ao carrinho.
3. Acessar o carrinho.
4. Clicar em "Checkout".
5. Deixar um dos campos obrigatórios vazio.
6. Preencher os demais campos.
7. Clicar em "Continue".

**Resultado esperado:**

O sistema deve impedir o avanço para a próxima etapa e apresentar uma mensagem informando qual campo obrigatório precisa ser preenchido.

Resultado obtido:

O sistema impediu o avanço do checkout e apresentou a mensagem "Error: Postal Code is required".

Status:

✅ PASSOU

