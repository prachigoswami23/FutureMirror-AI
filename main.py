from app.identity_agent import IdentityAgent
from app.future_simulator import FutureSimulator
from app.risk_detector import RiskDetector
from app.action_planner import ActionPlanner
from app.resource_agent import ResourceAgent
from app.career_score_agent import CareerScoreAgent
class ReportGenerator:
    def save_report(self, name, goal, prediction, risk, score):
        with open("career_report.txt", "w") as file:
            file.write("=== AI CAREER REPORT ===\n\n")
            file.write(f"Name: {name}\n")
            file.write(f"Goal: {goal}\n\n")

            file.write("Prediction:\n")
            file.write(prediction + "\n\n")

            file.write("Risk Analysis:\n")
            file.write(risk + "\n\n")

            file.write("Career Score:\n")
            file.write(str(score) + "/100\n")

agent = IdentityAgent()
sim = FutureSimulator()
risk = RiskDetector()
planner = ActionPlanner()
resource = ResourceAgent()
score_agent = CareerScoreAgent()
report = ReportGenerator()

print("=== AI CAREER COACH ===")

name = input("Apna naam likho: ")
goal = input("Apna career goal likho: ")

print("\n--- RESULT ---")

identity_result = agent.set_identity(name, goal)
prediction = sim.predict(goal)
risk_result = risk.analyze(goal)

print(identity_result)
print(prediction)
print(risk_result)

print("\n--- ROADMAP ---")
steps = planner.plan(goal)

for step in steps:
    print(step)

print("\n--- RESOURCES ---")
resources = resource.get_resources(goal)

for item in resources:
    print("-", item)

print("\n--- CAREER SCORE ---")
score = score_agent.calculate_score(goal)

print("Career Readiness Score:", score, "/100")
print(score_agent.feedback(score))
report.save_report(
    name,
    goal,
    prediction,
    risk_result,
    score
)

print("\nReport saved as career_report.txt")
