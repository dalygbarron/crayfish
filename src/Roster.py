class Roster:
    """Contains a list of mediums and checks for strikes against any of them."""
    def __init__(self):
        self.items = []

    def add(self, item):
        """Add an item to the roster"""
        self.items.append(item)

    def hit(self, ray, min, max):
        """Checks for hits against anything in the roster."""
        winner = None
        for item in self.items:
            strike = item.hit(ray, min, max)
            if ((strike and not winner ) or (strike and winner and strike.distance < winner.distance)):
                winner = strike
        return winner
