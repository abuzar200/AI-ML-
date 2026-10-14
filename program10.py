"""Lab 10: train a small decision tree by ID3 information gain."""
from collections import Counter
from math import log2
from typing import Any

EXAMPLES = [
    {'Outlook': 'Sunny',    'Humidity': 'High',   'Wind': 'Weak',   'Play': 'No'},
    {'Outlook': 'Sunny',    'Humidity': 'High',   'Wind': 'Strong', 'Play': 'No'},
    {'Outlook': 'Overcast', 'Humidity': 'High',   'Wind': 'Weak',   'Play': 'Yes'},
    {'Outlook': 'Rain',     'Humidity': 'High',   'Wind': 'Weak',   'Play': 'Yes'},
    {'Outlook': 'Rain',     'Humidity': 'Normal', 'Wind': 'Weak',   'Play': 'Yes'},
    {'Outlook': 'Rain',     'Humidity': 'Normal', 'Wind': 'Strong', 'Play': 'No'},
]

def entropy(rows: list[dict[str, str]]) -> float:
    counts = Counter(row['Play'] for row in rows)
    n = len(rows)
    return -sum((c/n) * log2(c/n) for c in counts.values()) if n else 0.0

def information_gain(rows: list[dict[str, str]], attribute: str) -> float:
    values = sorted({r[attribute] for r in rows})
    after = sum(len(group)/len(rows) * entropy(group) for v in values
                for group in [[r for r in rows if r[attribute] == v]])
    return entropy(rows) - after

def train(rows: list[dict[str, str]], attributes: list[str]) -> dict[str, Any] | str:
    if not rows:
        raise ValueError('A training subset cannot be empty.')
    labels = Counter(row['Play'] for row in rows)
    if len(labels) == 1:
        return next(iter(labels))
    if not attributes:
        return labels.most_common(1)[0][0]
    best = max(attributes, key=lambda key: (information_gain(rows, key), -attributes.index(key)))
    branches = {}
    for value in sorted({row[best] for row in rows}):
        group = [r for r in rows if r[best] == value]
        branches[value] = train(group, [a for a in attributes if a != best])
    return {'attribute': best, 'branches': branches, 'default': labels.most_common(1)[0][0]}

def predict(tree: dict[str, Any] | str, row: dict[str, str]) -> str:
    while isinstance(tree, dict):
        tree = tree['branches'].get(row.get(tree['attribute']), tree['default'])
    return tree

def explain(tree: dict[str, Any] | str, indent: str = '') -> list[str]:
    if isinstance(tree, str):
        return [f'{indent}Predict: {tree}']
    lines = []
    for value, branch in tree['branches'].items():
        lines.append(f"{indent}{tree['attribute']} == {value}")
        lines.extend(explain(branch, indent + '  '))
    return lines

if __name__ == '__main__':
    features = ['Outlook', 'Humidity', 'Wind']
    tree = train(EXAMPLES, features)
    print('Dataset entropy:', round(entropy(EXAMPLES), 3))
    for attr in features:
        print(f'Information gain for {attr}: {information_gain(EXAMPLES, attr):.3f}')
    print('Decision tree:')
    print('\n'.join(explain(tree)))
    print('Training accuracy:', sum(predict(tree, row) == row['Play'] for row in EXAMPLES), '/', len(EXAMPLES))
