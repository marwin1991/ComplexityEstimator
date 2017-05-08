from threading import Timer
from _thread import interrupt_main
from logger_init import init_logger


def exit_after(s):
    def outer(fn):
        def inner(*args, **kwargs):
            try:
                timer = Timer(s, quit_function)
                timer.start()
                result = fn(*args, **kwargs)
            except KeyboardInterrupt:
                logger = init_logger("exit_after_decorator")
                logger.info("Timeout reached!")
                print("Timeout reached!")
                timer.cancel()
                return -1
            finally:
                timer.cancel()
            return result
        return inner
    return outer


def quit_function():
    interrupt_main()
