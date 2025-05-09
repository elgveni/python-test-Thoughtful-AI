def sort(width, height, length, mass):
    """
    Sorts a package into one of the categories: STANDARD, SPECIAL, REJECTED
    """
    volume = width * height * length
    is_bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150
    is_heavy = mass >= 20

    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"


# --- Test ---
def run_tests():
    test_cases = [
        (10, 10, 10, 5, "STANDARD"),
        (200, 10, 10, 5, "SPECIAL"),
        (10, 10, 10, 25, "SPECIAL"),
        (200, 200, 200, 25, "REJECTED"),
        (100, 100, 100, 19.9, "SPECIAL"),
        (100, 100, 100, 20, "REJECTED"),
        (100, 100, 100, 100, "REJECTED"),
        (10, 10, 151, 5, "SPECIAL"),
    ]

    for i, (w, h, l, m, expected) in enumerate(test_cases):
        result = sort(w, h, l, m)
        assert result == expected, f"Test {i + 1} failed: got {result}, expected {expected}"
        print(f"Test {i + 1} passed {expected}")


if __name__ == "__main__":
    run_tests()