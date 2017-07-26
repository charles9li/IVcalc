from math import ceil, floor


def display_iv():
    """Prompts information and displays the possible IVs of a pokemon."""
    # Prompts pokemon species and looks up base stat information
    base_stat_list = pokemonList[input('Enter species name: ').lower()]
    # Prompts nature and looks up multiplier information
    nature = natureList[input('Enter nature: ').lower()]
    # Prompts level
    lvl = int(input('Enter level: '))
    # Prompts user to input stats
    stat_list = stat_input()
    # Promputs user to input EVs (if necessary)
    ev_list = ev_input()
    # Displays possible IVs
    old_lower_list, old_upper_list = iv_estimate_output(base_stat_list, nature, lvl, stat_list, ev_list)
    while input('Further input? [y/n] ').lower() == 'y':
        lvl = int(input('Enter level: '))
        stat_list = stat_input()
        ev_list = ev_input()


def iv_estimate_output(base_stat_list, nature, lvl, stat_list, ev_list):
    """Displays possible IV values and returns lower and upper bound lists."""
    lower_bound_list, upper_bound_list = [], []
    for i in range(0, 6):
        lower_bound, upper_bound = calc_iv_range(stat_str(i), base_stat_list[i], lvl, stat_list[i], nature, ev_list[i])
        lower_bound_list.append(lower_bound)
        upper_bound_list.append(upper_bound)
        print(stat_str(i) + ':', list(range(lower_bound, upper_bound + 1)))
        next_lvl = ' '
        if len(list(range(lower_bound, upper_bound + 1))) > 1:
            next_lvl = next_helpful_lvl(lower_bound, upper_bound, stat_str(i), base_stat_list[i], lvl, nature, ev_list[i])
        print('Next helpful level:', next_lvl)
    return lower_bound_list, upper_bound_list


def stat_input():
    """Prompts user to input stat values and returns a list of the inputted values."""
    stat_list = []
    for i in range(0, 6):
        stat_list.append(int(input('Enter ' + stat_str(i) + ' stat: ')))
    return stat_list


def ev_input():
    """Prompts user to input EVs and returns a list of the inputted EVs."""
    ev_list = []
    if input('EV input? [y/n] ').lower() == 'y':
        for i in range(0, 6):
            ev_list.append(int(input('Enter number of ' + stat_str(i) + ' EVs: ')))
    else:
        ev_list = [0] * 6
    return ev_list


def next_helpful_lvl(lower_bound, upper_bound, stat, base_stat, lvl, nature, ev=0):
    """Returns the next helpful level to narrow the IV range for a specified stat."""
    i = lvl
    while i < 100:
        i += 1
        if stat_calc(stat, base_stat, i, nature, lower_bound, ev) != stat_calc(stat, base_stat, i, nature, upper_bound, ev):
            return i
    return i
            

def calc_iv_range(stat, base_stat, lvl, stat_value, nature, ev=0):
    """Calculates the lower and upper bounds for the IV of a specified stat."""
    # Determines the multiplier for the given stat
    nature_multiplier_stat = nature_multiplier(nature, stat)
    lower_bound = 0  # Sets lower bound
    upper_bound = 31 # Sets upper bound
    # If the stat is HP
    if stat_index(stat) == 0:
    	lower_bound = (stat_value - lvl - 10) * 100 / lvl - 2 * base_stat - ev / 4
    	upper_bound = (stat_value - lvl - 9) * 100 / lvl - 2 * base_stat - ev / 4
    # If the stat is not HP
    else:
        i = 31
        while i >= 0:
            if stat_calc(stat, base_stat, lvl, nature, i, ev) == stat_value:
                lower_bound = i
            i -= 1
        while i <= 31:
            if stat_calc(stat, base_stat, lvl, nature, i, ev) == stat_value:
                upper_bound = i
            i += 1
    # Rounds up lower IV estimate and rounds down upper IV estimate
    lower_bound = ceil(lower_bound)
    upper_bound = floor(upper_bound)
    # Makes sure lower IV estimate is between 0 and 31 (inclusive)	
    if lower_bound < 0:
    	lower_bound = 0
    elif lower_bound > 31:
    	lower_bound = 31
    # Makes sure upper IV estimate is between 0 and 31 (inclusive)
    if upper_bound < 0:
    	upper_bound = 0
    elif upper_bound > 31:
    	upper_bound = 31
    return lower_bound, upper_bound # Returns lower and upper IV estimate


