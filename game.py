"""
Game
"""
class Room:
    """
    class Room
    >>> kitchen = Room("Kitchen")
    >>> kitchen.set_description("A dank and dirty room buzzing with flies.")
    >>> dining_hall = Room("Dining Hall")
    >>> dining_hall.set_description("A large room with ornate golden decorations on each wall.")
    >>> ballroom = Room("Ballroom")
    >>> ballroom.set_description("A vast room with a shiny wooden floor.\
 Huge candlesticks guard the entrance.")
    >>> kitchen.link_room(dining_hall, "south")
    >>> dining_hall.link_room(kitchen, "north")
    >>> dining_hall.link_room(ballroom, "west")
    >>> ballroom.link_room(dining_hall, "east")
    """
    def __init__(self, current_room):
        """
        Init
        """
        self.current_room = current_room
        self.description = None
        self.rooms = {}
        self.item = None
        self.character = None

    def set_description(self, description):
        """
        Information about room.
        """
        self.description = description

    def link_room(self, room_name, direction):
        """
        Possible rooms to go into.
        """
        self.rooms[direction] = room_name

    def set_character(self, inhabitant):
        """
        Information about character
        """
        if inhabitant:
            self.character = inhabitant
        else:
            self.character = None
        return None

    def get_character(self):
        """
        Gets information about character
        """
        return self.character

    def set_item(self, item):
        """
        setter
        """
        self.item = item

    def get_items(self):
        """
        getter
        """
        return self.item

    def get_details(self):
        """
        Gives details about room
        """
        print(self.current_room)
        print('--------------------')
        print(self.description)
        for key, value in self.rooms.items():
            print(f'{value.current_room} is {key}')

    def move(self, command):
        """
        Gets into another room
        """
        if command not in list(self.rooms.keys()):
            print('No way.')
            return self
        for key, value in self.rooms.items():
            if command == key:
                return value

class Character:
    """
    class Character
    """
    def __init__(self, name, description):
        """
        Init
        """
        self.name = name
        self.description = description

    def set_conversation(self, conversation):
        """
        setter
        """
        self.conversation = conversation

    def describe(self):
        """
        Gives information abouth character
        """
        print(f'{self.name} is here!')
        print(self.description)

    def talk(self):
        """
        Gives information abouth character says
        """
        print(f"[{self.name} says]: {self.conversation}")

class Enemy(Character):
    """
    успадковує class Character
    """
    def __init__(self, name, description):
        """
        Init
        """
        super().__init__(name, description)
        self.defeated = 0

    def set_weakness(self, weakness):
        """
        setter
        """
        self.weakness = weakness

    def fight(self, fight_with):
        """
        Determines if you have necessary item to win
        """
        if fight_with == self.weakness:
            self.defeated += 1
            return True
        else:
            return False

    def get_defeated(self):
        """
        Returns amount of times you defeated enemy
        """
        return self.defeated

class Item:
    """
    class Item
    """
    def __init__(self, name):
        """
        Init
        """
        self.name = name

    def set_description(self, description):
        """
        setter
        """
        self.description = description

    def get_description(self):
        """
        getter
        """
        return self.description

    def describe(self):
        """
        Gives information about item
        """
        print(f"The {[self.name]} - {self.description}.")

    def get_name(self):
        """
        getter
        """
        return self.name

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
