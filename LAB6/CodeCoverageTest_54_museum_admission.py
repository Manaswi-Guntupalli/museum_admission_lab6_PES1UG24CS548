"""Stage 1: execute every statement in the unmodified application."""

import pytest

from museum_admission import gallery_entry, group_discount, ticket_price


@pytest.mark.parametrize(
    "category,age,day,tour,expected",
    [
        pytest.param("adult", 30, "tuesday", False, 300, id="adult-weekday"),
        pytest.param("student", 20, "monday", True, 125, id="student-monday-tour"),
        pytest.param("senior", 70, "saturday", True, 350, id="senior-weekend-tour"),
        pytest.param("child", 4, "sunday", True, 0, id="under-five-free"),
        pytest.param("child", 5, "wednesday", False, 100, id="age-five-paid"),
    ],
)
def test_ticket_prices(category, age, day, tour, expected):
    assert ticket_price(category, age, day, tour) == expected


@pytest.mark.parametrize(
    "category,age,message",
    [("unknown", 30, "unknown category"), ("adult", -1, "invalid age")],
)
def test_invalid_ticket(category, age, message):
    with pytest.raises(ValueError, match=f"^{message}$"):
        ticket_price(category, age, "tuesday", False)


@pytest.mark.parametrize(
    "size,school,expected",
    [(20, True, 40), (19, True, 25), (15, False, 20), (8, False, 10), (4, False, 0)],
)
def test_group_discounts(size, school, expected):
    assert group_discount(size, school) == expected


def test_invalid_group():
    with pytest.raises(ValueError, match="^invalid group size$"):
        group_discount(0, False)


@pytest.mark.parametrize(
    "inside,capacity,slot,expected",
    [(100, 100, False, "wait"), (90, 100, False, "queue"), (50, 100, False, "enter")],
)
def test_gallery_decisions(inside, capacity, slot, expected):
    assert gallery_entry(inside, capacity, slot) == expected
