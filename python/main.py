import sys
import asyncio
import random

from People import People

async def main():
	jack = People('jack', 19, 'man')
	jack.self_introduction()
	print(jack)

	print('\n')

	rose = People('rose', 22, 'women')
	rose.self_introduction()
	print(rose)

	print('\n')

	if random.randint(0, 1) == 1:
		await jack.getMarried(rose)
	else:
		await jack.getDivorced(rose)

	cook = jack + rose
	cook.self_introduction()
	print(cook)

if __name__ == "__main__":
	sys.exit(asyncio.run(main()))
