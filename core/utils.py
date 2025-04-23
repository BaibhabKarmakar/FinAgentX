class BaseAgent: 
    def __init__(self , name):
        self.name = name
    
    def run(self , input_data):
        raise NotImplementedError("Subclasses must implement this method")