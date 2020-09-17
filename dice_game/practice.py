# cookies
# import json
#from flask import make_response

# json.load takes an existing JSON file and turns it into a python object
# json.loads takes existing JSON string and turns it into python code
# def get_saved_data():
#     try:
#         data = json.loads(request.cookies.get('character'))
#     except TypeError:
#         data = {}
#     return data

# json.dump creates a JSON file from a python dictionary
# json.dumps creates a JSON string from a python dictionary
#@app.route('/save', methods=['POST'])
#def save():
#   response = make_response(redirect(url_for('index')))
#   data = get_saved_data()
#   data.update(dict(request.form.items()))
#   response.set_cookie('character', json.dumps(data))
#   return response



# review json

# Non-in-place methods don't alter their object; instead, they return a copy of that object:
# In place methods alter their object in memory
# slicing a list is not an in-place operation:

# help(str.rjust)

# The syntax for id is: write a hash character (#) character, followed by an id name.
#<label for="name"> matches the id in <input type='text' id="name">

# Jinja templates
#dictionary math
# //, will return rounded-down results.
# inventory = [{'id': 1, 'price': 6.25}, {'id': 2, 'price': 2.98}, {'id': 3, 'price': 16.02}]
# prices = [dict['price'] for dict in inventory]
# total = sum(prices)
# discount = 15
# final_price = total - (total * discount//100)
# print(final_price)

# relative URL
# link to styles <link rel="stylesheet" href="<path to styles> /static/css/mystyles.css>"
#<img src="images/me.png" alt="Drawing of Jane Smith" class="profile-image">
# "images" is folder + "/" + "me.png" image name
# "absolute" would be full website url address
# alt = "alternative text" should hold a precise description of your image


# dictionary = {"Name": "Branden", "age": "37", "Name": "Tara"}
# print(dictionary) # {Name: Tara, age: 37}


#CSS
# "Rule" is the selector and properties together
# "selector" -> body {
#   margin: 0;
#   padding: 0;
#   text-align: center;
#   font-family: 'Roboto', sans-serif;
#   color: #222;
#   background: #f7f5f0;
# }

