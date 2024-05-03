class Field:
    """ Represents a field in the environment
    """
    
    def __init__(self, position: tuple, food: float = 10., danger: float = 10.):
        self.position = position
        self.food = food 
        self.danger = danger
        
    def __repr__(self):
        return "F ({}, {}), food: {}, danger: {}".format(
            self.position[0], self.position[1], 
            self.food, self.danger
            )
    
    def produce(self) -> int:
        """Make it possible for the field to produce new food

        Returns:
            int: quantity of food after the production
        """
        return self.food
    
    
class Config:
    
    def __init__(self, food_per_year: float, eaten_food: float, size: int):
        self.food_per_year = food_per_year
        self.eaten_food = eaten_food
        self.size = size


class Environment:
    
    def __init__(self, config: Config):
        self.config = config
        self.fields = {}
        for x in range(self.config.size):
            for y in range(self.config.size):
                f = Field(position=(x, y))
                self.fields[(x, y)] = f
        assert len(self.fields) == self.config.size ** 2
    
    def set_food(self, food: float, from_x: int, to_x: int, from_y: int, to_y: int):
        for x in range(from_x, to_x):
            for y in range(from_y, to_y):
                field = self.fields[(x, y)]
                field.food = food

    def set_danger(self, danger: float, from_x: int, to_x: int, from_y: int, to_y: int):
        for x in range(from_x, to_x):
            for y in range(from_y, to_y):
                field = self.fields[(x, y)]
                field.danger = danger
