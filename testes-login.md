# Testes de Login

## Objetivo

Validar o funcionamento do login da aplicação utilizando credenciais válidas e inválidas.

## TL001 — Login com credenciais válidas

**Objetivo:** Validar o acesso de um usuário com credenciais corretas.

**Dados de teste:**

- Usuário: `standard_user`
- Senha: `secret_sauce`

**Passos:**

1. Acessar a tela de login.
2. Informar o usuário `standard_user`.
3. Informar a senha `secret_sauce`.
4. Clicar em **Login**.

**Resultado esperado:**

O usuário deve acessar a página de produtos.

**Resultado obtido:**

O usuário acessou corretamente a página de produtos.

**Status:** ✅ PASSOU

---

## TL002 — Login com senha inválida

**Objetivo:** Validar o comportamento do sistema ao informar uma senha incorreta.

**Dados de teste:**

- Usuário: `standard_user`
- Senha: `senha_incorreta`

**Passos:**

1. Acessar a tela de login.
2. Informar o usuário `standard_user`.
3. Informar uma senha incorreta.
4. Clicar em **Login**.

**Resultado esperado:**

O sistema deve impedir o acesso e apresentar uma mensagem informando que as credenciais são inválidas.

**Resultado obtido:**

O acesso foi bloqueado e uma mensagem de erro foi apresentada.

**Status:** ✅ PASSOU
