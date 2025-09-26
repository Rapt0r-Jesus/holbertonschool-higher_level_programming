#!/usr/bin/env python3
"""
Defines the Verboselist class a subclass of list that provides
verbose output for list modification methods.
"""


class VerboseList(list):
    """Custom list class that prints notifications on modifications."""

    def append(self, item):
        """Add an item and notify."""
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        """Extend list and notify."""
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with {count} items.")

    def remove(self, item):
        """Remove item and notify."""
        print(f"Removed {item} from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pop item and notify."""
        item = super().pop(index)
        print(f"Popped {item} from the list.")
        return item
