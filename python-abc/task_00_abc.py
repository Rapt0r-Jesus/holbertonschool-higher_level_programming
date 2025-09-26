#!/usr/bin/env python3
"""
Defines an abstract Animal class and its subclasses
dog and cat. Implements the sound method to
return a specific sound.
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an animal."""

    @abstractmethod
    def sound(self):
        """Abstract method that must be implemented by subclasses."""
        pass


class Dog(Animal):
    """Dog class that inherits from Animal."""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Cat class that inherits from Animal."""

    def sound(self):
        return "Meow"
