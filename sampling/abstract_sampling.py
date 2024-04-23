from pymoo.core.sampling import Sampling
import numpy as np
from abc import ABC
from  generators.abstract_generator import AbstractGenerator


class AbstractSampling(Sampling, ABC):
    """
    AbstractSampling is an abstract base class for sampling methods.

    It provides a common interface for different sampling strategies.
    """

    def __init__(self, generator:AbstractGenerator) -> None:
        super().__init__()
        self.generator = generator


    def _do(self, problem, n_samples, **kwargs):
        """
        Generate a set of samples using the specified sampling strategy.

        Args:
            problem: The problem instance.
            n_samples: The number of samples to generate.
            **kwargs: Additional keyword arguments.

        Returns:
            X: The generated samples as a numpy array.
        """
        X = np.full((n_samples, 1), None, dtype=object)
        i = 0
        while i < n_samples:
            test = self.generator.generate_random_test()

            X[i, 0] = test
            i += 1

        return X
