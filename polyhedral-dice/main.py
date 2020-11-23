#access a script built into python
import random


def diceroll(n):
  return(random.randint(1,n))


#prints the number where the number after diceroll is n.
print (diceroll(15))

