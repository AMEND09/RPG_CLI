
import os
import random

health = random.randint(20, 35)
abilities = ['Sucker_Punch', 'Slice', 'Powerup', 'Heal']

os.system('mkdir user_profile')
os.system('touch user_profile/profile.txt')

profile = open('user_profile/profile.txt', 'w')
profile.write(f"health: {health} abilities: {abilities}")

os.system('mkdir user_profile/inventory')

os.system('mkdir dungeon')
os.system('mkdir dungeon/door_one')
os.system('mkdir dungeon/door_one/chest')
os.system('touch dungeon/door_one/chest/key.txt')

key = open('dungeon/door_one/chest/key.txt', 'w')
key.write("AbC98-76T")

os.system('mkdir dungeon/door_two')
os.system('touch dungeon/door_two/lock.py')

lock_code = 'code = input("Please enter the key")/n if code == "AbC-76T":/n      print("Congrats")/n else:/n      print("Wrong Code")'

lock = open('dungeon/door_two/lock.py','w')

lock.write(lock_code)
