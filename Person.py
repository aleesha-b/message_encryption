class Person:
    """
        The Person class is used to interact with the letterbox and letter classes
        and output the results of eac interaction.
        ...

        Attributes
        ----------
        has_letter : bool
            status of letter inventory

        Methods
        -------
        writes_letter(self, letter):
            Writes a letter
        reads_letter(self, letter):
            Reads a letter
        checks_letterbox(self, letterbox):
            Checks the letterbox, if there is a letter adds the letter to inventory
        delivers_letter(self, letterbox):
            Delivers a letter to the letterbox, removes letter from inventory
    """

    def __init__(self, name: str):
        self.name = name
        self.has_letter = False

    def writes_letter(self, letter, message):
        self.has_letter = True
        letter.write_letter(message)
        print(self.name, "has successfully written a letter, time to deliver it!")

    def reads_letter(self, letter):
        if self.has_letter:
            if letter.is_read:
                print(self.name, "someone has already read your letter!")
            letter.read_letter()
            return
        print(self.name, "the item 'Letter' is not in your inventory")

    def checks_letterbox(self, letterbox):
        if letterbox.flag_up:
            self.has_letter = True
            letterbox.letter_removed()
            print(self.name, "you have collected a letter from the Letterbox")
            return
        print(self.name + "'s letterbox is empty")

    def delivers_letter(self, letterbox):
        if self.has_letter:
            letterbox.letter_delivered()
            self.has_letter = False
            print(self.name, "has successfully delivered a letter")
            return
        print(self.name, "does not have a 'Letter' to deliver")
