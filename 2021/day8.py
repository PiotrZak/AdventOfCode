from collections import Counter, defaultdict
from os import set_inheritable
from typing import Dict, KeysView, List, ValuesView


with open('day8.txt') as f:
    file = [x for x in f.readlines()]

sol1 = 0

# for line in file:
#     print(line)
#     signals, output = line.split('|')
#     signals = [s.strip() for s in signals.split(' ')]  
#     output = [s.strip() for s in output.split(' ')] 

#     values = [set('cf'), set('bcdf'), set('acf'), set('abcdefg')]
#     values_length = [len(v) for v in values]    

#     for string in output:
#         characters = len(string)
#         if characters in values_length:
#             sol1+=1

# print (sol1)

#cf -> 2
#bcdf -> 4
#acf -> 3
#abcdefg -> 6

def infer_one_to_one_from_possibles(possibles):

    inferred = {}
    while len(possibles):
        # Find the item that only has one possibility associated with it and pull it out
        # of the possibles dictionary, and remove the ingredient from all of the other
        # sets.
        for key, possible_fields in possibles.items():
            if len(possible_fields) == 1:
                inferred[key] = possible_fields.pop()
                remove_item = inferred[key]
                del possibles[key]
                break
        else:  # nobreak
            assert False, "No keys have a single possible value"

        for x in possibles:
            if remove_item in possibles[x]:
                possibles[x].remove(remove_item)

    return inferred

def part2(lines: List[str]) -> int:
    ans =0

    for line in lines:
        seq, output = map(str.split, line.split("|"))

        possibles = defaultdict(lambda: set("abcdefg"))

        # Narrow down using the sequence on the left of the |. The unique-length
        # elements tell us what those characters could map to.
        for x in seq:
            possibilities = {2: "cf", 4: "bcdf", 3: "acf", 7: "abcdefg"}.get(len(x))
            if possibilities:
                for c in x:
                    possibles[c] &= set(possibilities)

        for k, v in counts.items():
            possibilities = {8: "ac", 7: "gd", 6: "b", 4: "e", 9: "f"}.get(v)
            if possibilities:
                possibles[k] &= set(possibilities)

        inferences = infer_one_to_one_from_possibles(possibles)

        segments_to_number = {
            "abcefg": 0,
            "cf": 1,
            "acdeg": 2,
            "acdfg": 3,
            "bcdf": 4,
            "abdfg": 5,
            "abdefg": 6,
            "acf": 7,
            "abcdefg": 8,
            "abcdfg": 9,
        }
        ans += int(
            "".join(
                str(segments_to_number["".join(sorted(inferences[c] for c in x))])
                for x in output
            )
        )

    return ans

print(part2(file))



    




#     count = 0
#     

#     if(string  in values):
#         count += 1

#     print(string)

# print(count)
