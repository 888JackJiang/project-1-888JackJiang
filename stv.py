import numpy as np
import ballot_data as bd



######    I write the run_election function in the final function ############





###### generalization for update_d ballots when there exists to_eliminate and multi-candidates'election situation base original update_ballots.


def update_ballots(ballots, to_eliminate, elected):
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
    elected:
        (list) :
        in the stage for elimination elected is as a list storing all the elections.
        
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

    # give the updated_ballots an initial value ballots and don't break the value of ballots using copy().
    # updated_ballots = np.zeros((n_rows,n_cols ))
    
    updated_ballots = ballots.copy()
    # record all the candidates:
    
    
    
    if to_eliminate != []:
        
        if  len(elected)!= 0 :
            list =elected.copy()
            list.append(to_eliminate)
        
            for i in range(n_rows):

            # to find the index for each row where is the elimination candidate.
    
            # in the row_i find the exact column index for candidate = to_eliminate
                where_to_elimination = []
            
                for r in range(n_cols):
                    if pre_updated_ballots[i,:][r] in list:
                        where_to_elimination.append(True)
                    else:
                        where_to_elimination.append(False)    
                
            # elimination_index_list= [k for k in range(n_cols )  if where_to_elimination[k]==True   ]
        
        
            # extract the value corresponding to no elimination and elected for each row:
        
           
                
                
                elimination_index_list= [k for k in range(n_cols )  if where_to_elimination[k]==True ]
            # to prove we have elimination_index items:
                if len(elimination_index_list) != 0:
            
    
                    m=0 # shift times
                    for c in range(len( elimination_index_list)) :
                    
                        elimination_index = elimination_index_list[c]
                        
                    # create a new vector or list for using each row_i from the index to the end, finally we add an extra zero.
                    # we need the shifted ones' vector staring from the next candidate(eliminated).
                        new_row = pre_updated_ballots[i,elimination_index+1:n_cols]
                    # cover the original position: left shift one.
                        updated_ballots[i,(elimination_index):(n_cols-1)] = new_row
                        updated_ballots[i,n_cols-1-m] = 0
                        m+=1

   
    elif  len(elected) == 0:
        
        for i in range(n_rows):

            # to find the index for each row where is the elimination candidate.
    
            # in the row_i find the exact column index for candidate = to_eliminate
            where_to_elimination = []
            # we don't need append here because to_eliminate is empty.
            list = elected
            for r in range(n_cols):
                if pre_updated_ballots[i,:][r] in list:
                    where_to_elimination.append(True)
                else:
                    where_to_elimination.append(False )        
                
            # elimination_index_list= [k for k in range(n_cols )  if where_to_elimination[k]==True   ]
        
        
            # extract the value corresponding to no elimination and elected for each row:
        
       #     for p in range(len(where_to_elimination)):
      #          updated_ballots[i,p] = where_to_elimination[p]
            elimination_index_list= [k for k in range(n_cols )  if where_to_elimination[k]==True ]
            # to prove we have elimination_index items:
            if len(elimination_index_list) != 0:
                m=0
                for c in range(len( elimination_index_list)) :
                    
                        elimination_index = elimination_index_list[c]
                        elimination_index = elimination_index -m 
                    # create a new vector or list for using each row_i from the index to the end, finally we add an extra zero.
                    # we need the shifted ones' vector staring from the next candidate(eliminated).
                        new_row = pre_updated_ballots[i,(elimination_index+1):(n_cols)]
                    # cover the original position: left shift one.
                        updated_ballots[i,elimination_index:(n_cols -1)] = new_row
                        updated_ballots[i,n_cols-1-m] = 0
                        m+=1

    
    elif    to_eliminate  == []:
        
            pre_updated_ballots = ballots.copy() # create a copy of the original ballots to avoid modifying it directly

            n_rows = pre_updated_ballots.shape[0] # we get the number of the rows
            n_cols = pre_updated_ballots.shape[1] # we get the number of the columns

            # give the updated_ballots an initial value ballots and don't break the value of ballots using copy().
            updated_ballots = ballots.copy()
            where_to_elimination = []
            for i in range(n_rows):

            # to find the index for each row where is the elimination candidate.
                
                #  where_to_elimination = pre_updated_ballots[i,:]== elected
                
                for j in range(n_cols):
                    
                    for k in range(len(elected)):
                        
                        if pre_updated_ballots[i,j] == elected[k]:
                            where_to_elimination.append(True)
                        else:
                            where_to_elimination.append(False)
                
                
                # in the row_i find the exact column index for candidate = to_eliminate
        
                elimination_index_list= [k for k in range(n_cols )  if where_to_elimination[k]==True ]
        
                if len(elimination_index_list) != 0:
                    elimination_index = elimination_index_list[0]
                    # create a new vector or list for using each row_i from the index to the end, finally we add an extra zero.
                    # we need the shifted ones' vector staring from the next candidate(eliminated).
                    new_row = pre_updated_ballots[i,(elimination_index+1):(n_cols)]
                    # cover the original position: left shift one.
                    updated_ballots[i,elimination_index:(n_cols -1)] = new_row
                    updated_ballots[i,n_cols-1] = 0
            
                # if == 0 we don't do any change.
            
    

    # After the whole looping we get the updated_ballots
    return updated_ballots # as the generalization situation.


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
            discarded_prev += 1 # update the value find the row is 0 (discarded) plus1
            
            
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


