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

write(c, "English", 200, 800, "Three Things")

write_lines(c, "Hebrew", 100, 750,
"""\
רַבָּן גַּמְלִיאֵל הָיָה אוֹמֵר: כָּל שֶׁלֹּא אָמַר שְׁלשָׁה דְּבָרִים אֵלּוּ בַּפֶּסַח,
 לא יָצָא יְדֵי חוֹבָתוֹ, וְאֵלּוּ הֵן: פֶּסַח, מַצָּה, וּמָרוֹר.
""")

write_lines(c, "English", 100, 700,
"""\
Rabban Gamliel haya omer:
kol sh'lo amar shlosha d'varim elu b'pesach,
lo yatza y'dei khovato, v'elu hen:
pesach, matza, u'maror
""")


write_lines(c, "English", 100, 600,
"""\
Rabban Gamliel was accustomed to say,
Anyone who has not said these three things on Pesach has not 
fulfilled his obligation, and these are them:
the Pesach sacrifice, matsa and marror. 
""")

c.showPage()

write(c, "Hebrew", 200, 800,  "בְּצֵאת יִשְׂרָאֵל מִמִצְרַיִם")

write_lines(c, "Hebrew", 350, 750,
"""\
בְּצֵאת יִשְׂרָאֵל מִמִצְרַיִם, בֵּית יַעֲקֹב מֵעַם לֹעֵז,
בְּצֵאת יִשְׂרָאֵל מִמִצְרַיִם, בֵּית יַעֲקֹב מֵעַם לֹעֵז,
הָיְתָה יְהוּדָה לְקָדְשׁוֹ,
יִשְׂרָאֵל מַמְשְׁלוֹתָיו.
הַיָּם רָאָה וַיַּנֹס,
הַיַּרְדֵּן יִסֹּב לְאָחוֹר.
בְּצֵאת יִשְׂרָאֵל מִמִצְרַיִם, בֵּית יַעֲקֹב מֵעַם לֹעֵז,
בְּצֵאת יִשְׂרָאֵל מִמִצְרַיִם, בֵּית יַעֲקֹב מֵעַם לֹעֵז,
הֶהָרִים רָקְדוּ כְאֵילִים,
גְּבַעוֹת כִּבְנֵי צֹאן.
מַה לְּךָ הַיָּם כִּי תָנוּס,
הַיַּרְדֵּן – תִּסֹּב לְאָחוֹר,
בְּצֵאת יִשְׂרָאֵל מִמִצְרַיִם, בֵּית יַעֲקֹב מֵעַם לֹעֵז,
בְּצֵאת יִשְׂרָאֵל מִמִצְרַיִם, בֵּית יַעֲקֹב מֵעַם לֹעֵז,
הֶהָרִים – תִּרְקְדוּ כְאֵילִים,
גְּבַעוֹת כִּבְנֵי־צֹאן.
מִלְּפְנֵי אָדוֹן חוּלִי אָרֶץ, מִלְּפְנֵי אֱלוֹהַ יַעֲקֹב.
בְּצֵאת יִשְׂרָאֵל מִמִצְרַיִם, בֵּית יַעֲקֹב מֵעַם לֹעֵז,
בְּצֵאת יִשְׂרָאֵל מִמִצְרַיִם, בֵּית יַעֲקֹב מֵעַם לֹעֵז,
מִלְּפְנֵי אָדוֹן חוּלִי אָרֶץ, מִלְּפְנֵי אֱלוֹהַ יַעֲקֹב.
הַהֹפְכִי הַצּוּר אֲגַם־מָיִם, חַלָּמִיש לְמַעְיְנוֹ־מָיִם.
בְּצֵאת יִשְׂרָאֵל מִמִצְרַיִם, בֵּית יַעֲקֹב מֵעַם לֹעֵז,
בְּצֵאת יִשְׂרָאֵל מִמִצְרַיִם, בֵּית יַעֲקֹב מֵעַם לֹעֵז,
""")

write_lines(c, "English", 50, 750,
"""\
B'tset yisrael mi'mitzrayim,
beit yaacov m'am loez
B'tset yisrael mi'mitzrayim,
beit yaacov m'am loez
Hayta yehuda lkodsho,
Yisrael mamshelotav
Hayam ra'a vayanos
Hayarden yisov l'akhor
B'tset yisrael mi'mitzrayim,
beit yaacov m'am loez
B'tset yisrael mi'mitzrayim,
beit yaacov m'am loez
He'harim rakdu k'elim
G'va'ot ki'vnei tzon
Ma lekha hayam ki tanus
Hayarden -- tisov l'akhor
B'tset yisrael mi'mitzrayim,
beit yaacov m'am loez
B'tset yisrael mi'mitzrayim,
beit yaacov m'am loez
Heharim tirkedu kh'elim
G'vaot ki'vnei tzon
Milifnei adon huli aretz
Milifnei eloha yaacov
B'tset yisrael mi'mitzrayim,
beit yaacov m'am loez
B'tset yisrael mi'mitzrayim,
beit yaacov m'am loez
Milifnei adon huli aretz
Milifnei eloha yaacov
Hahofkhi hatzur agam mayim
Halamish l'mayno mayim
B'tset yisrael mi'mitzrayim,
beit yaacov m'am loez
B'tset yisrael mi'mitzrayim,
beit yaacov m'am loez
""")

write_lines(c, "English", 300, 400,
"""\
In Israel's going out from Egypt,
the house of Ya'akov
from a people of foreign speech.
The Sea saw and fled,
the Jordan turned to the rear.
The mountains danced like rams,
the hills like young sheep.
What is happening to you,
O Sea, that you are fleeing,
O Jordan that you turn to the rear;
O mountains that you dance like rams,
O hills like young sheep?
From before the Master, tremble O earth,
from before the Lord of Ya'akov.
He who turns the boulder into a
pond of water,
the flint into a spring of water.
""")

c.showPage()

write(c, "Hebrew", 200, 800,  "קַדֵּשׁ")

write(c, "Hebrew", 100, 750, "מוזגים כוס ראשון. המצּות מכוסות.")
write(c, "English", 100, 725, "We pour the first cup.")

write_lines(c, "Hebrew", 100, 700,
"""\
סַבְרִי מָרָנָן וְרַבָּנָן וְרַבּוֹתַי.
בָּרוּךְ אַתָּה ה', אֱלֹהֵינוּ מֶלֶךְ הָעוֹלָם בּוֹרֵא פְּרִי הַגָּפֶן.
""")

write_lines(c, "English", 100, 650,
"""\
Blessed are You, Lord our God,
King of the universe,
who creates the fruit of the vine.
""")

