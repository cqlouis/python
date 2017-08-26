class Animal(object):
	def __init__(self):
		print("Animal.")

class Mammal(Animal):
	def __init__(self):
		super(Mammal, self).__init__()
		print("Mammal.")

class Bird(Animal):
	def __init__(self):
		super(Bird, self).__init__()
		print("Bird.")

class Flyable(Animal):
	def __init__(self):
		super(Flyable, self).__init__()
		print("Flying")

class Runnable(Animal):
	def __init__(self):
		super(Runnable, self).__init__()
		print("Running.")

class Bat(Mammal, Flyable):
	def __init__(self):
		super(Bat, self).__init__()
		print("Bat.")


class Ostrich(Bird, Runnable):
	def __init__(self):
		super(Ostrich, self).__init__()		

ba1 = Bat()
print("===================================")
Os1 = Ostrich()

