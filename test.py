def print_test(d):
    print(d)


def sort_lib(list):
    sorted(list)


def endless_loop():
    i = 0
    while i == 0:
        i = 0


def loop_test(n):
    i = 0
    while i < n:
        i += 1


def loop_in_loop(n):
    i, j = 0, 0
    while i < n:
        while j < n:
            j += 1
        j = 0
        i += 1