write_lines(c, "Hebrew", 100, 600,
"""\
בָּרוּךְ אַתָּה ה', אֱלהֵינוּ מֶלֶךְ הָעוֹלָם
אֲשֶׁר בָּחַר בָּנוּ מִכָּל־עָם וְרוֹמְמָנוּ מִכָּל־לָשׁוֹן וְקִדְּשָׁנוּ בְּמִצְוֹתָיו.
וַתִּתֶּן לָנוּ ה' אֱלֹהֵינוּ בְּאַהֲבָה מוֹעֲדִים לְשִׂמְחָה,
חַגִּים וּזְמַנִּים לְשָׂשוֹן,
אֶת יוֹם חַג הַמַּצּוֹת הַזֶּה זְמַן חֵרוּתֵנוּ,
מִקְרָא קֹדֶשׁ זֵכֶר לִיצִיאַת מִצְרָיִם.
כִּי בָנוּ בָחַרְתָּ וְאוֹתָנוּ קִדַּשְׁתָּ מִכָּל הָעַמִּים,
וּמוֹעֲדֵי קָדְשֶׁךָ בְּשִׂמְחָה וּבְשָׂשוֹן הִנְחַלְתָּנוּ.
""")

write_lines(c, "English", 100, 450,
"""\
Blessed are You, Lord our God,
King of the universe,
who has chosen us from all peoples and
has raised us above all tongues and has
sanctified us with His commandments.
And You have given us, Lord our God,
appointed times for happiness,
holidays and special times for joy,
this Festival of Matsot,
our season of freedom a holy convocation
in memory of the Exodus from Egypt.
For You have chosen us and sanctified us
above all peoples.
In Your gracious love,
You granted us Your special times for
happiness and joy.
""")

write_lines(c, "Hebrew", 100, 200,
"""\
בָּרוּךְ אַתָּה ה', מְקַדֵּשׁ יִשְׂרָאֵל וְהַזְּמַנִּים.
""")

write_lines(c, "English", 100, 175,
"""\
Blessed are You, O Lord, who sanctifies Israel,
and the appointed times.
""")

write_lines(c, "English", 100, 125,
"""\
Drink while reclining to the left and do not
recite a blessing after drinking.
""")

c.showPage()

write(c, "English", 200, 800, "Magid: Second cup of wine")

write_lines(c, "English", 50, 725,
"""\
We raise the cup until we reach "who redeemed Israel"
""")

write_lines(c, "Hebrew", 200, 700,
"""\
בָּרוּךְ אַתָּה ה' אֱלֹהֵינוּ מֶלֶךְ הָעוֹלָם,
אֲשֶׁר גְּאָלָנוּ וְגָאַל אֶת־אֲבוֹתֵינוּ מִמִּצְרַיִם,
וְהִגִּיעָנוּ הַלַּיְלָה הַזֶּה לֶאֱכָל־בּוֹ מַצָּה וּמָרוֹר.
כֵּן ה' אֱלֹהֵינוּ וֵאלֹהֵי אֲבוֹתֵינוּ יַגִּיעֵנוּ
לְמוֹעֲדִים וְלִרְגָלִים אֲחֵרִים הַבָּאִים לִקְרָאתֵנוּ לְשָׁלוֹם,
שְׂמֵחִים בְּבִנְיַן עִירֶךְ וְשָׂשִׂים בַּעֲבוֹדָתֶךָ.
וְנֹאכַל שָׁם מִן הַזְּבָחִים וּמִן הַפְּסָחִים אֲשֶׁר יַגִּיעַ דָּמָם עַל קִיר מִזְבַּחֲךָ לְרָצון,
וְנוֹדֶה לְךָ שִׁיר חָדָש עַל גְּאֻלָּתֵנוּ וְעַל פְּדוּת נַפְשֵׁנוּ.
בָּרוּךְ אַתָּה ה', גָּאַל יִשְׂרָאֵל.
""")

write_lines(c, "English", 50, 550,
"""\
Baruch attah adonai eloheinu melekh ha'olam
Asher ga'alanu v'ga'al at avoteinu mimitzrayim
v'higi'anu halayla hazeh le'ekhol bo matzah u'maror
Ken adonai eloheinu v'elohei avoteinu yagi'einu
l'moadim u'lrgalim aherim haba'im likrateinu l'shalom
smehim b'vinyan hirkha v'sassim b'avodatkha
v'nokhal sham min hazvahim u'min hapsahim
asher yagi'a damam al kir mizbeha lratzon
v'node l'kha shir hadash al g'eulateinu v'al pdut nafshenu
Barush attah adonai, ga'al yisrael
""")

write_lines(c, "English", 50, 400,
"""\
Blessed are You, Lord our God,
King of the universe, who redeemed us and 
redeemed our ancestors from Egypt, 
and brought us on this night to eat matsa and marror; 
so too, Lord our God, and God of our ancestors, 
bring us to other appointed times and holidays that 
will come to greet us in peace, joyful in the building of 
Your city and happy in Your worship; 
that we shall eat there from the offerings and from the 
Pesach sacrifices, the blood of which shall reach the 
wall of Your altar for favor, and we shall thank You 
with a new song upon our redemption and upon the restoration 
of our souls. 
Blessed are you, Lord, who redeemed Israel.
""")


write_lines(c, "English", 50, 175,
"""\
We say the blessing below and drink the cup while reclining to the left
""")

write_lines(c, "Hebrew", 200, 150,
"""\
בָּרוּךְ אַתָּה ה', אֱלֹהֵינוּ מֶלֶךְ הָעוֹלָם בּוֹרֵא פְּרִי הַגָּפֶן.
""")

write_lines(c, "English", 50, 125,
"""\
Barukh attah adonai, eloheinu melekh ha'olam, boreh pri hagafen
"""
)

write_lines(c, "English", 50, 100,
"""\
Blessed are You, Lord our God, who creates the fruit of the vine. 
""")

c.showPage()

write(c, "Hebrew", 200, 800, "רָחְצָה")

write_lines(c, "English", 50, 750,
"""\
We wash the hands and make the blessing.
""")

write_lines(c, "Hebrew", 200, 725,
"""\
בָּרוּךְ אַתָּה ה', אֱלֹהֵינוּ מֶלֶךְ הָעוֹלָם, אֲשֶׁר קִדְּשָׁנוּ בְּמִצְוֹתָיו וְצִוָּנוּ עַל נְטִילַת יָדַיִם.
""")

write_lines(c, "English", 50, 700,
"""\
Barukh atta adonai, eloheinu melekh ha'olam,
Asher kidshanu b'mitzvotav v'tsivanu al
ntilat yada'im
"""
)

write_lines(c, "English", 50, 650,
"""\
Blessed are You, Lord our God, King of the Universe,
who has sanctified us with His commandments and has commanded us
on the washing of the hands.
""")

c.showPage()

write(c,"English", 200, 800,  "Motzi Matzah")

