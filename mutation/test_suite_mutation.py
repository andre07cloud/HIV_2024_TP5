from .abstract_mutation import AbstractMutation
import numpy as np
import random
import copy

class TestSuiteMutation(AbstractMutation):
    '''
    Class for mutation of test suites 
    '''
    def __init__(self, mut_rate: float = 0.4, generator=None):
        super().__init__(mut_rate, generator)

    def _do_mutation(self, x) -> np.ndarray:

        possible_mutations = [
            self._insert_random_element,
            self._replace_random_element
        ]
        mutator = np.random.choice(possible_mutations)

        return mutator(x)

    def _delete_random_element(self, s):
        """Returns s with a random character deleted"""
        if len(s) > 2:
            index_to_remove = np.random.randint(len(s))
            s = np.delete(s, index_to_remove)
        return s

    def _insert_random_element(self, s):
        """Returns s with a random character inserted"""
        if len(s) < (self.generator.max_length):

            new_element = self.generator.test_gen.generate_random_test()
            s = np.append(s, new_element)
        return s

    def _replace_random_element(self, s):
        """Returns s with a random character replaced"""
        index_to_replace = np.random.randint(len(s))
        new_element = self.generator.test_gen.generate_random_test()
        s[index_to_replace] = new_element
        return s