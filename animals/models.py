import numpy as np 


softmax = lambda x: np.exp(x) / sum(np.exp(x))

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
    
    def produce(self, food_increment: float) -> int:
        """Make it possible for the field to produce new food

        Returns:
            int: quantity of food after the production
        """
        p = self.food / 100
        if np.random.uniform() <= p:
            self.food = np.min([self.food + food_increment, 100])
        return self.food


class Config:
    
    def __init__(self, food_per_year: float, eaten_food: float, size: int, children: int=2):
        self.food_per_year = food_per_year
        self.eaten_food = eaten_food
        self.size = size
        self.children = children


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
    
    def iteration(self):
        # animals act
        # animals survive
        # fields production
        for f in self.fields.values():
            f.produce(food_increment=self.config.food_per_year)
    
    @property
    def food_to_numpy(self):
        return self._field_to_numpy(field='food')
    
    @property
    def danger_to_numpy(self):
        return self._field_to_numpy(field='danger')
    
    def _field_to_numpy(self, field: str):
        m = np.zeros((self.config.size, self.config.size))
        for (col, row), f in self.fields.items():
            m[self.config.size - (row + 1), col] = getattr(f, field)
        return m

class Animal:
    
    def __init__(self, position: tuple, 
                environment: Environment, 
                dna: np.ndarray = None,
                energy: float = 50.):
        self.age = 0
        self.energy = energy
        self.position = position
        self.env = environment
        self.age_death = None
        if dna is None:
            self.dna = np.random.random(size=(4, 6))
        else:
            self.dna = dna
    
    def read_food(self) -> float:
        return self.env.fields[self.position].food
    
    def read_danger(self) -> float:
        return self.env.fields[self.position].danger
    
    @property
    def state(self):
        return np.array([self.energy, self.age, self.read_food(), self.read_danger()])
    
    def _action_choice(self):
        actions = softmax(self.dna.T.dot(self.state))
        return np.random.choice(range(len(actions)), p=actions)
    
    def do(self):
        action = self._action_choice()
        if action < 4:
            self._move(direction=action)
        elif action == 5:
            self._eat()
        else:
            self._generate()
    
    def _move(self, direction: int):
        """The animal moves in the direction

        Args:
            direction (int): 0: N, 1: S, 2: E, 3: W
        """
        if direction == 0:
            self.position = (self.position[0], np.min([self.position[1] + 1, self.env.config.size - 1]))
        elif direction == 1:
            self.position = (self.position[0], np.max([self.position[1] - 1, 0]))
        elif direction == 2:
            self.position = (np.min([self.position[0] + 1, self.env.config.size - 1]), self.position[1])
        elif direction == 3:
            self.position = (np.max([self.position[0] - 1, 0]), self.position[1])
        else:
            pass
    
    def _eat(self):
        q = self.env.config.eaten_food
        self.env.fields[self.position].food -= q
        self.energy = np.min([self.energy + q, 100])
    
    def _generate(self) -> list:
        children = []
        p = self.energy / 100
        for c in range(self.env.config.children):
            if np.random.uniform() <= p:
                mutation = self.dna + np.random.normal(loc=0, scale=.01, size=self.dna.shape)
                child = Animal(position=self.position, environment=self.env, dna=mutation)
                children.append(child)
        return children
    
    def survive(self) -> bool:
        pass
