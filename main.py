import random

possibleNumbers = [1, 2, 3, 4]
randomNum = random.choice(possibleNumbers)

print('Ben: Ben.')

while True:
  randomNum = random.choice(possibleNumbers)
  input('You: ')
  if randomNum == 1:
    print('Ben: No.')
  if randomNum == 2:
    print('Ben: Yes.')
  if randomNum == 3:
    print('Ben: GRRRR')
  if randomNum == 4:
    print('Ben: Hohoho')