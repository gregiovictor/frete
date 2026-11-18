# Consulta de Fretes

Script em Python desenvolvido para centralizar e padronizar a consulta de localidades e fretes, proporcionando respostas mais rápidas e reduzindo inconsistências na comunicação entre os setores envolvidos.

**Status:** Em desenvolvimento

---

## Sobre o projeto

Atualmente, a equipe de vendas consulta fretes de duas formas:

* **Entregas no mesmo município:** os valores ficam registrados em folhas de papel e são consultados manualmente.
* **Entregas pelos Correios:** o preço é consultado na plataforma Melhor Envio, encaminhado ao setor financeiro para conferência e ajuste e, posteriormente, repassado verbalmente à equipe de vendas.

Além disso, todos os funcionários compartilham a mesma conta do Melhor Envio. Quando algum funcionário fica sem acesso, precisa recorrer ao setor de logística, criando mais um gargalo no processo.

O resultado é um fluxo que envolve três setores (**Vendas**, **Financeiro** e **Logística**), demanda tempo e abre espaço para inconsistências, como valores esquecidos, ajustes aplicados de forma diferente e informações que podem se perder durante a comunicação.

O objetivo é desenvolver uma ferramenta interna que centralize e padronize essas consultas, reduzindo etapas manuais e dependências entre setores e proporcionando mais agilidade ao atendimento.

> **Próxima fase:** Com a futura integração à base local de entregas e à API do Melhor Envio, as consultas poderão ser realizadas diretamente pelo script, sem depender do acesso compartilhado à plataforma.

---

## Funcionalidades (versão atual)

* Recebe o CEP informado pelo usuário, com ou sem hífen.
* Higieniza e valida o formato (8 dígitos numéricos) antes de realizar a consulta (`valida_cep`).
* Consulta a API ViaCEP de forma modularizada (`consulta_cep`).
* Identifica CEPs inexistentes sem interromper o fluxo de atendimento.
* Retorna **Logradouro** e **Bairro** para consulta logística.

---

## Exemplo de uso

**Consulta realizada com sucesso:**
```text
$ python frete.py
Digite o CEP: 01001-000
Logradouro: Praça da Sé
Bairro: Sé

**CEP com formato inválido:**
Digite o CEP: 12345
Formato de CEP inválido

**CEP inexistente:**
Digite o CEP: 99999-999
CEP não encontrado

## Tecnologias utilizadas
Python 3: linguagem utilizada no desenvolvimento.
Requests: biblioteca utilizada para realizar requisições HTTP.
ViaCEP: API utilizada para consulta de informações de CEP.

## Como executar
Pré-requisitos: Python 3 instalado e conexão com a internet.

*Clone o repositório e acesse a pasta:
git clone <https://github.com/gregiovictor/frete>
cd frete

*Instale a dependência
pip install requests
(Ou via uv: uv venv e uv pip install requests)

*Execute o Script
python frete.py

[x] Consulta de CEP via ViaCEP com validação de formato.

[x] Modularização do código em funções (valida_cep e consulta_cep).

[ ] Integração com base local (Excel/Pandas) para entregas municipais (frete, motoboy e prazo).

[ ] Integração com a API do Melhor Envio para consulta de preços e prazos de frete.

[ ] Implementação de regras de cálculo e reajuste de valores, definidas em conjunto com o setor financeiro.

[ ] Padronização das informações de entrega para utilização pela equipe de vendas.

[ ] Disponibilização do script em servidor para uso compartilhado pela equipe.

[ ] Evolução para um painel de trabalho com novas ferramentas internas.

Nota de Segurança: Na integração com o Melhor Envio, a chave de API será armazenada em variável de ambiente (.env), nunca diretamente no código-fonte.

Autor: Victor Grégio