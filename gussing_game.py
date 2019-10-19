import random

print("What is you name?")
name = input()

print("Hello! "+name+" Guess a number between 1 and 20")
number = random.randint(1, 20)
print(number)


for i in range(1, 6):
	print("Take a guess:-")
	guess = int(input())

	if guess == number:
		print("Congratulations!! Your guess is right.")
		break
	elif guess > number:
		print("The guess is heigher then the number. Try again!!")
	elif guess < number:
		print("The guess is lower then the number. Try again!!")

	if i == 5:
		print("Guessing session is over, you lost the game.")
		print("The number is " + str(number))