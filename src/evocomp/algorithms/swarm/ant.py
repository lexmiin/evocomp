import random
from abc import abstractmethod

import numpy as np
from numpy.typing import NDArray


class AntOptimization:
    def __init__(
        self,
        ants: int,
        evaporation_rate: float,
        alpha: float,
        beta: float,
        epochs: int,
    ) -> None:
        self._ants = ants
        self._evaporation_rate = evaporation_rate
        self._alpha = alpha
        self._beta = beta
        self._epochs = epochs
        self._start_node = 0

    @abstractmethod
    def _choose_next_node(
        self,
        location: int,
        unvisited: NDArray,
        pheromone: NDArray,
        heuristic: NDArray,
    ) -> NDArray:
        pass

    @abstractmethod
    def _update_pheromone(
        self,
        pheromone: NDArray,
        min_route: NDArray,
        min_route_cost: int,
        nodes: int,
    ) -> NDArray:
        pass

    def route(self, distance_matrix: NDArray):
        best_route = None
        best_route_cost = np.inf
        nodes = len(distance_matrix)
        pheromone = self.__init_pheromone(nodes)
        route = self.__init_route(nodes)
        heuristic = self._init_heuristic(distance_matrix)

        for epoch in range(self._epochs):
            for ant in range(self._ants):
                route[ant, 0] = self._start_node
                unvisited = np.ones(nodes, np.bool_)
                for node in range(nodes - 1):
                    location = route[ant, node]
                    unvisited[location] = False
                    next_node = self._choose_next_node(location, unvisited, pheromone, heuristic)
                    route[ant, node + 1] = next_node

            min_route, min_route_cost = self.__get_min_route(distance_matrix, route)
            if min_route_cost < best_route_cost:
                best_route = min_route
                best_route_cost = min_route_cost

            pheromone = self._update_pheromone(pheromone, min_route, min_route_cost, nodes)

        return best_route, best_route_cost

    def __init_pheromone(self, nodes: int) -> NDArray:
        return random.random() * np.ones((nodes, nodes))

    def __init_route(self, nodes: int):
        return np.ones((self._ants, nodes)).astype(int)

    def __get_min_route(self, distance_matrix: NDArray, route: NDArray):
        dist_cost = np.sum(distance_matrix[route[:, :-1], route[:, 1:]], axis=1)
        dist_min_index = np.argmin(dist_cost)
        dist_min_cost = dist_cost[dist_min_index]
        min_route = route[dist_min_index, :]
        return min_route, dist_min_cost

    def _init_heuristic(self, distance_matrix: NDArray):
        heuristic = 1 / distance_matrix
        heuristic[heuristic == np.inf] = 0
        return heuristic


class ACO(AntOptimization):
    def __init__(
        self,
        ants: int,
        evaporation_rate: float,
        alpha: float,
        beta: float,
        epochs: int,
    ) -> None:
        super().__init__(ants, evaporation_rate, alpha, beta, epochs)
        self._k = 0
        self._p_best = -np.inf

    def _choose_next_node(
        self,
        location: int,
        unvisited: NDArray,
        pheromone: NDArray,
        heuristic: NDArray,
    ) -> NDArray:
        pheromone_feat = np.power(pheromone[location, unvisited], self._alpha)
        visibility_feat = np.power(heuristic[location, unvisited], self._beta)
        features = np.multiply(pheromone_feat, visibility_feat)
        feat_sum = np.sum(features)
        probabilities = features / feat_sum
        cummulative = np.cumsum(probabilities)
        chosen_index = np.flatnonzero(cummulative > random.random())[0]
        next_node = np.flatnonzero(unvisited)[chosen_index]
        if np.max(probabilities) > self._p_best:
            self._p_best = np.max(probabilities)
            self._k = len(probabilities)
        return next_node

    def _update_pheromone(
        self,
        pheromone: NDArray,
        min_route: NDArray,
        min_route_cost: float,
        nodes: int,
    ) -> NDArray:
        pheromone = (1 - self._evaporation_rate) * pheromone
        for j in range(nodes - 1):
            current_city = min_route[j]
            next_city = min_route[j + 1]
            pheromone[current_city, next_city] += 1 / min_route_cost
        tau_max = self._compute_tau_max(min_route_cost)
        tau_min = self._compute_tau_min(tau_max, nodes)
        return self._clip_pheromone(pheromone, tau_min, tau_max)

    def _compute_tau_max(self, min_route_cost: float):
        return (1 / self._evaporation_rate) * (1 / min_route_cost)

    def _compute_tau_min(self, tau_max: float, nodes: int):
        probability_dec = np.power(self._p_best, 1 / (nodes - 1))
        return (tau_max * (1 - probability_dec)) / (self._k * probability_dec)

    def _clip_pheromone(self, pheromone: NDArray, tau_min: float, tau_max: float):
        return np.clip(pheromone, tau_min, tau_max)
