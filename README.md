# OELAdvocate9914
Advocate
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.units import inch

def create_multi_orientation_pdf(filename):
    c = canvas.Canvas(filename, pagesize=letter)

    # === PORTRAIT (LETTER) PAGE ===
    width, height = letter
    # Top-right header with "0,zero"
    c.drawString(width - 72, height - 30, "0,zero") # Positioned 1 inch (72 pts) from top and right
    # Far-left header with "0,zero"
    c.drawString(30, height - 30, "0,zero") # Positioned 1 inch from top, 0.4 inches from left

    # Diagonal text in header
    # Rotate the canvas to draw the diagonal text, then restore it
    c.saveState()
    c.translate(30, height - 30) # Move to the starting point of the text
    c.rotate(-45) # Rotate 45 degrees counter-clockwise
    c.drawString(0, 0, "1/2")
    c.restoreState()

    # Diagonal text in footer
    c.saveState()
    c.translate(30, 30) # Move to the starting point of the text
    c.rotate(-45)
    c.drawString(0, 0, "1/2")
    c.restoreState()
    
    # Add a page break to move to the next page
    c.showPage()

    # === LANDSCAPE PAGE ===
    width, height = landscape(letter)
    c.setPageSize((width, height)) # Set the page size to landscape
    
    # Top-right header (rotated)
    c.drawString(width - 72, height - 30, "0,zero")
    # Far-left header (rotated)
    c.drawString(30, height - 30, "0,zero")

    # Diagonal header text (rotated)
    c.saveState()
    c.translate(30, height - 30)
    c.rotate(-45)
    c.drawString(0, 0, "1/2")
    c.restoreState()

    # Diagonal footer text (rotated)
    c.saveState()
    c.translate(30, 30)
    c.rotate(-45)
    c.drawString(0, 0, "1/2")
    c.restoreState()

    c.save()

# Generate the PDF file
create_multi_orientation_pdf("mixed_orientation_document.pdf")
