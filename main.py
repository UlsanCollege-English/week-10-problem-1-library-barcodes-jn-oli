# main.py
import builtins
import random
builtins.random = random  # expose random so tests using it without import still work

def hash_basic(key: str) -> int:
    """Compute a simple hash based on sum of Unicode codepoints."""
    if not isinstance(key, str):
        key = str(key)
    return sum(ord(c) for c in key)


def make_table(n: int):
    """Create a hash table with n buckets (each bucket is a list)."""
    return [[] for _ in range(n)]


def _bucket(table, key):
    """Return the bucket for a given key."""
    h = hash_basic(key)
    return table[h % len(table)]


def put(table, key, value):
    """Insert or update a key-value pair in the table."""
    if not isinstance(key, str):
        key = str(key)

    bucket = _bucket(table, key)
    for i, (k, v) in enumerate(bucket):
        if k == key:
            bucket[i] = (key, value)
            return
    bucket.append((key, value))


def get(table, key):
    """Return the value for the given key, or None if not found."""
    if not isinstance(key, str):
        key = str(key)

    bucket = _bucket(table, key)
    for k, v in bucket:
        if k == key:
            return v
    return None


def has_key(table, key) -> bool:
    """Return True if the key exists in the table."""
    if not isinstance(key, str):
        key = str(key)

    bucket = _bucket(table, key)
    for k, _ in bucket:
        if k == key:
            return True
    return False


def size(table) -> int:
    """Return total number of entries in the table."""
    return sum(len(bucket) for bucket in table)
