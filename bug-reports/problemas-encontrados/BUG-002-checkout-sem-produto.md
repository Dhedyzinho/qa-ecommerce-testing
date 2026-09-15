# 🐛 BUG-002 — Checkout pode ser finalizado sem produtos

## Título

Sistema permite finalizar o checkout mesmo com o carrinho vazio.

## Ambiente

- Aplicação: Sauce Labs Swag Labs
- Navegador: Google Chrome
- Sistema operacional: Windows
- Tipo de teste: Teste exploratório

## Pré-condição

Estar logado na aplicação com o carrinho vazio.

## Passos para reproduzir

1. Acessar o carrinho com nenhum produto adicionado.
2. Iniciar o processo de checkout.
3. Preencher os dados necessários para continuar.
4. Avançar até a tela Checkout: Overview.
5. Verificar que não existem produtos no pedido.
6. Clicar em Finish.

## Resultado esperado

O sistema deve impedir a finalização do checkout quando não houver produtos no carrinho.

## Resultado obtido

O sistema permitiu chegar à tela de Checkout: Overview com o carrinho vazio, apresentando total de $0.00.

Mesmo sem produtos, foi possível clicar em Finish e finalizar o pedido.

## Severidade

🟠 Média

## Prioridade

🟠 Alta

## Evidência

O comportamento foi identificado durante um teste exploratório.

A evidência mostra a finalização do checkout sem nenhum produto no pedido.
