class Letterbox:
    """
        The Letterbox class is used to deliver and remove letters
        while tracking if a letter is in the letterbox.
        ...

        Attributes
        ----------
        flag_up : bool
            empty/full status of the letterbox

        Methods
        ----------
        letter_delivered(self)
            Sets the flag up property to True
        letter_removed
            Sets the flag up property to False
    """

    def __init__(self):
        self.flag_up = False

    def letter_delivered(self):
        self.flag_up = True

    def letter_removed(self):
        self.flag_up = False
