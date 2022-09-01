from Alice import Alice
from Bob import Bob
from Letter import Letter
from Letterbox import Letterbox


letter1 = Letter()
alice = Alice()
bob = Bob()
letterbox = Letterbox()

alice.reads_letter(letter1)
alice.writes_letter(letter1)
print("Letter read?", letter1.is_read)
alice.reads_letter(letter1)
print("Letter read?", letter1.is_read)
bob.checks_letterbox(letterbox)
alice.delivers_letter(letterbox)
bob.checks_letterbox(letterbox)
bob.reads_letter(letter1)
print("Letter read?", letter1.is_read)