write_lines(c, "English", 50, 750,
"""\
He takes out the matsa in the order that he placed them,
the broken one between the two whole ones;
he holds the three of them in his hand and blesses 
"ha-motsi" with the intention to take from the top one and
"on eating matsa" with the intention of eating from the broken one.
Afterwards, he breaks off a kazayit from the top whole one and a second
kazayit from the broken one and he dips them into salt and eats both 
while reclining.
""")

write_lines(c, "Hebrew", 200, 600,
"""\
בָּרוּךְ אַתָּה ה', אֱלֹהֵינוּ מֶלֶךְ הָעוֹלָם הַמּוֹצִיא לֶחֶם מִן הָאָרֶץ.
""")

write_lines(c, "English", 50, 575,
"Barukh attah adonai, eloheinu melekh ha'olam, hamotzi lekhem min ha'aretz")

write_lines(c, "English", 50, 550,
"""\
Blessed are You, Lord our God, King of the Universe,
who brings forth bread from the ground.
""")

write_lines(c, "Hebrew", 200, 500,
"""\
בָּרוּךְ אַתָּה ה', אֱלֹהֵינוּ מֶלֶךְ הָעוֹלָם, אֲשֶׁר קִדְּשָׁנוּ בְּמִצְוֹתָיו וְצִוָּנוּ עַל אֲכִילַת מַצָּה.
""")

write_lines(c, "English", 50, 475,
"""\
Barukh attah adonai, eloheinu melekh ha'olam, asher kidshanu b'mitzvotav
v'tzivanu al akhilat matzah""")

write_lines(c, "English", 50, 425,
"""\
Blessed are You, Lord our God, King of the Universe, who has
sanctified us with His commandments and has commanded us on the
eating of matsa. 
""")


c.showPage()

write(c, "English", 200, 800, "Maror")

write_lines(c, "English", 50, 750,
"""\
All present should take a kazayit of marror, dip into the haroset,
shake off the haroset, make the blessing and eat without reclining.
""")

write_lines(c, "Hebrew", 50, 700,
"""\
בָּרוּךְ אַתָּה ה', אֱלֹהֵינוּ מֶלֶךְ הָעוֹלָם, אֲשֶׁר קִדְּשָנוּ בְּמִצְוֹתָיו וְצִוָּנוּ עַל אֲכִילַת מָרוֹר.
""")

write_lines(c, "English", 50, 675,
"""\
Barukh attah adonai, eloheinu melekh ha'olam, asher kidshanu b'mitzvotav
v'tzivanu al akhilat maror""")

write_lines(c, "English", 50, 625,
"""\
Blessed are You, Lord our God, King of the Universe, who has
sanctified us with His commandments and has commanded us on
the eating of marror. 
""")

c.showPage()

write(c, "English", 200, 800, "Korekh")

write_lines(c, "English", 50, 750,
"""\
All present should take a kazayit from the third whole
matsa with a kazayit of marror, wrap them together and eat
them while reclining and without saying a blessing.
Before he eats it, he should say:
""")

write_lines(c, "Hebrew", 200, 650,
"""\
זֵכֶר לְמִקְדָּשׁ כְּהִלֵּל. כֵּן עָשָׂה הִלֵּל בִּזְמַן שֶׁבֵּית הַמִּקְדָּשׁ הָיָה קַיָּם:
הָיָה כּוֹרֵךְ מַצָּה וּמָרוֹר וְאוֹכֵל בְּיַחַד, לְקַיֵּם מַה שֶּׁנֶּאֱמַר: עַל מַצּוֹת וּמְרוׂרִים יֹאכְלֻהוּ.
""")

write_lines(c, "English", 50, 600,
"""\
Zekher lamikdash k'Hillel.
Ken 'asah Hillel b'zman sh'beit hamikdash haya kayam:
Hayah korekh matzah u'maror v'okhel b'yahad, lekayem mah sh'ne'emar:
Al matzot u'mrorim yokhluhu
""")

write_lines(c, "English", 50, 525,
"""\
In memory of the Temple according to Hillel.
This is what Hillel would do when the
Temple existed:
He would wrap the matsa and marror and eat them together,
in order to fulfill what is stated, (Exodus 12:15): 
"You should eat it upon matsot and marrorim."
""")

c.showPage()

write(c, "English", 200, 800, "Shulkhan 'Orekh")

write(c, "English", 50, 750, "We eat and drink")

c.showPage()

write(c, "English", 200, 800, "Tzafun")

write_lines(c, "English", 50, 750,
"""\
After the end of the meal, all those present take a kazayit 
from the matsa, that was concealed for the afikoman, and eat a 
kazayit from it while reclining.

Before eating the afikoman, he should say: 
"In memory of the Pesach sacrifice that was 
eaten upon being satiated." 
""")

c.showPage()


write(c, "English", 200, 800, "Barekh")

write_lines(c, "Hebrew", 375, 750,
"""\
בָּרוּךְ אַתָּה ה', אֱלֹהֵינוּ מֶלֶךְ הָעוֹלָם,
הַזָּן אֶת הָעוֹלָם כֻּלּוֹ בְּטוּבוֹ בְּחֵן בְּחֶסֶד
וּבְרַחֲמִים, הוּא נוֹתֵן לֶחֶם לְכָל בָּשָׂר
כִּי לְעוֹלָם חַסְדוֹ. וּבְטוּבוֹ הַגָּדוֹל תָּמִיד
לֹא חָסַר לָנוּ, וְאַל יֶחְסַר לָנוּ מָזוֹן לְעוֹלָם וָעֶד.
בַּעֲבוּר שְׁמוֹ הַגָּדוֹל,
כִּי הוּא אֵל זָן וּמְפַרְנֵס לַכֹּל וּמֵטִיב לַכֹּל,
וּמֵכִין מָזוֹן לְכָל בְּרִיּוֹתָיו אֲשֶׁר בָּרָא.
בָּרוּךְ אַתָּה ה', הַזָּן אֶת הַכֹּל.
""")

write_lines(c, "English", 50, 750,
"""\
Ba-ruch a-tah A-do-nai, E-lo-hei-nu 
Me-lech Ha-o-lam, Ha-zan et ha-o-lam
ku-lo, b'tu-vo, b'chein b'che-sed
uv-ra-cha-mim, hu no-tein le-chem l'chawl
ba-sar, ki l'o-lam chas-do. Uv-tu-vo ha-ga-dol
i-ma-nu, ta-mid lo cha-seir la-nu, v'al yech-sar
la-nu, ma-zon l'o-lam va-ed. Ba-a-vur sh'mo
ha-ga-dol, ki hu Eil zan um-far-neis la-kol,
u-mei-tiv la-kol, u-mei-chin ma-zon
l'chawl b'ri-yo-tav a-sher ba-ra.
Ka-a-mur: Po-tei-ach et ya-de-cha, u-mas-bi-a
l'chawl chai ra-tson. Ba-ruch a-tah A-do-nai,
ha-zan et ha-kol. (A-mein. )
"""
)