def stat_calc(stat, base_stat, lvl, nature, IV, ev=0):
    """Returns the stat of a pokemon."""
    # If the stat is HP
    if stat_index(stat) == 0:
        return floor((2 * base_stat + IV + ev / 4) * lvl / 100) + lvl + 10
    # If the stat is not HP
    else:
        return floor((floor((2 * base_stat + IV + ev / 4) * lvl / 100) + 5) * nature_multiplier(nature, stat))


def nature_multiplier(nature, stat):
    """Returns the multiplier for stat given the nature input."""
    return nature[stat_index(stat)]


def stat_index(stat):
    """Returns the index number for a stat."""
    if stat.lower() == 'hp ':
        return 0
    elif stat.lower() == 'atk':
        return 1
    elif stat.lower() == 'def':
        return 2
    elif stat.lower() == 'spa':
        return 3
    elif stat.lower() == 'spd':
        return 4
    elif stat.lower() == 'spe':
        return 5


def stat_str(index):
    """Returns stat string correpsonding to the index.
    This function is used in other functions.
    """
    if index == 0:
        return 'HP '
    elif index == 1:
        return 'ATK'
    elif index == 2:
        return 'DEF'
    elif index == 3:
        return 'SPA'
    elif index == 4:
        return 'SPD'
    elif index == 5:
        return 'SPE'


"""List of natures and respective stat multipliers."""
hardy = 	[1, 1, 1, 1, 1, 1]
lonely = 	[1, 1.1, .9, 1, 1, 1]
adamant = 	[1, 1.1, 1, .9, 1, 1]
naughty = 	[1, 1.1, 1, 1, .9, 1]
brave = 	[1, 1.1, 1, 1, 1, .9]
bold = 		[1, .9, 1.1, 1, 1, 1]
docile = 	hardy
impish = 	[1, 1, 1.1, .9, 1, 1]
lax = 		[1, 1, 1.1, 1, .9, 1]
relaxed = 	[1, 1, 1.1, 1, 1, .9]
modest = 	[1, .9, 1, 1.1, 1, 1]
mild = 		[1, 1, .9, 1.1, 1, 1]
bashful = 	hardy
rash = 		[1, 1, 1, 1.1, .9, 1]
quiet = 	[1, 1, 1, 1.1, 1, .9]
calm = 		[1, .9, 1, 1, 1.1, 1]
gentle = 	[1, 1, .9, 1, 1.1, 1]
careful = 	[1, 1, 1, .9, 1.1, 1]
quirky = 	hardy
sassy = 	[1, 1, 1, 1, 1.1, .9]
timid = 	[1, .9, 1, 1, 1, 1.1]
hasty = 	[1, 1, .9, 1, 1, 1.1]
jolly = 	[1, 1, 1, .9, 1, 1.1]
naive = 	[1, 1, 1, 1, .9, 1.1]
serious = 	hardy

natureList = {}
natureList['hardy'] = hardy
natureList['lonely'] = lonely
natureList['adamant'] = adamant
natureList['naughty'] = naughty
natureList['brave'] = brave
natureList['bold'] = bold
natureList['docile'] = docile
natureList['impish'] = impish
natureList['lax'] = lax
natureList['relaxed'] = relaxed
natureList['modest'] = modest
natureList['mild'] = mild
natureList['bashful'] = bashful
natureList['rash'] = rash
natureList['quiet'] = quiet
natureList['calm'] = calm
natureList['gentle'] = gentle
natureList['careful'] = careful
natureList['quirky'] = quirky
natureList['sassy'] = sassy
natureList['timid'] = timid
natureList['hasty'] = hasty
natureList['jolly'] = jolly
natureList['naive'] = naive
natureList['serious'] = serious


"""List of pokemon and base stats."""
pokemonList = {}
pokemonList['venusaur'] =   [80, 82, 83, 100, 100, 80]
pokemonList['magikarp'] =   [20, 10, 55, 15, 20, 80]
pokemonList['torchic'] =    [45, 60, 40, 70, 50, 45]
pokemonList['salamence'] =  [95, 135, 80, 110, 80, 100]
pokemonList['larvesta'] =   [55, 85, 55, 50, 55, 60]