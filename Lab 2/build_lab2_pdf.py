from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.graphics.shapes import Drawing, Line, String, Circle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "lab2-deliverable.pdf"
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="CenterTitle", parent=styles["Title"], alignment=TA_CENTER, textColor=colors.HexColor("#1f4e79")))
styles.add(ParagraphStyle(name="Section", parent=styles["Heading2"], textColor=colors.HexColor("#1f4e79"), spaceBefore=8, spaceAfter=5))
styles.add(ParagraphStyle(name="Small", parent=styles["BodyText"], fontSize=8.2, leading=10))

def P(text, style="BodyText"):
    return Paragraph(text, styles[style])

def burndown():
    d = Drawing(500, 260)
    left, bottom, width, height = 55, 35, 400, 180
    d.add(String(250, 240, "Sprint 1 Burndown Chart", textAnchor="middle", fontName="Helvetica-Bold", fontSize=13, fillColor=colors.HexColor("#1f4e79")))
    d.add(Line(left, bottom, left, bottom + height))
    d.add(Line(left, bottom, left + width, bottom))
    for y in range(0, 26, 5):
        yy = bottom + y / 25 * height
        d.add(Line(left, yy, left + width, yy, strokeColor=colors.HexColor("#dddddd")))
        d.add(String(left - 8, yy - 3, str(y), textAnchor="end", fontSize=8))
    actual = [23, 20, 15, 10, 5, 0, 0]
    ideal = [23 - (23 / 6) * i for i in range(7)]
    def point(i, value):
        return left + i / 6 * width, bottom + value / 25 * height
    for values, colour, dash in [(ideal, colors.grey, [4, 3]), (actual, colors.HexColor("#1565c0"), None)]:
        for i in range(6):
            x1, y1 = point(i, values[i])
            x2, y2 = point(i + 1, values[i + 1])
            line = Line(x1, y1, x2, y2, strokeColor=colour, strokeWidth=2)
            if dash:
                line.strokeDashArray = dash
            d.add(line)
        if values is actual:
            for i, value in enumerate(values):
                x, y = point(i, value)
                d.add(Circle(x, y, 3.5, fillColor=colour, strokeColor=colour))
    for i in range(7):
        d.add(String(left + i / 6 * width, bottom - 15, str(i + 1), textAnchor="middle", fontSize=8))
    d.add(String(left + width / 2, 8, "Sprint day", textAnchor="middle", fontSize=9))
    d.add(String(10, bottom + height / 2, "Points", textAnchor="middle", fontSize=9, angle=90))
    return d

def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.grey)
    canvas.drawString(.6 * inch, .35 * inch, "Software Engineering Lab 2 - Dhyan Rao")
    canvas.drawRightString(7.9 * inch, .35 * inch, f"Page {doc.page}")
    canvas.restoreState()

