from math import log10
from logger_init import init_logger


def total_difference_between_two_lists(basic_list, compare_list):
    total_difference = 0
    if len(compare_list) < len(basic_list):
        return -1
    for index, elem in enumerate(basic_list):
        total_difference = abs(compare_list[index] - elem)
    return total_difference


class NotEnoughStepsError(Exception):
    pass


def estimate_complexity(time_list):
    logger = init_logger("complexity")
    if len(time_list) <= 2:
        print("It is imposible to calculate complexity with this data!")
        logger.info("Not enough arguments")
        raise NotEnoughStepsError
    if len(time_list) == 3:
        print("It is the minimum size od data so complexity can be wrong!")
        logger.info("minimum number of arguments")

    difference = time_list[1] - time_list[0]

    const_complex_list = [time_list[0]]
    n_complex_list = [time_list[0]]
    n_logn_complex_list = [time_list[0]]
    n_2_complex_list = [time_list[0]]
    n_3_complex_list = [time_list[0]]
    for i in range(0, len(time_list)-1):
        const_complex_list.append(time_list[1])
        n_complex_list.append(time_list[1] + difference * i)
        n_logn_complex_list.append(
            time_list[1] + (difference + log10(1 + difference)) * i)

    n_2_complex_list.append(time_list[1])
    n_3_complex_list.append(time_list[1])
    for i in range(2, len(time_list)):
        n_2_complex_list.append(n_2_complex_list[i-1] + 0.66 * i * difference)
        n_3_complex_list.append(
            n_3_complex_list[i-1] + i * i * difference * 0.33)

    print("Original: \t\t" + str(time_list))
    print("calculated O(1): \t" + str(const_complex_list))
    print("calculated O(n): \t" + str(n_complex_list))
    print("calculated O(nlogn):" + str(n_logn_complex_list))
    print("calculated O(n^2): \t" + str(n_2_complex_list))
    print("calculated O(n^3): \t" + str(n_3_complex_list))

    difference_list = list()

    difference_list.append(total_difference_between_two_lists(
        time_list, const_complex_list))
    difference_list.append(total_difference_between_two_lists(
        time_list, n_complex_list))
    difference_list.append(total_difference_between_two_lists(
        time_list, n_logn_complex_list))
    difference_list.append(total_difference_between_two_lists(
        time_list, n_2_complex_list))
    difference_list.append(total_difference_between_two_lists(
        time_list, n_3_complex_list))

    min_val = difference_list[0]
    min_val_index = 0
    for index, elem in enumerate(difference_list):
        if elem < min_val:
            min_val = elem
            min_val_index = index

    with open("complexity_tables.txt", "w") as file_to_s:
        file_to_s.writelines("N * step       time cost\n")
        if min_val_index == 0:
            print("Complexity is O(1).")
            for i in range(1, 100):
                file_to_s.writelines(str(i) + " * step    " +
                                     str(time_list[1])+"\n")

        if min_val_index == 1:
            print("Complexity is O(n).")
            for i in range(1, 100):
                file_to_s.writelines(str(i) + " * step    " +
                                     str(time_list[1] + difference * i)+"\n")
        if min_val_index == 2:
            print("Complexity is O(nlogn).")
            for i in range(1, 100):
                file_to_s.writelines(str(i) + " * step    " +
                                     str(time_list[1] +
                                         (difference +
                                          log10(1 + difference)) * i)+"\n")
        if min_val_index == 3:
            print("Complexity is O(n^2).")
            n_2_complex_list_to_save = [time_list[0]]
            n_2_complex_list_to_save.append(time_list[1])
            for i in range(2, 100):
                n_2_complex_list_to_save.append(
                    n_2_complex_list_to_save[i - 1] + 0.66 * i * difference)

            for i in range(0, 100):
                file_to_s.writelines(str(i) + " * step    " +
                                     str(n_2_complex_list_to_save[i])+"\n")
        if min_val_index == 4:
            print("Complexity is O(n^3).")
            n_3_complex_list_to_save = [time_list[0]]
            n_3_complex_list_to_save.append(time_list[1])
            for i in range(2, 100):
                n_3_complex_list_to_save.append(
                    n_3_complex_list_to_save[i - 1]
                    + i * i * difference * 0.33)

            for i in range(0, 100):
                file_to_s.writelines(str(i) + " * step    " +
                                     str(n_3_complex_list_to_save[i])+"\n")

    logger.info("End calculating complexity")
