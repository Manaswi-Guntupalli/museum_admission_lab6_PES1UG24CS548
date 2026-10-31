"""Stage 2: standalone decision, boundary, and short-circuit tests."""

import pytest

from museum_admission import gallery_entry, group_discount, ticket_price


@pytest.mark.parametrize(
    "category,age,day,tour,expected",
    [
        ("adult", 30, "tuesday", False, 300),
        ("student", 20, "tuesday", False, 150),
        ("child", 5, "tuesday", False, 100),
        ("senior", 70, "tuesday", False, 200),
        ("adult", 30, "monday", False, 150),
        ("student", 20, "monday", False, 75),
        ("child", 5, "monday", False, 50),
        ("senior", 70, "monday", False, 100),
        ("adult", 30, "saturday", False, 350),
        ("adult", 30, "sunday", False, 350),
        ("student", 20, "saturday", True, 250),
        ("child", 5, "sunday", True, 250),
        ("senior", 70, "saturday", True, 350),
        ("adult", 30, "tuesday", True, 400),
        ("student", 20, "tuesday", True, 200),
        ("adult", 30, "monday", True, 250),
        ("student", 20, "monday", True, 125),
        ("child", 5, "monday", True, 150),
        ("senior", 70, "monday", True, 200),
        ("child", 0, "tuesday", False, 0),
        ("child", 4, "sunday", True, 0),
        ("adult", 4, "monday", True, 0),
    ],
)
def test_ticket_decisions(category, age, day, tour, expected):
    """Free admission precedes day/tour adjustments; tour follows day pricing."""
    assert ticket_price(category, age, day, tour) == expected


@pytest.mark.parametrize(
    "category,age,message",
    [
        ("unknown", 30, "unknown category"),
        ("unknown", 0, "unknown category"),
        ("unknown", -1, "unknown category"),
        ("adult", -1, "invalid age"),
        ("child", -1, "invalid age"),
    ],
)
def test_validation_order(category, age, message):
    with pytest.raises(ValueError, match=f"^{message}$"):
        ticket_price(category, age, "tuesday", False)


@pytest.mark.parametrize("size", [-1, 0])
@pytest.mark.parametrize("school", [False, True])
def test_invalid_group(size, school):
    with pytest.raises(ValueError, match="^invalid group size$"):
        group_discount(size, school)


@pytest.mark.parametrize(
    "size,school,expected",
    [
        (1, True, 25), (7, True, 25), (8, True, 25),
        (14, True, 25), (15, True, 25), (19, True, 25),
        (20, True, 40), (21, True, 40),
        (1, False, 0), (7, False, 0),
        (8, False, 10), (9, False, 10), (14, False, 10),
        (15, False, 20), (16, False, 20), (20, False, 20),
    ],
)
def test_discount_boundaries(size, school, expected):
    assert group_discount(size, school) == expected


@pytest.mark.parametrize(
    "inside,capacity,slot,expected",
    [
        (0, 100, False, "enter"),
        (89, 100, False, "enter"),
        (89, 100, True, "enter"),
        (90, 100, False, "queue"),
        (90, 100, True, "enter"),
        (91, 100, False, "queue"),
        (99, 100, False, "queue"),
        (99, 100, True, "enter"),
        (100, 100, False, "wait"),
        (100, 100, True, "wait"),
        (101, 100, False, "wait"),
        (101, 100, True, "wait"),
        (0, 0, True, "wait"),
        (2, 3, False, "enter"),
        (9, 11, False, "enter"),
        (10, 11, False, "queue"),
        (10, 11, True, "enter"),
    ],
)
def test_gallery_boundaries(inside, capacity, slot, expected):
    """Exercise all outcomes of the compound condition and full-gallery priority."""
    assert gallery_entry(inside, capacity, slot) == expected
