from .abstract_generator import AbstractGenerator
import numpy as np
import string
import random
import typing
from .random_generator import RandomGenerator

class TestSuiteGenerator(AbstractGenerator):
    """
    A class that generates test suites using a random generator.

    Attributes:
        _name (str): The name of the generator.
        test_gen (RandomGenerator): The random generator used to generate individual tests.
        max_length (int): The maximum length of the test suite.
        min_length (int): The minimum length of the test suite.
    """

    def __init__(self) -> None:
        super().__init__()
        self._name = "RandomGenerator"
        self.test_gen = RandomGenerator()
        self.max_length = 15
        self.min_length = 10

    @property
    def name(self) -> int:
        return self._name

    def cmp_func(self, x: np.ndarray, y: np.ndarray) -> float:
        """
        Compare two test cases and return a similarity score.

        Args:
            x (np.ndarray): The first test case.
            y (np.ndarray): The second test case.

        Returns:
            float: The similarity score between the two test cases.
        """
        return 0.0

    def generate_random_test(self) -> str:
        """
        Generate a random test suite.

        Returns:
            str: The generated test suite.
        """
        n = random.randint(self.min_length, self.max_length)
        test_suite = []
        for i in range(n):
            test_suite.append(self.test_gen.generate_random_test())

        return np.array(test_suite)

