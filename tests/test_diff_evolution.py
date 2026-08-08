from typing import Literal

import numpy as np
import pytest

from evocomp.algorithms.evolutionary.diff_evolution import DifferentialEvolution
from evocomp.core.candidate import Candidate
from evocomp.core.objective import Objective


class BoxSphere(Objective):
    @property
    def bounds(self) -> np.ndarray:
        return np.array([[-2.0, 2.0], [-3.0, 3.0], [-4.0, 4.0]])

    def evaluate(self, solution: np.ndarray) -> float:
        return float(np.sum(solution**2))


@pytest.fixture(autouse=True)
def deterministic_numpy_randomness():
    state = np.random.get_state()
    np.random.seed(20260808)
    yield
    np.random.set_state(state)


def make_optimizer(*, operation: Literal['min', 'max'] = 'min') -> DifferentialEvolution:
    return DifferentialEvolution(
        operation=operation,
        f=0.8,
        crossover_rate=0.3,
        epochs=1,
        size=8,
    )


def assert_population_is_valid(
    population: list[Candidate],
    objective: Objective,
    *,
    expected_size: int,
) -> None:
    assert len(population) == expected_size
    for candidate in population:
        assert candidate.solution.shape == (len(objective.bounds),)
        assert np.all(candidate.solution >= objective.bounds[:, 0])
        assert np.all(candidate.solution <= objective.bounds[:, 1])


def test_initial_population_has_configured_size_shape_and_bounds() -> None:
    objective = BoxSphere()
    optimizer = make_optimizer()

    population = optimizer.generate_init_population(objective)

    assert_population_is_valid(population, objective, expected_size=optimizer.size)


def test_next_population_preserves_invariants_and_computes_fitness() -> None:
    objective = BoxSphere()
    optimizer = make_optimizer()
    population = optimizer.generate_init_population(objective)

    next_population = optimizer.compute_next_population(population, objective)

    assert_population_is_valid(next_population, objective, expected_size=optimizer.size)
    for candidate in next_population:
        assert candidate.fitness == pytest.approx(objective.evaluate(candidate.solution))


@pytest.mark.parametrize('operation', ['min', 'max'])
def test_selection_does_not_make_best_fitness_worse(
    operation: Literal['min', 'max'],
) -> None:
    objective = BoxSphere()
    optimizer = make_optimizer(operation=operation)
    population = optimizer.generate_init_population(objective)
    optimizer._compute_fitness(population, objective)
    previous_best = optimizer._select_best(population).fitness

    next_population = optimizer.compute_next_population(population, objective)
    next_best = optimizer._select_best(next_population).fitness

    if operation == 'min':
        assert next_best <= previous_best
    else:
        assert next_best >= previous_best
