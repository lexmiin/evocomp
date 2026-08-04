# Evolutionary computation

This is a collection of algorithms I studied at my university for the Evolutionary Computation course.

This repository includes 7 methods for function optimization:

- Evolutionary strategy
- Differential evolutionary
- Symbiotic optimization
- Artificial bee colony
- Deformed stars
- Fractal structurization
- Simulated Annealing

You can also find Genetic Programming (GP) algorithm and Ant Colony Optimization (ACO) algorithm.

## Installation

```bash
# Install directly from GitHub into a uv-managed environment
uv add git+https://github.com/lexmiin/evolutionary-computations.git

# Include the optional visualization feature
uv add 'evocomp[visual] @ git+https://github.com/lexmiin/evolutionary-computations.git'

# Or clone and set up the development environment
git clone https://github.com/lexmiin/evolutionary-computations.git
cd evolutionary-computations
uv sync
```

The project pins Python 3.14 in `.python-version`. `uv sync` installs that
Python version when necessary, creates `.venv`, and installs the locked
dependencies. Run project commands without manually activating the environment:

```bash
uv run python examples/basic.py
```

Visualization and spreadsheet export are available as an optional feature:

```bash
uv sync --extra visual
uv run --extra visual python examples/study.py
```

Development tools are installed by default and run through `uv`:

```bash
uv run ruff check .
uv run ruff format --check .
uv run --extra visual ty check src scripts examples
```

## Quick Start

```python
import evocomp

# Basic usage with Differential Evolution
optimizer = evocomp.DifferentialEvolution(f=2, operation='min', epochs=100)
optimizer.optimize(evocomp.Easom())
print(optimizer.best_candidate)

# Using convergence criteria and maximizing function instead
optimizer = evocomp.DifferentialEvolution(
    f=2,
    operation='max',
    halt_criteria=evocomp.FitnessConvergence(e=0.001)
)
optimizer.optimize(evocomp.Easom())
```

Check `examples/` directory for more usage examples.

## Features

### Parameter Studies

Study algorithm behaviour with different parameters values:

```python
from evocomp.visualization import study, display, plot_histories

results = study(
    param_values=[0.1, 0.2, 0.3],
    setup=lambda x: evocomp.DifferentialEvolution(f=x, operation='min'),
    objective=evocomp.Easom()
)

display(results, param_name='F coefficient')
plot_histories(results)
```

### Test Functions

Built-in test functions for algorithm evaluation:

```python
optimizer.optimize(evocomp.ThreeHumpCamel())
optimizer.optimize(evocomp.Ackley())
optimizer.optimize(evocomp.Easom())
```

Add your own objective functions by implementing the `Objective` interface:

```python
from evocomp import Objective
import numpy as np

class CustomFunction(Objective):
    @property
    def bounds(self) -> np.ndarray:
        return np.array([[-10.0, 10.0], [-10.0, 10.0]])

    def evaluate(self, solution: np.ndarray) -> float:
        x, y = solution
        return (x + 2*y - 7)**2 + (2*x + y - 5)**2
```
