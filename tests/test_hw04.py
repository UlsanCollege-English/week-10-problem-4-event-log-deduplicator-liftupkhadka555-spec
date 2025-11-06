
from main import make_set, add, contains, remove, size

# ---- Normal tests (4) ----

def test_empty_set_size():
    s = make_set(5)
    assert size(s) == 0

def test_add_and_contains():
    s = make_set(7)
    assert add(s, "ev1") is True
    assert contains(s, "ev1") is True
    assert size(s) == 1

def test_add_duplicate_returns_false():
    s = make_set(3)
    add(s, "x")
    assert add(s, "x") is False
    assert size(s) == 1

def test_remove_present_key():
    s = make_set(5)
    add(s, "a"); add(s, "b")
    assert remove(s, "a") is True
    assert contains(s, "a") is False
    assert size(s) == 1

# ---- Edge-case tests (3) ----

def test_remove_missing_key():
    s = make_set(5)
    assert remove(s, "nope") is False

def test_contains_on_empty_buckets():
    s = make_set(8)
    assert contains(s, "ghost") is False

def test_collisions_are_handled():
    s = make_set(2)  # force collisions
    keys = ["AA", "BB", "CC"]
    for k in keys:
        assert add(s, k) is True
    for k in keys:
        assert contains(s, k) is True
    assert size(s) == 3

# ---- More-complex tests (3) ----

def test_many_adds_and_removes():
    s = make_set(11)
    keys = [f"id{i}" for i in range(50)]
    for k in keys:
        add(s, k)
    assert size(s) == 50
    for k in keys[::3]:
        remove(s, k)
    assert size(s) == 50 - len(keys[::3])

def test_readd_after_remove():
    s = make_set(5)
    add(s, "k"); remove(s, "k")
    assert contains(s, "k") is False
    assert add(s, "k") is True

def test_collision_heavy_still_correct():
    s = make_set(3)
    for i in range(30):
        add(s, f"K{i}")
    # random spot checks
    assert contains(s, "K0") is True
    assert contains(s, "K29") is True