def eliminate_next(ballots,vote_diffs,quota,election):
    
    '''
    Determine which candidate should be eliminated next in an Instant Runoff Voting (IRV) round.
    there we consider the situation which we have no ties or ties.
    As a generalization situation for eliminate_next

    Input:
    ----------
    ballots : 
    (Numpy array)
    This is a two-dimensional NumPy array, where each row represents the ranking preference of a voter (each column corresponds to a candidate number).
    election : a list which is the status of elected candidates.
    vote_diffs: the difference of the candidates in the first preference.
    quota：
        (int) the quota is calculate by     quota = (num_votes // (seats + 1)) + 1 already
    
    Output :
    -------
    to_eliminate
    (int)
    The numbers of the candidates to be eliminated next (starting from 1) are determined based on the fewest votes they received in their first choice.
    In case of a tie, the subsequent ballots (second, third, etc.) will be checked one by one.
    If there is still a tie, the candidate with the smallest number will be eliminated.
    
    elections
    list
    a list storing candidates may be elected about many candidates.
    
    '''
    
    
    
    num_prefs = ballots.shape[1]   # total number of preference columns
    # we firstly run the first-preference situation( may be including the ties)
    candidates, counts = bd.count_votes(ballots, preference=0)
    
    
    
    
    #####!!!!!  the counts should add the changes before to update the count for the candidates who didn't be elected (after surplus transfers )
    counts = counts + vote_diffs
    # store candidate counts as a dictionary
    
    

    
    ### firstly we want to eal with zero situation.
    
    cand_counts = {}
            # we want to loop the indices of the cand_count we can use the range(len(candidates)) because of the length of cand_count and can are the same.
    for i in range(len(candidates)):
        #!!!! because we need to extract the candidate for no valid in the ballots(including removing)!!!
        if  counts[i] != 0 :
            cand_counts[candidates[i]] = counts[i]
        
        # now when counts[i] == 0 is True which means the first preference has zero votes for some candidate.
        Num_row_include_candidate_i = 0
        for k in range(num_prefs):
        # for j in range(ballots.shape[0]):
            Num_row_include_candidate_i += len(ballots[bd.ballot_selector(ballots, candidate=candidates[i], preference=k)])
        
        # !!!! to check whether or not other preference has this candidate to be eliminated in the following process though no candidate i in first preference.
        if counts[i] == 0 and Num_row_include_candidate_i != 0 :
            to_eliminate = candidates[i]
            elections = []
            return to_eliminate,  elections

  
    
    ##### !!!! generalization this process.##########!!!!!!!
    # ensure that: in this stage we have surplus candidate:
    candi_larger_quota=[]
    for i in range(len(counts)):
        if counts[i]>= quota:
            candi_larger_quota.append(candidates[i])
    
    
    if len(candi_larger_quota) > len(election):
        
        elections = candi_larger_quota
        to_eliminate = []
        return to_eliminate, elections
    
    
    
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
        elections = election
        return tied[0], elections
    
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
                #!!!! because we need to extract the candidate for no valid in the ballots(including removing)!!!
                if  count[i] != 0 :
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
                elections = election
                return tied[0], elections
            
            pref_level += 1 # update : going the the next preference to resolve.
    
    
        # if still tied, eliminate the smallest candidate number
        
    elections = election
    to_eliminate = min(tied)
    return to_eliminate, elections








