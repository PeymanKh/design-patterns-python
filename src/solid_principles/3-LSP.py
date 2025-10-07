"""
3. Liskov Substitution Principle:
Objects of a derived/child class should be substitutable for objects of the base/parent
class without breaking the program.
"""

## BAD Design
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Square(Rectangle):
    """A square IS-A rectangle... right?"""

    def __init__(self, side):
        super().__init__(side, side)

    def set_width(self, width):
        # Square must keep both sides equal
        self.width = width
        self.height = width  # Changes both!

    def set_height(self, height):
        # Square must keep both sides equal
        self.width = height  # Changes both!
        self.height = height


# This breaks LSP!
def test_rectangle(rect: Rectangle):
    rect.set_width(5)
    rect.set_height(4)
    expected_area = 5 * 4  # 20
    actual_area = rect.calculate_area()
    assert expected_area == actual_area, f"Expected {expected_area}, got {actual_area}"


# Works fine
test_rectangle(Rectangle(2, 3))  # Passes

# BREAKS!
test_rectangle(Square(2))  # ✗ Fails! Area is 16, not 20




## Good Design
from abc import ABC, abstractmethod


class Shape(ABC):
    """Base interface - no assumptions about dimensions"""

    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Square(Shape):
    """Square is NOT a Rectangle - it's a Shape!"""

    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2
