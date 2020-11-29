"""Provides class for a standard playing card.

Author: D. McGlinchey
email: damcglinchey@gmail.com
"""
from typing import Dict, List, Union


class Card:
    """Calss holding playing card information."""

    _face_cards: Dict[int, str] = {0: 'A', 10: 'J', 11: 'Q', 12: 'K'}
    _suits: Dict[int, str] = {0: 'C', 1: 'H', 2: 'S', 3: 'D'}
    _colors: Dict[int, str] = {0: 'B', 1: 'R', 2: 'B', 3: 'R'}
    _cards_per_suit: int = 13

    @staticmethod
    def _parse_str(card: str) -> int:
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

    def __init__(self, val: Union[int, str]) -> None:
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
    def suit(self) -> str:
        """Return the cards suit as a string."""
        return Card._suits[self._value // Card._cards_per_suit]

    @property
    def color(self) -> str:
        """Return the cards color as a string."""
        return Card._colors[self._value // Card._cards_per_suit]

    @property
    def rank(self) -> str:
        """Return the cards rank as a string."""
        r = self._value % Card._cards_per_suit
        if r in Card._face_cards:
            return Card._face_cards[r]
        else:
            return str(r+1)

    @property
    def int_suit(self) -> int:
        """Get an integer representation of the cards suit 0->3."""
        return self._value // Cards._cards_per_suit
    
    @property
    def int_rank(self) -> int:
        """Get an integer representation of the cards rank 1->13."""
        return (self._value % Cards._cards_per_suit) + 1
    
    def __str__(self) -> str:
        """Get str representation of Card."""
        return self.rank + self.suit

    def __int__(self) -> int:
        """Get integer representation of Card."""
        return self._value

    def __repr__(self) -> str:
        """Card class representation."""
        return "{}('{}')".format(self.__class__.__name__, self.__str__())

    def __lt__(self, other: 'Card') -> bool:
        """Operator self < other."""
        return self._value < other._value

    def __le__(self, other: 'Card') -> bool:
        """Operator self <= other."""
        return self._value <= other._value

    def __eq__(self, other: object) -> bool:
        """Operator self == other."""
        if isinstance(other, Card):
            return self._value == other._value
        else:
            return NotImplemented

    def __ne__(self, other: object) -> bool:
        """Operator self != other."""
        if isinstance(other, Card):
            return self._value != other._value
        else:
            return NotImplemented

    def __gt__(self, other: 'Card') -> bool:
        """Operator self > other."""
        return self._value > other._value

    def __ge__(self, other: 'Card') -> bool:
        """Operator self >= other."""
        return self._value >= other._value

    def __hash__(self) -> int:
        """Get hash value for Card.

        hash() should return an integer, so just return
        the internal Card._value, which is an int
        """
        return self._value
