from Person import Person
from Letter import Letter
from Letterbox import Letterbox

"""Code for demonstrating how the classes interact with each other"""
letter = Letter()
alice = Person("Alice")
bob = Person("Bob")
letterbox = Letterbox()

alice.reads_letter(letter)
alice.writes_letter(letter, "Hi Bob")
bob.checks_letterbox(letterbox)
alice.delivers_letter(letterbox)
bob.checks_letterbox(letterbox)
bob.reads_letter(letter)
bob.reads_letter(letter)
