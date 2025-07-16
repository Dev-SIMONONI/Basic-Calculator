weeklyAllowance= 2000
weeklyAllowance -= 400
print(f"I spent 400 on books i had ₦{weeklyAllowance}")

weeklyAllowance += 100
print(f"I saw ₦100 under my bed and added it to my balance now is ₦{weeklyAllowance}")

weeklyAllowance -= 250
print(f"I brought snacks worth ₦250 and my balance is ₦{weeklyAllowance}")

percentage=25 / 100
percentage *= weeklyAllowance
weeklyAllowance -= percentage
print(f"I gave 25% of my balance to my sibling so i had ₦{weeklyAllowance}")

oneThird= weeklyAllowance / 3
weeklyAllowance -= oneThird
print(f"I use one third of my balance to buy data so my balance is {weeklyAllowance}")

weeklyAllowance //= 2
print(f"Split my balance between saving and Tihthing so my balance is {weeklyAllowance}")

weeklyAllowance %= 100
print(f"my balance after all the expenses is ₦{weeklyAllowance}")

