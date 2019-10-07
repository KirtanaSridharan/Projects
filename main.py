from app import *

print("Welcome to bookmyshow")
print("-"*50 + "\n")
while True:
	print("1. Enter as admin\n2. Enter as user")
	n = int(input("Enter option: "))

	if n==1:
		admin()
	elif n==2:
		print("Welcome!!")
		while True:
			print("What would you like to do?")
			print("1. List movies\n2. Book ticket\n3. Generate ticket\n4. Cancel ticket\n5. Exit")
			ch = int(input("Enter your choice: "))
			if ch==1:
				list_movies()
			elif ch==2:
				book_ticket()
			elif ch==3:
				generate_ticket()
			elif ch==4:
				cancel_ticket()
			else:
				break

	