write_lines(c, "English", 50, 550,
"""\
Blessed are You, Lord our God, King of the Universe, who nourishes
the entire world in His goodness, in grace, in kindness and in mercy;
He gives bread to all flesh since His kindness is forever. And in His great
goodness, we always have not lacked, and may we not lack nourishment
forever and always, because of His great name. Since He is a Power that
feeds and provides for all and does good to all and prepares nourishment 
for all of his creatures that he created. Blessed are You, Lord,
who sustains all. 
""")

write_lines(c, "English", 50, 350,
"""\
No-deh l'cha
A-do-nai E-lo-hei-nu,
al she-hin-chal-ta la-a-vo-tei-nu
e-rets chem-dah to-vah ur-cha-vah.
V'al she-ho-tsei-ta-nu
A-do-nai E-lo-hei-nu
mei-e-rets mits-ra-yim,
uf-di-ta-nu mi-beit a-va-dim,
v'al b'ri-t'cha she-cha-tam-ta biv-sa-rei-nu,
v'al to-ra-t'cha she-li-mad-ta-nu,
v'al chu-ke-cha she-ho-da-ta-nu,
v'al chai-yim chein va-che-sed
she-cho-nan-ta-nu, v'al a-chi-lat ma-zon 
sha-a-tah zan um-far-neis o-ta-nu ta-mid,
b'chawl yom uv-chawl eit uv-chawl sha-ah.
""")

write_lines(c, "Hebrew", 300, 350,
"""\
נוֹדֶה לְךָ ה' אֱלֹהֵינוּ עַל
שֶׁהִנְחַלְתָּ לַאֲבוֹתֵינוּ אֶרֶץ חֶמְדָה טוֹבָה וּרְחָבָה,
וְעַל שֶׁהוֹצֵאתָנוּ ה' אֱלֹהֵינוּ מֵאֶרֶץ מִצְרַיִם,
וּפְדִיתָנוּ מִבֵּית עֲבָדִים,
וְעַל בְּרִיתְךָ שֶׁחָתַמְתָּ בְּבְשָׂרֵנוּ, וְעַל תּוֹרָתְךָ שֶׁלִּמַּדְתָּנוּ,
וְעַל חֻקֶּיךָ שֶׁהוֹדַעְתָּנוּ, וְעַל חַיִּים חֵן וָחֶסֶד שֶׁחוֹנַנְתָּנוּ,
וְעַל אֲכִילַת מָזוֹן שָׁאַתָּה זָן וּמְפַרְנֵס אוֹתָנוּ תָּמִיד,
בְּכָל יוֹם וּבְכָל עֵת וּבְכָל שָׁעָה:
""")

write_lines(c, "English", 50, 125,
"""\
We thank you, Lord our God, that you have given as an inheritance
to our ancestors a lovely, good and broad land, and that You took us out, 
Lord our God, from the land of Egypt and that You redeemed us from a 
house of slaves, and for Your covenant which You have sealed in our flesh, 
and for Your Torah that You have taught us, and for Your statutes which You 
have made known to us, and for life, grace and kindness that You have
granted  us and for the eating of nourishment that You feed and provide for
us always, on all days, and at all times and in every hour. 
""")


c.showPage()

write_lines(c, "English", 50, 750,
"""\
V'al ha-kol A-do-nai E-lo-hei-nu
a-nach-nu mo-dim lach, um-va-r'chim
o-tach, yit-ba-reich shim-cha b'fi
kawl chai ta-mid l'o-lam va-ed.
Ka-ka-tuv: v'a-chal-ta v'sa-va-ta,
u-vei-rach-ta et A-do-nai E-lo-he-cha,
al ha-a-rets ha-to-vah a-sher na-tan lach.
Ba-ruch a-tah A-do-nai,
al ha-a-rets v'al ha-ma-zon.
""")

write_lines(c, "Hebrew", 375, 750,
"""\
וְעַל הַכּל ה' אֱלֹהֵינוּ, 
אֲנַחְנוּ מוֹדִים לָךְ וּמְבָרְכִים
אוֹתָךְ, יִתְבָּרַךְ שִׁמְךָ בְּפִי כָּל חַי 
תָּמִיד לְעוֹלָם וָעֶד. כַּכָּתוּב:
וְאָכַלְתָּ וְשָׂבַעְתָּ וּבֵרַכְתָּ אֶת ה'
אֱלֹהֵיךָ עַל הָאָרֶץ הַטּוֹבָה אֲשֶּׁר נָתַן לָךְ.
בָּרוּךְ אַתָּה ה', עַל הָאָרֶץ וְעַל הַמָּזוֹן:
""")

write_lines(c, "English", 50, 600,
"""\
And for everything, Lord our God, we thank You and bless You;
may Your name be blessed by the mouth of all life, constantly
forever and always, as it is written; "And you shall eat and
you shall be satiated and you shall bless the Lord your God
for the good land that He has given you."
Blessed are You, Lord, for the land and for the nourishment. 
""")

write_lines(c, "English", 50, 450,
"""\
Ra-cheim A-do-nai E-lo-hei-nu al Yis-ra-eil
a-me-cha, v'al Y'ru-sha-la-yim i-re-cha,
v'al Tsi-yon mish-kan k'vo-de-cha,
v'al mal-chut beit Da-vid m'shi-che-cha,
v'al ha-ba-yit ha-ga-dol v'ha-ka-dosh
she-nik-ra shim-cha a-lav. E-lo-hei-nu
A-vi-nu r'ei-nu zo-nei-nu par-n'sei-nu
v'chal-k'lei-nu v'har-vi-chei-nu,
v'har-vach la-nu A-do-nai E-lo-hei-nu
m'hei-rah mi-kawl tsa-ro-tei-nu.
V'na al tats-ri-chei-nu A-do-nai E-lo-hei-nu,
lo li-dei ma-t'nat ba-sar v'dam,
v'lo li-dei hal-va-a-tam,
ki im l'ya-d'cha ha-m'lei-ah ha-p'tu-chah ha-k'do-shah
v'ha-r'cha-vah, she-lo nei-vosh v'lo ni-ka-leim
l'o-lam va-ed.
"""
)

