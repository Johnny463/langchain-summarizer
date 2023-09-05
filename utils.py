from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

    # Define the content (your string)
def create_pdf(content):

    # Create a PDF document
    pdf_file = "Summary.pdf"
    document = SimpleDocTemplate(pdf_file, pagesize=letter)

    # Register the Arial font and set it as the default font
    pdfmetrics.registerFont(TTFont('Arial', 'arial_narrow.ttf'))  # Replace 'arial.ttf' with the path to your Arial font file
    default_style = getSampleStyleSheet()["Normal"]
    default_style.fontName = 'Arial'
    default_style.fontSize = 14  # Font size 20 points

    # Create a list of flowables (elements to add to the PDF)
    story = []

    # Create a paragraph element with the custom style
    paragraph = Paragraph(content, default_style)

    # Add the paragraph to the story
    story.append(paragraph)

    # Build the PDF document
    document.build(story)

    print(f"PDF created: {pdf_file}")
