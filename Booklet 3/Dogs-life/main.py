#takes parmeter age then finds how old the dog is in dog years
def dog(age):
  if age <= 2:
    return (age * 12)
  elif age > 2:
    #not sure if it is (age - 2)*6 or just age * 6
    return (((age -2)  * 6) + 22)

print(dog(2.5))