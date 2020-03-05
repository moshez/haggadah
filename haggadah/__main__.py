import sys

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics 
from reportlab.pdfbase.ttfonts import TTFont 

from bidi import algorithm

pdfmetrics.registerFont(TTFont('Hebrew', 'LinuxLibertine.ttf'))
pdfmetrics.registerFont(TTFont('English', 'Vera.ttf'))

c = canvas.Canvas(sys.argv[1])

from haggadah.output import write, write_multi, write_lines

write(c, "Hebrew", 200, 800,
      "וּרְחַץ")
write(c, "English", 200, 600, "Wash your hands without blessing")

c.showPage()

write(c, "Hebrew", 200, 800,"כַּרְפַּס")
write(c, "English", 200, 600,
      "Take one small strawberry, "
       "and dip it in chocolate")

write(c, "Hebrew", 100, 500,
      "בָּרוּךְ אַתָּה יְ‑יָ אֱ‑לֹהֵינוּ מֶלֶךְ הָעוֹלָם בּוֹרֵא פְּרִי הָעֵץ")

write(c, "English", 100, 400,
"Baruch atah A-donay, Elo-heinu Melech Ha’Olam borei pri ha-aitz.")

write_multi(c, "English", 100, 300,
["Blessed are You, L-rd our G-d, King of the universe, who creates the ",
 "fruit of the tree."])

c.showPage()

write(c, "Hebrew", 200, 800, "יַחַץ")
write_multi(c, "English", 100, 600,
["Split the middle matsah in two, and conceal the larger piece to use",
 "it for the afikoman."])
write(c, "English", 100, 500, "From now on, the kids should try to steal the afikoman.")

c.showPage()

write(c, "Hebrew", 200, 800,
      "מַגִּיד")

write_multi(c, "English", 50, 600,
[ "We start in Aramaic. In Jewish tradition, we pray in Hebrew,",
  " to encourage the angels to intercede on our behalf.",
 "But tonight, we thank God in person for the miracles.",
 "Angels do not understand Aramaic, so God has to listen to us Himself.",
 "The leader uncovers the matsot, raises the Seder plate. ",
 "Everybody recites:"])

write_multi(c, "Hebrew", 50, 450,
["הָא לַחְמָא עַנְיָא דִּי אֲכָלוּ אַבְהָתָנָא בְאַרְעָא דְמִצְרָיִם.",
 "כָּל דִכְפִין יֵיתֵי וְיֵיכֹל, כָּל דִצְרִיךְ יֵיתֵי וְיִפְסַח.",
 "הָשַּׁתָּא הָכָא, לְשָׁנָה הַבָּאָה בְּאַרְעָא דְיִשְׂרָאֵל.",
 "הָשַּׁתָּא עַבְדֵי, לְשָׁנָה הַבָּאָה בְּנֵי חוֹרִין."
])

write_multi(c, "English", 50, 300,
["Ha lachma anya di achalu avhatana b’ara d’mitzrayim.",
 "Kol dichfin yeitei v’yeichol, kol ditzrich yeitei",
 "v’yifsach. Hashata hacha, l’shanah habaah b’ara d’Yisrael.",
 "Hashata avdei, l’shanah habaah b’nei chorin. "])


c.showPage()

write(c, "English", 200, 800, "Four Questions")


write_multi(c, "Hebrew", 100, 750, 
["מַה נִּשְׁתַּנָּה הַלַּיְלָה הַזֶּה מִכָּל הַלֵּילוֹת?",
"שֶׁבְּכָל הַלֵּילוֹת אָנוּ אוֹכְלִין חָמֵץ וּמַצָּה, הַלַּיְלָה הַזֶּה – כֻּלּוֹ מַצָּה.",
"שֶׁבְּכָל הַלֵּילוֹת אָנוּ אוֹכְלִין שְׁאָר יְרָקוֹת – הַלַּיְלָה הַזֶּה (כֻּלּוֹ) מָרוֹר.",
"שֶׁבְּכָל הַלֵּילוֹת אֵין אָנוּ מַטְבִּילִין אֲפִילוּ פַּעַם אֶחָת – הַלַּיְלָה הַזֶּה שְׁתֵּי פְעָמִים.",
"שֶׁבְּכָל הַלֵּילוֹת אָנוּ אוֹכְלִין בֵּין יוֹשְׁבִין וּבֵין מְסֻבִּין – הַלַּיְלָה הַזֶּה כֻּלָּנוּ מְסֻבִּין."
])

