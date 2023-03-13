from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(3):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(3):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    single_noun = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]

    for _ in range(10):
        word = get_noun(1)
        assert word in single_noun

    plural_nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    
    for _ in range(10):
        word = get_noun(2)
        assert word in plural_nouns

def test_get_verb():
    past_tense = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    
    for _ in range(10):
        word = get_verb(0,1)
        assert word in past_tense

    single_present = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    
    for _ in range(10):
        word = get_verb(1,1)
        assert word in single_present

    plural_present = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]

    for _ in range(10):
        word = get_verb(1,2)
        assert word in plural_present

    future_single = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

    for _ in range(10):
        word = get_verb(2,1)
        assert word in future_single

    plural_single = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

    for _ in range(10):
        word = get_verb(2,2)
        assert word in plural_single

def test_get_preposition():

    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    
    for _ in range(30):
        word = get_preposition()
        assert word in prepositions

def test_get_prepositional_phrase():

    single_phrase = [f"{get_preposition()} {get_determiner(1)} {get_noun(1)}"]

    for _ in range():
        word = get_prepositional_phrase()
        assert word in single_phrase

    plural_phrase = [f"{get_preposition()} {get_determiner(2)} {get_noun(2)}"]

    for _ in range():
        word = get_prepositional_phrase()
        assert word in plural_phrase


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
