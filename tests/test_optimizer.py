from collections.abc import Iterable
from typing import Literal

import numpy as np
import pytest

from evocomp.core.candidate import Candidate
from evocomp.core.halt_criteria import HaltCriteria
from evocomp.core.objective import Objective
from evocomp.core.optimizer import Optimizer


class UnusedObjective(Objective):
    @property
    def bounds(self) -> np.ndarray:
        return np.array([[-10.0, 10.0]])

    def evaluate(self, solution: np.ndarray) -> float:
        return float(solution[0])


class SequenceOptimizer(Optimizer):
    def __init__(
        self,
        populations: Iterable[list[Candidate]],
        *,
        operation: Literal['min', 'max'] = 'min',
        epochs: int = 2,
        halt_criteria: HaltCriteria | None = None,
    ) -> None:
        super().__init__(epochs, operation, halt_criteria)
        self._populations = iter(populations)

    def generate_init_population(self, objective: Objective) -> list[Candidate]:
        return next(self._populations)

    def compute_next_population(
        self,
        population: list[Candidate],
        objective: Objective,
    ) -> list[Candidate]:
        return next(self._populations)


class HaltImmediately(HaltCriteria):
    def __init__(self) -> None:
        super().__init__(e=1.0)
        self.calls = 0

    def halt(self, children: list[Candidate], parents: list[Candidate]) -> bool:
        self.calls += 1
        return True


def population(*fitnesses: float) -> list[Candidate]:
    return [Candidate(np.array([fitness]), fitness) for fitness in fitnesses]


@pytest.mark.parametrize(
    ('operation', 'expected_fitness'),
    [('min', 1.0), ('max', 3.0)],
)
def test_optimizer_selects_best_candidate_for_operation(
    operation: Literal['min', 'max'],
    expected_fitness: float,
) -> None:
    optimizer = SequenceOptimizer([population(3.0, 1.0, 2.0)], operation=operation, epochs=0)

    best = optimizer.optimize(UnusedObjective())

    assert best.fitness == expected_fitness


def test_optimizer_records_initial_and_each_epoch_population() -> None:
    optimizer = SequenceOptimizer(
        [population(3.0, 4.0), population(2.0, 5.0), population(1.0, 6.0)],
        epochs=2,
    )

    best = optimizer.optimize(UnusedObjective())

    assert best.fitness == 1.0
    assert optimizer.epochs == 2
    assert [candidate.fitness for candidate in optimizer.history] == [3.0, 2.0, 1.0]


def test_optimizer_stops_after_halt_criterion_matches() -> None:
    halt_criteria = HaltImmediately()
    optimizer = SequenceOptimizer(
        [population(2.0), population(1.0), population(0.0)],
        epochs=10,
        halt_criteria=halt_criteria,
    )

    best = optimizer.optimize(UnusedObjective())

    assert best.fitness == 1.0
    assert optimizer.epochs == 1
    assert halt_criteria.calls == 1
