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

class TestDeckComparison(unittest.TestCase):
	def testDeckEq(self):
		self.assertEqual(Deck([Card('AH')]), Deck([Card('AH')]))
		self.assertTrue(Deck([Card('AH')]) == Deck([Card('AH')]))

	def testDeckNe(self):
		self.assertTrue(Deck([Card('AH')]) != Deck([Card('AD')]))
		self.assertFalse(Deck([Card('AH')]) != Deck([Card('AH')]))		

class TestDeckMethods(unittest.TestCase):
	def setUp(self):
		self.cards = [Card('AS'), Card('4C'), Card('JD'), Card('10H')]

	def testCards(self):
		deck = Deck(self.cards[:])
		self.assertEqual(deck.cards(), self.cards)

	def testInDeck(self):
		deck = Deck(self.cards[:])
		for card in self.cards:
			self.assertTrue(deck.in_deck(card))
		self.assertFalse(deck.in_deck(Card('5H')))

	def testDraw(self):
		deck = Deck(self.cards[:])
		self.assertEqual(len(deck), len(self.cards))
		new_deck = deck.draw()
		self.assertEqual(len(new_deck), 1)
		new_deck = deck.draw(2)
		self.assertEqual(len(new_deck), 2)
		with self.assertRaises(ValueError):
			deck.draw(2)

	def testAdd(self):
		deck = Deck(self.cards[:])
		deck += Deck([Card('5D')])
		self.assertEqual(len(deck), len(self.cards)+1)

	def testSort(self):
		deck = Deck(self.cards[:])
		deck.sort()
		self.assertEqual(deck.draw(), Deck([Card('JD')]))
		self.assertEqual(deck.draw().cards()[0], Card('AS'))

	def testPlayCard(self):
		deck = Deck(self.cards[:])
		card = deck.play_card(self.cards[0])
		self.assertEqual(card, self.cards[0])
		# check that the card is no longer in the deck
		self.assertEqual(len(deck), len(self.cards) - 1)
		self.assertFalse(deck.in_deck(card))
		# play a card not in the deck and check that it returns 'None'
		card = deck.play_card(Card('5H'))
		self.assertTrue(card is None)