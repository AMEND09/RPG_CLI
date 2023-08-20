code = input("Please enter the key you obtained from the chest ")

key = open('dungeon/door_one/chest/key.txt', 'r')

if code == key:
  print("Congrats, you reached the end')
else:
  print("Wrong Code")
