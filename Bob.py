class Bob:

    def __init__(self):
        self.has_letter = False

    def writes_letter(self, letter):
        self.has_letter = True
        letter.is_read = False

    def reads_letter(self, letter):
        if self.has_letter:
            if letter.is_read:
                print("Someone has already read your letter!")
            else:
                letter.is_read = True
        else:
            print("The item 'Letter' is not in your inventory")

    def checks_letterbox(self, letterbox):
        if letterbox.contains_letter:
            self.has_letter = True
            letterbox.contains_letter = False
        else:
            print("Letterbox is empty")

    def delivers_letter(self, letterbox):
        if self.has_letter:
            letterbox.contains_letter = True
            self.has_letter = False
