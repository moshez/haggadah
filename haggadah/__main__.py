import sys

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics 
from reportlab.pdfbase.ttfonts import TTFont 

from bidi import algorithm

pdfmetrics.registerFont(TTFont('Hebrew', 'ShlomoSemiStam.ttf'))
pdfmetrics.registerFont(TTFont('English', 'Vera.ttf'))

c = canvas.Canvas(sys.argv[1])
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

c.setFont("Hebrew", 14)
c.drawString(200, 800,
             algorithm.get_display("יַחַץ"))
c.setFont("English", 14)
c.drawString(100, 600,
"Split the middle matsah in two, and conceal the larger piece to use it for the afikoman.")
c.drawString(100, 500, "From now on, the kids should try to steal the afikoman.")
c.showPage()


c.setFont("Hebrew", 14)
c.drawString(200, 800,
             algorithm.get_display("מַגִּיד"))
c.setFont("English", 14)
c.drawString(100, 600,
"We start in Aramaic. In Jewish tradition, we pray in Hebrew, to encourage the angels to intercede on our behalf")
c.drawString(100, 500,
"But tonight, we thank God in person for the miracles. Angels do not understand Aramaic. The leader uncovers the matsot, raises the Seder plate. Everybody recites:")

c.setFont("Hebrew", 14)
c.drawString(100, 450, algorithm.get_display("""
הָא לַחְמָא עַנְיָא דִּי אֲכָלוּ אַבְהָתָנָא בְאַרְעָא דְמִצְרָיִם. כָּל דִכְפִין יֵיתֵי וְיֵיכֹל, כָּל דִצְרִיךְ יֵיתֵי וְיִפְסַח. הָשַּׁתָּא הָכָא, לְשָׁנָה הַבָּאָה בְּאַרְעָא דְיִשְׂרָאֵל. הָשַּׁתָּא עַבְדֵי, לְשָׁנָה הַבָּאָה בְּנֵי חוֹרִין. 
"""))

c.setFont("English", 14)
c.drawString(100, 200, "Ha lachma anya di achalu avhatana b’ara d’mitzrayim. Kol dichfin yeitei v’yeichol, kol ditzrich yeitei v’yifsach. Hashata hacha, l’shanah habaah b’ara d’Yisrael. Hashata avdei, l’shanah habaah b’nei chorin. ")

c.showPage()
c.save()
