def fair_sharer(values, num_iterations, share=0.1):
    """ Runs num_iterations.
        In each iteration the highest value in "values" gives a fraction (share)
        to both the left and right neighbor. The leftmost field is considered
        the neightbor of the rightmost field.

        Examples:
        fair_sharer([0, 1000, 800, 0], 1) --> [100, 800, 900, 0]
        fair_sharer([0, 1000, 800, 0], 2) --> [100, 890, 720, 90]

        Args
        values:
            1D array of values (list or numpy array)
        num_iteration:
            Integer to set the number of iterations
        """
    
    for iter in range(num_iterations):
        # reset largest number and index
        largest = 0
        largest_idx = 0
        for i, val in enumerate(values):
            # find largest number and corresponding index
            if val > largest:
                largest = val
                largest_idx = i
        
        # get neighbouring indices
        l_idx = largest_idx - 1
        r_idx = largest_idx + 1
        share_v = largest * share
        if largest_idx == len(values)- 1:
            r_idx = 0

        # update list
        values[l_idx] = values[l_idx] + share_v
        values[r_idx] = values[r_idx] + share_v
        values[largest_idx] = values[largest_idx] - share_v * 2

    return values



