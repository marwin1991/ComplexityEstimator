from logger_init import init_logger


def add_step(value, step):
    logger = init_logger("add_step")
    value_list = str.split(value, ";")
    logger.debug(value_list)
    step_list = str.split(step, ";")
    for i in value_list:
        if i.find("=") == -1:
            value_list.remove(i)
    for i in step_list:
        if i.find("=") == -1:
            step_list.remove(i)
    logger.debug(value_list)

    for index, elem in enumerate(value_list):
        logger.debug(str.split(elem, "="))
        start_value = str.split(elem, "=")[1]
        old_val = start_value
        step_to_add = str.split(step_list[index], "=")[1]

        if not any(c.isalpha() for c in step_to_add) \
                and not any(c.isalpha() for c in start_value):
            if step_list[index].find("-") == -1:
                start_value = " " + str(float(start_value)
                                        + float(step_to_add))
            else:
                start_value = " " + str(float(start_value)
                                        - float(step_to_add))
        else:
            start_value += step_to_add

        start_value += ";"
        value_list[index] = str.replace(value_list[index], old_val, start_value)

    logger.info("End adding step values to value result: " + ''.join(value_list))
    return ''.join(value_list)

