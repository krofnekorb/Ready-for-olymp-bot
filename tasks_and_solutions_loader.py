task_number_limit = dict(
    tfcv=2,
    linal=2,
    calculus=1,
    algebra=1,
    comb=2,
    probability=1
)


def load_task(section, task_number):
    if task_number_limit[section] < task_number:
        return ''
    else:
        f = open('tasks/{}/{}.jpg'.format(section, task_number), 'rb')
        problem = f.read()
        f.close()
        return problem


def load_solution(section, task_number):
    assert (task_number_limit[section] >= task_number), \
        'Illegal attempt to load non-existing solution for section={} and task={}'.format(section, task_number)
    f = open('tasks/{}/{}-sol.jpg'.format(section, task_number), 'rb')
    solution = f.read()
    f.close()
    return solution
