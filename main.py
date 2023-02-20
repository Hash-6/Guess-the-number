text = input("Would you like to have a unlimted amout of guesses and be given a score the the end or there be a limit of five guesses? Say limit or unlimited ").lower()
if text == "limit".lower():
  import mode1
if text == "unlimited".lower():
  import mode2
else:
  print("Say limit or unlimited")