class Letter:
    """
        The Letter class is used read and write letters while tracking a letter's read status
        and storing a message in the letter.
        ...

        Attributes
        ----------
        is_read : bool
            read status of the letter
        contents: str
            contents of the letter

        Methods
        ----------
        reads_letter(self)
            Displays the content of the letter and sets the read status to True
        write_letter(self, message)
            Sets the contents of the letter as the message inserted
    """

    def __init__(self):
        self.contents = ""
        self.is_read = False

    def read_letter(self):
        self.is_read = True
        print("Letter reads:", self.contents)

    def write_letter(self, message):
        self.contents = message
