class ResourceAgent:
    def get_resources(self, goal):
        goal = goal.lower()

        if goal == "coder":
            return [
                "Python Official Tutorial",
                "Kaggle Learn",
                "FreeCodeCamp",
                "GitHub"
            ]

        elif goal == "doctor":
            return [
                "NCERT Biology",
                "NEET Preparation Materials",
                "Medical Entrance Practice Tests"
            ]

        elif goal == "teacher":
            return [
                "Teaching Skills Courses",
                "Public Speaking Practice",
                "Educational Psychology Resources"
            ]

        else:
            return [
                f"Research online courses related to {goal}",
                f"Follow professionals working as {goal}",
                f"Join communities related to {goal}"
            ]