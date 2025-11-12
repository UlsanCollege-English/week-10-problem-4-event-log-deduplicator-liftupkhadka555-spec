"""
HW04 — Simple Hash Set using Chaining.
No type hints. Standard library only.
"""

def make_set(m):
    """Return a new hash-set with m buckets."""
    # store buckets + count in a small dict
    return {"buckets": [[] for _ in range(m)], "count": 0}

def _bucket(s, key):
    """Return the bucket corresponding to key."""
    m = len(s["buckets"])
    return s["buckets"][hash(key) % m]

def add(s, key):
    """Add key if not present. Return True if added, False if duplicate."""
    b = _bucket(s, key)
    for k in b:
        if k == key:
            return False
    b.append(key)
    s["count"] += 1
    return True

def contains(s, key):
    """Return True if key is in set, else False."""
    b = _bucket(s, key)
    for k in b:
        if k == key:
            return True
    return False

def remove(s, key):
    """Remove key if present. Return True if removed, False if not."""
    b = _bucket(s, key)
    for i, k in enumerate(b):
        if k == key:
            b.pop(i)
            s["count"] -= 1
            return True
    return False

def size(s):
    """Return number of stored keys."""
    return s["count"]


if __name__ == "__main__":
    # Optional manual check (do nothing by default)
    pass