from fpdf import FPDF

class ReportGenerator:
    def save_report(self, name, goal, prediction, risk, score):

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, txt="AI CAREER REPORT", ln=True, align='C')

        pdf.ln(10)
        pdf.cell(200, 10, txt=f"Name: {name}", ln=True)
        pdf.cell(200, 10, txt=f"Goal: {goal}", ln=True)

        pdf.ln(5)
        pdf.cell(200, 10, txt="Prediction:", ln=True)
        pdf.multi_cell(0, 10, prediction)

        pdf.ln(5)
        pdf.cell(200, 10, txt="Risk Analysis:", ln=True)
        pdf.multi_cell(0, 10, risk)

        pdf.ln(5)
        pdf.cell(200, 10, txt=f"Career Score: {score}/100", ln=True)

        pdf.output("career_report.pdf")