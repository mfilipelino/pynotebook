import pytest


def rearrange(lst):
    return lst


def test_base():
    assert [] == rearrange([])
    assert [1] == rearrange([1])
    assert [-1] == rearrange([-1])


def test_case1():
    assert [1, 2] == rearrange([1, 2])



