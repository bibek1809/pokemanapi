from entity.entity import Entity

class Pokemon(Entity):
    def __init__(self, name=None, type=None, image=None):
        self.name: str = name
        self.type: str = type
        self.image: str = image