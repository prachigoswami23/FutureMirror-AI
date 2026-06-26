class ActionPlanner:
    def plan(self, goal):
        goal = goal.lower()

        if goal == "coder":
            return [
                "Step 1: Learn Python programming",
                "Step 2: Practice coding daily",
                "Step 3: Build real-world projects",
                "Step 4: Learn Git and GitHub",
                "Step 5: Apply for internships and jobs"
            ]

        elif goal == "doctor":
            return [
                "Step 1: Focus on Biology and Chemistry",
                "Step 2: Prepare for medical entrance exams",
                "Step 3: Complete medical education",
                "Step 4: Gain clinical experience",
                "Step 5: Apply for medical practice"
            ]

        elif goal == "teacher":
            return [
                "Step 1: Master your subject",
                "Step 2: Improve communication skills",
                "Step 3: Gain teaching experience",
                "Step 4: Learn classroom management",
                "Step 5: Apply for teaching positions"
            ]

        else:
            return [
                f"Step 1: Research the {goal} field",
                f"Step 2: Learn required skills for {goal}",
                f"Step 3: Practice consistently",
                f"Step 4: Build experience",
                f"Step 5: Apply for opportunities"
            ]