write_multi(c, "English", 100, 600, 
["Ma nishtanah halailah hazeh mikol haleilot?",
"Sheb’khol haleilot anu okhlin umatzah;", "halailah hazeh, kuloh matzah.",
"Sheb’khol haleilot anu okhlin sh’ar y’rakot;", "halailah hazeh, maror.",
"Sheb’khol haleilot ein anu matbilin afilu pa’am ehat;", "halailah hazeh, shtei f’amim.",
"Sheb’khol haleilot anu okhlin bein yoshvin uvein m’subin;", "halailah hazeh, kulanu m’subin."]
)

write_multi(c, "English", 100, 450,
["What differentiates this night from all [other] nights?",
 "On all [other] nights we eat chamets and matsa;", "this night, only matsa?", 
 "On all [other] nights we eat other vegetables;", "tonight (only) marror.",
 "On all [other] nights, we don't dip [our food], even one time;", "tonight [we dip it] twice.",
 "On [all] other nights, we eat either sitting or reclining;", "tonight we all recline."])
c.showPage()

c.drawString(200, 800, "The Ten Plagues")

write_lines(c, "English", 100, 750, """\
And when he says, "blood and fire and pillars of smoke" and the
ten plagues and  "detsakh," "adash" and "ba'achab," he should pour
out a little wine from his cup.
""")

write(c, "Hebrew", 100, 700, "דָּם וָאֵשׁ וְתִימְרוֹת עָשָׁן.")

write(c, "English", 100, 675, "Dam v'esh v'timrot ashan")

write(c, "English", 100, 650, "blood and fire and pillars of smoke.")

write(c, "Hebrew", 50, 625, "אֵלּוּ עֶשֶׂר מַכּוֹת שֶׁהֵבִיא הַקָּדוֹשׁ בָּרוּךְ הוּא עַל־הַמִּצְרִים בְּמִצְרַיִם, וְאֵלוּ הֵן:")

write_lines(c, "English", 50, 600, """\
Elu eser makot sh'hevi hakadosh baruch hu al hamitzri'im
b'mitzraim, v'elu hen      
""")
write_lines(c, "English", 100, 550, """\
These are [the] ten plagues that the Holy One, blessed be He,
brought on the Egyptians in Egypt and they are: """)

write_lines(c, "Hebrew", 500, 500, """\
דָּם
צְפַרְדֵּעַ
כִּנִּים
עָרוֹב
דֶּבֶר
שְׁחִין
בָּרָד
אַרְבֶּה
חשֶׁךְ
מַכַּת בְּכוֹרוֹת
""")

write_lines(c, "English", 50, 500, """\
Blood                      
Frogs                      
Lice                       
Mixture (of wild animals)  
Pestilence                 
Boils                      
Locusts                    
Hail                       
Darkness                   
Killing of the first born
""")

write_lines(c, "English", 250, 500, """\
Dam
Tzfarde'a
Kinim
Arov
Dever
Sh'khin
Barad
Arbeh
Hoshekh
Makat Bekhorot
""")

write_lines(c, "Hebrew", 100, 350, """\
רַבִּי יְהוּדָה הָיָה נוֹתֵן בָּהֶם סִמָּנִים: דְּצַ"ךְ עַדַ"שׁ בְּאַחַ"ב. 
""")

write(c, "English", 50, 325, "Rabbi Yehuda haya noten bahem simanim: datzakh adash b'akhav")

write_lines(c, "English", 50, 300, """\
Rabbi Yehuda was accustomed to giving mnemonics:
Detsakh, Adash, Beachav.""")


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
