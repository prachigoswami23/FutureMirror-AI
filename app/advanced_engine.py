class AdvancedEngine:

    def compare_goals(self, goal1, goal2):

        data = {
            "coder": {"salary": 85, "success": 85, "risk": 30},
            "doctor": {"salary": 95, "success": 90, "risk": 20},
            "teacher": {"salary": 60, "success": 80, "risk": 25}
        }

        g1 = data.get(goal1.lower(), {"salary": 50, "success": 70, "risk": 50})
        g2 = data.get(goal2.lower(), {"salary": 50, "success": 70, "risk": 50})

        return g1, g2