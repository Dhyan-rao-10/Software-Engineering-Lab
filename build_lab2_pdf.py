from pathlib import Path
import csv
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak,
    Image, KeepTogether
)
from reportlab.graphics.shapes import Drawing, Line, String, Circle

ROOT = Path(__file__).resolve().parent
pdf_path = ROOT / "lab2-deliverable.pdf"

days, remaining = [], []
with (ROOT / "lab2-burndown-data.csv").open(newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        days.append(int(row["Day"]))
        remaining.append(int(row["Remaining Story Points"]))

def make_burndown_drawing():
    drawing = Drawing(500, 270)
    left, bottom, width, height = 55, 35, 400, 190
    drawing.add(String(250, 245, "Sprint 1 Burndown Chart", textAnchor="middle", fontName="Helvetica-Bold", fontSize=13, fillColor=colors.HexColor("#1f4e79")))
    drawing.add(Line(left, bottom, left, bottom + height, strokeColor=colors.black))
    drawing.add(Line(left, bottom, left + width, bottom, strokeColor=colors.black))
    for y in range(0, 31, 5):
        yy = bottom + (y / 30) * height
        drawing.add(Line(left, yy, left + width, yy, strokeColor=colors.HexColor("#dddddd")))
        drawing.add(String(left - 8, yy - 3, str(y), textAnchor="end", fontSize=8))
    for d in days:
        xx = left + ((d - 1) / 6) * width
        drawing.add(String(xx, bottom - 15, str(d), textAnchor="middle", fontSize=8))
    drawing.add(String(left + width / 2, 8, "Sprint day", textAnchor="middle", fontSize=9))
    drawing.add(String(10, bottom + height / 2, "Points", textAnchor="middle", fontSize=9, angle=90))
    ideal = [26 - (26 / 6) * (d - 1) for d in days]
    def point(d, v):
        return left + ((d - 1) / 6) * width, bottom + (v / 30) * height
    for vals, colour, dash in [(ideal, colors.HexColor("#777777"), [4, 3]), (remaining, colors.HexColor("#1565c0"), None)]:
        for i in range(len(days) - 1):
            x1, y1 = point(days[i], vals[i]); x2, y2 = point(days[i + 1], vals[i + 1])
            line = Line(x1, y1, x2, y2, strokeColor=colour, strokeWidth=2)
            if dash:
                line.strokeDashArray = dash
            drawing.add(line)
        if vals is remaining:
            for d, v in zip(days, vals):
                x, y = point(d, v)
                drawing.add(Circle(x, y, 3.5, fillColor=colour, strokeColor=colour))
    drawing.add(String(315, 225, "Actual remaining", fontSize=8, fillColor=colors.HexColor("#1565c0")))
    drawing.add(String(405, 225, "Ideal", fontSize=8, fillColor=colors.HexColor("#777777")))
    return drawing

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="TitleCenter", parent=styles["Title"], alignment=TA_CENTER, textColor=colors.HexColor("#1f4e79"), spaceAfter=12))
styles.add(ParagraphStyle(name="Section", parent=styles["Heading2"], textColor=colors.HexColor("#1f4e79"), spaceBefore=10, spaceAfter=6))
styles.add(ParagraphStyle(name="Small", parent=styles["BodyText"], fontSize=8.5, leading=11))
styles.add(ParagraphStyle(name="Tiny", parent=styles["BodyText"], fontSize=7.5, leading=9))

def P(text, style="BodyText"):
    return Paragraph(text, styles[style])

def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.grey)
    canvas.drawString(0.65 * inch, 0.4 * inch, "Software Engineering Lab 2 - Dhyan Rao")
    canvas.drawRightString(7.85 * inch, 0.4 * inch, f"Page {doc.page}")
    canvas.restoreState()

story = []
story.append(P("Software Engineering Lab 2", "TitleCenter"))
story.append(P("Agile Backlog Creation & Sprint Simulation in Jira", "TitleCenter"))
story.append(P("Remote Patient Vitals Alert & Monitoring App", "Heading2"))
story.append(P("<b>Student:</b> Dhyan Rao &nbsp;&nbsp; <b>SRN:</b> PES1UG24AM090 &nbsp;&nbsp; <b>Section:</b> B"))
story.append(Spacer(1, 8))
story.append(P("This report converts the Lab 1 functional requirements into Jira-style epics and user stories, prioritizes and estimates them, and documents a one-week Sprint 1 simulation."))

story.append(P("1. Epics", "Section"))
epics = [
    [P("Epic", "Small"), P("Description", "Small"), P("Lab 1 coverage", "Small")],
    [P("EPIC-1: Continuous Vital Telemetry", "Tiny"), P("Reliable collection and viewing of remote patient vital readings.", "Tiny"), P("FR-001, FR-005", "Tiny")],
    [P("EPIC-2: Threshold Detection and Alerts", "Tiny"), P("Detect abnormal readings and provide actionable alert information.", "Tiny"), P("FR-002, FR-003", "Tiny")],
    [P("EPIC-3: Caregiver Notification and Escalation", "Tiny"), P("Deliver alerts to the correct caregiver and escalate emergencies.", "Tiny"), P("FR-004", "Tiny")],
    [P("EPIC-4: Alert Response and Audit", "Tiny"), P("Record caregiver responses and preserve traceable event history.", "Tiny"), P("FR-005", "Tiny")],
]
tbl = Table(epics, colWidths=[2.2*inch, 3.6*inch, 1.3*inch], repeatRows=1)
tbl.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#d9eaf7")), ("GRID", (0,0), (-1,-1), 0.5, colors.grey),
    ("VALIGN", (0,0), (-1,-1), "TOP"), ("LEFTPADDING", (0,0), (-1,-1), 6), ("RIGHTPADDING", (0,0), (-1,-1), 6),
]))
story.append(tbl)
story.append(Spacer(1, 8))

