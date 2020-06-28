letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# now dictionary can handle lowercase inputs as well
letters += [letter.lower() for letter in letters]
points *=2 

#creating dictionary called letter_to_points that has the elements of letters as the keys and the elements of points as the values.
letter_to_points  = {key:value for key, value in zip(letters, points)}

# Our letters list did not take into account blank tiles. So we can Add an element to the letter_to_points dictionary that has a key of " " and a point value of 0.
letter_to_points [" "] = 0

#print(letter_to_points)


# score_word() - A function that will take in a word and return how many points that word is worth.
def score_word (word):
  point_total = 0
  for letter in word: 
    #print(i)
    point_total += letter_to_points.get(letter,0)
  return point_total

#test for above function
# brownie_points  = score_word("BROWNIE")
# print(brownie_points)

# Dumy player Data
player_to_words = {
"player1": ["BLUE","TENNIS","EXIT"], 
"player2": ["EARTH", "EYES", "MACHINE"], 
"player3": ["ERASER", "BELLY", "HUSKY"], 
"player4": ["ZAP", "COMA", "PERIOD"]
}

# update_point_totals() — A function that you can call any time to update score of each player.

def update_point_totals(players):

  player_to_points={}

  for player, words in player_to_words.items():
    player_points = 0
    #print (words)
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points
  return player_to_points

#print(update_point_totals(player_to_words))

# play_word() — a function that would take in a player and a word, and add that word to the list of words they’ve played
def play_word(player, words):
  player_to_words[player] = words 


#test for above function
play_word("test", ["TEST","test","test"])
print(player_to_words)
print("\n \t \t Final Score")
print(update_point_totals(player_to_words))


