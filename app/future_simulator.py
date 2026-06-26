class FutureSimulator:
    def predict(self, goal):
        goal = goal.lower()

        if goal == "coder":
            return "If you practice consistently, you can become a software developer in 1-2 years."

        elif goal == "doctor":
            return "You will need years of medical education and training to become a doctor."

        elif goal == "teacher":
            return "With strong communication skills and subject knowledge, you can become a successful teacher."

        else:
            return f"With dedication and effort, you can build a career as a {goal}."