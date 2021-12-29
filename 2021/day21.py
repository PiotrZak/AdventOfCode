# class Die:
# 	def __init__(self):
# 		self.num_rolls = 0
# 		self.last_roll = 0
# 		self.last_sum = -3
        
# 	def next_sum(self):
# 		self.num_rolls += 3
# 		self.last_roll += 3
# 		last_sum = self.last_sum + 9
# 		if self.last_roll > 100:
# 			self.last_roll -= 100
# 			last_sum -= 100 * self.last_roll
# 			self.last_sum = last_sum - 100
# 		else:
# 			self.last_sum = last_sum
# 		return last_sum


# def start_game(position):
# 	die = Die()
# 	score = [0, 0]
# 	player = 0
# 	while True:
# 		position[player] = (position[player] + die.next_sum()) % 10
# 		score[player] += position[player] + 1
# 		if score[player] >= 1000:
# 			break
        
#         #switch turn player
# 		player = 1 - player
# 	return score[1 - player] * die.num_rolls


# position = [9-1,4-1]

# result = start_game(position)
# print(f"Part 1: {result}")


#As you experiment with the die, you feel a little strange. 
# An informational brochure in the compartment explains 
# that this is a quantum die: when you roll it,
#  the universe splits into multiple copies,
#  one copy for each possible outcome of the die.
#  In this case, rolling the die always splits the universe into three copies:
#  one where the outcome of the roll was 1, 
#  one where it was 2, and one where it was 3.


from collections import Counter, defaultdict
from itertools import product
from timeit import default_timer as timer

# get all combinations of 3 dice rolls and sum them
COMBINATIONS = {
    combination: sum(combination)
    for combination in product([1, 2, 3], repeat=3)
}

# Get Counter of all possible outcomes (sums) of three dice rolls
# Counter({3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1})
COUNTER = Counter(COMBINATIONS.values())


def move_player(position, score, steps):
    position_final = (position + steps - 1) % 10 + 1
    return position_final, score + position_final


def roll_next(position, score, length, p, length_dict):
    for roll_sum, count in COUNTER.items():
        if score >= 21:
            return
        new_position, new_score = move_player(position, score, roll_sum)
        new_length = length + 1
        p_new = p * count
        length_dict[(new_length, new_score)] += p_new
        roll_next(new_position, new_score, new_length, p_new, length_dict)


if __name__ == '__main__':
    start = timer()
    # player_positions = [7,8]
    player_positions = [9, 4]
    # the length dicts contain all possibilities for a given (number of rolls, score)
    length_dicts = []
    for player_position in player_positions:
        d = defaultdict(lambda: 0)
        roll_next(player_position, 0, 0, 1, d)
        length_dicts.append(d)

    won = [0, 0]
    for (length1, score1), value1 in length_dicts[0].items():
        for (length2, score2), value2 in length_dicts[1].items():
            # Player1 plays first -> Player2 is one roll behind and must not have won (score>=21)
            if score1 >= 21 and length2 == length1 - 1 and score2 < 21:
                won[0] += value1 * value2
            # Player2 plays 2nd -> 1 and 2 must have same number of rolls, 1 must not have won
            if score2 >= 21 and length2 == length1 and score1 < 21:
                won[1] += value1 * value2
    end = timer()
    print(end - start)
    print(len(won))
    print(won)
    print(max(won))


# Using your given starting positions, determine every possible outcome.
# Find the player that wins in more universes;
# in how many universes does that player win?

# pos,scores,rnd,goal=[9,4],[0,0],0,1000
# while max(scores)<goal:
#     oldscores=scores
#     pos[0]=(pos[0]+5+18*rnd)%10+1
#     pos[1]=(pos[1]+14+18*rnd)%10+1
#     scores=[scores[i]+pos[i] for i in [0,1]]
#     rnd+=1
# if scores[0]>=goal:
#     print((rnd*6-3)*oldscores[1])#overcounted if Player 1 won
# else:
#     print(rnd*6*scores[0])


# what do you get if you multiply the score of the losing player
#  by the number of times the die was rolled during the game?



# pos = [9, 4] # position [player1,player2] 
# tot = [0,0] # total [player1,player2]
# r = 1 # next roll
# p = 1 # player who just moved (next player is p=0 which is player 1

# while tot[p] < 1000:
#     p = 1 - p
#     pos[p] = (pos[p] + 3*r + 3) % 10
#     tot[p] += pos[p] + 1
#     r += 3

# print("Losing score:", min(tot), ". Last roll:", r-1)
# print("LS * LR:", min(tot) * (r-1)) 

# rf = [(3,1),(4,3),(5,6),(6,7),(7,6),(8,3),(9,1)]

# ## if p1 is about to move, return (w1,w2) where
# ## wj is the number of universes where player j wins
# def wins(p1,t1,p2,t2):
#     if t2 <= 0: return (0,1) # p2 has won (never p1 since p1 about to move)

#     w1,w2 = 0,0
#     for (r,f) in rf:
#         c2,c1 = wins(p2,t2,(p1+r)%10,t1 - 1 - (p1+r)%10) # p2 about to move
#         w1,w2 = w1 + f * c1, w2 + f * c2

#     return w1,w2

# print("Bigger winner universes:",max(wins(3,21,1,21))) # initially p1=4,p2=2