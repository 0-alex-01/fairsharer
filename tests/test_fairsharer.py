"""Tests for the fairsharer.my_module module.
"""

from fairsharer.fair_sharer import fair_sharer

vals = [10, 100, 0, 900]
def test_fair_sharer():
    assert fair_sharer(vals, 1) == [100, 100, 90, 720]

vals2 = [1000, 100, 0, 900] # [800, 200, 0, 1000] -> [900, 200, 100, 800]
def test_fair_sharer2():
    assert fair_sharer(vals2, 2) == [900, 200, 100, 800]
    
