# Laboratory guide

Each exercise is independently implemented using Python's standard library.

### 1. Rule-based assistant
**Aim:** Understand a simple intelligent agent. **Method:** Match keyword patterns to predefined responses. **Observation:** The program responds only to defined intents; it is not a learned language model.

### 2. Eight-puzzle using A*
**Aim:** Formulate a state-space search problem. **Method:** Represent the board as a tuple; expand legal moves using f(n) = g(n) + h(n), where h is Manhattan distance. **Observation:** A* returns an optimal path for unit-cost moves when the heuristic is admissible.

### 3. Breadth-first search
**Aim:** Find a route using the fewest graph edges. **Method:** Use a FIFO queue, predecessors, and route reconstruction. **Complexity:** O(V + E) time.

### 4. Depth-first search
**Aim:** Explore a graph branch by branch. **Method:** Use a stack and a visited set. **Complexity:** O(V + E) time.

### 5. Uniform-cost search
**Aim:** Find the minimum-weight route. **Method:** Use a cost-ordered priority queue. **Condition:** Edge weights must be nonnegative.

### 6. Greedy best-first search
**Aim:** Explore heuristic-guided searching. **Method:** Expand cells with the lowest Manhattan distance to the goal. **Limitation:** Does not guarantee a shortest path.

### 7. A* grid search
**Aim:** Find optimal paths around obstacles. **Method:** Use f(n) = g(n) + h(n) on a four-direction grid. **Observation:** Manhattan distance is admissible for unit-cost moves.

### 8. Hill climbing
**Aim:** Demonstrate local optimization. **Method:** Move to a neighboring integer with a strictly greater score. **Limitation:** May stop at local maxima or plateaus.

### 9. Minimax
**Aim:** Choose an optimal Tic-Tac-Toe move. **Method:** Score terminal outcomes (+1, 0, -1), and recursively maximize/minimize according to the player's turn.

### 10. ID3 decision tree
**Aim:** Classify Play Tennis with information gain. **Method:** Split on the attribute with the largest entropy reduction. **Observation:** Outlook is the root and Wind separates Rain cases on the six-record example; training accuracy is 6/6.

## Verification

```bash
python -m unittest discover -s tests -v
```

The programs and their tests are original teaching examples, not an exact copy of another person's lab source.
