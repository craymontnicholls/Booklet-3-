def Year(y):
  if y % 4 == 0:
    return("leap year")
  elif y % 100 == 0:
    return("not a leap year")
  else :
    return("not a leap year")

print(Year(2000))