def run_election_stv(ballots, seats, display=True):
    
    
    # the number of the rows and column of the ballots.
    num_votes, num_candidates = ballots.shape
    
    quota = (num_votes // (seats + 1)) + 1
    
    
    eliminated = []
    
    # start with weight 1 per ballot
    weights = np.ones(num_votes)  
    
    current_ballots = ballots.copy()
    # set the initial values for elections
    elections = []
    # set the initial values for vote_differs for the first preference.
    vote_differs = [0 for i in range(num_candidates )]
    
    
    # we want clear up the current_ballots, remove all the cases for candidate whose first preference votes are zero.
    # update the ballots until we clear all of them.
    while len(elections)==0:
            
        to_eliminate,elections = eliminate_next(current_ballots ,vote_differs ,quota, election=elections)
        current_ballots = update_ballots(ballots = current_ballots, to_eliminate=to_eliminate , elected = elections)
        eliminated.append(to_eliminate)
    
    
    # the state of the stage.
    # Initialize.
    stage = 0
    
    while len(elections) < seats:
        
        ########## surplus stage #####################
        #### here we transfer all the candidates in the election whose surplus.
        # Count first-preference votes
        candidates, vote_count = bd.count_votes(current_ballots, preference=0, sort_by='candidate')
        
        to_eliminate,elections = eliminate_next(current_ballots ,vote_differs ,quota, election=elections)
        
        # in this stage we don't need to give any value for to_eliminate
        to_eliminate= []
        # for each election we will go into a surplus stage:( because we have different weights)
        for i in elections:
            select = bd.ballot_selector(ballots = current_ballots, candidate=i, preference=0)
        
        
            # update the ballots for surplus stage( we start transfers)
            update_ballot= update_ballots(ballots = current_ballots[select], to_eliminate=to_eliminate , elected = elections)
        
        
            candidates, vote_diffs_update, discarded_diff = vote_transfers(previous_ballots = current_ballots[select], updated_ballots = update_ballot)
        
    
         
            num_candidate_i_election = current_ballots[select].shape[0]
            num_surplus = num_candidate_i_election - quota
            
            # calculate the weight for candidate i
            weight = num_surplus/ num_candidate_i_election
            vote_diffs_update_weight =  vote_diffs_update * weight
            # the record which stage,
            stage += 1
            if display:
                print(f'Stage {stage} surplus stage :{vote_transfers(previous_ballots=current_ballots[select], updated_ballots=current_ballots)}')
            # we accumulate all the vote_differs.
                vote_differs+= vote_diffs_update_weight
            
  
    where_vote_count_larger_quota =0       
    while where_vote_count_larger_quota < 1:
        # 3️ Redistribute eliminated candidate’s votes fully (weight = 1)
        
            
        
            # we use the ballots = current_ballots as the previous ballots. Then we start find the elimination candidate to run
            # the elimination stage.
            
            # firstly we want to find the elimination candidate.
            to_eliminated ,elect= eliminate_next(ballots= current_ballots, quota=quota, vote_diffs=vote_differs, election = elections)

            # secondly we want to update the ballot after we eliminate our candidate. 
            Elimination_stage_ballots= update_ballots(ballots= current_ballots, to_eliminate = to_eliminated, elected=elections)
           
            
            # update the eliminated.
            
            eliminated.append(to_eliminated)
            
            
            stage += 1
            
            if display :
                
                print(f'Stage {stage} Elimination stage: {vote_transfers(previous_ballots=current_ballots, updated_ballots=Elimination_stage_ballots)}')
                
            
            # update the current ballots after we finish the elimination stage
            current_ballots = Elimination_stage_ballots 
            
            # after we update our ballots, the we want to calculate the 
            candidates, vote_count = bd.count_votes(Elimination_stage_ballots, preference=0, sort_by='candidate')
            # consider the coincidence we update a candidate is just exact = quota.
            if np.sum(vote_count == quota)==seats:
                break

                # or we calculate the where vote_count > quota
            for i in range(len(vote_count)):
                if vote_count[i] > quota:
                
                    where_vote_count_larger_quota+=1
                    
            elections.append(candidates[i])
            
            
            
        
    elected = elections
    
    
    return elected, eliminated 
                
            
            
            