write_lines(c, "Hebrew", 350, 450,
"""\
רַחֵם נָא ה' אֱלֹהֵינוּ עַל יִשְׂרָאַל עַמֶּךָ וְעַל 
יְרוּשָׁלַיִם עִירֶךָ וְעַל צִיּוֹן מִשְׁכַּן כְּבוֹדֶךָ
 וְעַל מַלְכוּת בֵּית דָּוִד מְשִׁיחֶךָ וְעַל הַבַּיִת
 הַגָּדוֹל וְהַקָּדוֹשׁ שֶׁנִּקְרָא שִׁמְךָ עָלָיו: אֱלֹהֵינוּ אָבִינוּ,
 רְעֵנוּ זוּנֵנוּ פַרְנְסֵנוּ וְכַלְכְּלֵנוּ וְהַרְוִיחֵנוּ,
 וְהַרְוַח לָנוּ ה' אֱלֹהֵינוּ מְהֵרָה מִכָּל צָרוֹתֵינוּ.
 וְנָא אַל תַּצְרִיכֵנוּ ה' אֱלֹהֵינוּ,
 לֹא לִידֵי מַתְּנַת בָּשָׂר וָדָם וְלֹא לִידֵי הַלְוָאתָם,
 כִּי אִם לְיָדְךָ הַמְּלֵאָה הַפְּתוּחָה הַקְּדוֹשָׁה וְהָרְחָבָה,
 שֶׁלֹא נֵבוֹשׁ וְלֹא נִכָּלֵם לְעוֹלָם וָעֶד.
""")

write_lines(c, "English", 50, 200,
"""
Please have mercy, Lord our God, upon Israel, Your people;
and upon Jerusalem, Your city; and upon Zion, the dwelling
place of Your Glory; and upon the monarchy of the House of David,
Your appointed one; and upon the great and holy house that
Your name is called upon. Our God, our Father, tend us, sustain us,
provide for us, relieve us and give us quick relief, Lord our God,
from all of our troubles. And please do not make us needy, 
Lord our God, not for the gifts of flesh and blood, and not for 
their loans, but rather from Your full, open, holy and broad hand, 
so that we not be embarrassed and we not be ashamed forever and always. 
""")

c.showPage()

write_lines(c, "English", 50, 750,
"""\
Elohainu Veilohei Avoteinu ya’aleh v’yavo,
v’yagiya, v’yeiraheh, v’yeirathzeh
v’yishma, v’yipahkeyd, v’yizahcher, 
zichroneynu u’fikdoneinu, v’zichron 
avoteynu, v’zichron mahshiyach ben 
Dahveed ahvdecha, vzichron yerushalayim 
ir kadshehchah,  v’zichron kol amcha beit
yisrael l’fahnecha, l’flaytah,  l’tovah,
l’cheyn, ul’chesed, ulerachahmim,
lechayyim, uleshalom b’yom Chag Hamatzot
hazeh, zahchreynu Adonai Eloheinu bo 
l’tovah,  ufahkdeynu bo l’v’racha,
v’hoshiyeinu bo l’chayyim. U’cidcahr
y’shuah v’rachamim choos v’chaneynu 
vrahcheym aleynu, v’hoshiyeinu, ki 
ailecha eyneynu, ki El melech chanun
v’rachum ahata. 
""")

write_lines(c, "Hebrew", 375, 750,
"""\
אֱלֹהֵינוּ וֵאלֹהֵי אֲבוֹתֵינוּ,
יַעֲלֶה וְיָבֹא וְיַגִּיעַ וְיֵרָאֶה וְיֵרָצֶה
וְיִשָּׁמַע וְיִפָּקֵד וְיִזָּכֵר זִכְרוֹנֵנוּ וּפִקְדּוֹנֵנוּ,
וְזִכְרוֹן אֲבוֹתֵינוּ,
וְזִכְרוֹן מָשִׁיחַ בֶּן דָּוִד עַבְדֶּךָ,
וְזִכְרוֹן יְרוּשָׁלַיִם עִיר קָדְשֶׁךָ,
וְזִכְרוֹן כָּל עַמְּךָ בֵּית יִשְׂרָאַל לְפָנֶיךָ,
לִפְלֵיטָה לְטוֹבָה לְחֵן וּלְחֶסֶד וּלְרַחֲמִים,
לְחַיִּים וּלְשָׁלוֹם בְּיוֹם חַג הַמַּצּוֹת הַזֶּה זָכְרֵנוּ ה'
אֱלֹהֵינוּ בּוֹ לְטוֹבָה וּפָקְדֵנוּ בוֹ לִבְרָכָה
וְהושִׁיעֵנוּ בוֹ לְחַיִּים. וּבִדְבַר יְשׁוּעָה וְרַחֲמִים
חוּס וְחָנֵּנוּ וְרַחֵם עָלֵינוּ וְהוֹשִׁיעֵנוּ,
כִּי אֵלֶיךָ עֵינֵינוּ, כִּי אֵל מֶלֶךְ
חַנּוּן וְרַחוּם אָתָּה.וּבְנֵה יְרוּשָׁלַיִם עִיר הַקֹּדֶשׁ
בִּמְהֵרָה בְיָמֵינוּ. בָּרוּךְ אַתָּה ה',
בּוֹנֶה בְרַחֲמָיו יְרוּשָׁלַיִם. אָמֵן.
""")

write_lines(c, "English", 50, 500,
"""\
God and God of our ancestors, may there ascend and come and
reach and be seen and be acceptable and be heard and be recalled
and be remembered - our remembrance and our recollection;
and the remembrance of our ancestors; and the remembrance of the
messiah, the son of David, Your servant; and the remembrance of
Jerusalem, Your holy city; and the remembrance of all Your people,
the house of Israel - in front of You, for survival, for good,
for grace, and for kindness, and for mercy, for life and for peace 
on this day of the Festival of Matsot. Remember us, Lord our God, 
on it for good and recall us on it for survival and save us on it 
for life, and by the word of salvation and mercy, pity and grace us
and have mercy on us and save us, since our eyes are upon You, since 
You are a graceful and merciful Power. And may You build Jerusalem,
the holy city, quickly and in our days. Blessed are You, Lord, who 
builds Jerusalem in His mercy. Amen. 
""")

c.showPage()

write_lines(c, "English", 50, 750,
"""\
Ba-ruch a-tah A-do-nai,
E-lo-hei-nu Me-lech Ha-o-lam,
ha-Eil a-vi-nu mal-kei-nu
a-di-rei-nu bor-ei-nu go-a-lei-nu 
yots-rei-nu k'do-shei-nu k'dosh 
Ya-a-kov, ro-ei-nu, ro-ei Yis-ra-eil,
ha-me-lech ha-tov v'ha-mei-tiv la-kol,
b'chawl yom va-yom hu hei-tiv la-nu,
hu mei-tiv la-nu, hu yei-tiv la-nu.
Hu g'ma-la-nu, hu gom-lei-nu, hu 
yig-m'lei-nu la-ad, l'chein ul-che-sed 
ul-ra-cha-mim ul-re-vach, ha-tsa-lah 
v'hats-la-chah, b'ra-cha vi-shu-ah, 
ne-cha-mah par-na-sah v'chal-ka-lah,
v'ra-cha-mim v'chai-yim v'sha-lom 
v'chawl tov, u-mi-kawl tuv l'o-lam al
y'chas-rei-nu.
""")

