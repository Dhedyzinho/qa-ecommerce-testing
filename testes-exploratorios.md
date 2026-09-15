# 🔎 Testes Exploratórios

Durante os testes da aplicação, também foram realizados alguns testes exploratórios para verificar comportamentos além dos casos de teste planejados.

## Exploratório 01 — Ordenação dos produtos

**Objetivo:**

Verificar se a ordenação dos produtos funciona corretamente.

**Teste realizado:**

1. Acessar a página Products.
2. Alterar a ordenação de Name (A to Z) para Name (Z to A).
3. Verificar a ordem dos produtos.

**Resultado obtido:**

Os produtos foram reorganizados corretamente em ordem alfabética do Z para o A.

**Status:**

✅ Passou

---

## Exploratório 02 — Carrinho após logout

**Objetivo:**

Verificar se o produto permanece no carrinho após sair da conta e fazer login novamente.

**Teste realizado:**

1. Adicionar um produto ao carrinho.
2. Fazer logout.
3. Fazer login novamente.
4. Verificar o carrinho.

**Resultado obtido:**

O produto permaneceu no carrinho após o novo login.

**Status:**

✅ Passou

---

## Exploratório 03 — Checkout com carrinho vazio

**Objetivo:**

Verificar se é possível finalizar uma compra sem produtos no carrinho.

**Teste realizado:**

1. Acessar o carrinho vazio.
2. Iniciar o checkout.
3. Avançar até a tela Checkout: Overview.
4. Verificar o total da compra.
5. Clicar em Finish.

**Resultado obtido:**

O sistema permitiu acessar o Checkout: Overview com o carrinho vazio, apresentando total de $0.00.

Também foi possível clicar em Finish e finalizar o pedido.

**Status:**

⚠️ Problema encontrado

**Problema relacionado:**

🐛 BUG-002 — Checkout pode ser finalizado sem produtos.
