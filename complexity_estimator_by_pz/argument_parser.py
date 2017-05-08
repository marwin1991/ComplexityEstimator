from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from logger_init import init_logger


# class to contains a parse arguments
class ProgramArguments:
    def __init__(self):
        self.function_name = "main"
        self.path_to_file = ""
        self.timeout = 30
        self.init_struct_code = ""
        self.clean_code = ""
        self.module_name = "module"
        self.step = ""
        self.repeat = 3

    def parse(self):
        logger = init_logger("parse")
        par = ArgumentParser(
            description='Program to estimate python scripts complexity.',
            formatter_class=ArgumentDefaultsHelpFormatter,
            epilog='')
        par.add_argument('-f', '--function', nargs='?', type=str,
                         default="main",
                         help="function to be measure", dest="function_name")
        par.add_argument('-m', '--module', nargs='?', type=str,
                         default="module?",
                         help="module frm witch is function",
                         dest="module_name")
        par.add_argument('-p', '--path',
                         type=str, default="",
                         help="path to file containing function",
                         dest="path_to_file")
        par.add_argument('-t', '--timeout', type=int,
                         default=30,
                         help="maximum time of execution function in seconds",
                         dest="timeout")
        par.add_argument('-i', '--init', type=str,
                         default="",
                         help="initializaion code of varaibles/structurs "
                              "used by function", dest="init_struct_code")
        par.add_argument('-c', '--clean', type=str,
                         default="",
                         help="code responsible for cleaning",
                         dest="clean_code")
        par.add_argument('-s', '--step', type=str,
                         default="",
                         help="incrementation step",
                         dest="step")
        par.add_argument('-r', '--repeat', type=int,
                         default=3,
                         help="number of repeats",
                         dest="repeat")

        # par.print_help()
        args = par.parse_args()
        if args.path_to_file != "":
            try:
                with open(args.path_to_file, 'r'):
                    self.path_to_file = args.path_to_file
            except IOError:
                logger.info("ERROR cannot open" + str(args.path_to_file))
                print("Could not read from file: " + str(args.path_to_file))
                raise ArgPathToFileError

        self.function_name = args.function_name
        self.timeout = args.timeout
        self.init_struct_code = args.init_struct_code
        self.clean_code = args.clean_code
        self.step = args.step
        self.repeat = args.repeat
        logger.info("End parsing arguments")


class ArgPathToFileError(Exception):
    pass


class ArgFunNameError(Exception):
    pass

