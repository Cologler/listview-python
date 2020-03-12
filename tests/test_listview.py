# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import pytest

from listview import ListView

def test_all_methods_added():
    dv = set(dir(ListView(None, None)))
    for k in dir([]):
        assert k in dv

def test_len():
    ls = [1, 2, 3, 4, 5]
    lv = ListView(ls, lambda x: 1 < x < 5)
    assert list(lv) == [2, 3, 4]
    assert len(lv) == 3

def test_insert():
    ls = [1, 2, 3, 4, 5, 6, 7]
    lv = ListView(ls, lambda x: (1 < x < 4) or (7 > x > 4))
    assert list(lv) == [2, 3, 5, 6]

    # unmatch value error
    with pytest.raises(ValueError):
        lv.insert(3, 999)
    assert ls == [1, 2, 3, 4, 5, 6, 7]
    assert list(lv) == [2, 3, 5, 6]

    # matched value error
    lv.insert(3, 5.5)
    assert ls == [1, 2, 3, 4, 5, 5.5, 6, 7]
    assert list(lv) == [2, 3, 5, 5.5, 6]

    lv.insert(0, 4.5)
    assert ls == [1, 4.5, 2, 3, 4, 5, 5.5, 6, 7]
    assert list(lv) == [4.5, 2, 3, 5, 5.5, 6]

    lv.insert(1000, 3.5)
    assert ls == [1, 4.5, 2, 3, 4, 5, 5.5, 6, 7, 3.5]
    assert list(lv) == [4.5, 2, 3, 5, 5.5, 6, 3.5]

def test_setitem_int():
    ls = [1, 2, 3, 4, 5, 6, 7]
    lv = ListView(ls, lambda x: (1 < x < 4) or (7 > x > 4) or (x > 10))
    # lv: [2, 3, 5, 6]

    # normal
    lv[3] = 15
    assert list(lv) == [2, 3, 5, 15]
    assert ls == [1, 2, 3, 4, 5, 15, 7]

    # out of range
    with pytest.raises(IndexError):
        lv[4] = 100

    lv[-2] = 18
    assert list(lv) == [2, 3, 18, 15]
    assert ls == [1, 2, 3, 4, 18, 15, 7]

def test_setitem_slice():
    ls = [1, 2, 3, 4, 5, 6, 7]
    lv = ListView(ls, lambda x: (1 < x < 4) or (7 > x > 4) or (x > 10))
    # lv: [2, 3, 5, 6]

    # normal
    lv[1:] = [15, 18, 21]
    assert list(lv) == [2, 15, 18, 21]
    assert ls == [1, 2, 15, 4, 18, 21, 7]

    # out of range
    with pytest.raises(IndexError):
        lv[4] = 100

    lv[:] = [18]
    assert list(lv) == [18]
    assert ls == [1, 18, 4, 7]

def test_getitem_int():
    ls = [1, 2, 3, 4, 5, 6, 7]
    lv = ListView(ls, lambda x: (1 < x < 4) or (7 > x > 4) or (x > 10))
    # lv: [2, 3, 5, 6]

    # normal
    assert lv[2] == 5
    # out of range
    with pytest.raises(IndexError):
        print(lv[7])

def test_getitem_slice():
    ls = [1, 2, 3, 4, 5, 6, 7]
    lv = ListView(ls, lambda x: (1 < x < 4) or (7 > x > 4) or (x > 10))
    # lv: [2, 3, 5, 6]

    assert lv[:] == [2, 3, 5, 6]
    assert lv[1:] == [3, 5, 6]

def test_delitem_int():
    ls = [1, 2, 3, 4, 5, 6, 7]
    lv = ListView(ls, lambda x: (1 < x < 4) or (7 > x > 4) or (x > 10))
    # lv: [2, 3, 5, 6]

    # normal
    del lv[2]
    assert list(lv) == [2, 3, 6]
    assert ls == [1, 2, 3, 4, 6, 7]

    # out of range
    with pytest.raises(IndexError):
        del lv[7]

def test_delitem_slice():
    ls = [1, 2, 3, 4, 5, 6, 7]
    lv = ListView(ls, lambda x: (1 < x < 4) or (7 > x > 4) or (x > 10))
    # lv: [2, 3, 5, 6]

    del lv[1:]
    assert list(lv) == [2]
    assert ls == [1, 2, 4, 7]

    del lv[:]
    assert list(lv) == []
    assert ls == [1, 4, 7]

def test_sort():
    ls = [1, 7, 4, 6, 15, 0, 8, 2, 4]
    lv = ListView(ls, lambda x: (1 < x < 4) or (7 > x > 4) or (x > 10))
    assert list(lv) == [6, 15, 2]
    lv.sort()
    assert list(lv) == [2, 6, 15]
    assert ls == [1, 7, 4, 2, 6, 0, 8, 15, 4]
