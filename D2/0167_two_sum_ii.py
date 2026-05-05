"""
167. Two Sum II - Input Array Is Sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Dado um array de inteiros ordenado em ordem não-decrescente (1-indexed),
encontre dois números que somam ao target. Retorne os índices 1-based
[index1, index2] com index1 < index2. Exatamente uma solução existe.
Não pode usar o mesmo elemento duas vezes.

Time:  O(?)
Space: O(?)
"""


def two_sum_v1(numbers: list[int], target: int) -> list[int]:
    """Hashmap. Time O(n) / Space O(n)."""
    hashmap = {num: i for i, num in enumerate(numbers)}
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in hashmap and hashmap[complement] != i:
            return sorted([i + 1, hashmap[complement] + 1])


def two_sum(numbers: list[int], target: int) -> list[int]:
    """Two pointers. Time O(n) / Space O(1)."""
    l, r = 0, len(numbers) - 1
    while l < r:
        s = numbers[l] + numbers[r]
        if s == target:
            return [l + 1, r + 1]
        elif s < target:
            l += 1
        else:
            r -= 1
    ...


# ---------------------------------------------------------------------------
# Testes
# ---------------------------------------------------------------------------

def test_exemplo_basico() -> None:
    # Caso do enunciado
    assert two_sum([2, 7, 11, 15], target=9) == [1, 2]


def test_elementos_nao_adjacentes() -> None:
    # Resposta não é o primeiro par adjacente
    assert two_sum([2, 3, 4], target=6) == [1, 3]


def test_apenas_dois_elementos() -> None:
    assert two_sum([1, 3], target=4) == [1, 2]


def test_ultimos_dois_elementos() -> None:
    # Força percorrer até o fim
    assert two_sum([1, 2, 3, 4, 5], target=9) == [4, 5]


def test_primeiros_dois_elementos() -> None:
    assert two_sum([1, 2, 3, 4, 5], target=3) == [1, 2]


def test_negativos() -> None:
    assert two_sum([-1, 0], target=-1) == [1, 2]


def test_negativos_e_positivos() -> None:
    assert two_sum([-8, -3, 2, 5, 9], target=-1) == [2, 3]


def test_valores_iguais() -> None:
    # Dois elementos idênticos somando ao target
    assert two_sum([1, 1], target=2) == [1, 2]


def test_valores_iguais_no_meio() -> None:
    assert two_sum([1, 3, 3, 7], target=6) == [2, 3]


def test_numeros_grandes() -> None:
    assert two_sum([100, 200, 300, 400, 500], target=900) == [4, 5]
