

# Counts the number of cycles in the solution. solution[i] == i is counted as a cycle.
# parameter: solution: a solution to the TSP, the ith element of the list is the city visited after the ith one
# return: the number of cycles in the solution or -1 if one of elements of the solution is not between 0 and the number
# of cities - 1
def nb_cycles(solution):
    """
    :param solution a solution of the TSP, the ith element of the list is the city visited after the ith one
    :return the number of cycles in the given solution if all the elements in the solution are between 0 and (the number
    of cities - 1), -1 otherwise
    """
    visited = [0] * len(solution)
    nb = 0
    for i in range(len(solution)):
        j = i
        if visited[j] == 0:
            nb += 1
        first_index = j
        while visited[j] < 1:
            visited[j] += 1
            if solution[j] not in range(len(solution)):
                return -1
            j = solution[j]
        if j != first_index:
            return 0
    return nb
