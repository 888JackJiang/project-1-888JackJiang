import numpy as np


def generate_ballots(votes=100, total_candidates=5, target_results=[32, 28, 21, 13, 6]):
    '''
    Generate random ballot data given a total number of ballots (votes),
    a total number of candidates, and a target probability distribution
    of preferences.
    The probabilities are randomly attributed to each candidate for each
    level of preference.
    
    Returns a NumPy array with shape (votes, candidates), where each row
    is one ranked-choice ballot for one voter, and each column corresponds
    to one candidate.
    '''
    # Initialise a random number generator
    rng = np.random.default_rng()
    
    # Set target probabilities for each stage (normalised)
    prob = np.array(target_results, dtype=float)
    prob = np.tile(prob, (total_candidates, 1))
    # shuffle probabilities so they're applied differently for each rank; add some noise too
    prob = np.abs(rng.permuted(prob, axis=1) + rng.normal(scale=2, size=prob.shape))
    
    # Create an empty array to store the ballots
    ballots = np.zeros((votes, total_candidates), dtype=int)
    
    # Create each ballot one after the other
    for v in range(votes):
        # Voter ranks at most "total_candidates" candidates; introduce "stages" for clarity
        stages = total_candidates
        for r in range(stages):
            
            # Generates rth preference for an arbitrary candidate (use normalised probabilities)
            chosen_candidate = rng.choice(total_candidates, p=prob[r, :]/prob[r, :].sum()) + 1
            
            if chosen_candidate in ballots[v]:
                # Arbitrarily decide that voter is done if they choose the same candidate twice,
                # i.e. if chosen_candidate has already been placed in row v
                break
            else:
                # If they hadn't previously chosen that candidate, choose it as rth preference (r indexes from 0)
                ballots[v, r] = chosen_candidate
    
    return ballots


def ballot_selector(ballots, candidate, preference=0):
    '''
    Returns a selector for all ballots which have ranked a given candidate at a given preference.
    '''
    return ballots[:, preference] == candidate






def count_votes(ballots, preference=0, sort_by='count'):
    """
    Count how many votes each candidate gotten at a given preference level.
    for example, when preference =0, we are counting the first preference votes for each candidate
    we get a list for which voters do that candidate as their first preference may be like [ True, False, False, True, ....]
    and the according to the True values we get the total number of first preference votes for that candidate
    
    Input:
    ballots :
        (np.ndarray)
        2 dimension array, where each row represents one ballot, and each column represents one candidate.
        Non-zero values indicate the ranking given by the voter (1st place, 2nd place, 3rd place, etc.) 。
    preference : 
        (int) the default value is 0
        The preference rank (0 = first preference, 1 = second preference, etc.)
    sort_by : 
        (str) the default value is "count"  An alternative is "candidate"
        'count' represents sort candidates by number of votes ( which is increasing direction)
        'candidate' represents sort by candidate number (which is also increasing direction)
    
    Output:
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
    vote_counts = np.zeros(num_candidates, dtype=int) # the final result of vote_count should be integer.


    # Count how many ballots ranked each candidate at the given preference level
    for i in candidates:  
        
        # create the selector to filter  result for candidate i at the given preference level  to find which voters 
        selector = ballot_selector(ballots, candidate=i, preference=preference) 
        vote_counts[i - 1] = sum(selector)
            
        
    # Store in a dictionary key is the candidate number, value is the corresponding vote count
    cadi_vote_dict = {candidates[i]: vote_counts[i] for i in range(num_candidates)} # range ( num_candidates to create the index for looping)

    #  sort the vote_ counts and candidate with specified method(order).
    if sort_by == 'count':
        # we need to sort the vote_counts( which is the values from the dictionary) firstly in ascending order
        sorted_vote_counts = sorted(cadi_vote_dict.values())  # ascending by number of votes
        
        # set the initial empty list to store the corresponding candidate number after sorting
        sorted_candidates =[]
        # create a one-to-one mapping from vote count to candidate
        for i in range(len(sorted_vote_counts)):
            current_value = sorted_vote_counts[i]
            # With the default sorting by 'count', when there are tied candidates with the same number of votes, you can return them in any order in candidates
            # there we test the newest one whether or not equal to the next one.
            
            if i < len(sorted_vote_counts)-1: # ensure that we cannot move outside the sorted_vote_counts when we are checking the next item.
                if current_value == sorted_vote_counts[i+1]: 
                
                    # if same we donn't consider it because we have already added the candidate number for the next one
                    continue 
            
            ###### why we do the step before avoid appending many times below.######
            
            # loop through the dictionary to find the corresponding candidate number
            for key, value in cadi_vote_dict.items():   # key and value for finding each tuple in cadi_vote_dict.items()
                if value == current_value:
                    sorted_candidates.append(key)
        
        

    # This is the reverse process above we need to sort candidate firstly
    else:  # sort_by == 'candidate'
        
        # the same operation as above to handle the tie situation  we use the reverse direction: let us sort the candidates( the keys)
        # and find the corresponding vote counts( the values)
        sorted_candidates = sorted(cadi_vote_dict.keys()) 
        sorted_vote_counts =[]
        # Here we delete the process to deal with the situation which two candidates are the same because candidate numbers are unique
        for i in range(len(sorted_candidates)):
            current_key = sorted_candidates[i]
            # loop through the dictionary to find the corresponding count_vote number (the value)
            for key, value in cadi_vote_dict.items():   # key and value for finding each tuple in cadi_vote_dict.items()
                if key == current_key:
                    sorted_vote_counts.append(value)
        
        
    candidates = sorted_candidates
    vote_counts = sorted_vote_counts
    return candidates, vote_counts








