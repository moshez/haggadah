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

c.drawString(200, 800, "Four Questions")


c.setFont("Hebrew", 14)

c.drawString(100, 750, 
algorithm.get_display("מַה נִּשְׁתַּנָּה הַלַּיְלָה הַזֶּה מִכָּל הַלֵּילוֹת? שֶׁבְּכָל הַלֵּילוֹת אָנוּ אוֹכְלִין חָמֵץ וּמַצָּה, הַלַּיְלָה הַזֶּה – כֻּלּוֹ מַצָּה. שֶׁבְּכָל הַלֵּילוֹת אָנוּ אוֹכְלִין שְׁאָר יְרָקוֹת – הַלַּיְלָה הַזֶּה (כֻּלּוֹ) מָרוֹר. שֶׁבְּכָל הַלֵּילוֹת אֵין אָנוּ מַטְבִּילִין אֲפִילוּ פַּעַם אֶחָת – הַלַּיְלָה הַזֶּה שְׁתֵּי פְעָמִים. שֶׁבְּכָל הַלֵּילוֹת אָנוּ אוֹכְלִין בֵּין יוֹשְׁבִין וּבֵין מְסֻבִּין – הַלַּיְלָה הַזֶּה כֻּלָּנוּ מְסֻבִּין. "))

c.setFont("English", 14)

c.drawString(100, 600, "Ma nishtanah halailah hazeh mikol haleilot? Sheb’khol haleilot anu okhlin umatzah; halailah hazeh, kuloh matzah. Sheb’khol haleilot anu okhlin sh’ar y’rakot; halailah hazeh, maror. Sheb’khol haleilot ein anu matbilin afilu pa’am ehat; halailah hazeh, shtei f’amim. Sheb’khol haleilot anu okhlin bein yoshvin uvein m’subin; halailah hazeh, kulanu m’subin.")

c.drawString(100, 500, "What differentiates this night from all [other] nights? On all [other] nights we eat chamets and matsa; this night, only matsa? On all [other] nights we eat other vegetables; tonight (only) marror. On all [other] nights, we don't dip [our food], even one time; tonight [we dip it] twice. On [all] other nights, we eat either sitting or reclining; tonight we all recline. ")
c.showPage()

c.drawString(200, 800, "The Ten Plagues")

c.showPage()

c.drawString(200, 800, "Three Things")

c.showPage()

c.setFont("Hebrew", 14)

c.drawString(200, 800,  algorithm.get_display("בְּצֵאת יִשְׂרָאֵל מִמִצְרַיִם"))

c.showPage()

c.setFont("Hebrew", 14)
c.drawString(200, 800,  algorithm.get_display("קַדֵּשׁ"))

c.showPage()

c.setFont("English", 14)

c.drawString(200, 800, "Magid: Second cup of wine")

c.showPage()

c.setFont("Hebrew", 14)
c.drawString(200, 800,  algorithm.get_display("רָחְצָה"))
c.showPage()

c.setFont("Hebrew", 14)
c.drawString(200, 800,  algorithm.get_display("מוֹצִיא מַצָּה"))
c.showPage()

c.setFont("Hebrew", 14)
c.drawString(200, 800,  algorithm.get_display("מָרוֹר"))
c.showPage()


c.setFont("Hebrew", 14)
c.drawString(200, 800,  algorithm.get_display("כּוֹרֵךְ"))
c.showPage()


c.setFont("Hebrew", 14)
c.drawString(200, 800,  algorithm.get_display("שֻׁלְחָן עוֹרֵךְ"))
c.showPage()


c.setFont("Hebrew", 14)
c.drawString(200, 800,  algorithm.get_display("צָפוּן"))
c.showPage()

c.setFont("Hebrew", 14)
c.drawString(200, 800,  algorithm.get_display("בָּרֵךְ"))
c.showPage()

c.setFont("Hebrew", 14)
c.drawString(200, 800,  algorithm.get_display("הַלֵּל"))
c.showPage()


c.setFont("Hebrew", 14)
c.drawString(200, 800,  algorithm.get_display("נִרְצָה"))
c.showPage()


c.save()
