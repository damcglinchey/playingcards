import unittest
from playingcards.player import Player
from playingcards.deck import Deck
from playingcards.card import Card

class TestPlayerConstruct(unittest.TestCase):
	def testDefInit(self):
		player = Player("P1")
		self.assertEqual(player.name, "P1")
		self.assertEqual(player.deck, None)
	def testInitDeck(self):
		deck = Deck([Card(0), Card(1), Card(3)])
		player = Player("me", deck)
		self.assertEqual(player.name, "me")
		self.assertEqual(player.deck, deck)