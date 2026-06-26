class IdentityAgent:
    def __init__(self):
        self.name = ""
        self.goal = ""

    def set_identity(self, name, goal):
        self.name = name
        self.goal = goal
        return f"{self.name} wants to become {self.goal}"