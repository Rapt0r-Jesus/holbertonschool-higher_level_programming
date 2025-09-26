#!/usr/bin/env python3
"""Create a class named CountedIterator that extends the built-in 
iterator obtained from the iter function."""


class CountedIterator:
    """Custom iterator that counts how many items have been iterated."""

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """Retourne combien d’éléments ont été consommés."""
        return self.count
