


'''
the main idea:Each level has corresponding scores → Add up the scores of all candidates → The one with the highest score wins.
'''




'''

the main idea of IRV: The IRV (Instant Runoff Voting) method automatically conducts multiple elections. 
    In each round, the loser is eliminated, and the second-choice preferences of the voters are transferred to the next candidate.
    This process continues until one candidate obtains more than half of the remaining votes.

'''






def count_votes(ballots, preference=0, sort_by='count'):
    """
    Count how many votes each candidate received at a given preference level.
    
    Parameters
    ----------
    ballots : np.ndarray
        2D NumPy array, where each row = one ballot, and each column = one candidate.
        Non-zero entries indicate the rank (1st, 2nd, 3rd...) assigned by that voter.
    preference : 
        (int) the default value is 0
        The preference rank (0 = first preference, 1 = second preference, etc.)
    sort_by : str, default 'count'
        'count' → sort candidates by number of votes (ascending)
        'candidate' → sort by candidate number (ascending)
    
    Output
    candidates ( np.ndarray )
        return candidate numbers sorted according to the argument " sort_by"
    vote_counts (np.ndarray )
        return vote counts corresponding to each candidate( one to one ) which is sorted according to the  argument ''sorted by''
    """

    # Number of candidates is given by the number of columns in ballots
    num_candidates = ballots.shape[1] # using shape to get the attribute of the array ballots 1 represents column

    ## Initialise
    
    # we call the numbers for candidates ， an integer between 1 and the total number of candidates, corresponding to a particular candidate
    candidates = np.arange(1, num_candidates + 1) # we loop from 1 to num_candidates -> initialise the numbers of the looping
    # each （candidate-1） corresponds to an index in vote_counts.
    # for each candidate, we will count how many votes they received at the specified preference performance.
    vote_counts = np.zeros(num_candidates)



    # Count how many ballots ranked each candidate at the given preference level
    for i in candidates:  
        # create the selector to filter  result for candidate i at the given preference level  to find which voters 
        selector = ballot_selector(ballots, candidate=i, preference=preference) 
        vote_counts[i - 1] = np.sum(selector) 
            
        
    # Store in a dictionary key is the candidate number, value is the corresponding vote count
    cadi_vote_dict = {candidates[i]: vote_counts[i] for i in range(num_candidates)} # range ( num_candidates to create the index for looping)

    #  sort the vote_ counts and candidate with specified method(order).
    if sort_by == 'count':
        # we need to sort the vote_counts( which is the values from the dictionary) firstly in ascending order
        sorted_vote_counts = sorted(cadi_vote_dict.values())  # ascending by number of votes
        
    

    # This is the reverse process above we need to sort candidate firstly
    else:  # sort_by == 'candidate'
        sorted_candidates =  candidates # actually we crate the candidates in ascending order already
        # we have already corresponding vote_counts for each candidate already
        sorted_vote_counts = vote_counts
    return sorted_candidates, sorted_vote_counts






