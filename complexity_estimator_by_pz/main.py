from argument_parser import *
from timer import Timer
from complexity import *
from logger_init import init_logger
from sys import exit


def main():
    logger = init_logger("main")
    logger.info("start program")

    p = ProgramArguments()
    try:
        p.parse()
    except ArgPathToFileError:
        exit(2)
    logger.info(p.path_to_file + p.function_name + p.module_name
                + str(p.timeout) + p.init_struct_code + p.step + str(p.repeat))

    timer = Timer(p.path_to_file, p.function_name, p.module_name, p.timeout,
                  p.init_struct_code, p.step, p.repeat)

    try:
        time_list = timer.measure_time()
    except ArgFunNameError:
        print("There is no such a fucntion :" + p.function_name)
        exit(2)

    try:
        estimate_complexity(time_list)
    except NotEnoughStepsError:
        exit(2)

    logger.info("end program")

if __name__ == "__main__":
    main()
