from typing import Literal

import numpy as np
from numpy import random

from evocomp.core.candidate import Candidate
from evocomp.core.halt_criteria import HaltCriteria
from evocomp.core.objective import Objective
from evocomp.core.optimizer import Optimizer


def symbiotic_optimisation(
    objective: Objective,
    *,
    operation: Literal['min', 'max'] = 'min',
    bf1: int = 1,
    bf2: int = 2,
    epochs: int = 100,
    size: int = 100,
    halt_criteria: HaltCriteria | None = None,
) -> 'SymbioticOptimisation':
    """Optimize an objective with Symbiotic Organism Search.

    Args:
        objective: Objective function to optimize.
        operation: Direction of optimization (``'min'`` or ``'max'``).
        bf1: Benefit factor for the first organism in the mutualism phase.
        bf2: Benefit factor for the second organism in the mutualism phase.
        epochs: Maximum number of iterations.
        size: Population size.
        halt_criteria: Optional convergence criteria to stop optimization
            before reaching maximum epochs.

    Returns:
        The fitted optimizer, including the best candidate and optimization history.
    """
    optimizer = SymbioticOptimisation(
        operation=operation,
        bf1=bf1,
        bf2=bf2,
        epochs=epochs,
        size=size,
        halt_criteria=halt_criteria,
    )
    optimizer.optimize(objective)
    return optimizer


class SymbioticOptimisation(Optimizer):
    """Symbiotic Organism Search (SOS) algorithm for global optimization.

    SOS mimics the symbiotic relationships among organisms in nature.
    It uses three phases: mutualism, commensalism, and parasitism.

    Args:
        operation: Direction of optimization ('min' or 'max').
        bf1: First benefit factor, controls mutual benefit in mutualism phase.
            Usually set to either 1 or 2.
        bf2: Second benefit factor, similar to bf1 but for the second organism.
            Usually set to either 1 or 2.
        epochs: Maximum number of iterations.
        size: Population size (number of organisms).
        halt_criteria: Optional convergence criteria to stop optimization
            before reaching maximum epochs.

    Note:
        - Benefit factors (bf1, bf2) are typically randomly chosen between 1 and 2
    """

    def __init__(
        self,
        operation: Literal['min', 'max'],
        bf1: int,
        bf2: int,
        epochs: int = 100,
        size: int = 100,
        halt_criteria: HaltCriteria | None = None,
    ):
        super().__init__(epochs, operation, halt_criteria)
        self.bf1 = bf1
        self.bf2 = bf2
        self.size = size

    def _get_random_index(self, current_index: int):
        idx_pool = np.delete(np.arange(self.size), current_index)
        return random.choice(idx_pool)

    def _mutualism_phase(
        self,
        i: int,
        x_best: Candidate,
        population: list[Candidate],
        new_population: list[Candidate],
        objective: Objective,
    ):
        j = self._get_random_index(i)
        xj = population[j]
        xi = population[i]
        mutual = (xi.solution + xj.solution) / 2
        xi_new = xi.solution + random.rand() * (x_best.solution - mutual * self.bf1)
        xj_new = xj.solution + random.rand() * (x_best.solution - mutual * self.bf2)
        xi_new = self._clip_bounds(xi_new, objective.bounds)
        xj_new = self._clip_bounds(xj_new, objective.bounds)
        xi_new = Candidate(xi_new, objective.evaluate(xi_new))
        xj_new = Candidate(xj_new, objective.evaluate(xj_new))
        new_population[i] = self._compare_candidates(xi, xi_new)
        new_population[j] = self._compare_candidates(xj, xj_new)

    def _commensalism_phase(
        self,
        i: int,
        x_best: Candidate,
        population: list[Candidate],
        new_population: list[Candidate],
        objective: Objective,
    ):
        j = self._get_random_index(i)
        xj = population[j]
        xi = population[i]
        xi_new = xi.solution + random.uniform(-1, 1) * (x_best.solution - xj.solution)
        xi_new = self._clip_bounds(xi_new, objective.bounds)
        xi_new = Candidate(xi_new, objective.evaluate(xi_new))
        new_population[i] = self._compare_candidates(xi_new, xi)

    def _parasite_phase(
        self,
        i: int,
        population: list[Candidate],
        new_population: list[Candidate],
        objective: Objective,
    ):
        j = self._get_random_index(i)
        xj = population[j]
        xi = population[i]
        parasite_solution = xi.solution.copy()
        random_index = random.randint(len(parasite_solution))
        parasite_solution[random_index] = random.uniform(-1, 1)
        x_parasite = Candidate(parasite_solution, objective.evaluate(parasite_solution))
        new_population[j] = self._compare_candidates(x_parasite, xj)

    def generate_init_population(self, objective: Objective) -> list[Candidate]:
        bounds = objective.bounds
        solutions = random.uniform(bounds[:, 0], bounds[:, 1], (self.size, len(bounds)))
        return [Candidate(x, objective.evaluate(x)) for x in solutions]

    def compute_next_population(
        self,
        population: list[Candidate],
        objective: Objective,
    ) -> list[Candidate]:
        new_population = population.copy()
        x_best = self._select_best(population)
        for i in range(len(population)):
            self._mutualism_phase(i, x_best, population, new_population, objective)
            self._commensalism_phase(i, x_best, population, new_population, objective)
            self._parasite_phase(i, population, new_population, objective)
        return new_population
