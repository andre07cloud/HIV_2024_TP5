import numpy as np
from abstract_crossover import AbstractCrossover



class OnePointCrossover(AbstractCrossover):
    def __init__(self, cross_rate: float = 0.9):
        super().__init__(cross_rate)


    def _do_crossover(self, problem, a, b) -> tuple:

        return a, b