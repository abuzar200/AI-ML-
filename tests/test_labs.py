"""Tests for the ten independent AI laboratory experiments."""
from __future__ import annotations
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import program1, program2, program3, program4, program5
import program6, program7, program8, program9, program10

class TestArtificialIntelligenceLabs(unittest.TestCase):
    def test_assistant(self):
        self.assertIn('Artificial intelligence', program1.reply('What is AI?'))
        self.assertIn('Goodbye', program1.reply('Bye'))
        self.assertIn('Please enter', program1.reply(''))

    def test_eight_puzzle(self):
        self.assertEqual(program2.manhattan(program2.GOAL), 0)
        route = program2.solve((1, 2, 3, 4, 0, 6, 7, 5, 8))
        self.assertIsNotNone(route)
        self.assertEqual(len(route) - 1, 2)
        self.assertEqual(route[-1], program2.GOAL)
        self.assertIsNone(program2.solve((2, 1, 3, 4, 5, 6, 7, 8, 0)))
        with self.assertRaises(ValueError):
            program2.solve((0, 1, 2))

    def test_breadth_first(self):
        graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
        self.assertEqual(program3.shortest_path(graph, 'A', 'D'), ['A', 'B', 'D'])
        self.assertIsNone(program3.shortest_path(graph, 'D', 'A'))

    def test_depth_first(self):
        graph = {'A': ['B', 'C'], 'B': ['D'], 'C': [], 'D': []}
        self.assertEqual(program4.depth_first(graph, 'A'), ['A', 'B', 'D', 'C'])

    def test_uniform_cost(self):
        graph = {'A': {'B': 5, 'C': 1}, 'C': {'B': 1}, 'B': {}}
        self.assertEqual(program5.cheapest_route(graph, 'A', 'B'), (2.0, ['A', 'C', 'B']))
        self.assertIsNone(program5.cheapest_route(graph, 'B', 'A'))
        with self.assertRaises(ValueError):
            program5.cheapest_route({'A': {'B': -1}}, 'A', 'B')

    def test_greedy(self):
        route = program6.search(3, 3, (0, 0), (2, 2), {(1, 1)})
        self.assertEqual(route[0], (0, 0))
        self.assertEqual(route[-1], (2, 2))
        self.assertIsNone(program6.search(3, 3, (0, 0), (2, 2), {(2, 2)}))

    def test_a_star(self):
        route = program7.a_star(3, 3, (0, 0), (2, 2), {(1, 1)})
        self.assertEqual(len(route) - 1, 4)
        self.assertIsNone(program7.a_star(2, 2, (0, 0), (1, 1), {(0, 1), (1, 0)}))

    def test_hill_climbing(self):
        x, history = program8.hill_climb(-3)
        self.assertEqual((x, program8.score(x)), (3, 20))
        self.assertEqual(history[0][0], -3)

    def test_minimax(self):
        board = ('X', 'X', ' ', 'O', 'O', ' ', ' ', ' ', ' ')
        self.assertEqual(program9.best_move(board), 2)
        self.assertIsNone(program9.best_move(('X',)*3 + ('O',)*3 + (' ',)*3))

    def test_decision_tree(self):
        data = program10.EXAMPLES
        tree = program10.train(data, ['Outlook', 'Humidity', 'Wind'])
        self.assertEqual(tree['attribute'], 'Outlook')
        self.assertAlmostEqual(program10.entropy(data), 1.0)
        self.assertAlmostEqual(program10.information_gain(data, 'Outlook'), 0.5408520829727552)
        self.assertTrue(all(program10.predict(tree, row) == row['Play'] for row in data))

if __name__ == '__main__':
    unittest.main()
