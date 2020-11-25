import unittest
from playingcards.card import Card
from playingcards.deck import Deck

class TestDeckConstruct(unittest.TestCase):
	def testDefaultConstruct(self):
		deck = Deck()
		self.assertEqual(len(deck), 0)

	def testCardConstruct(self):
		deck = Deck([Card(0), Card(1), Card(2)])
		self.assertEqual(len(deck), 3)

	def testStandardDeck(self):
		deck = Deck.create_standard_deck()
		self.assertEqual(len(deck), 52)