story = [P("Software Engineering Lab 2", "CenterTitle"), P("Agile Backlog Creation & Sprint Simulation in Jira", "CenterTitle"), P("Academic Elective Bidding & Allocation System", "Heading2"), P("<b>Student:</b> Dhyan Rao &nbsp; <b>SRN:</b> PES1UG24AM090 &nbsp; <b>Section:</b> B"), Spacer(1, 8), P("This report converts the corrected Lab 1 requirements for Problem Statement #05 into a Jira-style backlog and one-week Scrum sprint simulation.")]
story.append(P("1. Epics", "Section"))
epics = [["Epic", "Description"], ["EPIC-1: Student Bidding and Preferences", "View eligible electives, rank choices, and allocate bidding credits."], ["EPIC-2: Eligibility and Allocation Engine", "Validate prerequisites and allocate seats using capacity and timetable constraints."], ["EPIC-3: Registrar Configuration and Oversight", "Configure offerings and review allocation outcomes."], ["EPIC-4: Results and Notifications", "Publish allocation results, waitlists, exceptions, and notifications."]]
table = Table([[P(x, "Small") for x in row] for row in epics], colWidths=[2.5 * inch, 4.4 * inch])
table.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#d9eaf7")), ("GRID", (0, 0), (-1, -1), .5, colors.grey), ("VALIGN", (0, 0), (-1, -1), "TOP")]))
story.append(table)
story.append(P("2. User Stories and Estimates", "Section"))
rows = [["ID", "Epic", "Summary", "Priority", "Points"], ["US-001", "EPIC-1", "View eligible electives", "High", "3"], ["US-002", "EPIC-1", "Distribute 100 bidding credits", "High", "5"], ["US-003", "EPIC-1", "Save and submit ranked preferences", "High", "5"], ["US-004", "EPIC-2", "Validate allocation constraints", "High", "5"], ["US-005", "EPIC-2", "Run elective allocation", "High", "5"], ["US-006", "EPIC-3", "Configure offerings and rules", "Medium", "3"], ["US-007", "EPIC-4", "View allocation result", "Medium", "3"], ["US-008", "EPIC-4", "Review audit and conflict views", "Low", "3"]]
table = Table([[P(x, "Small") for x in row] for row in rows], colWidths=[.55 * inch, .65 * inch, 4.0 * inch, .75 * inch, .5 * inch], repeatRows=1)
table.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#d9eaf7")), ("GRID", (0, 0), (-1, -1), .35, colors.lightgrey), ("VALIGN", (0, 0), (-1, -1), "TOP")]))
story.append(table)
story.append(PageBreak())
story.append(P("3. Sprint 1 Simulation", "Section"))
story.append(P("Sprint duration: one week. Select US-001 through US-005 for a commitment of <b>23 story points</b>. Keep US-006 through US-008 in the backlog."))
sprint = [["Day", "Completed work", "Remaining"], ["Day 1", "Sprint started; selected stories To Do", "23"], ["Day 2", "US-001", "20"], ["Day 3", "US-002", "15"], ["Day 4", "US-003", "10"], ["Day 5", "US-004", "5"], ["Day 6", "US-005; sprint completed", "0"], ["Day 7", "Buffer / review", "0"]]
table = Table([[P(x, "Small") for x in row] for row in sprint], colWidths=[1 * inch, 4.9 * inch, 1 * inch], repeatRows=1)
table.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#d9eaf7")), ("GRID", (0, 0), (-1, -1), .5, colors.grey), ("VALIGN", (0, 0), (-1, -1), "TOP")]))
story.append(table)
story.append(Spacer(1, 10))
story.append(P("4. Burndown Chart", "Section"))
story.append(burndown())
story.append(PageBreak())
story.append(P("5. Reflection", "Section"))
for question, answer in [("Did the estimates reflect the actual effort?", "The estimates reflected relative complexity. Viewing eligible electives was a focused 3-point story, while credit validation, preference submission, constraint validation, and allocation were 5-point stories because they combine business rules and edge cases."), ("Was the backlog well-prioritized?", "Yes. The sprint prioritizes the student-to-allocation path. Registrar configuration and reporting remain in the backlog because they support the core flow but are not prerequisites for demonstrating allocation."), ("How did the simulated sprint align with your plan?", "Sprint 1 commits to 23 points across five stories. The order follows the dependency chain from eligible electives through credit validation, preference submission, constraint checking, and final allocation."), ("What insights did the burndown chart give about team capacity?", "The burndown shows that a 23-point commitment is achievable within one week in the simulation. The three unselected stories should be reserved for a later sprint unless additional capacity is available.")]:
    story.extend([P(f"<b>{question}</b>"), P(answer), Spacer(1, 7)])
story.append(P("6. Jira Evidence Checklist", "Section"))
for item in ["Backlog screenshot with epics and stories.", "Story point and priority evidence.", "Active Sprint board screenshot.", "Burndown Chart screenshot.", "This PDF uploaded to GitHub."]:
    story.append(P("- " + item))

doc = SimpleDocTemplate(str(OUT), pagesize=letter, rightMargin=.55 * inch, leftMargin=.55 * inch, topMargin=.55 * inch, bottomMargin=.6 * inch)
doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print(OUT)
