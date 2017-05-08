import inspect
from argument_parser import ArgFunNameError
from timeout_decorator import *
from importlib.machinery import SourceFileLoader
import timeit
from step_counter import add_step
from logger_init import init_logger


class Timer:
    def __init__(self,
                 path_to_module="C:/Users/Krzysztof/"
                                "Desktop/Python/zad2/test.py",
                 function_to_measure="loop_test(n)",
                 module_name="test",
                 timeout=10,
                 init_struct_code="n=10",
                 step="n = 10",
                 repeats=5):
        self.path_to_module = path_to_module
        self.function_to_measure = function_to_measure
        self.module_name = module_name
        self.timeout = timeout
        self.init_struct_code = init_struct_code
        self.step = step
        self.repeats = repeats

    def measure_time(self):
        logger = init_logger("measure_time")
        logger.info("Begin measure time")
        loaded_module = SourceFileLoader(
            self.module_name,
            self.path_to_module).load_module()
        all_functions = inspect.getmembers(loaded_module, inspect.isfunction)

        fun_names = []
        for i in all_functions:
            fun_names.append(i[0])

        if self.function_to_measure.split("(")[0] not in fun_names:
            logger.info("ArgFunNameError raised because "
                        "of no function with this name")
            logger.debug(self.function_to_measure.split("(")[0])
            logger.debug(all_functions)
            raise ArgFunNameError

        returns_values_list = []
        init_struct_code_copy = self.init_struct_code
        for i in range(0, self.repeats):
            setup = "from {0} import {1}; {2}"\
                .format(self.module_name, self.function_to_measure.split("(")[0],
                        init_struct_code_copy)

            @exit_after(self.timeout)
            def __inside_measure():

                returns_values_list.append(
                    timeit.timeit(self.function_to_measure, setup=setup,
                                  number=1))
            __inside_measure()
            logger.debug(init_struct_code_copy)
            logger.info("Times loop: " + str(i))
            init_struct_code_copy = add_step(init_struct_code_copy, self.step)
        logger.info(returns_values_list)
        logger.info("End measure time")
        return returns_values_list
