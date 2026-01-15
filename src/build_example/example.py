"""Example class definition."""

class Example:
    """Not a very intersting class, just a MWE.

    'data' is a dictionary that contains words and pre-computed lengths of words.
    """

    def __init__(self):
        """Create an empty data structure."""
        self.data = {}

    def insert_word(self, word):
        """Insert a new word into the internal data dictionary.

        Imagine that pre-computing word length represents an expensive calculation that
        we want to perform once during build time.
        """
        self.data[word] = len(word)
