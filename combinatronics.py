from dataclasses import replace
import re
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
    
    
    """ret = []
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
    return [list(item) for item in set(tuple(row) for row in ret)]"""
    
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
        
    """for i in possible_list:
        temp = []
        for j in range(n):
            temp.append(combined_list[j][i])"""
    
    return final
            
    
    """potencia = 0
    for i in range(n):
        potencia += len(s)**i 
        
    combined_list = []
    for i in range(potencia):
        combined_list.append([i for i in s])
        
    # return(combined_list)
    print(f"len {len(combined_list)}")

    final_list = []
    
    
    for i in range(int((len(s) ** n) / len(s))):
        for j in range(len(s)):
            temp = []
            for k in range(n):
                print(combined_list[i+j+k][j])
                print(f'i {i} j {j} k {k}')
                print(f'ik {i+k}')
                temp.append(combined_list[i+k][j])
                
            final_list.append(temp)"""

    """for i in range(len(combined_list)):
        temp = []
        for j in range(n):
            print(combined_list[j][i])
            temp.append(combined_list[j][i])
        final_list.append(temp)"""
    
    # return(final_list)
    
    """# print(combinations_with_repetitions(s, n))
    # print(permute([0,0,0,1]))
    return [list(item) for item in set(tuple(row) for row in sum([permute(t) for t in combinations_with_repetition(s, n)], []))]"""

# print(permutations_with_repetition([1, 2, 3, 4], 3))
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
    # pprint(b)
    return b


# pprint(len(sorted(get_list_possibles(5, 4))))
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
    # pprint(sorted_nicely(combinations(['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b', 'c', 'd'], 3)))
    # pprint(sorted(
      #          combinations_with_repetition([1, 2, 3], 4)))
    # pprint(len(combinations_with_repetition(range(6), 5)))
    # pprint(len(Cartesian(permutations_with_repetition([1, 2, 3], 2), len(permutations_with_repetition([1, 2, 3], 2)))))
    # pprint(permutations_with_repetition([1, 2, 3], 3))
    # pprint(permutations_with_repetition([1, 2, 3, 4], 3))
    # pprint(permutations([0, 1, 2, 3, 4], 5))
    pprint(len(combinations_with_repetition(
                             range(10), 4)))