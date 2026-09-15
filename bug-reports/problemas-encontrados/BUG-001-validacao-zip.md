# 🐛 BUG-001 — Validação do campo ZIP/Postal Code

## Título

Sistema permite avançar no checkout com ZIP/Postal Code em formato inválido.

## Ambiente

- Aplicação: Sauce Labs Swag Labs
- Navegador: Google Chrome
- Sistema operacional: Windows
- Tipo de teste: Teste funcional

## Pré-condição

Estar logado na aplicação e possuir um produto no carrinho.

## Passos para reproduzir

1. Adicionar um produto ao carrinho.
2. Acessar o carrinho.
3. Iniciar o checkout.
4. Preencher os campos First Name e Last Name.
5. Informar um valor inválido no campo ZIP/Postal Code.
6. Clicar em Continue.

## Resultado esperado

O sistema deve validar o formato do ZIP/Postal Code e impedir o avanço quando o valor informado for inválido.

## Resultado obtido

O sistema permite avançar no checkout mesmo quando o ZIP/Postal Code informado está em um formato inválido.

## Severidade

🟢 Baixa

## Prioridade

🟡 Média

## Evidência

A evidência do comportamento está registrada na pasta `evidence`.

> Observação: o problema foi identificado durante os testes exploratórios. A necessidade de validação do formato do ZIP/Postal Code foi considerada como comportamento esperado para o campo.
