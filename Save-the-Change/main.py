def SaveTheChange(Amount):
  NearestPound = int(Amount) + 1
  if int(Amount) != Amount:
    return NearestPound - Amount
  else:
    NearestPound = Amount

Price = 1.20
Savings = SaveTheChange(Price)

print("Debit -purchase: £{:.2f}".format(Price))
print("Debit - Save the change: £{:.2f}".format(Savings))
print("Credit - Save the changes: £{:.2f}".format(Savings))
