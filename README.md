# Artificial Intelligence — Python Lab Portfolio

**Student:** Mohammad Abuzar  
**Roll number:** 24BECS178  
**Coursework:** Artificial Intelligence and Machine Learning

Ten standalone Python exercises demonstrate fundamental AI methods, from rule-based agents to search algorithms, game playing, and ID3 classification.

## Programs

| Lab | Script | Topic |
|---|---|---|
| 01 | `program1.py` | Rule-based chatbot |
| 02 | `program2.py` | 8-puzzle solved with A* |
| 03 | `program3.py` | Breadth-first search |
| 04 | `program4.py` | Depth-first search |
| 05 | `program5.py` | Uniform-cost search |
| 06 | `program6.py` | Greedy best-first search |
| 07 | `program7.py` | A* shortest path on a grid |
| 08 | `program8.py` | Hill-climbing optimization |
| 09 | `program9.py` | Tic-Tac-Toe minimax |
| 10 | `program10.py` | ID3 information-gain decision tree |

## Running

Use **Python 3.10 or newer**. The programs use only Python's standard library.

```bash
python program3.py
python program10.py
python -m unittest discover -s tests -v
```

`program1.py` is interactive; enter `bye` to quit. For each experiment, see [LAB_GUIDE.md](LAB_GUIDE.md) and the generated examples in [outputs](outputs).

## Provenance

These are independently written educational exercises. The file naming was inspired by [Harshil-0106/AI](https://github.com/Harshil-0106/AI), but this repository is **not** an exact reproduction of that repository's unverified source code. The 8-puzzle and search concepts connect to Assignment 1; the ID3 example uses the six-row Play Tennis dataset from Assignment 3.

The implementation was tested locally before publication; rerun the commands above to verify it on your own system.
