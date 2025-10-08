"""
Cross-Platform UI Toolkit Scenario:
Build a GUI framework that creates consistent UI components for different operating systems. The system should support:

System should support:
    1. Windows UI
    2. macOS UI
    3. Linux UI

UI components:
    1. Button: Has a render() method that prints how it appears
    2. Checkbox: Has a render() method that prints how it appears
    3. TextField: Has a render() method that prints how it appears
"""
# Import libraries
from abc import ABC, abstractmethod


# Abstract Products
class Button(ABC):
    """Button interface acts as a bluprint for concrete buttons"""
    @abstractmethod
    def render(self):
        """Renders the button"""
        pass


class Checkbox(ABC):
    """Checkbox interface acts as a bluprint for concrete checkboxes"""
    @abstractmethod
    def render(self):
        """Renders the checkbox"""
        pass


class TextField(ABC):
    """Textfield interface acts as a bluprint for concrete textfields"""
    @abstractmethod
    def render(self):
        """Renders the textfield"""
        pass


# Concrete Products
class WindowsButton(Button):
    """Concrete button for creating Windows button"""
    def render(self):
        print("Rendering Windows button...")

class WindowsCheckbox(Checkbox):
    """Concrete checkbox for creating Windows checkbox"""
    def render(self):
        print("Rendering Windows checkbox...")

class WindowsTextField(TextField):
    """Concrete textfield for creating Windows textfield"""
    def render(self):
        print("Rendering Windows textfield...")


class MacButton(Button):
    """Concrete button for creating Mac button"""

    def render(self):
        print("Rendering Mac button...")


class MacCheckbox(Checkbox):
    """Concrete checkbox for creating Mac checkbox"""

    def render(self):
        print("Rendering Mac checkbox...")


class MacTextField(TextField):
    """Concrete textfield for creating Mac textfield"""

    def render(self):
        print("Rendering Mac textfield...")


class LinuxButton(Button):
    """Concrete button for creating Linux button"""

    def render(self):
        print("Rendering Linux button...")


class LinuxCheckbox(Checkbox):
    """Concrete checkbox for creating Linux checkbox"""

    def render(self):
        print("Rendering Linux checkbox...")


class LinuxTextField(TextField):
    """Concrete textfield for creating Linux textfield"""

    def render(self):
        print("Rendering Linux textfield...")


# Abstract Creator
class GUICreator(ABC):
    """Abstract factory class for creating GUI objects"""
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass

    @abstractmethod
    def create_textfield(self):
        pass


# Concrete creators
class WindowsGUICreator(GUICreator):
    """Concrete factory for creating Windows GUI"""
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

    def create_textfield(self) -> TextField:
        return WindowsTextField()


class MacGUICreator(GUICreator):
    """Concrete factory for creating Mac GUI"""

    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()

    def create_textfield(self) -> TextField:
        return MacTextField()


class LinuxGUICreator(GUICreator):
    """Concrete factory for creating Linux GUI"""

    def create_button(self) -> Button:
        return LinuxButton()

    def create_checkbox(self) -> Checkbox:
        return LinuxCheckbox()

    def create_textfield(self) -> TextField:
        return LinuxTextField()


# Client
class Client:
    def __init__(self, platform: GUICreator):
        self.platform = platform

    def create_ui(self):
        button = self.platform.create_button()
        checkbox = self.platform.create_checkbox()
        textfield = self.platform.create_textfield()

        button.render()
        checkbox.render()
        textfield.render()


if __name__ == "__main__":
    client = Client(platform=MacGUICreator())
    client.create_ui()