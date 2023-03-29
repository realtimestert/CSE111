"""Verify that all of the random effects can be used correctly."""   

from staff_of_chaos import random_magic
from inspect import signature
from os import path
from tempfile import mktemp
import pytest

def test_random_magic():
    
    filename = mktemp(dir= "." , prefix= "not" , suffix= ".txt")


pytest.main(["-v", "--tb=line", "-rN", __file__])