write_lines(c, "Hebrew", 350, 750,
"""\
בָּרוּךְ אַתָּה ה', אֱלֹהֵינוּ מֶלֶךְ הָעוֹלָם, הָאֵל
אָבִינוּ מַלְכֵּנוּ אַדִירֵנוּ בּוֹרְאֵנוּ גּוֹאֲלֵנוּ יוֹצְרֵנוּ
קְדוֹשֵׁנוּ קְדוֹשׁ יַעֲקֹב רוֹעֵנוּ רוֹעֵה יִשְׂרָאַל
הַמֶּלֶךְ הַטּוֹב וְהַמֵּטִיב לַכּל שֶׁבְּכָל יוֹם וָיוֹם
הוּא הֵטִיב, הוּא מֵטִיב, הוּא יֵיטִיב לָנוּ.
הוּא גְמָלָנוּ הוּא גוֹמְלֵנוּ הוּא יִגְמְלֵנוּ לָעַד,
לְחֵן וּלְחֶסֶד וּלְרַחֲמִים וּלְרֶוַח הַצָּלָה וְהַצְלָחָה,
בְּרָכָה וִישׁוּעָה נֶחָמָה פַּרְנָסָה
וְכַלְכָּלָה וְרַחֲמִים וְחַיִּים וְשָׁלוֹם וְכָל טוֹב,
וּמִכָּל טוּב לְעוֹלָם עַל יְחַסְּרֵנוּ.
""")

write_lines(c, "English", 50, 500,
"""
Blessed are You, Lord our God, King of the Universe,
the Power, our Father, our King, our Mighty One, our 
Creator, our Redeemer, our Shaper, our Holy One, 
the Holy One of Ya'akov, our Shepard, the Shepard of Israel, 
the good King, who does good to all, since on every single 
day He has done good, He does good, He will do good, to us; 
He has granted us, He grants us, He will grant us forever - 
in grace and in kindness, and in mercy, and in relief - 
rescue and success, blessing and salvation, consolation, 
provision and relief and mercy and life and peace and all 
good; and may we not lack any good ever.
""")

c.showPage()

write_lines(c, "English", 50, 750,
"""\
Ha-ra-cha-man, hu yim-loch a-lei-nu
l'o-lam va-ed. Ha-ra-cha-man,hu
yit-ba-reich ba-sha-ma-yim u-va-a-rets.
Ha-ra-cha-man, hu yish-ta-bach l'dor
do-rim, v'yit-pa-eir ba-nu la-ad
ul-nei-tsach n'tsa-chim, v'yit-ha-dar
ba-nu la-ad ul-ol-mei o-la-mim. 
Ha-ra-cha-man, hu y'far-n'sei-nu
b'cha-vod. Ha-ra-cha-man, hu yish-bor
ol hago-yim mei-al tsa-va-rei-nu,
v'hu yo-li-chei-nu ko-m'mi-yut l'ar-tsei-nu.
Ha-ra-cha-man, hu yish-lach b'ra-chah
m'ru-bah b'-va-yit zeh, v'al shul-chan
zeh she-a-chal-nu a-lav. Ha-ra-cha-man,
hu yish-lach la-nu et Ei-li-ya-hu ha-na-vi,
za-chur la-tov, vi-va-ser la-nu b'so-rot
to-vot, y'shu-ot v'ne-cha-mot.
Ha-ra-cha-man, hu y'va-reich et ba-al 
ha-ba-yit ha-zeh, v'et  ba-a-lat ha-ba-yit
ha-zeh, o-tam v'et bei-tam v'et zar-am v'et
kawl a-sher la-hem, o-ta-nu v'et kawl
a-sher la-nu, k'mo she-berach et
a-vo-tei-nu Av-ra-ham Yits-chak v'Ya-a-kov
ba-kol mi-kol kol, kein y'va-reich o-ta-nu,
ku-la-nu ya-chad, biv-ra-chah sh'lei-mah,
v'no-mar a-mein.
Be-ma-rom y'lam-du a-lav v'-a-lei-nu
z'chut, shet-hei l'mish-me-ret sha-lom.
V'ni-sa v'ra-chah mei-eit A-do-nai,
uts-da-kah mei-E-lo-hei yish-ei-nu,
v'nim-tsa chein v'sei-chel tov b'ei-nei
E-lo-him v'a-dam. Ha-ra-cha-man,
hu yan-chi-lei-nu l'yom she-ku-lo tov.
Ha-ra-cha-man, hu y'za-kei-nu li-mot
ha-ma-shi-ach ul-chai-yei ha-o-lam ha-ba.
Mig-dol y'shu-ot mal-ko v'o-seh che-sed
lim-shi-cho, l'Da-vid ul-zar-o ad o-lam.
O-seh sha-lom bim-ro-mav, hu ya-a-seh
sha-lom a-lei-nu v'al kawl Yis-ra-eil,
v'im-ru a-mein.
Y'ru et A-do-nai, k'do-shav, ki ein mach-sor li-rei-av.
K'fi-rim ra-shu v'ra-ei-vu, v'dor-shei A-do-nai lo yach-s'ru
chawl tov. Ho-du La-do-nai ki tov,
ki l'o-lam chas-do. Po-tei-ach et ya-de-cha,
u-mas-bi-a l'chawl chai ra-tson.
Ba-ruch ha-ge-ver a-sher yiv-tach ba-do-nai,
v'ha-yah A-do-nai miv-ta-cho.
""")

