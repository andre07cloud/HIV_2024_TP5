from abc import ABC, abstractmethod
from pymoo.core.problem import ElementwiseProblem
from common.abstract_executor import AbstractExecutor
from problems.abstract_problem import AbstractProblem

class TestSuiteProblem(AbstractProblem):
    """
    This is the base class for performing solution evaluation.

    Attributes:
        executor (AbstractExecutor): The executor used for executing the test cases.
        n_var (int): The number of decision variables.
        n_obj (int): The number of objectives.
        n_ieq_constr (int): The number of inequality constraints.
        xl (list or None): The lower bounds of the decision variables.
        xu (list or None): The upper bounds of the decision variables.
        _name (str): The name of the problem.
        previous_coverage (int): The previous coverage value.
        first_evaluation (bool): Flag indicating if it's the first evaluation.

    Methods:
        __init__: Initializes the problem.
        _evaluate: Evaluates the fitness of the solution.

    """

    def __init__(self, executor: AbstractExecutor, n_var: int=1, n_obj=1, n_ieq_constr=0, xl=None, xu=None):
        """Initialize the problem.

        Args:
            executor (AbstractExecutor): The executor used for executing the test cases.
            n_var (int, optional): The number of decision variables. Defaults to 1.
            n_obj (int, optional): The number of objectives. Defaults to 1.
            n_ieq_constr (int, optional): The number of inequality constraints. Defaults to 0.
            xl (list or None, optional): The lower bounds of the decision variables. Defaults to None.
            xu (list or None, optional): The upper bounds of the decision variables. Defaults to None.
        """
        super().__init__(executor, n_var, n_obj, n_ieq_constr, xl, xu)
        self.executor = executor
        self._name = "TestSuiteProblem"
        self.previous_coverage = 0
        self.first_evaluation = True

    def _evaluate(self, x, out, *args, **kwargs):
        """
        Evaluates the fitness of the solution.

        Args:
            x (numpy.ndarray): The decision variables.
            out (dict): The output dictionary.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.
        """
        tests = x[0]
        self.executor._full_coverage = [] # reset the coverage evaluation
        self.executor._coverage = set()

        for test in tests:
            exceptions, execution_time, coverage = self.executor._execute_input(test)
            
        fitness = len(coverage) / (len(test))

        self.execution_data[self.n_evals] = {"input": test, "output": fitness, "execution_time": execution_time}

        self.n_evals += 1

        out["F"] = -fitness