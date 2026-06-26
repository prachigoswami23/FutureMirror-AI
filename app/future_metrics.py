class FutureMetrics:

    def success_probability(self, goal):
        goal = goal.lower()

        if goal in ["coder", "software engineer", "developer"]:
            return 85
        elif goal in ["doctor", "medical"]:
            return 90
        elif goal in ["teacher"]:
            return 80
        else:
            return 70

    def salary_prediction(self, goal):
        goal = goal.lower()

        if goal in ["coder", "developer", "software engineer"]:
            return "₹3 LPA - ₹25 LPA"
        elif goal in ["doctor"]:
            return "₹6 LPA - ₹50 LPA"
        elif goal in ["teacher"]:
            return "₹2 LPA - ₹12 LPA"
        else:
            return "₹2 LPA - ₹10 LPA"

    def risk_level(self, score):
        if score >= 85:
            return "Low Risk"
        elif score >= 70:
            return "Medium Risk"
        else:
            return "High Risk"