from .abstract_crossover import AbstractCrossover

import numpy as np
import random

class SearchTestSuiteCrossover(AbstractCrossover):

    def __init__(self, cross_rate: float = 0.9):
        super().__init__(cross_rate)

    
    def _do_crossover(self, problem, a, b) -> tuple: 
        """
        Performs crossover between two parents and returns the offspring.

        Parameters:
        - problem: The optimization problem.
        - a: The first parent.
        - b: The second parent.

        Returns:
        - tuple: The offspring generated from crossover.
        """
        parent1 = a
        parent2 = b
        point = random.randint(1, len(parent1))
        child1_start = parent1[:point]
        child1_end = parent2[point:]
        child2_start = parent2[:point]
        child2_end = parent1[point:]
        #print("******** PREFIX ****** :")
        #print(child1_start)
        #print("******** SUFFIX ****** :")
        #print(child1_end) 
        child1 = np.concatenate((child1_start, child1_end))
        #print("******** FULL ****** :")
        #print(child1)
        child2 = np.concatenate((child2_start, child2_end))
        
        #print(parent1)
        #print("*******************")
        #print(parent2)
        #child1 = urlunparse(child1._replace(scheme = parent2.scheme, netloc = parent2.netloc))
        #child2 = urlunparse(child2._replace(scheme = parent1.scheme, netloc = parent1.netloc))
        #print(child1)
        #print("CHILD1*******************CHILD2")
        #print(child2)
        #print("CHILD1*******************CHILD2 ENNNNNNNNNNNNNNNNNNNNNNNNNDDD")
        return child1 , child2