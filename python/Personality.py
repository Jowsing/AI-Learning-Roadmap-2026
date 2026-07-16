from abc import ABC, abstractmethod

class Character(ABC):
	@abstractmethod
	def character(self):
		pass

class Looks(ABC):
	@abstractmethod
	def looks(self):
		pass
