import numbers
import collections
import itertools

from python_toolbox import nifty_collections
from python_toolbox import cute_iter_tools

infinity = float('inf')


###############################################################################

_length_of_recurrent_perm_space_cache = {}

def calculate_length_of_recurrent_perm_space(k, ftt):
    cache = _length_of_recurrent_perm_space_cache
    if not isinstance(ftt, nifty_collections.FrozenTallyTally):
        ftt = nifty_collections.FrozenTallyTally(ftt)
    if k == 0:
        return 1
    elif k == 1:
        assert ftt
        # (Works because `FrozenTallyTally` has a functioning `__bool__`,
        # unlike Python's `Counter`.)
        return ftt.n_elements
    try:
        return cache[(k, ftt)]
    except KeyError:
        pass
    
    levels = []
    current_ftts = {ftt}
    while len(levels) < k and current_ftts:
        k_ = k - len(levels)
        levels.append(
            {ftt_: ftt_.get_sub_ftts_for_one_crate_removed()
             for ftt_ in current_ftts
                          if (k_, ftt_) not in cache}
        )
        current_ftts = set(itertools.chain(*levels[-1].values()))
        
    # The last level is calculated. Time to make our way up.
    for k_, level in enumerate(reversed(levels), (k - len(levels) + 1)):
        if k_ == 1:
            for ftt_, sub_ftt_tally in level.items():
                cache[(k_, ftt_)] = ftt_.n_elements
        else:
            for ftt_, sub_ftt_tally in level.items():
                cache[(k_, ftt_)] = sum(
                    (cache[(k_ - 1, sub_ftt)] * factor for
                           sub_ftt, factor in sub_ftt_tally.items())
                )
    
    return cache[(k, ftt)]
        
    


###############################################################################

_length_of_recurrent_comb_space_cache = {}

def calculate_length_of_recurrent_comb_space(k, ftt):
    cache = _length_of_recurrent_comb_space_cache
    if not isinstance(ftt, nifty_collections.FrozenTallyTally):
        ftt = nifty_collections.FrozenTallyTally(ftt)
    if k == 0:
        return 1
    elif k == 1:
        assert ftt
        # (Works because `FrozenTallyTally` has a functioning `__bool__`,
        # unlike Python's `Counter`.)
        return ftt.n_elements
    try:
        return cache[(k, ftt)]
    except KeyError:
        pass
    
    levels = []
    current_ftts = {ftt}
    while len(levels) < k and current_ftts:
        k_ = k - len(levels)
        levels.append(
            {ftt_: ftt_.get_sub_ftts_for_one_crate_and_previous_piles_removed()
             for ftt_ in current_ftts
                                                    if (k_, ftt_) not in cache}
        )
        current_ftts = set(itertools.chain(*levels[-1].values()))
        
    # The last level is calculated. Time to make our way up.
    for k_, level in enumerate(reversed(levels), (k - len(levels) + 1)):
        if k_ == 1:
            for ftt_, sub_ftts in level.items():
                cache[(k_, ftt_)] = len(sub_ftts)
        else:
            for ftt_, sub_ftts in level.items():
                cache[(k_, ftt_)] = sum(
                    (cache[(k_ - 1, sub_ftt)] for sub_ftt in sub_ftts)
                )
    
    return cache[(k, ftt)]
        
    
            
