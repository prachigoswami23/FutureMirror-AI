import streamlit as st

from app.identity_agent import IdentityAgent
from app.future_simulator import FutureSimulator
from app.risk_detector import RiskDetector
from app.action_planner import ActionPlanner
from app.resource_agent import ResourceAgent
from app.career_score_agent import CareerScoreAgent
from app.report_generator import ReportGenerator
from app.future_metrics import FutureMetrics
from app.advanced_engine import AdvancedEngine

st.title("🚀 AI CAREER SIMULATOR (TOP 3 EDITION)")

# ---------------- AGENTS ----------------
agent = IdentityAgent()
sim = FutureSimulator()
risk = RiskDetector()
planner = ActionPlanner()
resource = ResourceAgent()
score_agent = CareerScoreAgent()
report = ReportGenerator()
metrics = FutureMetrics()
engine = AdvancedEngine()

# ---------------- INPUT ----------------
name = st.text_input("Enter your name")
goal1 = st.text_input("Primary Career Goal")
goal2 = st.text_input("Compare With (optional)")

# ---------------- BUTTON ----------------
if st.button("Run Simulation"):

    if not name or not goal1:
        st.warning("Enter required fields")
        st.stop()

    identity = agent.set_identity(name, goal1)
    prediction = sim.predict(goal1)
    risk_result = risk.analyze(goal1)
    steps = planner.plan(goal1)
    resources = resource.get_resources(goal1)
    score = score_agent.calculate_score(goal1)

    prob = metrics.success_probability(goal1)
    salary = metrics.salary_prediction(goal1)
    risk_level = metrics.risk_level(score)

    st.success(f"{name} wants to become {goal1}")

    # ---------------- TIMELINE ----------------
    st.subheader("📅 Future Timeline")
    st.write("""
    Year 1 → Learning Phase  
    Year 2 → Skill Building  
    Year 3 → Job / Internship  
    Year 5 → Growth Phase  
    Year 10 → Leadership Level
    """)

    # ---------------- OUTPUT ----------------
    st.subheader("🔮 Prediction")
    st.write(prediction)

    st.subheader("⚠️ Risk")
    st.write(risk_result)

    st.subheader("🛣️ Roadmap")
    for step in steps:
        st.write(step)

    st.subheader("📊 Career Metrics")
    st.write(f"Success Probability: {prob}%")
    st.progress(prob / 100)
    st.write(f"Salary: {salary}")
    st.write(f"Risk: {risk_level}")

    # ---------------- COMPARISON MODE ----------------
    if goal2:
        g1, g2 = engine.compare_goals(goal1, goal2)

        st.subheader("⚔️ Career Comparison")

        col1, col2 = st.columns(2)

        with col1:
            st.write(f"🔥 {goal1}")
            st.write(f"Salary Score: {g1['salary']}")
            st.write(f"Success: {g1['success']}%")
            st.write(f"Risk: {g1['risk']}%")

        with col2:
            st.write(f"🔥 {goal2}")
            st.write(f"Salary Score: {g2['salary']}")
            st.write(f"Success: {g2['success']}%")
            st.write(f"Risk: {g2['risk']}%")

    # ---------------- REPORT ----------------
    report.save_report(name, goal1, prediction, risk_result, score)
    st.success("📄 Report Generated")