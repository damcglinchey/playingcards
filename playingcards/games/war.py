"""The game of War.

Rules: https://bicyclecards.com/how-to-play/war/

Author: D. McGlinchey
email: damcglinchey@gmail.com
"""

# standard library imports
from typing import List, Optional, Tuple

# local imports
from playingcards import Card, Deck, Player


class War:
    """The game of War."""
    
    def __init__(self, names: Tuple[str, str] = ['Player1', 'Player2'], 
                
                 verbose: bool = False):
        """Setup a game of War.

        Args:
            names: Tuple of 2 names, 1 for each player
            verbose: Silent if 'False', prints battles if 'True'

        """
        full_deck = Deck.create_standard_deck()
        full_deck.shuffle()
        self._p1 = Player(names[0], full_deck.draw(26))
        self._p2 = Player(names[1], full_deck.draw(26))
        self.verbose = verbose

    def _war_compare(self, d1: Deck, d2: Deck) -> Tuple[bool, Deck, Deck]:
        """Compare cards from a battle or war in the game of War.

        *Reminder: Ace is high!*
        - If one card is higher, that player wins and gets all played cards.
        - If cards are equal, proceed with 'war':
            * draw 2 cards each and re-compare

        Args:
            d1: Player 1's played cards in this battle
            d2: Player 2's played cards in this battle

        Returns:
            bool, Deck, Deck
            bool: True if player 1 one, False if player 2
            Deck: Player 1's played cards
            Deck: Player 2's played cards

        """
        c1r = d1.cards()[-1].int_rank
        c2r = d2.cards()[-1].int_rank
        # Ace is high
        if c1r == 1:
            c1r += 13
        if c2r == 1:
            c2r += 13

        if c1r == c2r:
            if self.verbose:
                print('!!WAR!!')
            if len(self._p1.deck) < 2:
                d1 += self._p1.deck.draw(len(self._p1.deck))
                return False, d1, d2
            elif len(self._p2.deck) < 2:
                d2 += self._p2.deck.draw(len(self._p2.deck))
                return True, d1, d2
            else:
                d1 += self._p1.deck.draw(2)
                d2 += self._p2.deck.draw(2)
                return self._war_compare(d1, d2)
        elif c1r > c2r:
            if self.verbose:
                print('{} Wins!: *{}* {}'.format(self._p1.name, 
                      str(d1), str(d2)))
            return True, d1, d2
        else:
            if self.verbose:
                print('{} Wins!: {} *{}*'.format(self._p2.name, 
                      str(d1), str(d2)))
            return False, d1, d2

    def _war_battle(self) -> bool:
        """Execute a 'battle' in the game of War.

        Execute a single battle in the game of War between two
        players. 
        1. Draw the top card from each players deck.
        2. Compare ranks
    
        Returns:
            True if battle was successfuly, False if one of the players
            had no more cards to draw

        """
        if len(self._p1.deck) == 0 or len(self._p2.deck) == 0:
            return False

        try:        
            p1wins, d1, d2 = self._war_compare(self._p1.deck.draw(), 
                                               self._p2.deck.draw())
        except ValueError:
            return False
        else:
            winnings = d1 + d2
            winnings.shuffle()
            if p1wins:
                self._p1.deck += winnings
            else:
                self._p2.deck += winnings
            return True

    def play(self) -> Tuple[str, int]:
        """Play a game of War.

        Returns:
            str, int
            str: The name of the winning player
            int: The number of battles played.

        """
        n_rounds = 0
        keep_playing = self._war_battle()
        while keep_playing:
            n_rounds += 1
            keep_playing = self._war_battle()

        if len(self._p1.deck) > len(self._p2.deck):
            winner = self._p1.name
        else:
            winner = self._p2.name

        if self.verbose:
            print('*** {} Wins after {} rounds! ***'.format(winner, n_rounds))

        return winner, n_rounds
