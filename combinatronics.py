
# ----------------------------------------------------------
# Lab #3: Combinatorics
# Permutations and combinations with repetition.
#
# Date: 09-Sep-2022
# Authors:
#           A01745446 Sergio Manuel Gonzalez Vargas
#           A01720627 Rodrigo Alfredo Mendoza España
# ----------------------------------------------------------

from comparable import C
from pprint import pprint


def power_set(s: list[C]) -> list[list[C]]:
    if s:
        r = power_set(s[:-1])
        return r + [t + [s[-1]] for t in r]
    else:
        return [[]]


def sorted_nicely(s: list[list[C]]) -> list[list[C]]:

    def compare_by_size_and_content(t: list[C]) -> tuple[int, list[C]]:
        return (len(t), t)

    return sorted(s, key=compare_by_size_and_content)


def combinations(s: list[C], n: int) -> list[list[C]]:
    return [t for t in power_set(s) if len(t) == n]


def insert(x: C, lst: list[C], i: int) -> list[C]:
    return lst[:i] + [x] + lst[i:]


def insert_many(x: C, lst: list[C]) -> list[list[C]]:
    return [insert(x, lst, i) for i in range(len(lst) + 1)]


def permute(s: list[C]) -> list[list[C]]:
    if s:
        r = permute(s[:-1])
        return sum([insert_many(s[-1], t) for t in r], [])
    else:
        return [[]]


def permutations(s: list[C], n: int) -> list[list[C]]:
    return sum([permute(t) for t in combinations(s, n)], [])


def combinations_with_repetition(s: list[C], n: int) -> list[list[C]]:
    """Returns a list of lists with all the possible combinations with repetition

    Args:
        s (list[C]): Initial list
        n (int): the length of each list

    Returns:
        list[list[C]]: List of lists with all the possible combinations with repetition
    """
    combined_list = permutations_with_repetition(s, n)
    combined_list = [sorted(item) for item in combined_list]
    return [list(item) for item in set(tuple(row) for row in combined_list)]


def permutations_with_repetition(s: list[C], n: int) -> list[list[C]]:
    """Returns a list of lists with all the possible permutations with repetition

    Args:
        s (list[C]): Initial list
        n (int): the length of each list

    Returns:
        list[list[C]]: List of lists with all the possible permutations with repetition
    """
    if n == 0:
        return []
    if s:
        combined_list = [s for _ in range(n)]
        possible_list = get_list_possibles(len(s), n)
        final = []

        # print(len(s) ** n)
        for i in range(len(s) ** n):
            temp = []
            for j in range(n):
                temp.append(combined_list[j][possible_list[i][j]])
            final.append(temp)

        return final
    else:
        return []


def get_list_possibles(len_s: int, n: int) -> list[list[int]]:
    """Returns a list of lists with all the possible combinations of numbers

    Args:
        len_s (int): Length of the initial list
        n (int): the length of each list

    Returns:
        list[list[int]]: List of lists with all the possible combinations of numbers
    """
    if len_s and n > 0:
        ceros = [0] * n
        goal = [len_s - 1] * n
        temp = []
        counter = -1
        while ceros != goal:
            if ceros[counter] == len_s:
                # print(ceros)
                ceros[counter] = 0
                for i in range(-2, -(len(ceros)+1), -1):
                    if ceros[i] != len_s - 1:
                        ceros[i] += 1
                        for k in range(i + 1, 0, 1):
                            ceros[k] = 0
                        break
            else:
                c = ceros.copy()
                temp.append(c)
                ceros[counter] += 1

        c = ceros.copy()
        temp.append(c)
        return temp
    return []


if __name__ == '__main__':
    from pprint import pprint

    pprint(len(permutations_with_repetition(
        range(10), 4)))
