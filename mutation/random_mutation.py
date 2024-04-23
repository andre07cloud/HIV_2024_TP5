from .abstract_mutation import AbstractMutation
import numpy as np
import random
import copy

class RandomMutation(AbstractMutation):
    '''
    Some mutation ideas 
    '''
    def __init__(self, mut_rate: float = 0.4):
        super().__init__(mut_rate)

    def _do_mutation(self, x) -> np.ndarray:

        possible_mutations = [
            self._delete_random_character,
            self._insert_random_character,
            self._replace_random_character
        ]
        mutator = np.random.choice(possible_mutations)

        return mutator(x)

    def _delete_random_character(self, s):
        """Returns s with a random character deleted"""
        if len(s) > 5:
            pos = random.randint(0, len(s) - 1)
            return s[:pos] + s[pos + 1 :]
        else:
            return s

    def _insert_random_character(self, s):
        """Returns s with a random character inserted"""
        pos = random.randint(0, len(s))
        random_character = chr(random.randrange(32, 127))
        return s[:pos] + random_character + s[pos:]

    def _replace_random_character(self, s):
        """Returns s with a random character replaced"""
        if s == "":
            return ""
        pos = random.randint(0, len(s) - 1)
        random_character = chr(random.randrange(32, 127))
        return s[:pos] + random_character + s[pos + 1 :]