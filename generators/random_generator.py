

from .abstract_generator import AbstractGenerator
import numpy as np
import string
import random
import typing

class RandomGenerator(AbstractGenerator):

    """RandomGenerator is a generator that generates random strings."""

    def __init__(self) -> None:
        super().__init__()
        self._name = "RandomGenerator"
        self.min_length = 10
        self.max_length = 100

    @property
    def name(self) -> int:
        return self._name

    def cmp_func(self, x:np.ndarray, y:np.ndarray) -> float:
        return 0.0


    def generate_random_test(self) -> str:
        return self.generate_random_string(
            random.randint(self.min_length, self.max_length)
        )
    
    def generate_random_string(self, length) -> str:
        """Generate a random string of specified length."""
        letters = string.ascii_letters + string.digits + string.punctuation
        return "".join(random.choice(letters) for _ in range(length))