write_lines(c, "Hebrew", 350, 750,
"""\
הָרַחֲמָן הוּא יִמְלוֹךְ עָלֵינוּ לְעוֹלָם וָעֶד.
 הָרַחֲמָן הוּא יִתְבָּרַךְ בַּשָּׁמַיִם וּבָאָרֶץ.
 הָרַחֲמָן הוּא יִשְׁתַּבַּח לְדוֹר דּוֹרִים,
 וְיִתְפָּאַר בָּנוּ לָעַד וּלְנֵצַח נְצָחִים,
 וְיִתְהַדַּר בָּנוּ לָעַד וּלְעוֹלְמֵי עוֹלָמִים. הָרַחֲמָן הוּא יְפַרְנְסֵנוּ בְּכָבוֹד.
 הָרַחֲמָן הוּא יִשְׁבּוֹר עֻלֵּנוּ מֵעַל צַּוָּארֵנוּ,
 וְהוּא יוֹלִיכֵנוּ קוֹמְמִיּוּת לְאַרְצֵנוּ. הָרַחֲמָן הוּא יִשְׁלַח לָנוּ
 בְּרָכָה מְרֻבָּה בַּבַּיִת הַזֶּה, וְעַל שֻׁלְחָן זֶה שֶׁאָכַלְנוּ עָלָיו.
 הָרַחֲמָן הוּא יִשְׁלַח לָנוּ אֶת אֵלִיָּהוּ הַנָּבִיא זָכוּר לַטּוֹב,
 וִיבַשֶּׂר לָנוּ בְּשׂוֹרוֹת טוֹבוֹת יְשׁוּעוֹת וְנֶחָמוֹת.
 הָרַחֲמָן הוּא יְבָרֵךְ אֶת אִשְתִּי.
 הָרַחֲמָן הוּא יְבָרֵךְ אֶת
 בַּעַל הַבַּיִת הַזֶּה. וְאֶת בַּעֲלַת הַבַּיִת הַזֶּה,
 אוֹתָם וְאֶת בֵּיתָם וְאֶת זַרְעָם וְאֶת כָּל אֲשֶׁר לָהֶם.
 אוֹתָנוּ וְאֶת כָּל אֲשֶׁר לָנוּ, כְּמוֹ שֶׁנִּתְבָּרְכוּ
 אֲבוֹתֵינוּ אַבְרָהָם יִצְחָק וְיַעֲקֹב בַּכֹּל מִכֹּל כֹּל,
 כֵּן יְבָרֵךְ אוֹתָנוּ כֻּלָּנוּ יַחַד בִּבְרָכָה שְׁלֵמָה,
 וְנֹאמַר, אָמֵן. בַּמָּרוֹם יְלַמְּדוּ עֲלֵיהֶם
 וְעָלֵינוּ זְכוּת שֶׁתְּהֵא לְמִשְׁמֶרֶת שָׁלוֹם.
 וְנִשָּׂא בְרָכָה מֵאֵת ה', וּצְדָקָה מֵאלֹהֵי יִשְׁעֵנוּ,
 וְנִמְצָא חֵן וְשֵׂכֶל טוֹב בְּעֵינֵי אֱלֹהִים וְאָדָם.
 הָרַחֲמָן הוּא יְזַכֵּנוּ לִימוֹת הַמָּשִׁיחַ
 וּלְחַיֵּי הָעוֹלָם הַבָּא. מִגְדּוֹל יְשׁוּעוֹת מַלְכּוֹ
 וְעֹשֶׂה חֶסֶד לִמְשִׁיחוֹ לְדָוִד וּלְזַרְעוֹ עַד עוֹלָם.
 עשֶׂה שָׁלוֹם בִּמְרוֹמָיו, הוּא יַעֲשֶׂה שָׁלוֹם
 עָלֵינוּ וְעַל כָּל יִשְׂרָאַל וְאִמְרוּ, אָמֵן.
 יִרְאוּ אֶת ה' קְדֹשָׁיו,
 כִּי אֵין מַחְסוֹר לִירֵאָיו. כְּפִירִים רָשׁוּ וְרָעֵבוּ,
 וְדֹרְשֵׁי ה' לֹא יַחְסְרוּ כָל טוֹב.
 הוֹדוּ לַיי כִּי טוֹב כִּי לְעוֹלָם חַסְדּוֹ.
 פּוֹתֵחַ אֶת יָדֶךָ, וּמַשְׂבִּיעַ לְכָל חַי רָצוֹן.
 בָּרוּךְ הַגֶּבֶר אֲשֶׁר יִבְטַח בַּיי, וְהָיָה ה' מִבְטַחוֹ.
 נַעַר הָיִיתִי גַם זָקַנְתִּי, וְלֹא רָאִיתִי צַדִּיק נֶעֱזָב,
 וְזַרְעוֹ מְבַקֶּשׁ לָחֶם. יי עֹז לְעַמּוֹ יִתֵּן,
 ה' יְבָרֵךְ אֶת עַמּוֹ בַשָּׁלוֹם.
""")

c.showPage()

write_lines(c, "English", 50, 750,
"""\
May the Merciful One reign over us forever and always.
May the Merciful One be blessed in the heavens and in the earth.
May the Merciful One be praised for all generations,
and exalted among us forever and ever, and glorified among us
always and infinitely for all infinities. May the Merciful One sustain
us honorably. May the Merciful One break our yolk from upon our necks and
bring us upright to our land. May the Merciful One send us multiple blessing,
to this home and upon this table upon which we have eaten.
May the Merciful One send us Eliyahu the prophet -
may he be remembered for good - and he shall announce to us 
tidings of good,of salvation and of consolation.
May the Merciful One bless my wife. May the Merciful One bless the
master of  this home and the mistress of this home, they and their home 
and their offspringand everything that is theirs. Us and all that is ours;
as were blessed Avraham, Yitschak and Ya'akov, in everything,
from everything, with everything,so too should He bless us,
all of us together, with acomplete blessing and we shall say, Amen.
From above,may they advocate upon them and upon us merit,
that should protect us in peace; and may we carry a  blessing from the Lord 
and charity from the God of our salvation; and find grace and good
understanding in the eyes of God and man. May the Merciful One give us to
inherit the day that will be all good. May the Merciful One give us merit for
the times of the messiah and for life in the world to come. A tower of
salvations is our King;  may He do kindness with his messiah, with David and
his offspring, forever. The One who makes peace above, may He make peace
upon us and upon all of Israel; and say, Amen. Fear the Lord, His holy ones,
since there isno lacking for those that fear Him. Young lions may go
without and hunger, but those that seek the Lord will not lack any good thing.
Thank the Lord, since He is good, since His kindness is forever. You open
Your hand and satisfy the will of all living things. Blessed is the man that
trusts in the Lord and the Lord is his security. I was a youth and I have also
aged and I have not seen a righteous man forsaken and his offspring seeking
bread. The Lord will give courage to His people.
The Lord will bless His people with peace. 
""")

c.showPage()

write(c, "English", 200, 800, "Barekh -- Third Cup")

write_lines(c, "English", 50, 750,
"""\
Baruch Attah Ad-nai Eloheinu Melekh
HaOlam, Boreh Pri HaGafen
""")

write_lines(c, "Hebrew", 350, 750,
"""\
בָּרוּךְ אַתָּה ה', אֱלהֵינוּ מֶלֶךְ הָעוֹלָם בּוֹרֵא פְּרִי הַגָּפֶן.
""")

write_lines(c, "English", 50, 700,
"""\
Blessed are You, Lord our God, King of the universe, who creates
the fruit of the vine.

We drink while reclining and do not say a blessing afterwards.

We pour the cup for Elijah and open the door.
""")

c.showPage()

write(c, "English", 200, 800, "Hallel")

write_lines(c, "English", 50, 750,
"""\
We pour the fourth cup and complete the Hallel 
""")

