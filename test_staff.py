"""Verify that all of the random effects can be used correctly."""   

from staff_of_chaos import adjectives, nouns, insults
from inspect import signature
from os import path
from tempfile import mktemp
import pytest

def read_file(filename):
    """Reads and returns the contents
    of a text file as a list of strings.
    """
    lines = None
    with open(filename, "rt") as infile:

        # Read all the characters in the file into a string.
        string = infile.read()

    # Split the string into a list of strings named
    # lines. Each line of text from the text file
    # will be stored in its own element in the list.
    lines = string.splitlines()

    return lines

def test_read_adjectives():
    """Verify that the read_file function works correctly."""
    # Write a sample file with three lines
    filename = "adjectives.txt"
    lines = ["aggressive","arrogant","boastful","bossy","boring",
            "careless","clingy","cruel","cowardly","deceitful",
            "dishonest","fussy","greedy","grumpy","harsh","impatient",
            "impulsive","jealous","moody","narrow-minded","overcritical",
            "rude","selfish","uncultured","untrustworthy","unhappy"]
    with open(filename, "wt") as outfile:
        print(*lines, sep="\n", file=outfile)

    # Call read_file to read the sample file.
    read = read_file(filename)

    # Verify that read_file read the file correctly.
    assert read == lines

def test_read_nouns():
    filename = "nouns.txt"
    lines = ["cretin","swine","goat herder","milk-drinker",
            "child","coward"]
    with open(filename, "wt") as outfile:
        print(*lines, sep="\n", file=outfile)

    # Call read_file to read the sample file.
    read = read_file(filename)

    # Verify that read_file read the file correctly.
    assert read == lines

pytest.main(["-v", "--tb=line", "-rN", __file__])