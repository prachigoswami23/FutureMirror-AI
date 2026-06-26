class RiskDetector:
    def analyze(self, goal):
        goal = goal.lower()

        risky_goals = ["hacker", "illegal hacker", "criminal"]

        if goal in risky_goals:
            return "Warning: This goal may involve harmful or illegal activities."

        elif goal == "doctor":
            return "This is a respected career but requires long-term study and dedication."

        elif goal == "coder":
            return "This is a safe and high-demand career path."

        elif goal == "teacher":
            return "This is a stable career that requires communication and teaching skills."

        else:
            return "No major risks detected. Focus on learning and consistency."