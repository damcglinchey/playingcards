"""Tools for holding & manipulating Cards.

Author: D. McGlinchey
email: damcglinchey@gmail.com
"""
import random
from typing import List, Optional, Union
from playingcards.card import Card


class Deck(object):
    """Container for holding and manipulating Cards."""

    def __init__(self, card_list: Optional[List[Card]] = None) -> None:
        """Initialize the deck of cards with either list of Cards or empty."""
        if card_list is None:
            self._cards = []
        else:
            self._cards = card_list

    def __str__(self) -> str:
        """Get string of all cards in Deck."""
        return ' '.join([str(c) for c in self._cards])

    def __repr__(self) -> str:
        """Get class representation."""
        return "{}('{}')".format(self.__class__.__name__, self.__str__())

    def __len__(self) -> int:
        """Get the number of cards in the Deck."""
        return len(self._cards)

    @classmethod
    def create_standard_deck(cls) -> "Deck":
        """Create a standard deck of 52 cards."""
        return Deck([Card(i) for i in range(0, 52)])

    def cards(self) -> List[Card]:
        """Get a list of all cards in the deck."""
        return self._cards[:]

    def shuffle(self) -> None:
        """Shuffle this deck of cards.

        Randomly reorder the cards in this Deck.
        """
        random.shuffle(self._cards)

    def sort(self) -> None:
        """Sort this decks cards in ascending order."""
        self._cards.sort()

    def in_deck(self, card: Card) -> bool:
        """Check if the card is in this deck."""
        if card in self._cards:
            return True
        else:
            return False

    def __eq__(self, other: object) -> bool:
        """Test if all cards are in both decks."""
        if isinstance(other, Deck):
            if len(other) != len(self):
                return False
            if self._cards == other._cards:
                return True
            else:
                return False
        else:
            return NotImplemented

    def __ne__(self, other: object) -> bool:
        """Test if all cards are not in both decks."""
        return not self.__eq__(other)

    def play_card(self, card: Card) -> Optional[Card]:
        """Play a specific card from the Deck.

        Play the requested card from the Deck. If the card
        doesn't exist in the deck, returns 'None'. If it
        does exist in the deck, return the Card and remove
        it from this Deck.

        Args:
            card: Requested Card to play

        Returns:
            'card' if it exists in the deck, else None

        """
        if self.in_deck(card):
            self._cards.remove(card)
            return card
        else:
            return None

    def draw(self, num: int = 1) -> "Deck":
        """Draw a number of cards from this Deck.

        Draw a number of cards from this Deck.
        This removes those cards from the Deck itself.
        If the number of cards requested exceeds the
        number of cards in the Deck, a 'ValueError' is
        raised.

        Args:
            num: Number of cards to deal

        Returns:
            New Deck of cards containing the drawn cards.

        Raises:
            TypeError: if num is not int
            ValueError: if num > len(self)

        """
        if not isinstance(num, int):
            raise TypeError('Argument "num" must be int')
        elif num > len(self):
            raise ValueError('Not enough cards remain in the Deck')
        else:
            return Deck([self._cards.pop(0) for i in range(0, num)])

    def __iadd__(self, other: "Deck") -> "Deck":
        """Add cards from another deck to this deck.

        Take cards from 'other' and add them to 'self'.
        This removes all cards from 'other'
        """
        self._cards.extend(other._cards)
        other._cards = []
        return self

    def __add__(self, other: "Deck") -> "Deck":
        """Add cards from two decks to make new deck."""
        return Deck(self.cards() + other.cards())
