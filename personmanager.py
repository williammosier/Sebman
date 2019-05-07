import csv
import sqlite3

class PersonManager:
	def __init__(self):
		self.conn = sqlite3.connect('person.db')

		self.c = self.conn.cursor()

	def importPerson(self, data):
		print(data)
		with self.conn:
			self.c.execute("INSERT INTO people VALUES (:full, :first, :last, :id, :month, :day, :year, :phone, :email, :address, :known)", {'full': data[0], 'first': data[1], 'last': data[2], 'id': data[3], 'month': data[4], 'day': data[5], 'year': data[6], 'phone': data[7], 'email': data[8], 'address': data[9], 'known': data[10]})

	def importPeople(self):
		with open('Relationship data 1.csv', 'r') as csv_file:
			csv_reader = csv.reader(csv_file)

			for line in csv_reader:
				self.importPerson(line)

	def selectPerson(self, ID):
		self.c.execute("SELECT * FROM people WHERE id=:id", {'id': ID})
		person = self.c.fetchall()
		return person

	def selectPeople(self, search):
		search = search.split()
		if len(search) == 2:
			self.c.execute("SELECT * FROM people WHERE first LIKE (:first || '%') AND last LIKE (:last || '%')", {"first": search[0], "last": search[1]})
		elif len(search) == 1:
			self.c.execute("SELECT * FROM people WHERE first LIKE (:first || '%')", {'first': search[0]})
		else:
			return []
		people = self.c.fetchall()
		return people

	def selectAllPeople(self):
		self.c.execute("SELECT * FROM people")
		self.c.fetchone()
		people = self.c.fetchall()
		return people

	def updatePerson(self, person, update):
		with self.conn:
			self.c.execute("""UPDATE people SET first = :first, last = :last, month = :month, day = :day, year = :year, phone = :phone, email = :email, address = :address, known = :known
							WHERE id = :id""",
							{"id": person, "first": update[0], "last": update[1], "month": update[2], "day": update[3], "year": update[4], "phone": update[5], "email": update[6], "address": update[7], "known": update[8]})
		self.conn.commit()
		person = self.selectPerson(person)
		return person

	def initializeTable(self):
		self.c.execute("""CREATE TABLE people (
							full text,
							first text,
							last text,
							id integer,
							month integer,
							day integer,
							year integer,
							phone text,
							email text,
							address text,
							known text
							)""")

	#def exportPeople(self):

	def purgeTable(self):
		with self.conn:
			self.c.execute("DELETE FROM people")

	def getMaxId(self):
		self.c.execute("SELECT id FROM people ORDER BY id DESC LIMIT 1 OFFSET 1")
		return self.c.fetchall()[0][0]

def main():

	manager = PersonManager()

	#manager.purgeTable()

	#manager.initializeTable()

	#manager.importPeople()

	print(manager.selectAllPeople())

	#print(manager.selectPeople("w"))

	# print(full)
	# ID = full[3]
	# print(manager.updatePerson(ID, ('william mosier', 'william', 'mosier', '', 5, 11, 1952, '3152379363', '', '', '')))
	
	print(manager.getMaxId())
	
	manager.conn.close()

if __name__ == "__main__":
	main()

#c.execute("DELETE FROM people")

#conn.commit()