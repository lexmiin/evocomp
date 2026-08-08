import numpy as np
import pytest

from evocomp.core.candidate import Candidate
from evocomp.core.halt_criteria import FitnessConvergence
from evocomp.core.halt_criteria import SolutionConvergence


def candidate(solution: list[float], fitness: float = 0.0) -> Candidate:
    return Candidate(np.array(solution), fitness)


@pytest.mark.parametrize('epsilon', [0.0, -0.1])
def test_halt_criteria_requires_positive_epsilon(epsilon: float) -> None:
    with pytest.raises(ValueError, match='epsilon cannot be zero or negative'):
        FitnessConvergence(epsilon)


def test_fitness_convergence_halts_when_mean_fitness_change_is_below_epsilon() -> None:
    criterion = FitnessConvergence(e=0.2)
    parents = [candidate([0.0], 1.0), candidate([1.0], 3.0)]
    children = [candidate([0.0], 1.1), candidate([1.0], 3.1)]

    assert criterion.halt(children, parents)


def test_fitness_convergence_does_not_halt_at_epsilon_boundary() -> None:
    criterion = FitnessConvergence(e=0.1)
    parents = [candidate([0.0], 1.0)]
    children = [candidate([0.0], 1.1)]

    assert not criterion.halt(children, parents)


def test_solution_convergence_uses_farthest_pair_of_children() -> None:
    criterion = SolutionConvergence(e=2.0)
    parents = [candidate([100.0, 100.0])]
    children = [
        candidate([0.0, 0.0]),
        candidate([1.0, 0.0]),
        candidate([0.0, 1.0]),
    ]

    assert criterion.halt(children, parents)


def test_solution_convergence_does_not_halt_at_epsilon_boundary() -> None:
    criterion = SolutionConvergence(e=1.0)
    children = [candidate([0.0, 0.0]), candidate([1.0, 0.0])]

    assert not criterion.halt(children, parents=[])
