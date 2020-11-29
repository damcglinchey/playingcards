"""Play the game of War from the cmd line.

Author: D. McGlinchey
email: damcglinchey@gmail.com
"""
# standard library imports
import argparse

# local pkg imports
from playingcards.games import War

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Play a game of War')
	parser.add_argument('-v', '--verbose', dest='verbose', action='store_true',
		help='Print out battle information.')
	parser.add_argument('players', metavar='PLAYER', type=str, nargs='*',
		default=['Player 1', 'Player 2'],
		help='Player name')
	args = parser.parse_args()

	players = args.players + ['Player 1', 'Player 2']

	game = War(players, args.verbose)
	winner, rounds = game.play()

	# print out only the result if it hasn't been already
	if not args.verbose:
		print('{} wins after {} battles'.format(winner, rounds))