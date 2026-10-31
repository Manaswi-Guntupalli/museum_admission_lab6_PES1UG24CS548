"""Additive coverage milestone tests for the unchanged Museum Admission module."""
import pytest
from museum_admission import ticket_price, group_discount, gallery_entry


def test_adult_weekday():
    assert ticket_price("adult", 30, "tuesday", False) == 300


def test_small_group():
    assert group_discount(4, False) == 0


def test_ticket_price_student_20_saturday_true():
    assert ticket_price('student', 20, 'saturday', True) == 250


def test_ticket_price_adult_30_monday_true():
    assert ticket_price('adult', 30, 'monday', True) == 250


def test_ticket_price_child_0_tuesday_false():
    assert ticket_price('child', 0, 'tuesday', False) == 0


def test_ticket_price_unknown_30_tuesday_false():
    with pytest.raises(ValueError, match='^unknown category$'):
        ticket_price('unknown', 30, 'tuesday', False)


def test_group_discount_1_true():
    assert group_discount(1, True) == 25


def test_ticket_price_adult_negative_1_tuesday_false():
    with pytest.raises(ValueError, match='^invalid age$'):
        ticket_price('adult', -1, 'tuesday', False)


def test_group_discount_20_true():
    assert group_discount(20, True) == 40


def test_group_discount_8_false():
    assert group_discount(8, False) == 10


def test_group_discount_15_false():
    assert group_discount(15, False) == 20


def test_gallery_entry_100_100_false():
    assert gallery_entry(100, 100, False) == 'wait'


def test_gallery_entry_0_100_false():
    assert gallery_entry(0, 100, False) == 'enter'


def test_gallery_entry_90_100_false():
    assert gallery_entry(90, 100, False) == 'queue'


def test_group_discount_negative_1_false():
    with pytest.raises(ValueError, match='^invalid group size$'):
        group_discount(-1, False)
