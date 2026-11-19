# Consulta de Fretes

Script em Python desenvolvido para centralizar e padronizar a consulta de localidades e fretes, proporcionando respostas mais rápidas e reduzindo inconsistências na comunicação entre os setores envolvidos.

**Status:** Em desenvolvimento

---

## Sobre o projeto

Atualmente, a equipe de vendas consulta fretes de duas formas:

- **Entregas no mesmo município:** os valores ficam registrados em folhas de papel e são consultados manualmente.
- **Entregas pelos Correios:** o preço é consultado na plataforma Melhor Envio, encaminhado ao setor financeiro para conferência e ajuste e, posteriormente, repassado verbalmente à equipe de vendas.

Além disso, todos os funcionários compartilham a mesma conta do Melhor Envio. Quando algum funcionário fica sem acesso, precisa recorrer ao setor de logística, criando mais um gargalo no processo.

O resultado é um fluxo que envolve três setores (**Vendas**, **Financeiro** e **Logística**), demanda tempo e abre espaço para inconsistências, como valores esquecidos, ajustes aplicados de forma diferente e informações que podem se perder durante o atendimento.

O objetivo é desenvolver uma ferramenta interna que centralize e padronize essas consultas, reduzindo etapas manuais e dependências entre setores e proporcionando mais agilidade ao atendimento.

> **Próxima fase:** Com a futura integração à base local de entregas e à API do Melhor Envio, as consultas poderão ser realizadas diretamente pelo script, sem depender do acesso compartilhado à plataforma.

---

## Funcionalidades (versão atual)

- Recebe o CEP informado pelo usuário, com ou sem hífen.
- Higieniza e valida o formato (8 dígitos numéricos) antes de realizar a consulta (`valida_cep`).
- Consulta a API ViaCEP de forma modularizada (`consulta_cep`).
- Identifica CEPs inexistentes ou mal formatados sem interromper o fluxo de atendimento.
- Retorna **Logradouro** e **Bairro** para consulta logística.
- **Fluxo contínuo no terminal:** permite realizar múltiplas consultas seguidas na mesma sessão (`0` para nova consulta ou qualquer outra tecla para encerrar).

---

## Exemplo de uso

**Consulta realizada com sucesso e nova consulta:**
```text
$ python frete.py
Digite o CEP: 01001-000
Logradouro: Praça da Sé
Bairro: Sé

Digite 0 para nova consulta (outra tecla para sair): 0
Digite o CEP: 20040-002
Logradouro: Avenida Rio Branco
Bairro: Centro

Digite 0 para nova consulta (outra tecla para sair): 1
Encerrando...