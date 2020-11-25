"""Provides class for a standard playing card

Author: D. McGlinchey
email: damcglinchey@gmail.com
"""


class Card:
	"""Calss holding playing card information."""

	_face_cards = {0:'A', 10:'J', 11:'Q', 12:'K'}
	_suits = {0:'C', 1:'H', 2:'S', 3:'D'}
	_colors = {0:'B', 1:'R', 2:'B', 3:'R'}
	_cards_per_suit = 13

	@staticmethod
	def _parse_str(card):
		"""Parse card string representation to int."""
		# suit is the last character of the string
		suit = None
		for s in Card._suits:
			if Card._suits[s] == card[-1]:
				suit = s
				break
		if suit is None:
			raise ValueError('unable to parse suit from {}'.format(card))

		rank = None
		for r in Card._face_cards:
			if Card._face_cards[r] == card[:-1]:
				rank = r
				break
		if rank is None:
			try:
				rank = int(card[:-1]) - 1  # offset by 1, i.e. Ace is 0 not 1
			except ValueError:
				raise ValueError('unable to parse rank from {}'.format(card))
		if rank < 0 or rank >= Card._cards_per_suit:
			raise ValueError('invalid rank from {}'.format(card))

		return suit * Card._cards_per_suit + rank

	def __init__(self, val):
		"""Initialize the card.
	
		Args:
			val: Either valid 'int' or valid 'str'
		"""
		if isinstance(val, int):
			self._value = val
		elif isinstance(val, str):
			self._value = Card._parse_str(val)
		else:
			raise ValueError('Card must be initialized with int or str')

		if self._value < 0 or self._value > 51:
			raise ValueError('Invalid card representation: {}'.format(val))

	@property
	def suit(self):
		"""Return the cards suit as a string."""
		return Card._suits[self._value // Card._cards_per_suit]
	
	@property
	def color(self):
		"""Return the cards color as a string."""
		return Card._colors[self._value // Card._cards_per_suit]

	@property
	def rank(self):
		"""Return the cards rank as a string."""
		r = self._value % Card._cards_per_suit
		if r in Card._face_cards:
			return Card._face_cards[r]
		else:
			return str(r+1)
		
	def __str__(self):
		"""Get str representation of Card."""
		return self.rank + self.suit

	def __int__(self):
		"""Get integer representation of Card."""
		return self._value

	def __repr__(self):
		"""Card class representation."""
		return "{}('{}')".format(self.__class__.__name__, self.__str__())

	def __lt__(self, other):
		"""Operator self < other."""
		return self._value < other._value

	def __le__(self, other):
		"""Operator self <= other."""
		return self._value <= other._value

	def __eq__(self, other):
		"""Operator self == other."""
		return self._value == other._value

	def __ne__(self, other):
		"""Operator self != other."""
		return self._value != other._value

	def __gt__(self, other):
		"""Operator self > other."""
		return self._value > other._value

	def __ge__(self, other):
		"""Operator self >= other."""
		return self._value >= other._value

	def __hash__(self):
		"""Get hash value for Card. 

		hash() should return an integer, so just return
		the internal Card._value, which is an int
		"""
		return self._value