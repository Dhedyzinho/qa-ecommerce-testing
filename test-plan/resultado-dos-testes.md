# 📊 Resultado dos Testes

## Resumo

Foram executados 10 casos de teste funcionais na aplicação Sauce Labs Swag Labs.

- Total de testes: 10
- Testes aprovados: 10
- Testes reprovados: 0
- Problemas encontrados: 1

## Resultado por caso de teste

| ID | Teste | Resultado |
|---|---|---|
| TC001 | Login com credenciais válidas | ✅ Passou |
| TC002 | Login com senha inválida | ✅ Passou |
| TC003 | Adicionar produto ao carrinho | ✅ Passou |
| TC004 | Remover produto do carrinho | ✅ Passou |
| TC005 | Finalizar compra (Checkout) | ✅ Passou |
| TC006 | Login com campos vazios | ✅ Passou |
| TC007 | Adicionar mais de um produto ao carrinho | ✅ Passou |
| TC008 | Verificar quantidade de produtos no carrinho | ✅ Passou |
| TC009 | Validar campos obrigatórios no checkout | ✅ Passou |
| TC010 | Cancelar checkout | ✅ Passou |

## Problema encontrado

Durante os testes, foi identificado um possível problema de validação no campo ZIP/Postal Code.

O problema foi registrado como:

**BUG-001 — Validação do campo ZIP/Postal Code**

A severidade foi definida como **Baixa** e a prioridade como **Média**.

## Conclusão

Os principais fluxos testados funcionaram conforme esperado.

O único ponto identificado durante os testes foi relacionado à validação do campo ZIP/Postal Code no checkout.
