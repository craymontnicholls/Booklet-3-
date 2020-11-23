def Divis(a,b):
  if b == 0:
    return ("false")
  elif a == 0:
    return("false")
  elif b % a == 0:
    return ("True")
  elif b % a != 0:
    return ("False")


print (Divis(0,1))