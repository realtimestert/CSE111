"""Verify that all of the random effects can be used correctly."""   

from staff_of_chaos import random_magic, adjectives, nouns, insults
from inspect import signature
from os import path
from tempfile import mktemp
import pytest

def test_adjectives():
   adjective = ["aggressive", "arrogant", "boastful", "bossy", "boring", "careless",
         "clingy", "cruel", "cowardly", "deceitful", "dishonest", "fussy",
         "greedy", "grumpy", "harsh", "impatient", "impulsive", "jealous",
         "moody", "narrow-minded", "overcritical", "rude", "selfish",
         "uncultured", "untrustworthy", "unhappy"]
   for _ in range(26):
      word = adjectives()
      assert word in adjective

def test_nouns():
   noun = ["cretin", "swine", "goat herder", "milk-drinker", "child", "coward"]
   for _ in range(46):
      word = nouns()
      assert word in noun

pytest.main(["-v", "--tb=line", "-rN", __file__])