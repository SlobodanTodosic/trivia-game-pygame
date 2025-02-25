class Player:
    _instance = None  # Variable to store the class instance

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Player, cls).__new__(cls) # Create object if no object
        return cls._instance # Return the instance of the class

    def __init__(self, name="Default Player"):
        if not hasattr(self, 'initialized'):  # If not already initiated, initiate new object
            self.name = name
            self.score = 0
            self.initialized = True  # To ensure __init__ runs only once