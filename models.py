from peewee import *

db = SqliteDatabase('cinema.db')

class Movies(Model):
	name = CharField()
	show_time = CharField()
	screen_no = IntegerField()
	class Meta:
		database = db

class Seatings(Model):
	name = CharField()
	price = IntegerField()
	class Meta:
		database = db

class Reservations(Model):
	name = CharField()
	movie_name = CharField()
	no_of_tickets = IntegerField()
	screen_no = IntegerField()
	seat_type = CharField()
	ticket_ref = IntegerField()
	total_amt = IntegerField()
	class Meta:
		database=db


class Food(Model):
	name = CharField()
	price = IntegerField()
	class Meta:
		database=db

if __name__ == '__main__':
	db.connect()
	db.create_tables([Movies, Seatings, Reservations, Food])