write_lines(c, "Hebrew", 375, 725,
"""\
הוֹדוּ לַיי כִּי טוֹב כִּי לְעוֹלָם חַסְדּוֹ
הוֹדוּ לֵאלהֵי הָאֱלהִים כל"ח
הוֹדוּ לָאֲדֹנֵי הָאֲדֹנִים כל"ח
לְעֹשֵׂה נִפְלָאוֹת גְדֹלוֹת לְבַדּוֹ כל"ח
לְעֹשֵׂה הַשָּׁמַיִם בִּתְבוּנָה כל"ח
לְרוֹקַע הָאָרֶץ עַל הַמָּיִם כל"ח 
לְעֹשֵׂה אוֹרִים גְּדֹלִים כל"ח 
אֶת הַשֶּׁמֶשׁ לְמֶמְשֶׁלֶת בַּיּוֹם כל"ח 
אֶת הַיָּרֵחַ וְכוֹכָבִים לְמֶמְשְׁלוֹת בַּלַּיְלָה כל"ח

לְמַכֵּה מִצְרַיִם בִּבְכוֹרֵיהֶם כל"ח 
וַיוֹצֵא יִשְׂרָאֵל מִתּוֹכָם כל"ח 
בְּיָד חֲזָקָה וּבִזְרוֹעַ נְטוּיָה כל"ח 
לְגֹזֵר יַם סוּף לִגְזָרִים כל"ח 
וְהֶֶעֱבִיר יִשְׂרָאֵל בְּתוֹכוֹ כל"ח 
וְנִעֵר פַּרְעֹה וְחֵילוֹ בְיַם סוּף כל"ח 
לְמוֹלִיךְ עַמּוֹ בַּמִּדְבָּר כל"ח 
לְמַכֵּה מְלָכִים גְּדֹלִים כל"ח 
וַיַּהֲרֹג מְלָכִים אַדִּירִים כל"ח 
לְסִיחוֹן מֶלֶךְ הָאֱמֹרִי כל"ח 
וּלְעוֹג מֶלֶךְ הַבָּשָׁן כל"ח 
וָנָתַן אַרְצָם לְנַחֲלָה כל"ח 
נַחֲלָה לְיִשְׂרָאֵל עַבְדוּ כל"ח 
שֶׁבְּשִׁפְלֵנוּ זָכַר לָנוּ כל"ח 
וַיִפְרְקֵנוּ מִצָּרֵינוּ כל"ח
נֹתֵן לֶחֶם לְכָל בָּשָׂר כל"ח 
הוֹדוּ לְאֵל הַשָּׁמַיִם כל"ח 
""")

write_lines(c, "English", 50, 725,
"""\
Hodu l’Adonai ki tov, ki l’olam chasdo.
Hodu lalohei ha’Elohim, k-l-c
Hodu l’Adonai ha’adonim, k-l-c
L’oseh nila’ot g’dolot l’vado, k-l-c
L’oseh hashamayim bit’vunah, k-l-c
L’roka ha’aretz al hamayim, k-l-c
L’oseh orim g’dolim, k-l-c
Et hashemesh l’memshelet bayom, k-l-c
Et hayareich v’kochavim
      l’memsh’lot balaylah, k-l-c
L’makeh mitzrayim bivchoraihem, k-l-c
Vayotzai Yisrael mitocham, k-l-c
B’yad chazakah u’vizro’a n’tuyah, k-l-c
L’gozer yam suf lig’zarim, k-l-c
V’he’evir Yisrael b’tocho, k-l-c
V’ni’er paroah v’chailo b’yam suf, k-l-c
L’molich amo bamidbar, k-l-c
L’makeh m’lachim g’dolim, k-l-c
Vayaharog m’lachim adirim, k-l-c
L’sichon melech ha’emori, k-l-c
U’l’og melech habashan, k-l-c
Vanatan artzam l’nachalah, k-l-c
Nachalah l’Yisrael avdu, k-l-c
Sheb’shiflainu zachar lanu, k-l-c
Vayif’rikainu mitzrainu, k-l-c
Notein lechem l’chol basar, k-l-c 
Hodu l’El hashamim, k-l-c
""")

write_lines(c, "English", 50, 360,
"""
Thank the Lord, since He is good, since His kindness is forever. 
Thank the Power of powers SHKIF
To the Master of mastersSHKIF
To the One who alone does wondrously great deeds SHKIF
To the one who made the Heavens with discernment SHKIF
To the One who spread the earth over the waters SHKIF
To the One who made great lights SHKIF
The sun to rule in the day SHKIF
The moon and the stars to rule in the night SHKIF
To the One that smote Egypt through their firstborn SHKIF
And He took Israel out from among them SHKIF
With a strong hand and an outstretched forearm SHKIF
To the One who cut up the Reed Sea into strips SHKIF
And He made Israel to pass through it SHKIF
And He jolted Pharaoh and his troop in the Reed Sea SHKIF 
To the One who led his people in the wilderness SHKIF 
To the One who smote great kings SHKIF 
And he killed mighty kings SHKIF Sichon, king of the Amorite SHKIF 
And Og, king of the Bashan SHKIF 
And he gave their land as an inheritance SHKIF 
An inheritance for Israel, His servant SHKIF 
That in our lowliness, He remembered us SHKIF 
And he delivered us from our adversaries SHKIF 
He gives bread to all flesh SHKIF 
Thank the Power of the heavens SHKIF 
""")

c.showPage()

write(c, "English", 200, 800, "Hallel, Fourth Cup of Wine")

write_lines(c, "English", 50, 175,
"""\
We say the blessing below and drink the cup while reclining to the left
""")

write_lines(c, "Hebrew", 200, 150,
"""\
בָּרוּךְ אַתָּה ה', אֱלֹהֵינוּ מֶלֶךְ הָעוֹלָם בּוֹרֵא פְּרִי הַגָּפֶן.
""")

write_lines(c, "English", 50, 125,
"""\
Barukh attah adonai, eloheinu melekh ha'olam, boreh pri hagafen
"""
)

write_lines(c, "English", 50, 100,
"""\
Blessed are You, Lord our God, who creates the fruit of the vine. 
""")

c.showPage()

write(c, "English", 200, 800, "Nirtzah")

lines = [
("shunra", "akhla"),
("kalba", "nashakh"),
("hutra", "hikah"),
("nura", "saraf"),
("maya", "khavah"),
("tora", "shata"),
("shohet", "shahat"),
("mal'akh hamavet", "shahat"),
("hakadosh barukh hu", "shahat"),
]

text = """\
Had gadya had gadya
di'zabin abba bitrei zuzey, had gadya, had gadya
"""

for i in range(len(lines)):
    actor, action = lines[i]
    current = f"Va'ata {actor} ve'{action} "
    for run, j in enumerate(range(i-1, -1, -1)):
        actor, action = lines[j]
        current += f"le'{actor} de'{action}"
        if run % 3 == 0:
              current += "\n"
        else:
              current += " "
    current = current[:-1] + " legadya\n"
    current += "di'zabin abba b'trei zuzey, had gadya, had gadya\n"
    text += current

write_lines(c, "English", 50, 750, text)

c.showPage()

heb_lines = [
("שׁוּנְרָא", "אָכְלָה"),


]


c.save()
