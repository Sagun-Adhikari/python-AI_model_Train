import random
people = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ian", "Jack"]
verbs = ["buys", "steals", "destroys", "creates", "finds", "announces", "launches", "breaks", "reveals", "hides"]
objects = ["a car", "a secret", "the city", "a phone", "a treasure", "a plan", "a robot", "a building", "the truth", "a laptop"]

one=random.choice(people)
two=random.choice(verbs)
three=random.choice(objects)
print(one+" "+two+" "+three)