



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






def eliminate_next(ballots):
    """
    Determine which candidate should be eliminated next in an Instant Runoff Voting (IRV) round.
    there we consider the situation which we have no ties or ties.

    Input:
    ----------
    ballots : 
    (Numpy array)
    This is a two-dimensional NumPy array, where each row represents the ranking preference of a voter (each column corresponds to a candidate number).
    Output :
    -------
    int
    The numbers of the candidates to be eliminated next (starting from 1) are determined based on the fewest votes they received in their first choice.
    In case of a tie, the subsequent ballots (second, third, etc.) will be checked one by one.
    If there is still a tie, the candidate with the smallest number will be eliminated.
    """
    
    num_prefs = ballots.shape[1]   # total number of preference columns
    # we firstly run the fisrt-preference situation( may be including the ties)
    candidates, counts = bd.count_votes(ballots, preference=0)
    # store candidate counts as a dictionary
    cand_counts = dict(zip(candidates, counts))
    
    
    ####### There we will run the tie-resolving rule ###########
    
    ##### we initialise ######
    
    
    # we cath the least value for the candidates in fisrt-preference choice( including the ties)
    min_count = min(cand_counts.values())
    # find all candidates tied with the fewest votes
    tied = [c for c, v in cand_counts.items() if v == min_count]
    # we restore into a meaningful variable to illustrate the tied to corresponding counts.
    counts_for_tied = min_count
    # There we create Tie-resolving rule.
    # initialise: there we want to loop starting from pre_level =1  which means from the second preference.
    pref_level = 1
    # we need to keep comparing if we always satisfy : there still exists ties after we run the tie-resolving rule.
    # but we cannot run all the time if we cannot reduce all the ties so our looping step can't exceed the number of preference.
    
    if len(tied) == 1: # no ties' situation
        return tied[0]
    
    else:
    
        while len(tied) > 1 and pref_level < num_prefs:
        
        
            cand, count = bd.count_votes(ballots, preference=pref_level)
            # we want to a generalized method too: if we set the argument sort_by = " count" which means the candidates and their counts can't correspond
            # cani= [1, 2, 3, 4, 5, ...] one to one mapping the counts ( the index of the candi = the candi value of corresponding index = the count value of correspnding index)
            # so if we know the count, we can catch the corresponding the candidate.
        
        
        
            # Then we create the dictionary for cand and count
            # initialise 
            cand_count = {}
            # we want to loop the indices of the cand_count we can use the range(len(cand)) because of the length of cand_count and can are the same.
            for i in range(len(cand)):
                cand_count[cand[i]] = count[i]
                # we know the length of count = the length of the cand and we already get the value of the count,
                # and so we don't need to update the value by manually.
            
            
            # we want to extract the next step's candidates and ties
            # Next to solve this we will store them in a dictionary.
            cand_tied_counts_dict = {}
            # there we want to catch:  only keep the tied candidates, and check their counts

            for i in range(len(tied)): 
                keys = [ key for key in cand_count.keys() if key == tied[i]]
                num_items_of_dic = len(keys) # you also can usethe numbers of the items in cand_tied_counts_dict are the same as in keys(extracted)
            
                # find the corresponding value from for each key in keys and store them in cand_tied_counts_dict
                for j in range(num_items_of_dic):
                    cand_tied_counts_dict[keys[j]] = cand_count[keys[j]]
        
        
            # To check whether or not they are still tied, we can catch any number(for the keys(candidates) corresponding values) from the candi_tied_counts_dict
            # if the any number is equal to the left numbers -> these candidates exits tied.( but the number of the ties may be reduced or still unchanged)
            # if the any number isn't equal to the left numbers -> these candidates are not tied.
        
            # There, we use min function simply to catch a value from the tied_counts dictionary to check whether or not  they are the same.
            min_count = min(cand_tied_counts_dict.values())
        
            # How do we know matching result ( the number of matching):
            # firstly we can use logical operation to get their boolen values and sum up to get the macthcing numbers 
            # Secondly, we can first catch which the items are match the number and store them in a list, and finally calculate the 
            tied = [c for c, v in cand_tied_counts_dict.items() if v == min_count]
            
            
            # check whether or not elimination progress is finished means the elements in tied is only one.
            if len(tied) == 1:
                return tied[0]
            
            pref_level += 1 # update : going the the next preference to resolve.
        
        # if still tied, eliminate the smallest candidate number
    return min(tied)




def run_election(ballots, display=False):
    '''
    
    Method:
    1. Call `eliminate_next(ballots)` to determine the candidate with the fewest first-choice votes.
    2. Add this candidate to the `eliminated` list.
    3. Call `update_ballots(ballots, candidate)` to remove this candidate from all ballots.
    4. If `display=True`, it is optional to call `vote_transfers()` to show how the ballots are redistributed.
    When there is only one candidate remaining that has not been eliminated, this candidate is declared the winner.
    
    Outputs:
    -------
    winner : 
        (int)
        The final result of the remaining candidates' numbers (counting from 1) - that is, the winner of the election.
        If the final candidate 1 is left so that candidate 1 is the winner.
        
    eliminated : 
        (np.ndarray) 
        A 1D NumPy array vector or you can write a list listing candidates in the order they were eliminated.
        The length of this array is  (number of candidates - 1). The total number of the candidates - the number of the candidates eliminated.
    
    
    '''
    
    # tally all the number of the candidates:
    num_candidates = ballots.shape[1] # using shape to get the attribute of the array ballots 1 represents column
    # we store the according to the looping order when I search for who is prepared to be eliminated, we eliminate an candidate I store it in the list
    eliminated_candidates = []
    #  tally all the number of the candidates are eliminated.
    num_eliminated_candidates = len(eliminated_candidates)
    # set a separated ballots as the election initial value, at the same time we shouldn't break the original data for ballots
    # because we will update the ballots for each stage after the candidate is eliminated before we go to the next stage.
    current_ballots = ballots.copy()
    
    # the left number of the candidates who aren't eliminated.
    left_num_candidates = num_candidates - num_eliminated_candidates
    
    # Continue until only one candidate remains: we must eliminate the candidates until we have one left
    while left_num_candidates > 1:
        
        # using the eliminate_next function to find who to eliminate
        elim_candi = eliminate_next(current_ballots)
        # eliminated_candidates as a list we can using append attribute to push a new candidate on the last term which matches the next position corresponding to the new 
        # , eliminated candidate chosen.
        # update the eliminated candidate for each stage.
        eliminated_candidates.append(elim_candi)
        
        previous_ballots = current_ballots.copy()
        
        # Update ballots for next round ( after we eliminate the candidate )
        current_ballots =update_ballots(current_ballots, elim_candi)
        
        
        left_num_candidates = num_candidates - num_eliminated_candidates
        
        # Optional display of vote transfers
        # there if argument display is equal to True: we want to see the transfers result for each stage after we eliminate the candidate
        if display:
            vote_transfers(previous_ballots=previous_ballots, updated_ballots=current_ballots)
            
            
    
    # there we want to return the final result and set eliminated_candidates as an Numpy vector.
    return winner, np.array(eliminated_candidates)



