
from abc import ABC, abstractmethod
from pymoo.core.problem import ElementwiseProblem
from common.abstract_executor import AbstractExecutor
from problems.abstract_problem import AbstractProblem

class RandomProblem(AbstractProblem):
    """
    This is the base class for performing solution evalaution
    """

    def __init__(self, executor: AbstractExecutor, n_var: int=1, n_obj=1, n_ieq_constr=0, xl=None, xu=None):
        """Initialize the problem.
        """
        super().__init__(executor, n_var, n_obj, n_ieq_constr, xl, xu)
        self.executor = executor
        self._name = "RandomProblem"
        self.previous_coverage = 0
        self.first_evaluation = True

    def _evaluate(self, x, out, *args, **kwargs):

        test = x[0]

        fitness = 0
        #print("Test: ", test)

        exceptions, execution_time, coverage = self.executor._execute_input(test)
        
        fitne = len(coverage)

        out["F"] = -fitness

        
      



