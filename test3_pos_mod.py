




def positional_voting(ballots, weights):
    
    
    '''
    the core method:  Count the number of first, second and third votes received by each candidate respectively,and multiply each count by the corresponding weight.
    Sum up all the data - the candidate with the highest total votes wins.
    
    This function will count the number of times each candidate appears at each preference position (first, second, third, etc.), 
    multiply these counts by the corresponding weights, and then sum up the results of all preference levels to obtain the total score for each candidate. 
    the candidates will be sorted in corresponding order based on their total scores.
    
    
    Input:
        ballots ( np.ndarray)
        A 2D NumPy array which is a matrix representing all the ballots submitted by voters.
        each row represents one ballot submitted by one voter;
        each non-zero value represents a candidate;
        each column represents a preference rank, from first to last preference going left to right, for example a 2 in the first column means that Candidate 2 was the voter's first preference;
    
        weights : (list) that the element is float defining the weight for specified preference the fist index to the value of list corresponding to the first preference, 
        the second index to the value of list corresponding to the second preference ( one to one mapping).
        
        
    Output:
        candidates (np.ndarray) A Numpy vector
        An array of candidate IDs sorted by the total weighted score (in an increasing order). The candidate with the highest score is placed at the end.
        points     (np.ndarray) A Numpy vector
        A NumPy array consisting of the corresponding total weighted scores for each candidate, arranged in the same order as "candidates".(one to one  corresponding order)
        
    '''


    # Number of candidates is given by the number of columns in ballots 
    num_candidates = ballots.shape[1] # using shape to get the attribute of the array ballots 1 represents column
    # initialise the score for each candidate at each preference level , so we create a 2D array(matrix)
    # the impotant thing is column represent candidate number specified order : candidate 1, candidate 2, ..., candidate n
    score_pre_candi = np.zeros((len(weights), num_candidates))  # row represents preference level, column represent candidate number
    # initialise the total scores for each candidate
    total_scores = np.zeros(num_candidates)  
    
    # create the dictionary for  because we need to loop through weights with their corresponding preference level for each loop (we need to calculate the scores for all the candiates)
    weights_dict = {}
    # we create the key as preference level 0,1,2,... and value as corresponding weight from weights list
    index = 0 
    for w in weights:
        weights_dict[index] = w
        index += 1

    # Now loop through the weights_dict to get each preference and its corresponding weight
    for preference, weight in weights_dict.items():
        # Count how many votes each candidate got at specific preference
        candidates, counts = bd.count_votes(ballots, preference=preference, sort_by='candidate') # we need to sort by candidate to ensure the counts correspond to the candidates correctly
        # we loop the index j for total_scores j from 0 to len(candidates)-1
        # we loop from each row of the matrix ( nrow is the number of element in wights) from 0 to len(wights)-1,
        
            # we get the weight for each preference level for all candidates stored in the row i
            # Because  we loop through preference from 0 to len(weights)-1 so we can use preference as the index for row
        i = preference
        for j in range(len(candidates)):  # range(len(candidates) to create the index for looping from 0 to len(candidates)-1
            # accumulate the total scores for each candidate
            score_pre_candi[i,j] += counts[j] * weight
                
                
                
    # let we calculate the total scores for each candidate from the score_pre_candi
    # the core idea is to sum up each cloumn in score_pre_candi to get the total scores for each candidate
    for i in range(num_candidates):     # loop according to the number of candidates corresponding to the number of columns
        total_scores[i] = np.sum(score_pre_candi[:, i])

    
    # Store in a dictionary key is the candidate number, value is the corresponding vote count
    # we already specified the candidate number in bd.count_votes function above.
    cadi_total_scores_dict = {candidates[i]: total_scores[i] for i in range(num_candidates)} # range ( num_candidates to create the index for looping)

    sorted_total_scores= sorted(cadi_total_scores_dict.values())  # ascending by number of totals scores.
    
    
        
        # set the initial empty list to store the corresponding candidate number after sorting
    sorted_candidates =[]
        # create a one-to-one mapping from vote count to candidate
    for i in range(len( sorted_total_scores)):
            # for each vote count to get the corresponding value in dictionary
            current_value = sorted_total_scores[i]
            
            if i < len(sorted_total_scores)-1: # ensure that we cannot move outside the sorted_total_scores when we are checking the next item.
                # check for the repeated situation for scores.
                if current_value == sorted_total_scores[i+1]: 
                
                    # if same we donn't consider it because we have already added the candidate number for the next one
                    continue 
    
                # loop through the dictionary to find the corresponding candidate number
            for key, value in cadi_total_scores_dict.items():   # key and value for finding each tuple in cadi_total_scores_dict.items()
                if value == current_value:
                    sorted_candidates.append(key)
    # store all the sorted result into NumPy vector 
    
    candidates = np.array(sorted_candidates)
    points =np.array(sorted_total_scores)
    return candidates, points




