import sys

from People import People

def main():
	jack = People('jack', 19, 'man')
	jack.self_introduction()
	print(jack)

	print('\n')

	rose = People('rose', 22, 'women')
	rose.self_introduction()
	print(rose)

	print('\n')

	cook = jack + rose
	cook.self_introduction()
	print(cook)

if __name__ == "__main__":
	sys.exit(main())
