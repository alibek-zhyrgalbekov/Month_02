import sqlite3
connection = sqlite3.connect("db.sqlite3")
cursor = connection.cursor()
cursor.execute("CREATE TABLE cars(id INTEGER , model TEXT, volume INTEGER, made TEXT)")

cursor.execute("INSERT INTO cars VALUES ('1', 'Masseratti', '6', 'Italy')")

connection.close()

class Car:

    def __init__(self, id, model, volume, made):
        self.id = id
        self.model = model
        self.volume = volume
        self.made = made

    def save(self):

        try:
            cursor.execute(f"INSERT INTO cars values (?, ?, ?, ?)",
                           (self.id, self.model, self.volume, self.made))
            connection.commit()

        except Exception:
            cursor.execute(
                "CREATE TABLE cars (id INTEGER model TEXT, volume TEXT, made TEXT)")
            cursor.execute(f"INSERT INTO cars values (?, ?, ?, ?)",
                           (self.id, self.model, self.volume, self.made))
            connection.commit()


    def link(self, cls):
        cursor.execute(
            "CREATE TABLE cars_managers (cars_id INTEGER , managers_id INTEGER,FOREIGN KEY (cars_id) references cars(id),FOREIGN KEY (managers_id) references managers(id)")
        connection.commit()

class Manager:

    def __init__(self, id, name, year, cash):
        self.id = id
        self.name = name
        self.year = year
        self.cash = cash

    def save(self):
        try:
            cursor.execute(f"INSERT INTO managers values (?, ?, ?, ?)",
                           (self.id, self.name, self.year, self.cash))
            connection.commit()

        except Exception:
            cursor.execute("CREATE TABLE managers (id INTEGER , name TEXT, year INTEGER, cash INTEGER)")
            cursor.execute(f"INSERT INTO managers values (?, ?, ?, ?)",
                           (self.id, self.name, self.year, self.cash))
            connection.commit()

car = Car(1, "Masseratti", 6, "Italy")
car.save()
car2 = Car("Audi", 5.5, "Germany")
car2.save()
m = Manager(3, "Alibek", 26, 15000)
car.link(m)

