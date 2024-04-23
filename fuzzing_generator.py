from common.abstract_executor_new import AbstractExecutorNew
from fuzzers.random_fuzzer import RandomFuzzer 



def test_llm_generated_code(function_name):
    executor = AbstractExecutorNew(function_name)
    fuzzer = RandomFuzzer(executor)
    output = fuzzer.run_fuzzer(budget=5)  # Example time budget of 10 inputs
    assert output is not None
    print("INPUT FUZZING ****************************************************")
    print(output)
    print("INPUT FUZZING ****************************************************")
    return output['inputs']