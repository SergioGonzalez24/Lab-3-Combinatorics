from dataclasses import replace
from comparable import C


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
    ret = []
    for k in range(len(s)):
        temp = []
        for i in range(n):
            temp.append(s[k])
        
                
        for i in range(n):
            for u in range(len(s)):
                # print("vuelta")
                # print(f'i {s[u]} u {i}')
                # print(f'temp antes: {temp}')
                temp[i] = s[u]
                temp2 = temp.copy()
                # print(temp)
                # print(f'temp cambio: {temp2}\n')
                temp2.sort()
                # print(temp2)
                ret.append(temp2)
                # print(ret)
                
    # pprint(sorted(ret))
    # print('\n')
    return [list(item) for item in set(tuple(row) for row in ret)]
    
def permutations_with_repetition(s: list[C], n: int) -> list[list[C]]:
    # print(combinations_with_repetitions(s, n))
    # print(permute([0,0,0,1]))
    return [list(item) for item in set(tuple(row) for row in sum([permute(t) for t in combinations_with_repetition(s, n)], []))]



if __name__ == '__main__':
    from pprint import pprint

    # pprint(sorted_nicely(power_set([1, 2, 3, 4])))
    # print()
    # pprint(sorted_nicely(combinations(['a', 'b', 'c', 'd'], 2)))
    # print()
    # pprint(sorted_nicely(combinations([True, False], 1)))
    # print(insert_many(5, [1, 2, 3, 4]))
    # pprint(sorted_nicely(permutations([1, 2, 3, 4], 4)))
    # pprint(sorted(combinations_with_repetitions(['a', 'b', 'c', 'd'], 2)))
    pprint(sorted(
                combinations_with_repetition([1, 2, 3], 4)))