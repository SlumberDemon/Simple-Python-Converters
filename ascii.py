asciihex = [41,42,43,44,45,46,47,48,49,"4A","4B","4C","4D","4E","4F",50,51,52,53,54,55,56,57,58,59,"5A"]
asciichar=["A","B","C","D","E","F","G","H","I","J","K","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
asciiden =[65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90]

choose = input ("Enter letter, please keep it capital: ")
i = 0
for beans in asciichar:
  if choose == (beans):
    print('User Input: '+(beans))
    print('Hex Value: '+str(asciihex[i]))
    print('Denary Value: '+str(asciiden[i]))
    print(bin(asciiden[i]))
  else:
    i = i+1
