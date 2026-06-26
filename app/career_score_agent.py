class CareerScoreAgent:
    def calculate_score(self, goal):
        goal = goal.lower()

        if goal == "coder":
            return 85

        elif goal == "doctor":
            return 90

        elif goal == "teacher":
            return 80

        else:
            return 75

    def feedback(self, score):
        if score >= 90:
            return "Excellent career path with strong commitment required."

        elif score >= 80:
            return "Strong career choice. Keep learning and building skills."

        else:
            return "Good career goal. Focus on consistency and growth."