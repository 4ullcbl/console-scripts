

class Player:
    def __init__(self, char="@", loc=0, items = []):
        self.char = char
        self.loc = loc
        self.items = items
    
    def set_loc(self, loc: int):
        self.loc = loc

    def add_item(self, item: str):
        self.items.append(item)
