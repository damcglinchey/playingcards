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

class TestCardConversion(unittest.TestCase):
	def testConvInt(self):
		for i in range(0, 52):
			card = Card(i)
			self.assertEqual(int(card), i)

	def testConvStr(self):
		for s in Card._suits:
			for r in Card._face_cards:
				cstr = Card._face_cards[r] + Card._suits[s]
				card = Card(cstr)
				self.assertEqual(str(card), cstr)
			for r in range(2, 11):
				cstr = str(r) + Card._suits[s]
				card = Card(cstr)
				self.assertEqual(str(card), cstr)

class TestCardComparison(unittest.TestCase):
	def testLessThan(self):
		for i in range(0, 52):
			for j in range(i+1, 52):
				self.assertTrue(Card(i) < Card(j))

	def testLessThanEqual(self):
		for i in range(0, 52):
			for j in range(i, 52):
				self.assertTrue(Card(i) <= Card(j))

	def testGreaterThan(self):
		for i in range(0, 52):
			for j in range(i+1, 52):
				self.assertTrue(Card(j) > Card(i))

	def testGreaterThanEqual(self):
		for i in range(0, 52):
			for j in range(i, 52):
				self.assertTrue(Card(j) >= Card(i))

	def testEqual(self):
		for i in range(0, 52):
			self.assertTrue(Card(i) == Card(i))

	def testNotEqual(self):
		for i in range(0, 52):
			for j in range(0, 52):
				if i == j:
					continue
				else:
					self.assertTrue(Card(i) != Card(j))