# class RaceCar:
#     def __init__(self, color, fuel_remaining, laps=0, **kwargs):
#         self.color = color
#         self.fuel_remaining = fuel_remaining
#         self.laps = laps
#
#         for key, value in kwargs.items():
#             setattr(self, key, value)
#
#     def run_lap(self, length):
#         self.laps += 1
#         self.fuel_remaining -= length * 0.125
#         return self.fuel_remaining
#
#
#
#
#
# timmy = RaceCar('red', 100, max_speed=120)
# print(timmy.laps)
# print(timmy.run_lap(10))
# print(timmy.laps)
# print(timmy.run_lap(20))
# print(timmy.laps)
# print(timmy.laps)
# print(timmy.run_lap(10))
# print(timmy.laps)
# print(timmy.run_lap(20))
# print(timmy.laps)
#
#
# stuff = ["apple", 5.2, "dog", 8]
# def combiner(my_list):
#     strings = []
#     numbers = []
#     for item in my_list:
#         if isinstance(item, str):
#             strings.append(item)
#         if isinstance(item, int):
#             numbers.append(item)
#         if isinstance(item, float):
#             numbers.append(item)
#     num_string = sum(numbers)
#     string = ('').join(strings)
#     return string + str(num_string)
#
# print(combiner(stuff))
#
#
# class Letter:
#     def __init__(self, pattern=None):
#         self.pattern = pattern
#
#     def __str__(self):
#         morse = []
#         for char in self.pattern:
#             if char == '.':
#                 morse.append('dot')
#             else:
#                 morse.append('dash')
#         return ('-').join(morse)
#
#
# class S(Letter):
#     def __init__(self):
#         pattern = ['.', '.', '.']
#         super().__init__(pattern)
#
# morse = S()
# print(morse)
#
#
# class Liar(list):
#     def __init__(self, my_list=None):
#         super().__init__()
#         self.my_list = []
#
#     def __len__(self):
#         return len(self.my_list) + 1
#
#
# class Letter:
#     def __init__(self, pattern=None):
#         self.pattern = pattern
#
#     def __iter__(self):
#         yield from self.pattern
#
#     def __str__(self):
#         output = []
#         for blip in self:
#             if blip == '.':
#                 output.append('dot')
#             else:
#                 output.append('dash')
#         return '-'.join(output)
#
#     @classmethod
#     def from_string(cls, string):
#         char_list = string.split('-')
#         new_list = []
#         for char in char_list:
#             if char == 'dash':
#                 new_list.append('_')
#             if char == 'dot':
#                 new_list.append('.')
#         return cls(new_list)
#
# class S(Letter):
#     def __init__(self):
#          pattern = ['.', '.', '.']
#          super().__init__(pattern)
#
# morse_string = "dash-dot"
# print(Letter.from_string(morse_string))
#
#
#
# def from_string(string):
#     char_list = string.split('-')
#     new_list = []
#     for char in char_list:
#         if char == 'dash':
#             new_list.append('_')
#         if char == 'dot':
#             new_list.append('.')
#     return new_list
# morse_string = "dash-dot"
# print(from_string(morse_string))
#
#
# def roll(num_of_d20s):
#         empty_list = []  # list of D20
#         for _ in range(num_of_d20s):
#             empty_list.append("D20")
#         return empty_list # return cls(empty_list)
# print("Current challenge", roll(2))
#
# def roll(num_of_dice):
#     count = 0
#     dice = []
#     while count < num_of_dice:
#         dice.append("D20()")
#         count += 1
#     return dice
#
# print(roll(2))
#
# def score_yatzy(list_hand):
#     # if list_hand[1:] == list_hand[:-1]:
#     #     return 50
#     # else:
#     #     return 0
#
#     return list_hand[1:], list_hand[:-1]
#
#
# print(score_yatzy([1, 1, 1, 3, 1]))
#
# def score_fullhouse(hand):
#     triples = []
#     doubles = []
#     for die in hand:
#         if hand.count(die) == 3:
#             triples.append(die)
#         if hand.count(die) == 2:
#             doubles.append(die)
#     if len(triples) == 3 and len(doubles) == 2:
#         return "Is fullhouse"
#     else:
#         return "Not fullhouse"
#
# print(score_fullhouse([3, 3, 4, 2, 1]))
#
# def score_3_of_a_kind(hand):
#     triples = []
#     others = []
#     for die in hand:
#         if hand.count(die) == 3:
#             triples.append(die)
#         else:
#             others.append(die)
#     if len(triples) == 3 and len(others) == 2:
#         score = sum(triples) + sum(others)
#         return score
#     return 'Not 3 of a kind.'
# print(score_3_of_a_kind([2, 1, 1, 2, 2]))
#
# def score_4_of_a_kind(hand):
#     quads = []
#     other = []
#     for die in hand:
#         if hand.count(die) == 4:
#             quads.append(die)
#         else:
#             other.append(die)
#     if len(quads) == 4 and len(other) == 1:
#         score = sum(quads) + sum(other)
#         return score
#     return "Not 4 of a kind"
#
# print(score_4_of_a_kind([4, 4, 4, 3, 2]))
#
#
#
# def score_high_straight(hand):
#     hand.sort()
#     if len(set(hand)) == 5 and hand[4] == 6 and hand[0] == 2:
#         return True
#     return False
#
# print(score_high_straight([2, 3, 4, 5, 6]))
#
# def score_low_straight(hand):
#     hand.sort()
#     if len(set(hand)) == 5 and hand[4] == 5 and hand[0] == 1:
#         return True
#     return False
# print(score_low_straight([1, 2, 3, 4, 5]))
