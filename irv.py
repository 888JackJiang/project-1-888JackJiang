import numpy as np
import ballot_data as bd


def update_ballots(ballots, to_eliminate):
    """
    
    core method: Return redistributed copy of the ballots, in which the candidate "to_eliminate" has been deleted.
    
    For each ballot (row), remove the item "to_eliminate", shift the remaining candidate numbers to the left (one by one),
    and the fill the right side with zeros because we don't want to change the number of columns.
    For the code implementation:
    The main method is that we loop through each row to catch the eliminated candidate and then we update the ballots as redistribute the candidate number

    Input:
    ----------
    ballots : 
        (np.ndarray)
        2D array(rows = ballots, columns = preference positions)
    to_eliminate : 
        (int)
        Candidate id to remove (1..num_candidates)

    Output
    -------
    updated_ballots 
    (np.ndarray)
        redistributed copy of the ballots, in which the candidate "to_eliminate" has been deleted.
    """
    # We don't want to break the original ballots, so we create a copy to modify
    pre_updated_ballots = ballots.copy() # create a copy of the original ballots to avoid modifying it directly

    n_rows = pre_updated_ballots.shape[0] # we get the number of the rows
    n_cols = pre_updated_ballots.shape[1] # we get the number of the columns

    # pre_updated_ballots and updated_ballots have the same shape
    updated_ballots = np.zeros((n_rows, n_cols)) # create an array with the same shape as pre_updated_ballots to store the updated ballots
    
    # we loop through each row to catch the eliminated candidate and then we update the ballots as redistribute the candidate number
    for i in range(n_rows):
        row = np.array(pre_updated_ballots[i, :])           # get the current row i from the pre_updated_ballots array
        # Build an updated row by storing values that not the eliminated candidate( we find the eliminated candidate and remove it),
        # preserving original left-to-right order.
        # why use list because np.array has no attribute for append so we must using list to store here
        new_row = [value for value in row if (value != to_eliminate)]  # using array to stor
        
        
        if len(new_row) <  pre_updated_ballots.shape[1]: # if the length of new_row_vals is less than the number of columns
            # we need to fill the rest with zeros
            new_row.append(0)

        # convert the new_row to an 1-D array and then assign back to updated array
        updated_ballots[i, :] = np.array(new_row)

    # After the whole looping we get the updated_ballots
    return updated_ballots




