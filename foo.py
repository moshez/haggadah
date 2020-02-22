from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics 
from reportlab.pdfbase.ttfonts import TTFont 

from bidi import algorithm

pdfmetrics.registerFont(TTFont('Hebrew', 'ShlomoSemiStam.ttf'))
pdfmetrics.registerFont(TTFont('English', 'Vera.ttf'))

c = canvas.Canvas("hello.pdf") 
c.setFont("Hebrew", 14)
input = "וּרְחַץ"
c.drawString(200, 800, algorithm.get_display(input))
c.setFont("English", 14)
c.drawString(200, 600,
             algorithm.get_display("Wash your hands without blessing"))
c.showPage()
c.setFont("Hebrew", 14)
c.drawString(200, 800,
             algorithm.get_display("כַּרְפַּס"))
c.setFont("English", 14)
c.drawString(200, 600,
             algorithm.get_display("Take one small strawberry, "
                                   "and dip it in chocolate"))
c.setFont("Hebrew", 14)
c.drawString(100, 500,
       algorithm.get_display("בָּרוּךְ אַתָּה יְ‑יָ אֱ‑לֹהֵינוּ מֶלֶךְ הָעוֹלָם בּוֹרֵא פְּרִי הָעֵץ"))
c.setFont("English", 14)
c.drawString(100, 400,
"Baruch atah A-donay, Elo-heinu Melech Ha’Olam borei pri ha-aitz.")
c.drawString(100, 300,
"Blessed are You, L-rd our G-d, King of the universe, who creates the fruit of the tree.")
c.showPage()
c.save()
