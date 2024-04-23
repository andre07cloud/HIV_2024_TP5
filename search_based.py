from datetime import datetime
from common.random_seed import get_random_seed
from common.abstract_executor import AbstractExecutor
from common.abstract_executor_new import AbstractExecutorNew
from common.prompt_generator import PromptGenerator
from common.llm_test_generator import LLMTestGenerator
from pymoo.algorithms.soo.nonconvex.ga import GA
from pymoo.algorithms.soo.nonconvex.random_search import RandomSearch
from sampling.abstract_sampling import AbstractSampling
from crossover.search_crossover import SearchTestSuiteCrossover
from problems.test_suite_problem import TestSuiteProblem
from mutation.test_suite_mutation import TestSuiteMutation
from generators.test_suite_generator import TestSuiteGenerator

from pymoo.optimize import minimize
from to_test.number_to_words import number_to_words
from to_test.strong_password_checker import strong_password_checker



def search_based(function, runs=5):

    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y")
    # Get the function from the module

    #function = number_to_words
    for run in range(runs):

        seed = get_random_seed()
        pop_size = 10
        n_eval = 90

        generator = TestSuiteGenerator() 

        executor = AbstractExecutorNew(function) 
        problem = TestSuiteProblem(executor) 
        
        method = GA(pop_size=pop_size,
                n_offsprings=int(pop_size/2),
                sampling=AbstractSampling(generator),
                mutation=TestSuiteMutation(generator=generator),
                crossover=SearchTestSuiteCrossover(cross_rate=0.9),
                eliminate_duplicates=False,
                )
        print("################ SEARCH BASED ALGORITHM ************")
        res = minimize(problem,
                method,
                termination=('n_eval', n_eval),
                seed=seed,
                verbose=True,
                eliminate_duplicates=False,
                save_history=True
                )
        

        print("Best solution found: %s" % res.X)
        print("Function value: %s" % res.F)
        print("Execution data:", res.problem.execution_data)

        return res.problem.execution_data
    
#search_based(strong_password_checker)