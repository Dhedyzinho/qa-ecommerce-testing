# BUG-001 — Validação do campo ZIP/Postal Code

## Título

Sistema permite avançar no checkout com ZIP/Postal Code em formato inválido.

## Severidade

Baixa

## Prioridade

Média

## Ambiente

- **Aplicação:** SauceDemo
- **Navegador:** Google Chrome
- **Sistema operacional:** Windows

## Pré-condições

- Usuário autenticado na aplicação.
- Produto adicionado ao carrinho.
- Usuário na tela de checkout.

## Dados de teste

- **First Name:** Wesley
- **Last Name:** QA
- **ZIP/Postal Code:** `abc123`

## Passos para reproduzir

1. Acessar a aplicação.
2. Realizar login com um usuário válido.
3. Adicionar um produto ao carrinho.
4. Acessar o carrinho.
5. Clicar em **Checkout**.
6. Preencher o campo **First Name** com `Wesley`.
7. Preencher o campo **Last Name** com `QA`.
8. Preencher o campo **ZIP/Postal Code** com `abc123`.
9. Clicar em **Continue**.

## Resultado esperado

O sistema deve validar o formato do campo ZIP/Postal Code e impedir o avanço quando um valor inválido for informado.

## Resultado obtido

O sistema aceitou o valor `abc123` e permitiu que o usuário avançasse para a tela **Checkout: Overview**.

## Impacto

A ausência de validação do formato do ZIP/Postal Code permite o envio de dados potencialmente inválidos durante o processo de checkout.

## Evidência

Screenshot do teste exploratório demonstrando que o sistema permitiu avançar para a tela de resumo do pedido utilizando o valor inválido `abc123`.

## Status

🔴 Aberto

## Observação

Este defeito foi identificado durante um teste exploratório de validação de campos do checkout.
