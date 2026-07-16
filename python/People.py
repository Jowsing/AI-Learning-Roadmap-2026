from random import randint
from Personality import Character, Looks

class People(Character, Looks, object):
	name = ''
	age = 0
	sex = ''

	__character = ''
	__looks = ''

	def self_introduction(self):
		self.say()
		self.character()
		self.looks()

	def say(self):
		print(f"My name is {self.name} and age is {self.age} years old {self.sex}")

	def character(self):
		print(self.__character)

	def looks(self):
		print(self.__looks)

	def __init__(self, name, age, sex):
		self.name = name
		self.age = age
		self.sex = sex
		self.__character = "i am good people" if randint(0, 1) == 1 else 'i am bad people'
		self.__looks = 'i am handsome' if randint(0, 1) == 1 else 'i am ugly'

	def __str__(self):
		return f"People(name = {self.name}; age = {self.age}; sex = {self.sex})"

	def __repr__(obj):
		return f"People(name = {obj.name}; age = {obj.age}; sex = {obj.sex})"

	def __add__(self, other):
		sonName = f"son of {self.name} + {other.name}"
		sonAge = 1
		sonSex = 'boy' if randint(0, 1) == 1 else 'girl'
		return People(sonName, sonAge, sonSex)
