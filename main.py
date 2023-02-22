text = input("Would you like to have unlimited guesses and be given a score at the end or have a limit of five guesses? Say 'unlimited' or 'limited' ").lower()

if text == "limited":
  import mode1
elif text == "unlimited":
  import mode2
else:
  print("Please say 'limit' or 'unlimited'") 