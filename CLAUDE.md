# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Contexto

Repositório de estudo de algoritmos e estruturas de dados em Python, focado em preparação para entrevistas técnicas (LeetCode, NeetCode roadmap). Python 3.13, gerenciado com `uv`.

## Comandos

```bash
# Rodar uma solução diretamente (asserts inline)
uv run 0001_contains_duplicate.py

# Lint + format
uv run ruff check .
uv run ruff format .

# Verificação de tipos
uv run mypy .

# Adicionar dependência de desenvolvimento
uv add --dev <pacote>
```

## Convenção de arquivos

- Nome: `NNNN_nome_do_problema.py` onde `NNNN` é o número do LeetCode com zeros à esquerda.
- Cada arquivo é autossuficiente: definição da função + bloco `if __name__ == "__main__"` com `assert`s cobrindo edge cases.
- Docstring no topo: enunciado resumido, URL do problema, complexidade Time/Space.

## Padrão de solução

```python
"""
NNN. Nome do Problema
https://leetcode.com/problems/...

<enunciado resumido>

Time:  O(?)
Space: O(?)
"""

def nome_funcao(param: tipo) -> tipo:
    ...

if __name__ == "__main__":
    assert nome_funcao(...) == ...
    print("ok")
```

- Type hints obrigatórios (`list[int]`, não `List[int]`).
- Sem pytest — asserts inline são suficientes para exploração rápida.
- Se uma solução tiver múltiplas abordagens (brute force → otimizada), definir funções separadas com sufixo `_v1`, `_v2` e comentar a complexidade de cada uma.
