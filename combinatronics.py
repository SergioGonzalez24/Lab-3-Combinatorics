
# ----------------------------------------------------------
# Lab #1: Steganography
# Image processing through bit manipulation.
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
    # combined_list = [i for i in s for _ in range(n)]
    combined_list = permutations_with_repetition(s, n)
    combined_list = [sorted(item) for item in combined_list]
    return [list(item) for item in set(tuple(row) for row in combined_list)]
    
    
def permutations_with_repetition(s: list[C], n: int) -> list[list[C]]:
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
            
            
def get_list_possibles(s, n):
    a = [0] * n
    d = [s - 1] * n
    b = []
    counter = -1
    while a != d:
        if a[counter] == s:
            # print(a)
            a[counter] = 0
            for i in range(-2, -(len(a)+1), -1):
                if a[i] != s - 1:
                    a[i] += 1
                    for k in range(i + 1, 0, 1):
                        a[k] = 0
                    break   
        else:
            c = a.copy()
            b.append(c)
            a[counter] += 1
    
    c = a.copy()
    b.append(c)
    return b


if __name__ == '__main__':
    from pprint import pprint
    
    pprint(len(permutations_with_repetition(
                             range(3), 6)))
