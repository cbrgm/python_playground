# Challenge 4. Good vs Evil
# Good: Hobbits - 1, Men - 2, Elves - 3, Dwarves - 3, Eagles - 4, Wizards - 10
# Evil: Orcs - 1, Men - 2, Wargs - 2, Goblins - 2, Uruk Hai - 3, Trolls - 5, Wizards - 10
# Input the count of each parameter and output the result of the battle

def goodVsEvil(good, evil):
    result = {'good': 'Battle Result: Good triumphs over Evil', 
              'evil': 'Battle Result: Evil eradicates all trace of Good',
              'tie': 'Battle Result: No victor on this battle field'}
    good_value = [1,2,3,3,4,10]
    evil_value = [1,2,2,2,3,5,10]
    good_sum = sum([int(x)*y for x, y in zip(good.split(), good_value)])
    evil_sum = sum([int(x)*y for x, y in zip(evil.split(), evil_value)])

    if good_sum > evil_sum:
        return result['good']
    elif good_sum < evil_sum:
        return result['evil']
    else:
        return result['tie']