import unittest
from playingcards.card import Card

class TestCardConstruct(unittest.TestCase):
	def testIntConstruct(self):
		card = Card(0)
	def testStrConstruct(self):
		card = Card('2C')

class TestCardAccess(unittest.TestCase):
	def testRank(self):
		card = Card('AC')
		self.assertEqual(card.rank, 'A')
		for r in range(2, 11):
			card = Card(str(r) + 'C')
			self.assertEqual(card.rank, str(r))
		card = Card('JC')
		self.assertEqual(card.rank, 'J')
		card = Card('QC')
		self.assertEqual(card.rank, 'Q')
		card = Card('KC')
		self.assertEqual(card.rank, 'K')

	def testSuit(self):
		for s in ['C', 'H', 'S', 'D']:
			card = Card('2' + s)
			self.assertEqual(card.suit, s)

	def testColor(self):
		for s in ['C', 'S']:
			card = Card('2' + s)
			self.assertEqual(card.color, 'B')
		for s in ['H', 'D']:
			card = Card('2' + s)
			self.assertEqual(card.color, 'R')