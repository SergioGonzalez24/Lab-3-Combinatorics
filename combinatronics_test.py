# File: combinatorics_test.py

from unittest import TestCase, main
from combinatronics import \
    permutations_with_repetition, \
    combinations_with_repetition


class TestCombinatorics(TestCase):

    def test_permutations_with_repetition_1(self):
        self.assertEqual([], permutations_with_repetition([], 5))

    def test_permutations_with_repetition_2(self):
        self.assertEqual(
            [],
            permutations_with_repetition([1, 2, 3, 4], 0))

    def test_permutations_with_repetition_3(self):
        self.assertEqual(
            [[1], [2], [3], [4]],
            sorted(
                permutations_with_repetition([1, 2, 3, 4], 1)))

    def test_permutations_with_repetition_4(self):
        self.assertEqual(
            [['a', 'a'], ['a', 'b'], ['a', 'c'], ['a', 'd'],
             ['b', 'a'], ['b', 'b'], ['b', 'c'], ['b', 'd'],
             ['c', 'a'], ['c', 'b'], ['c', 'c'], ['c', 'd'],
             ['d', 'a'], ['d', 'b'], ['d', 'c'], ['d', 'd']],
            sorted(permutations_with_repetition(['a', 'b',
                                                 'c', 'd'],
                                                2)))

    def test_permutations_with_repetition_5(self):
        self.assertEqual(
            [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0],
             [0, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1],
             [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 0, 0],
             [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1],
             [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0],
             [1, 1, 1, 1]],
            sorted(permutations_with_repetition([0, 1], 4)))

    def test_permutations_with_repetition_6(self):
        self.assertEqual(
            [['a', 'a'], ['a', 'b'], ['a', 'c'], ['b', 'a'],
             ['b', 'b'], ['b', 'c'], ['c', 'a'], ['c', 'b'],
             ['c', 'c']],
            sorted(
                permutations_with_repetition(['a', 'b', 'c'],
                                             2)))

    def test_permutations_with_repetition_7(self):
        self.assertEqual(
            [[1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 1, 3],
             [1, 1, 2, 1], [1, 1, 2, 2], [1, 1, 2, 3],
             [1, 1, 3, 1], [1, 1, 3, 2], [1, 1, 3, 3],
             [1, 2, 1, 1], [1, 2, 1, 2], [1, 2, 1, 3],
             [1, 2, 2, 1], [1, 2, 2, 2], [1, 2, 2, 3],
             [1, 2, 3, 1], [1, 2, 3, 2], [1, 2, 3, 3],
             [1, 3, 1, 1], [1, 3, 1, 2], [1, 3, 1, 3],
             [1, 3, 2, 1], [1, 3, 2, 2], [1, 3, 2, 3],
             [1, 3, 3, 1], [1, 3, 3, 2], [1, 3, 3, 3],
             [2, 1, 1, 1], [2, 1, 1, 2], [2, 1, 1, 3],
             [2, 1, 2, 1], [2, 1, 2, 2], [2, 1, 2, 3],
             [2, 1, 3, 1], [2, 1, 3, 2], [2, 1, 3, 3],
             [2, 2, 1, 1], [2, 2, 1, 2], [2, 2, 1, 3],
             [2, 2, 2, 1], [2, 2, 2, 2], [2, 2, 2, 3],
             [2, 2, 3, 1], [2, 2, 3, 2], [2, 2, 3, 3],
             [2, 3, 1, 1], [2, 3, 1, 2], [2, 3, 1, 3],
             [2, 3, 2, 1], [2, 3, 2, 2], [2, 3, 2, 3],
             [2, 3, 3, 1], [2, 3, 3, 2], [2, 3, 3, 3],
             [3, 1, 1, 1], [3, 1, 1, 2], [3, 1, 1, 3],
             [3, 1, 2, 1], [3, 1, 2, 2], [3, 1, 2, 3],
             [3, 1, 3, 1], [3, 1, 3, 2], [3, 1, 3, 3],
             [3, 2, 1, 1], [3, 2, 1, 2], [3, 2, 1, 3],
             [3, 2, 2, 1], [3, 2, 2, 2], [3, 2, 2, 3],
             [3, 2, 3, 1], [3, 2, 3, 2], [3, 2, 3, 3],
             [3, 3, 1, 1], [3, 3, 1, 2], [3, 3, 1, 3],
             [3, 3, 2, 1], [3, 3, 2, 2], [3, 3, 2, 3],
             [3, 3, 3, 1], [3, 3, 3, 2], [3, 3, 3, 3]],
            sorted(permutations_with_repetition([1, 2, 3], 4)))

    def test_permutations_with_repetition_8(self):
        self.assertEqual(
            [['w', 'w', 'w'], ['w', 'w', 'x'], ['w', 'w', 'y'],
             ['w', 'w', 'z'], ['w', 'x', 'w'], ['w', 'x', 'x'],
             ['w', 'x', 'y'], ['w', 'x', 'z'], ['w', 'y', 'w'],
             ['w', 'y', 'x'], ['w', 'y', 'y'], ['w', 'y', 'z'],
             ['w', 'z', 'w'], ['w', 'z', 'x'], ['w', 'z', 'y'],
             ['w', 'z', 'z'], ['x', 'w', 'w'], ['x', 'w', 'x'],
             ['x', 'w', 'y'], ['x', 'w', 'z'], ['x', 'x', 'w'],
             ['x', 'x', 'x'], ['x', 'x', 'y'], ['x', 'x', 'z'],
             ['x', 'y', 'w'], ['x', 'y', 'x'], ['x', 'y', 'y'],
             ['x', 'y', 'z'], ['x', 'z', 'w'], ['x', 'z', 'x'],
             ['x', 'z', 'y'], ['x', 'z', 'z'], ['y', 'w', 'w'],
             ['y', 'w', 'x'], ['y', 'w', 'y'], ['y', 'w', 'z'],
             ['y', 'x', 'w'], ['y', 'x', 'x'], ['y', 'x', 'y'],
             ['y', 'x', 'z'], ['y', 'y', 'w'], ['y', 'y', 'x'],
             ['y', 'y', 'y'], ['y', 'y', 'z'], ['y', 'z', 'w'],
             ['y', 'z', 'x'], ['y', 'z', 'y'], ['y', 'z', 'z'],
             ['z', 'w', 'w'], ['z', 'w', 'x'], ['z', 'w', 'y'],
             ['z', 'w', 'z'], ['z', 'x', 'w'], ['z', 'x', 'x'],
             ['z', 'x', 'y'], ['z', 'x', 'z'], ['z', 'y', 'w'],
             ['z', 'y', 'x'], ['z', 'y', 'y'], ['z', 'y', 'z'],
             ['z', 'z', 'w'], ['z', 'z', 'x'], ['z', 'z', 'y'],
             ['z', 'z', 'z']],
            sorted(
                permutations_with_repetition(['w', 'x', 'y', 'z'],
                                             3)))

    def test_permutations_with_repetition_9(self):
        self.assertEqual(729,
                         len(permutations_with_repetition(
                             range(3), 6)))
        self.assertEqual(4_096,
                         len(permutations_with_repetition(
                             [0, 1], 12)))
        self.assertEqual(7_776,
                         len(permutations_with_repetition(
                             range(6), 5)))
        self.assertEqual(10_000,
                         len(permutations_with_repetition(
                             range(10), 4)))

    def test_combinations_with_repetition_1(self):
        self.assertEqual([], combinations_with_repetition([], 5))

    def test_combinations_with_repetition_2(self):
        self.assertEqual([],
                         combinations_with_repetition([1, 2, 3, 4],
                                                      0))

    def test_combinations_with_repetition_3(self):
        self.assertEqual(
            [[1], [2], [3], [4]],
            sorted(combinations_with_repetition([1, 2, 3, 4],
                                                1)))

    def test_combinations_with_repetition_4(self):
        self.assertEqual(
            [['a', 'a'], ['a', 'b'], ['a', 'c'], ['a', 'd'],
             ['b', 'b'], ['b', 'c'], ['b', 'd'], ['c', 'c'],
             ['c', 'd'], ['d', 'd']],
            sorted(
                combinations_with_repetition(['a', 'b',
                                              'c', 'd'],
                                             2)))

    def test_combinations_with_repetition_5(self):
        self.assertEqual(
            [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 1],
             [0, 1, 1, 1], [1, 1, 1, 1]],
            sorted(combinations_with_repetition([0, 1], 4)))

    def test_combinations_with_repetition_6(self):
        self.assertEqual(
            [['a', 'a'], ['a', 'b'], ['a', 'c'], ['b', 'b'],
             ['b', 'c'], ['c', 'c']],
            sorted(
                combinations_with_repetition(['a', 'b', 'c'],
                                             2)))

    def test_combinations_with_repetition_7(self):
        self.assertEqual(
            [[1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 1, 3],
             [1, 1, 2, 2], [1, 1, 2, 3], [1, 1, 3, 3],
             [1, 2, 2, 2], [1, 2, 2, 3], [1, 2, 3, 3],
             [1, 3, 3, 3], [2, 2, 2, 2], [2, 2, 2, 3],
             [2, 2, 3, 3], [2, 3, 3, 3], [3, 3, 3, 3]],
            sorted(combinations_with_repetition([1, 2, 3], 4)))

    def test_combinations_with_repetition_8(self):
        self.assertEqual(
            [['w', 'w', 'w'], ['w', 'w', 'x'], ['w', 'w', 'y'],
             ['w', 'w', 'z'], ['w', 'x', 'x'], ['w', 'x', 'y'],
             ['w', 'x', 'z'], ['w', 'y', 'y'], ['w', 'y', 'z'],
             ['w', 'z', 'z'], ['x', 'x', 'x'], ['x', 'x', 'y'],
             ['x', 'x', 'z'], ['x', 'y', 'y'], ['x', 'y', 'z'],
             ['x', 'z', 'z'], ['y', 'y', 'y'], ['y', 'y', 'z'],
             ['y', 'z', 'z'], ['z', 'z', 'z']],
            sorted(
                combinations_with_repetition(
                    ['w', 'x', 'y', 'z'], 3)))

    def test_combinations_with_repetition_9(self):
        self.assertEqual(28,
                         len(combinations_with_repetition(
                             range(3), 6)))
        self.assertEqual(13,
                         len(combinations_with_repetition(
                             [0, 1], 12)))
        self.assertEqual(252,
                         len(combinations_with_repetition(
                             range(6), 5)))
        self.assertEqual(715,
                         len(combinations_with_repetition(
                             range(10), 4)))


if __name__ == '__main__':
    main()