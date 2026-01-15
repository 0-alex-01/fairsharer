"""Tests for the fairsharer.my_module module.
"""

from fairsharer.fair_sharer import fair_sharer

vals = [10, 100, 0, 900]
def test_fair_sharer():
    assert fair_sharer(vals, 1) == [100, 100, 90, 720]
    
