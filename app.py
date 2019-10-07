from models import *
from datetime import datetime
from tabulate import tabulate
import random


def admin():
	username= "admin"
	password = "password"
	userInput = input("Username: ")
	if userInput == username:
		a = input("Password: ")
		if a == password:
			print("WELCOME")
			admin_page()
		else:
			print("Wrong password. Enter again")
	else:
		print("Wrong username. Enter valid username")		


def admin_page():
	while True:
		print("1. Add movies\n2. Edit movies\n3. Delete movies\n4. Add seat type\n5. Add food menu\n6. Edit food menu\n7. Delete item from food menu\n8. See all Reservations\n9. Exit")
		n = int(input("Enter option: "))
		if n==1:
			name = input("Enter movie name: ")
			show_time = input("Enter the show time: ")
			screen_no = int(input("Enter screen no.: "))
			movie = Movies.create(name=name, show_time=show_time, screen_no=screen_no)
		elif n==2:
			list_movies()
			movie_id = int(input("Enter a movie ID: "))
			movie = Movies.get(Movies.id==movie_id)
			movie.name = input("Enter movie name: ")
			movie.show_time = input("Enter the show time: ")
			movie.screen_no = int(input("Enter screen no.: "))
			movie.save()
		elif n==3:
			list_movies()
			movie_id = int(input("Enter a movie ID: "))
			movie = Movies.get(Movies.id==movie_id)
			movie.delete_instance()
		elif n==4:
			name=input("Enter seat type: ")
			price = int(input("Enter the price: "))
			seat_type = Seatings.create(name=name, price=price)
		elif n==5:
			name=input("Enter item name: ")
			price = int(input("Enter price: "))
			food = Food.create(name=name, price=price)
		elif n==6:
			list_foodmenu()
			item_id = int(input("Enter item ID: "))
			item = Food.get(Food.id==item_id)
			item.name=input("Enter item name: ")
			item.price = int(input("Enter price: "))
			item.save()
		elif n==7:
			list_foodmenu()
			item_id=int(input("Enter item ID: "))
			item = Food.get(Food.id==item_id)
			item.delete_instance()
		elif n==8:
			list_reservations()
		else:
			break
	




def list_movies():
	movies = list()
	for movie in Movies.select():
		movies.append((movie.id, movie.name, movie.show_time, movie.screen_no))

	print(tabulate(movies, headers=["ID", "Name","Show time", "Screen no."], tablefmt="fancy_grid"))


def list_foodmenu():
	menu = list()
	for food in Food.select():
		menu.append((food.id, food.name, food.name, food.price))

	print(tabulate(menu, headers=["ID", "Item","Price"], tablefmt="fancy_grid"))



def list_seatTypes():
	seats = list()
	for seat in Seatings.select():
		seats.append((seat.id, seat.name, seat.price))
	print(tabulate(seats, headers=["ID", "Seat type", "Price"], tablefmt="fancy_grid"))




def book_ticket():
	list_movies()
	movie_id = int(input("Enter movie ID: "))
	movie = Movies.get(Movies.id == movie_id)
	no_of_tickets = int(input("Enter no of tickets: "))
	list_seatTypes()
	seat_id = int(input("Select seat type: "))
	seat = Seatings.get(Seatings.id == seat_id)
	name = input("Enter your name: ")
	ticket_ref = random.randint(100,999)
	print(f"Your ticket reference number is {ticket_ref}")
	movie_amount = no_of_tickets*seat.price
	print(f"The ticket price is {movie_amount}")
	choice = input("Would you like to prebook a meal? Y/N")
	if choice=="Y":
		f_amount = book_meal()
		amount = movie_amount+f_amount
	elif choice=="N":
		pass
	user = Reservations.create(name=name, movie_name=movie.name, no_of_tickets=no_of_tickets, screen_no=movie.screen_no,
								seat_type=seat.name, ticket_ref=ticket_ref, total_amt=amount)



def list_reservations():
	print("1. List all reservations\n2. List all reservations for a particular movie")
	b = int(input("Enter option: "))
	users = list()
	if b==1:
		for user in Reservations.select():
			users.append((user.id, user.name, user.movie_name, user.no_of_tickets, user.screen_no, user.seat_type,
							user.ticket_ref, user.total_amt))
		print(tabulate(users, headers=["ID","Name","Movie","No of tickets","Screen no","Seat type","Ticket reference",
										"Total amount"], tablefmt="fancy_grid"))
	elif b==2:
		list_movies()
		movie_id = int(input("Enter movie ID: "))
		movie = Movies.get(Movies.id == movie_id)
		for user in Reservations.select().where(Reservations.movie_name == movie.name):
			users.append((user.id, user.name, user.no_of_tickets, user.seat_type, user.ticket_ref))
		print(tabulate(users, headers=["ID","Name","No of tickets","Seat type","Ticket reference"], tablefmt="fancy_grid"))


def generate_ticket():
	users = list()
	for user in Reservations.select():
		users.append((user.id, user.name, user.movie_name, user.ticket_ref))
	print(tabulate(users, headers=["ID","Name","Movie","Ticket reference"], tablefmt="fancy_grid"))
	user_id = int(input("Enter user ID: "))
	user = Reservations.get(Reservations.id == user_id)
	print("-"*50 + "\n")
	print(f"Ticket reference: {user.ticket_ref}")
	print(f"Name: {user.name}")
	print(f"Movie: {user.movie_name}")
	print(f"No of tickets: {user.no_of_tickets}")
	print(f"Screen no: {user.screen_no}")
	print(f"Seat type: {user.seat_type}")
	print(f"Total amount: {user.total_amt}")
	print("Enjoy your show!!")
	print("-"*50 + "\n")

def cancel_ticket():
	users = list()
	for user in Reservations.select():
		users.append((user.id, user.name, user.movie_name, user.ticket_ref))
	print(tabulate(users, headers=["ID","Name","Movie","Ticket reference"], tablefmt="fancy_grid"))
	user_id = int(input("Enter user ID: "))
	user = Reservations.get(Reservations.id == user_id)
	user.delete_instance()

def book_meal():
	list_foodmenu()
	item_id = int(input("Enter item ID: "))
	item = Food.get(Food.id == item_id)
	food_amount = item.price
	return food_amount
