from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    # set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.line(10, 21, 200, 21)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)

    # set line
    y = 21
    for i in range(20):
        y = y + 12
        pdf.line(10, y, 200, y)

    # set the footer
    pdf.ln(260)
    pdf.set_font(family="Times", style="I", size=15)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")


    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # set the footer
        pdf.ln(260)
        pdf.set_font(family="Times", style="I", size=15)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

        # set line
        y = 21
        for i in range(20):
            y = y + 12
            pdf.line(10, y, 200, y)


pdf.output("output.pdf")