#!/usr/bin/env python3
"""
Contains mixins and a
Dragon class demonstrating multiple inheritance.
"""


class SwimMixin:
    """Mixin pour ajouter la capacité de nager."""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin pour ajouter la capacité de voler."""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Classe Dragon qui combine SwimMixin et FlyMixin."""

    def roar(self):
        print("The dragon roars!")
