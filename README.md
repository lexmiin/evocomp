# Evolutionary computation

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
uv add git+https://github.com/lexmiin/evocomp.git

# Include the optional visualization feature
uv add 'evocomp[visual] @ git+https://github.com/lexmiin/evocomp.git'

# Or clone and set up the development environment
git clone https://github.com/lexmiin/evocomp.git
cd evocomp
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

## Releasing

Releases use two manually started GitHub Actions workflows. **Prepare Release**
updates the package version and lockfile, generates `CHANGELOG.md` from commit
messages with git-cliff, and opens a release pull request for review. After that
pull request is merged, **Release** builds the Python wheel and source
distribution, publishes both to PyPI, and only then creates the `v<version>` tag
and GitHub release with the reviewed notes and distributions attached.

Before the first release:

1. Create a GitHub environment named `pypi` and add any desired deployment
   protection rules, such as required reviewer approval.
2. In the repository's GitHub Actions settings, allow workflows to create pull
   requests so **Prepare Release** can open its review branch.
3. On PyPI, add a pending trusted publisher for project `evocomp` with owner
   `lexmiin`, repository `evocomp`, workflow `release.yml`,
   and environment `pypi`. No PyPI API token is required.

Write commit descriptions as `<topic>: <summary>`, for example
`algorithms: default crossover rate to 0.4 in diff evolution`. The topic is a
human-readable area of change; Conventional Commits are not required.

For each release:

1. Open **Actions → Prepare Release → Run workflow**, select the default branch,
   and enter the exact `X.Y.Z` version without a `v` prefix.
2. Review and merge the generated release pull request, editing `CHANGELOG.md`
   when the generated notes need clarification.
3. Open **Actions → Release → Run workflow**, select the default branch, enter
   the same version, and choose whether GitHub should mark it as a prerelease.

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
