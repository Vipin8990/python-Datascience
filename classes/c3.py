import random
class Mylist(list): # inherits from my list
    
    def shuffle(self):
        random.shuffle(self)

    def get_random(self):
        return random.choice(self)

# object

a = Mylist([12, 121, 3, 1, 2, 3, 4, 5, 1, 5 ])
a.sort()
print(a)
a.shuffle()
print(a)
print("random item from list=", a.get_random())