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









###### undo




def vote_transfers(previous_ballots, updated_ballots):
    """

    Compare the changes in the first preference choices in the two ballot sets (before and after the elimination operation), 
    and count how many ballots were discarded.
    
    core method: first we do a vectorization difference of the original ballot votes for fist preference and after using IRV method ones
                second we do a zeros elements checking for the array rows one by one to search the discarded ballots in two ballots: previous_ballots and updated_ballots.
                which is based on a looping.
    Input:
    ----------
    previous_ballots : 
        (np.ndarray)
        Ballot array before a candidate elimination.
        each row represents one ballot submitted by one voter;
        each non-zero value represents a candidate;
        each column represents a preference rank, from first to last preference going left to right, 
        for example a 2 in the first column means that Candidate 2 was the voter's first preference;
    updated_ballots : 
        (np.ndarray)
        Ballot array after a candidate elimination from using the function update_ballots()).
        There we use IRV method to get the updated_ballots based on previous_ballots
        
    Outputs:
    -------
    candidates :
        (np.ndarray)
        candidates, a NumPy vector or list containing all candidates in the election in numerical order (e.g. [1 2 3 ...])  
    vote_diffs : 
        (np.ndarray)
        a NumPy vector or list of the same length as candidates, containing the differences in first-preference votes 
        obtained by each of the candidates between previous_ballots and updated_ballots (given in the same order as candidates)
    
        The difference in the number of first-choice votes between the updated ballot and the previous one. 
        A positive value indicates an increase in the number of votes; a negative value indicates an increase in the number of lost votes.   
        
    discarded_diff : 
        (int)
        Number of ballots that became invalid/discarded (all zeros) after elimination.


    Example
    -------
    we use the prev_ballots:
    >>> vote_transfers(np.array([[1, 4, 0, 0],[1, 5, 3, 2, 4],[3, 5, 4, 1, 0]]),
    and the updated_ballots:                np.array([[1, 4, 0, 0],[1, 5, 2, 4, 0],[5 ,4 ,1 ,0 , 0]]))
    
    we get the result like that: (candidates <- array([1, 2, 3, 4, 5]), vote_diffs <- array([0, 0, -1, 0, 1)
    """
    
    # Count the total votes for the ballots program; which is the the number of rows of the array ballots.
    n_votes = previous_ballots.shape[0]
    
    # Count first-preference we count the votes before and after voting based the corresponding oder candidate (default numerical order)
    prev_cands, prev_counts = bd.count_votes(previous_ballots, preference=0, sort_by='candidate')
    upd_cands, upd_counts   = bd.count_votes(updated_ballots, preference=0, sort_by='candidate')
    
    # we know prev_cands and upd_cands are the same results for candidates so we create a numpy vector or a list to store the candidates.
    candidates = upd_cands

    # Next we aim to align counts with candidate order
    # Instead of one by one difference for two vectors we just use vectorization to do a difference for two vectors.
    
    
    # # avoid the type is different before difference ; there we both use a Numpy vector
    upd_counts = np.array(upd_counts)
    prev_counts = np.array(prev_counts)
    # we create the vote_ diffs: after - before.
    vote_diffs = upd_counts - prev_counts
    

    # Next we start counting discarded ballots
    
    # Initialise
    discarded_prev = 0 # we start the loop which we want to do a accumulation for the the number    
    # we start to loop the row of the matrix from the number of the n_votes which is equal to the number of the row of the matrix.
    for i in range(n_votes): 
        # we check whether or not the row i all the elements are zero 
        # the condition is that when row i each element is 0 then the sum of all the elements are zero, if there exists no zero item then the sum of the row isn't equal to zero
        if np.sum(previous_ballots[i,:])==0 :
            discarded_pre += 1 # update the value find the row is 0 (discarded) plus1
            
            
    # next we update all the ballots based on the elimination.    
    # the same operation as discarded_prev, we want to find the discarded numbers in updated ballots
    # Initialise
    discarded_upd = 0 # we start the loop which we want to do a accumulation for the the number    
    
    for i in range(n_votes): # the same number of the row for previous_ballots and updated_ballots.
        # the same operation as before.
        if np.sum(updated_ballots[i,:])==0 :
            discarded_upd += 1  # update the value find the row is 0 (discarded) plus1    
    # avoid the type is different before difference ; there we both use a Numpy vector
    discarded_upd = np.array(discarded_upd)
    discarded_prev = np.array(discarded_prev)       
    
    # get the total situation before and after
    discarded_diff = discarded_upd - discarded_prev

    return candidates, vote_diffs, discarded_diff









