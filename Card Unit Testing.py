# unitTestingCard.py
# unit testing rank

import sys
import unittest

from Card import *

class RankTest(unittest.TestCase):
  """ Tests Rank methods: rank() and rankName() """
  
  def testRanks(self): # unit test for ranks 1-13
    """ creates cards of rank 1 through 13 of clubs (can be any other fixed suit),
    and verifies that the created card's rank is equal to the
    rank it was created with """
    
    for i in range(1,14):
      myCard = Card(i,'c') # create i of clubs
      self.assertEqual(myCard.rank(),i) # verifies that the card's rank is i

  def testRankName(self): # unit test for rank names, 'ace', 'two', 'three',...
    """ creates cards of rank 1 through 13 of clubs (can be any other fixed suit),
    and then checks for equivalency: card's rank name, by calling method rankName,
    and the rank name that was given to the card - note that the number was used for rank,
    so it needs to be 'converted' to a rank name"""
    for i in range(2,14):     # create ith indexed rank name
        myName = Card(i,'c')
        self.assertEqual(Card.RANK_NAMES[i-1],myName.rankName())  #verifies that the rank names are correct


class SuitTest(unittest.TestCase):
  """ Tests Suit methods: suit() and suitName() """
    
  def testSuits(self): # unit test for suits, 'c', 'd', 'h', 's'
    """ creates cards of rank 4 (any other fixed rank can be used)of 
    c (clubs), d (diamonds), h(hearts) and s (spades), and 
    verifies that the created card's suit is equal to the suit it was 
    created with (c,d,h,s) """
    index = 0
    for i in ['c','d','h','s']:
        mySuit = Card(1,i)  # create rank 1 of suit i
        self.assertEqual(mySuit.suit(),Card.SUITS[index])   #verifies the suits I hope
        index += 1

    
    
  def testSuitName(self): # unit test for suit names, 'clubs', 'diamonds',...
    """ creates cards with all the suit names ...
    and then checks for equivalency: card's suit name, by calling method suitName,
    and the suit name that was given to the card - note that the letter (c,d,h, or s) 
    was used for suit, so it needs to be converted to a corresponding 'full' suit name"""
    index = 0
    for i in ['c','d','h','s']:
        
        mySuit = Card(1,i)  # create rank 1 of suit i
        self.assertEqual(mySuit.suitName(),Card.SUIT_NAMES[index])
        index += 1


      
    
def main(argv):
  unittest.main()

if __name__ == '__main__':
  main(sys.argv)