story.append(P("2. User Story Backlog", "Section"))
rows = [[P("ID", "Tiny"), P("Epic", "Tiny"), P("User story", "Tiny"), P("Priority", "Tiny"), P("Points", "Tiny")]]
backlog = [
    ("US-001", "EPIC-1", "As a Remote Patient, I want my registered device to send timestamped SpO2, heart-rate, and blood-pressure readings so that my caregiver can monitor me remotely.", "High", "5"),
    ("US-002", "EPIC-1", "As an On-Call Caregiver, I want to view current and recent patient vitals so that I can assess the patient's condition.", "Medium", "3"),
    ("US-003", "EPIC-2", "As an On-Call Caregiver, I want every valid reading evaluated against active clinical thresholds so that anomalies are detected consistently.", "High", "5"),
    ("US-004", "EPIC-2", "As an On-Call Caregiver, I want an alert to show the metric, value, threshold, patient, and time so that I can respond quickly.", "High", "5"),
    ("US-005", "EPIC-3", "As an assigned On-Call Caregiver, I want an immediate critical-alert notification so that I can begin a response.", "High", "3"),
    ("US-006", "EPIC-3", "As a care-team member, I want an unacknowledged critical alert escalated through the caregiver matrix so that emergencies are not missed.", "High", "5"),
    ("US-007", "EPIC-4", "As an On-Call Caregiver, I want to acknowledge an alert and record an action or note so that the response is documented.", "Medium", "3"),
    ("US-008", "EPIC-4", "As an On-Call Caregiver, I want notification attempts and acknowledgements timestamped so that the event history is traceable.", "Low", "3"),
]
for row in backlog:
    rows.append([P(x, "Tiny") for x in row])
tbl = Table(rows, colWidths=[0.55*inch, 0.7*inch, 4.8*inch, 0.7*inch, 0.45*inch], repeatRows=1)
tbl.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#d9eaf7")), ("GRID", (0,0), (-1,-1), 0.35, colors.lightgrey),
    ("VALIGN", (0,0), (-1,-1), "TOP"), ("LEFTPADDING", (0,0), (-1,-1), 4), ("RIGHTPADDING", (0,0), (-1,-1), 4),
]))
story.append(tbl)

story.append(PageBreak())
story.append(P("3. Sprint 1 Simulation", "Section"))
story.append(P("Sprint duration: one week. Selected stories: US-001, US-003, US-004, US-005, US-006, and US-007. Total commitment: <b>26 story points</b>. US-002 and US-008 remain in the backlog."))
sprint_rows = [[P("Day", "Small"), P("Completed work", "Small"), P("Remaining points", "Small")]]
for day, work, pts in [("Day 1", "Sprint started; selected stories in To Do", "26"), ("Day 2", "US-001", "21"), ("Day 3", "US-003", "16"), ("Day 4", "US-004", "11"), ("Day 5", "US-005", "8"), ("Day 6", "US-006", "3"), ("Day 7", "US-007; Sprint completed", "0")]:
    sprint_rows.append([P(day, "Small"), P(work, "Small"), P(pts, "Small")])
tbl = Table(sprint_rows, colWidths=[1.0*inch, 4.8*inch, 1.4*inch], repeatRows=1)
tbl.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,0), colors.HexColor("#d9eaf7")), ("GRID", (0,0), (-1,-1), 0.5, colors.grey), ("VALIGN", (0,0), (-1,-1), "TOP")]))
story.append(tbl)
story.append(Spacer(1, 12))
story.append(P("4. Burndown Chart", "Section"))
story.append(P("The red/blue actual line represents remaining story points as work moves from To Do through In Progress to Done. The dashed line is the ideal linear guideline."))
story.append(make_burndown_drawing())

story.append(PageBreak())
story.append(P("5. Reflection", "Section"))
reflection = [
    ("Did the estimates reflect the actual effort?", "The estimates were reasonably aligned with the simulated effort. Three-point stories covered focused notification or response actions, while five-point stories involved integration, clinical rules, or escalation behavior. Real device integration and security testing could increase the effort."),
    ("Was the backlog well-prioritized?", "Yes. The high-priority path establishes monitoring, detection, alert generation, notification, and escalation before lower-priority viewing and audit improvements. This keeps emergency safety work ahead of convenience features."),
    ("How did the simulated sprint align with your plan?", "The sprint completed all six selected stories and delivered 26 points within the one-week simulation. The order followed the dependency chain from telemetry to detection, notification, escalation, and caregiver response."),
    ("What insights did the burndown chart give about team capacity?", "The chart reaches zero by Day 7, indicating that the simulated team could complete the 26-point commitment. The two unselected stories show why future sprint commitments should remain within demonstrated capacity. A real Jira chart would also expose delays and scope changes."),
]
for q, a in reflection:
    story.append(P(f"<b>{q}</b>"))
    story.append(P(a))
    story.append(Spacer(1, 8))

story.append(P("6. Jira Evidence Checklist", "Section"))
for item in [
    "Backlog screenshot showing all four epics and eight user stories.",
    "Story point and priority fields visible for the stories.",
    "Active Sprint screenshot showing work in To Do, In Progress, and Done.",
    "Reports > Burndown Chart screenshot.",
    "This PDF uploaded to the GitHub repository.",
]:
    story.append(P(f"- {item}"))

doc = SimpleDocTemplate(str(pdf_path), pagesize=letter, rightMargin=0.55*inch, leftMargin=0.55*inch, topMargin=0.55*inch, bottomMargin=0.65*inch)
doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print(pdf_path)
