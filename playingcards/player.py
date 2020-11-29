"""Tools for a card game player.

Author: D. McGlinchey
email: damcglinchey@gmail.com
"""
from typing import Optional
from playingcards.deck import Deck

class Player(object):
	"""Representation of a card game player."""
	def __init__(self, name: str, deck: Optional[Deck] = None) -> None:
		"""Player initialization.

		Args:
		    name: Name of the player
		    deck: Starting hand

		"""
		self.name = name
		self.deck = deck