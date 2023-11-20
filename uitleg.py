
import pyxel

MENU = 0
DOEL = 1
BEGIN = 2
VERLOOP_EN_EINDE = 3
TERREIN = 4
EENHEDEN = 5
BOOTEN = 6
AANVALLEN = 7
MUNITIE = 8
UITHOUDING_EN_BEWEGEN = 9
ZICHT_EENHEDEN = 10
ZICHT_TERREIN = 11
KNOPPEN = 12
TERREININSTELLINGEN = 13
WEG = 0
RIVIER = 1
BOS = 2
BERG = 3
MEER = 4
ZEE = 5
GEBOUW = 6


menu = [
    [
['                                                                '],
[' 2: doel                                                        '],
[' 3: begin                                                       '],
[' 4: verloop en einde                                            '],
[' 5: terrein                                                     '],
[' 6: eenheden                                                    '],
[' 7: boten                                                       '],
[' 8: aanvallen                                                   '],
[' 9: munitie                                                     '],
['10: uithouding en bewegen                                       '],
['11: zicht: eenheden                                             '],
['12: zicht: terrein                                              '],
['13: knoppen                                                     '],
['14: terreininstellingen                                         '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
    ],# MENU
    [
['Doel                                                            '],
['Het doel van het spel is om het leger van de vijand te verslaan '],
['Dit doe je door eenheden te plaatsen                            '],
['en je tegenstander aan te vallen                                '],
    ],# DOEL
    [
['Begin                                                           '],
['  - Je hebt vanaf de start een terrein                          '],
['       Wil je een ander random terrein? Druk op                 '],
['  - Je kiest een budget.                                        '],
['      Dit zie je naast de letter p in de rechterbovenhoek       '],
['  - Je hebt de keuze tussen meer   of minder   punten           '],
['      Het budget heb je nodig om eenheden te plaatsen           '],
['  - Je kiest een kleur voor je eenheden                         '],
['Het aanpassen van punten,kleur,... doe je niet in het menu zelf '],
['Je plaatst je eenheden (linkermuisknop)                         '],
['hiervoor betaal je 1 punt per nivo                              '],
['Je eenheden verwijderen is via de rechtermuisknop               '],
['LET OP:                                                         '],
['je mag alleen een eenheid zetten als                            '],
['het vakje bij je muis geen kruis is                             '],
['Op welk nivo je jezelf bevindt (1-4)                            '],
['zie je aan de linkerkant van de eenheid                         '],
['PAS OP Je moet een generaal bij je eenheden hebben(zie eenheden)'],
['Je kan van elk type/nivo, een beperkt aantal eenheden plaatsen  '],
['Als beide spelers hun eenheden hebben geplaatst                 '],
['druk je op   om te beginnen                                     '],
    ],# BEGIN
    [
['Verloop                                                         '],
['Wanneer je aan de beurt bent kan je eenheden selecteren en      '],
['verplaatsen of aanvallen, dit staat uitgelegd onder aanvallen   '],
['Om de informatie over je terrein te bekijken druk je op (i)     '],
['Als je een beurt wil overslaan met de geselecteerde eenheid     '],
['druk je op de  spatiebalk                                       '],
['Via  Tab  ga je naar de volgende eenheid die binnen diezelfde   '],
['beurt nog niets gedaan heeft                                    '],
['Via enter begin of eindig je je beurt                           '],
['Je plaatst je eenheden (linkermuisknop)                         '],
['Selecteren en verplaatsen, doe je via de linkermuisknop         '],
['Aanvallen doe je via de rechtermuisknop.                        '],
['Via de middelste muisknop kan je bouwen(acties van de ingenieur)'],
['Deze staan verder uitgelegd bij de eenheden                     '],
['                                                                '],
['                                                                '],
['Einde                                                           '],
['Als alle eenheden van een kleur verslagen zijn                  '],
['is het spel gedaan                                              '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
    ],# VERLOOP_EN_EINDE
    [
['Terrein                                                         '],
['Er zijn 7 soorten terrein,                                      '],
['deze zijn te zien aan de verschillende kleuren                  '],
['1: Gras: standaard, er verandert niets                          '],#[11, 3, 6, 13, 15, 4, 14, 13, 4]
['2: Bos: 2 vakjes minder bereik zichtbaarheid gaat omhoog met 3  '],
['   hierdoor kan je moeilijker gezien worden                     '],
['3: Water: Je kan minder goed verdedigen (-20)                   '],
['4: Berg: je kan beter verdedigen + 15,                          '],
['   je bereik gaat omhoog (+ 2 vakjes),                          '],
['   je zicht wordt beter waardoor je verder kan zien (+4)        '],
['   je zichtbaarheid daalt -2, je word makkelijker gezien        '],
['5: Weg: Je kan verder lopen                                     '],
['6: Brug: Je kan verder lopen                                    '],
['7: Gebouw: je kan je beter verdedigen (+5)                      '],
['   je zichtbaarheid gaat omhoog +2, je word moeilijker gezien   '],
['   maar je zicht daalt waardoor je minder ver kan zien (-1)     '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
    ],# TERREIN
    [
['Eenheden                                                        '],
['Nivo I = Soldaat                                                '],
['Nivo II = Sergeant                                              '],
['Nivo III = Kapitein                                             '],
['Nivo IV = Generaal                                              '],
['Hieronder vind je de eigenschappen van de verschillende eenheden'],
['   Deze kwaliteiten zijn niet afhankelijk van de kleur          '],
['            Zwaard| Speer| Paard| Kanon| Boogschutter| Ingenieur'],
['Aanvallen  |+     |-     |+     |+     |             |-         '],
['Verdedigen |+     |++    |      |-     |-            |-         '],
['Bewegen    |      |      |++    |-     |nivoI+       |          '],
['Bereik     |      |      |      |++    |             |          '],
['Zicht      |      |      |nivoI+|      |             |          '],
['Extra      |      |      |      |      |             |bouwen    '],
['De waarde van je eenheden zie je rechts onderaan in dit kader   '],
['Let op: per kleur kan dit verschillen                           '],
['Ook kan je de sterkte herkennen aan de sterren rechts bovenaan  '],
['Extra                                                           '],
['Enkel de ingenieur kan ‘bouwen’                                 '],
['   Dit betekent dat hij volgende veranderingen kan doen:        '],
['Bos --> gras                                                    '],
['Gras --> weg                                                    '],
['Water --> brug                                                  '],
    ],# EENHEDEN
    [
['Boten                                                           '],
['druk op   om boten te kunnen plaatsen                           '],
['boten kunnen alleen op water bewegen                            '],
['bij transportboten is het net als of er een weg onder is        '],
['hierdoor kunnen eenheden gemakelijker een rivier over           '],
['LET OP                                                          '],
['je kunt de eenheden niet op de boot zeten                       '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
    ],# BOOTEN
    [
['Aanvallen                                                       '],
['Je valt een vijand aan door op je rechtermuisknop te klikken    '],
['Je klikt hiervoor op de eenheid van de andere kleur             '],
['1: algemene aanval                                              '],
['Om een vijand aan te vallen moet hij binnen je bereik zijn      '],
['Dit wil zeggen dat je naast je vijand moet staan                '],
['of in een rechte lijn naar je vijand moet kunnen bewegen        '],
['Een aanval op je vijand zorgt ervoor                            '],
['dat hij moraal en gezondheid verliest                           '],
['Tip: Een aanval met een aanloop bezorgt je vijand meer schade   '],
['Hoe groter de aanloop, hoe meer schade                          '],
['Wanneer je aanvalt is er de mogelijkheid                        '],
['dat de eenheid van je vijand verplaatst naar achteren           '],
['                                                                '],
['2 Schieten                                                      '],
['Om een vijand aan te vallen moet hij binnen je bereik zijn      '],
['Je kan op de vijand schieten wanneer er een doelwit op staat    '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
    ],# AANVALLEN
    [
['munitie                                                         '],
['de munitie van een eenheid is                                   '],
['het aantal keren dat het kan schieten                           '],
['als dit bij een boogschuter of kanon op 0 graakt                '],
['veranderd deze eenheid in een zwaardvechter van dat nivo        '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
    ],# MUNITIE
    [
['Uithouding                                                      '],
['Verliezen                                                       '],
['Je verliest uithouding bij bewegingen                           '],
['De hoeveelheid hangt af van de ondergrond waarover je beweegt   '],
['(Staat aangegeven bij de terreininformatie)                     '],
['                                                                '],
['Bijkrijgen                                                      '],
['Je uithouding gaat terug omhoog na iedere beurt,                '],
['de hoeveelheid uithouding is afhankelijk van je type en nivo    '],
['                                                                '],
['                                                                '],
['Bewegen                                                         '],
['Als je een eenheid hebt geselecteerd die je wil verplaatsen,    '],
['kan je met je muis naar een vakje bewegen waar je naartoe wil   '],
['Wanneer dit oplicht kan je je naar dat vakje verplaatsen        '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
    ],# UITHOUDING_EN_BEWEGEN
    [
['Zicht                                                           '],
['Eenheden                                                        '],
['Je kan zien wanneer je het zicht van je eenheid                 '],
['min de zichtbaarheid van je vijand                              '],
['min het aantal vakjes verschil doet en dit groter is dan 0      '],
['Bijvoorbeeld                                                    '],
['Zicht eigen eenheid - zichtbaarheid vijand - vakjes verschil >0 '],
['8 - 4 - 1 = 3                                                   '],
['Zicht eigen eenheid                                             '],
['Je zicht is standaard 8 maar kan veranderen met terrein         '],
['Het zicht is ook afhankelijk van welke eenheid je gebruikt      '],
['Zichtbaarheid vijand                                            '],
['De zichtbaarheid van je vijand is standaard 4                   '],
['maar kan veranderen met terrein (bos, berg, …)                  '],
['Aantal vakjes verschil                                          '],
['Het aantal vakjes dat aanwezig is tussen                        '],
['jouw eenheid en die van de vijand                               '],
['Het vakje waarop je tegenstander staat telt ook mee als 1       '],
['DUS 2 vakjes tussen jou en je vijand wordt geteld als 3 vakjes  '],
['                                                                '],
['                                                                '],
    ],# ZICHT_EENHEDEN
    [
['Zicht                                                           '],
['Terrein                                                         '],
['Je kan zien wanneer je het zicht van je eenheid                 '],
['min de zichtbaarheid van het terrein                            '],
['min het aantal vakjes verschil doet en dit groter is dan 0      '],
['Bijvoorbeeld                                                    '],
['Zicht eigen eenheid - zichtbaarheid terrein - vakjes verschil >0'],
['8 - 4 - 1 = 3                                                   '],
['Zicht eigen eenheid                                             '],
['Je zicht is standaard 8 maar kan veranderen met terrein         '],
['Het zicht is ook afhankelijk van welke eenheid je gebruikt      '],
['Zichtbaarheid terrein                                           '],
['De zichtbaarheid is terug te vinden bij de terrein info         '],
['Een berg kan je van verder zien                                 '],
['Aantal vakjes verschil                                          '],
['Het aantal vakjes dat aanwezig is tussen                        '],
['jouw eenheid en het terrein                                     '],
['                                                                '],
['                                                                '],
['                                                                '],
['                                                                '],
    ],# ZICHT_TERREIN
]

def toon_menu(game):
    pyxel.blt((game.breedte // 2) - 16, game.hoogte - 32, 2, 64, 0, 16, 16, pyxel.COLOR_BLACK)
    pyxel.blt((game.breedte // 2) + 0, game.hoogte - 32, 2, 80, 0, 16, 16, pyxel.COLOR_BLACK)
    pyxel.text((game.breedte // 2) - 32, game.hoogte - 8, f"pagina {game.menu_pagina + 1} van de {game.aantal_menu_paginas + 1}", 7)
    pyxel.text(2, 2, ' 1: menu', 7)

    if game.menu_pagina == KNOPPEN:
        begin_y = 180
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            pyxel.rect(65, 65, 60, 79, 9)
        if pyxel.btn(pyxel.MOUSE_BUTTON_MIDDLE):
            pyxel.rect(125, 81, 6, 54, 9)
        if pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT):
            pyxel.rect(131, 65, 60, 79, 9)
        if pyxel.btn(pyxel.KEY_TAB):
            pyxel.rect(51, begin_y, 14, 7, 9)
            pyxel.text(86, begin_y - 30, 'volgende eenheid', 7)
        # if pyxel.btn(pyxel.KEY_A):
        #     pyxel.rect(66, 196, 7, 7, 9)
        #     pyxel.text(86, 166, 'kleiner terrein', 7)
        # if pyxel.btn(pyxel.KEY_Z):
        #     pyxel.rect(74, 196, 7, 7, 9)
        #     pyxel.text(86, 166, 'groter terrein', 7)
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.rect(69, begin_y + 8, 7, 7, 9)
            pyxel.text(86, begin_y - 30, 'minder punten', 7)
        if pyxel.btn(pyxel.KEY_S):
            pyxel.rect(77, begin_y + 8, 7, 7, 9)
            pyxel.text(86, begin_y - 30, 'meer punten', 7)
        if pyxel.btn(pyxel.KEY_R):
            pyxel.rect(90, begin_y, 7, 7, 9)
            pyxel.text(86, begin_y - 30, 'random terrein', 7)
        if pyxel.btn(pyxel.KEY_C):
            pyxel.rect(88, begin_y + 16, 7, 7, 9)
            pyxel.text(86, begin_y - 30, 'volgende kleur', 7)
        if pyxel.btn(pyxel.KEY_B):
            pyxel.rect(104, begin_y + 16, 7, 7, 9)
            pyxel.text(86, begin_y - 30, 'veranderen tussen boten en eenheden', 7)
        if pyxel.btn(pyxel.KEY_I):
            pyxel.rect(122, begin_y, 7, 7, 9)
            pyxel.text(86, begin_y - 30, 'terrein info', 7)
        if pyxel.btn(pyxel.KEY_SPACE):
            pyxel.rect(88, begin_y + 24, 40, 7, 9)
            pyxel.text(86, begin_y - 30, 'geselecteerde eenheid beurt overslaan', 7)
        if pyxel.btn(pyxel.KEY_P):
            pyxel.rect(138, begin_y, 7, 7, 9)
            pyxel.text(86, begin_y - 30, 'begingen spelen', 7)
        if pyxel.btn(pyxel.KEY_M):
            pyxel.rect(141, begin_y + 8, 7, 7, 9)
            pyxel.text(86, begin_y - 30, 'menu', 7)
        if pyxel.btn(pyxel.KEY_LEFT):
            pyxel.rect(153, begin_y + 16, 7, 7, 9)
            pyxel.text(86, begin_y - 30, 'vorig type', 7)
        if pyxel.btn(pyxel.KEY_UP):
            pyxel.rect(161, begin_y + 8, 7, 7, 9)
            pyxel.text(86, begin_y - 30, 'hoger nivo', 7)
        if pyxel.btn(pyxel.KEY_DOWN):
            pyxel.rect(161, begin_y + 16, 7, 7, 9)
            pyxel.text(86, begin_y - 30, 'lager nivo', 7)
        if pyxel.btn(pyxel.KEY_RIGHT):
            pyxel.rect(169, begin_y + 16, 7, 7, 9)
            pyxel.text(86, begin_y - 30, 'volgend type', 7)
        if pyxel.btn(pyxel.KEY_KP_ENTER):
            pyxel.rect(184, begin_y + 8, 7, 15, 9)
            pyxel.text(86, begin_y - 30, 'begin / einde beurt', 7)
        pyxel.blt(64, 64, 2, 0, 24, 128, 80, pyxel.COLOR_GRAY)
        pyxel.blt(48, begin_y - 2, 2, 0, 104, 144, 40, pyxel.COLOR_BLACK)
    elif game.menu_pagina == TERREININSTELLINGEN:
        pyxel.text(2,  12, 'terreininstellingen                                             ', 7)
        pyxel.text(2,  22, '                    kans                    grootte             ', 7)
        pyxel.text(2,  32, 'weg                                                             ', 7) ,pyxel.text(89, 33, str(game.terein_instelingen[WEG].kans), 7) ,pyxel.text(189, 33, str(game.terein_instelingen[WEG].grote), 7)
        pyxel.text(2,  42, 'rivier                                                          ', 7) ,pyxel.text(89, 43, str(game.terein_instelingen[RIVIER].kans), 7) ,pyxel.text(189, 43, str(game.terein_instelingen[RIVIER].grote), 7)
        pyxel.text(2,  52, 'bos                                                             ', 7) ,pyxel.text(89, 53, str(game.terein_instelingen[BOS].kans), 7) ,pyxel.text(189, 53, str(game.terein_instelingen[BOS].grote), 7)
        pyxel.text(2,  62, 'berg                                                            ', 7) ,pyxel.text(89, 63, str(game.terein_instelingen[BERG].kans), 7) ,pyxel.text(189, 63, str(game.terein_instelingen[BERG].grote), 7)
        pyxel.text(2,  72, 'meer                                                            ', 7) ,pyxel.text(89, 73, str(game.terein_instelingen[MEER].kans), 7) ,pyxel.text(189, 73, str(game.terein_instelingen[MEER].grote), 7)
        pyxel.text(2,  82, 'zee                                                             ', 7) ,pyxel.text(89, 83, str(game.terein_instelingen[ZEE].kans), 7) ,pyxel.text(189, 83, str(game.terein_instelingen[ZEE].grote), 7)
        pyxel.text(2,  92, 'gebouw                                                          ', 7) ,pyxel.text(89, 93, str(game.terein_instelingen[GEBOUW].kans), 7) ,pyxel.text (189, 93, str(game.terein_instelingen[GEBOUW].grote), 7)
        pyxel.text(2, 102, '                                                                ', 7)
        pyxel.text(2, 112, '                                                                ', 7)
        pyxel.text(2, 122, '                                                                ', 7)
        pyxel.text(2, 132, '                                                                ', 7)
        pyxel.text(2, 142, '                                                                ', 7)
        pyxel.text(2, 152, '                                                                ', 7)
        pyxel.text(2, 162, '                                                                ', 7)
        pyxel.text(2, 172, '                                                                ', 7)
        pyxel.text(2, 182, '                                                                ', 7)
        pyxel.text(2, 192, '                                                                ', 7)
        pyxel.text(2, 202, '                                                                ', 7)
        pyxel.text(2, 212, '                                                                ', 7)
        pyxel.text(2, 172, '                                                                ', 7)
        pyxel.text(2, 182, '                                                                ', 7)
        pyxel.text(2, 192, '                                                                ', 7)
        pyxel.text(2, 202, '                                                                ', 7)
        pyxel.text(2, 212, '                                                                ', 7)
        pyxel.rect(0, 18, game.breedte, 1, 7)
        pyxel.blt( 78, 32, 2, 64, 16, 8, 8, pyxel.COLOR_BLACK)
        pyxel.blt( 94, 32, 2, 72, 16, 8, 8, pyxel.COLOR_BLACK)
        pyxel.blt(178, 32, 2, 64, 16, 8, 8, pyxel.COLOR_BLACK)
        pyxel.blt(194, 32, 2, 72, 16, 8, 8, pyxel.COLOR_BLACK)

        pyxel.blt( 78, 42, 2, 64, 16, 8, 8, pyxel.COLOR_BLACK)
        pyxel.blt( 94, 42, 2, 72, 16, 8, 8, pyxel.COLOR_BLACK)
        pyxel.blt(178, 42, 2, 64, 16, 8, 8, pyxel.COLOR_BLACK)
        pyxel.blt(194, 42, 2, 72, 16, 8, 8, pyxel.COLOR_BLACK)

        pyxel.blt( 78, 52, 2, 64, 16, 8, 8, pyxel.COLOR_BLACK)
        pyxel.blt( 94, 52, 2, 72, 16, 8, 8, pyxel.COLOR_BLACK)
        pyxel.blt(178, 52, 2, 64, 16, 8, 8, pyxel.COLOR_BLACK)
        pyxel.blt(194, 52, 2, 72, 16, 8, 8, pyxel.COLOR_BLACK)

        pyxel.blt( 78, 62, 2, 64, 16, 8, 8, pyxel.COLOR_BLACK)
        pyxel.blt( 94, 62, 2, 72, 16, 8, 8, pyxel.COLOR_BLACK)
        pyxel.blt(178, 62, 2, 64, 16, 8, 8, pyxel.COLOR_BLACK)
        pyxel.blt(194, 62, 2, 72, 16, 8, 8, pyxel.COLOR_BLACK)

        pyxel.blt( 78, 72, 2, 64, 16, 8, 8, pyxel.COLOR_BLACK)
        pyxel.blt( 94, 72, 2, 72, 16, 8, 8, pyxel.COLOR_BLACK)
        pyxel.blt(178, 72, 2, 64, 16, 8, 8, pyxel.COLOR_BLACK)
        pyxel.blt(194, 72, 2, 72, 16, 8, 8, pyxel.COLOR_BLACK)

        pyxel.blt( 78, 82, 2, 64, 16, 8, 8, pyxel.COLOR_BLACK)
        pyxel.blt( 94, 82, 2, 72, 16, 8, 8, pyxel.COLOR_BLACK)
        pyxel.blt(178, 82, 2, 64, 16, 8, 8, pyxel.COLOR_BLACK)
        pyxel.blt(194, 82, 2, 72, 16, 8, 8, pyxel.COLOR_BLACK)

        pyxel.blt( 78, 92, 2, 64, 16, 8, 8, pyxel.COLOR_BLACK)
        pyxel.blt( 94, 92, 2, 72, 16, 8, 8, pyxel.COLOR_BLACK)
        pyxel.blt(178, 92, 2, 64, 16, 8, 8, pyxel.COLOR_BLACK)
        pyxel.blt(194, 92, 2, 72, 16, 8, 8, pyxel.COLOR_BLACK)
    else:
        menupagina = menu[game.menu_pagina]
        for index, line in enumerate(menupagina):
            pyxel.text(2, 12 + index * 10, line[0], 7)

    # if game.menu_pagina == DOEL:
    #     pyxel.text(2,  12, '                                                                ', 7)
    #     pyxel.text(2,  22, ' 2: doel                                                        ', 7)
    #     pyxel.text(2,  32, ' 3: begin                                                       ', 7)
    #     pyxel.text(2,  42, ' 4: verloop en einde                                            ', 7)
    #     pyxel.text(2,  52, ' 5: terrein                                                     ', 7)
    #     pyxel.text(2,  62, ' 6: eenheden                                                    ', 7)
    #     pyxel.text(2,  72, ' 7: boten                                                       ', 7)
    #     pyxel.text(2,  82, ' 8: aanvallen                                                   ', 7)
    #     pyxel.text(2,  92, ' 9: munitie                                                     ', 7)
    #     pyxel.text(2, 102, '10: uithouding en bewegen                                       ', 7)
    #     pyxel.text(2, 112, '11: zicht: eenheden                                             ', 7)
    #     pyxel.text(2, 122, '12: zicht: terrein                                              ', 7)
    #     pyxel.text(2, 132, '13: knoppen                                                     ', 7)
    #     pyxel.text(2, 142, '14: terreininstellingen                                         ', 7)
    #     pyxel.text(2, 152, '                                                                ', 7)
    #     pyxel.text(2, 162, '                                                                ', 7)
    #     pyxel.text(2, 172, '                                                                ', 7)
    #     pyxel.text(2, 182, '                                                                ', 7)
    #     pyxel.text(2, 192, '                                                                ', 7)
    #     pyxel.text(2, 202, '                                                                ', 7)
    #     pyxel.text(2, 212, '                                                                ', 7)
    # if game.menu_pagina == DOEL:
    #     pyxel.text(2,  12, 'Doel                                                            ', 7)
    #     pyxel.text(2,  22, 'Het doel van het spel is om het leger van de vijand te verslaan ', 7)
    #     pyxel.text(2,  32, 'Dit doe je door eenheden te plaatsen                            ', 7)
    #     pyxel.text(2,  42, 'en je tegenstander aan te vallen                                ', 7)
    #     pyxel.rect(0, 18, game.breedte, 1, 7)
    # if game.menu_pagina == BEGIN:
    #     pyxel.text(2,  12, 'Begin                                                           ', 7)
    #     pyxel.text(2,  22, '  - Je hebt vanaf de start een terrein                          ', 7)
    #     pyxel.text(2,  32, '       Wil je een ander random terrein? Druk op                 ', 7), pyxel.text(190, 32, '(R)', 10)
    #     pyxel.text(2,  42, '  - Je kiest een budget.                                        ', 7)
    #     pyxel.text(2,  52, '      Dit zie je naast de letter p in de rechterbovenhoek       ', 7),
    #     pyxel.text(2,  62, '  - Je hebt de keuze tussen meer   of minder   punten           ', 7), pyxel.text(130, 62, '(S)', 10), pyxel.text(178, 62, '(q)', 10)
    #     pyxel.text(2,  72, '      Het budget heb je nodig om eenheden te plaatsen           ', 7)
    #     pyxel.text(2,  82, '  - Je kiest een kleur voor je eenheden                         ', 7), pyxel.text(158, 82, '(c)', 10)
    #     pyxel.text(2,  92, 'Het aanpassen van punten,kleur,... doe je niet in het menu zelf ', 7)
    #     pyxel.text(2, 102, 'Je plaatst je eenheden (linkermuisknop)                         ', 7)
    #     pyxel.text(2, 112, 'hiervoor betaal je 1 punt per nivo                              ', 7)
    #     pyxel.text(2, 122, 'Je eenheden verwijderen is via de rechtermuisknop               ', 7)
    #     pyxel.text(2, 132, 'LET OP:                                                         ', 7)
    #     pyxel.text(2, 142, 'je mag alleen een eenheid zetten als                            ', 7)
    #     pyxel.text(2, 152, 'het vakje bij je muis geen kruis is                             ', 7)
    #     pyxel.text(2, 162, 'Op welk nivo je jezelf bevindt (1-4)                            ', 7)
    #     pyxel.text(2, 172, 'zie je aan de linkerkant van de eenheid                         ', 7)
    #     pyxel.text(2, 182, 'PAS OP Je moet een generaal bij je eenheden hebben(zie eenheden)', 7)
    #     pyxel.text(2, 192, 'Je kan van elk type/nivo, een beperkt aantal eenheden plaatsen  ', 7)
    #     pyxel.text(2, 202, 'Als beide spelers hun eenheden hebben geplaatst                 ', 7)
    #     pyxel.text(2, 212, 'druk je op   om te beginnen                                     ', 7), pyxel.text(42, 212, '(P)', 10)
    #     pyxel.rect(0, 18, game.breedte, 1, 7)
    # if game.menu_pagina == VERLOOP_EN_EINDE:
    #     pyxel.text(2,  12, 'Verloop                                                         ', 7)
    #     pyxel.text(2,  22, 'Wanneer je aan de beurt bent kan je eenheden selecteren en      ', 7)
    #     pyxel.text(2,  32, 'verplaatsen of aanvallen, dit staat uitgelegd onder aanvallen   ', 7)
    #     pyxel.text(2,  42, 'Om de informatie over je terrein te bekijken druk je op (i)     ', 7) ,pyxel.text(226, 42, '(i)', 6)
    #     pyxel.text(2,  52, 'Als je een beurt wil overslaan met de geselecteerde eenheid     ', 7)
    #     pyxel.text(2,  62, 'druk je op de  spatiebalk                                       ', 7), pyxel.text(62, 62, 'spatiebalk', 6)
    #     pyxel.text(2,  72, 'Via  Tab  ga je naar de volgende eenheid die binnen diezelfde   ', 7), pyxel.text(22, 72, 'Tab', 6)
    #     pyxel.text(2,  82, 'beurt nog niets gedaan heeft                                    ', 7)
    #     pyxel.text(2,  92, 'Via enter begin of eindig je je beurt                           ', 7)
    #     pyxel.text(2, 102, 'Je plaatst je eenheden (linkermuisknop)                         ', 7), pyxel.text(94, 102, '(linkermuisknop)', 6)
    #     pyxel.text(2, 112, 'Selecteren en verplaatsen, doe je via de linkermuisknop         ', 7), pyxel.text(166, 112, 'linkermuisknop', 6)
    #     pyxel.text(2, 122, 'Aanvallen doe je via de rechtermuisknop.                        ', 7), pyxel.text(98, 122, 'rechtermuisknop', 6)
    #     pyxel.text(2, 132, 'Via de middelste muisknop kan je bouwen(acties van de ingenieur)', 7), pyxel.text(30, 132, 'middelste muisknop', 6)
    #     pyxel.text(2, 142, 'Deze staan verder uitgelegd bij de eenheden                     ', 7)
    #     pyxel.text(2, 152, '                                                                ', 7)
    #     pyxel.text(2, 162, '                                                                ', 7)
    #     pyxel.text(2, 172, 'Einde                                                           ', 7)
    #     pyxel.text(2, 182, 'Als alle eenheden van een kleur verslagen zijn                  ', 7)
    #     pyxel.text(2, 192, 'is het spel gedaan                                              ', 7)
    #     pyxel.text(2, 202, '                                                                ', 7)
    #     pyxel.text(2, 212, '                                                                ', 7)
    #     pyxel.text(2, 172, '                                                                ', 7)
    #     pyxel.text(2, 182, '                                                                ', 7)
    #     pyxel.text(2, 192, '                                                                ', 7)
    #     pyxel.text(2, 202, '                                                                ', 7)
    #     pyxel.text(2, 212, '                                                                ', 7)
    #     pyxel.rect(0, 18, game.breedte, 1, 7)
    #     pyxel.rect(0, 178, game.breedte, 1, 7)
    # if game.menu_pagina == TERREIN:
    #     pyxel.text(2,  12, 'Terrein                                                         ', 7)
    #     pyxel.text(2,  22, 'Er zijn 7 soorten terrein,                                      ', 7)
    #     pyxel.text(2,  32, 'deze zijn te zien aan de verschillende kleuren                  ', 7)
    #     pyxel.text(2,  42, '1: Gras: standaard, er verandert niets                          ',11)
    #     pyxel.text(2,  52, '2: Bos: 2 vakjes minder bereik zichtbaarheid gaat omhoog met 3  ', 3)
    #     pyxel.text(2,  62, '   hierdoor kan je moeilijker gezien worden                     ', 3)
    #     pyxel.text(2,  72, '3: Water: Je kan minder goed verdedigen (-20)                   ', 6)
    #     pyxel.text(2,  82, '4: Berg: je kan beter verdedigen + 5,                           ',13)
    #     pyxel.text(2,  92, '   je bereik gaat omhoog (+ 2 vakjes),                          ',13)
    #     pyxel.text(2, 102, '   je zicht wordt beter waardoor je verder kan zien (+4)        ',13)
    #     pyxel.text(2, 112, '   je zichtbaarheid daalt -2, je word makkelijker gezien        ',13)
    #     pyxel.text(2, 122, '5: Weg: Je kan verder lopen                                     ',15)
    #     pyxel.text(2, 132, '6: Brug: Je kan verder lopen                                    ', 4)
    #     pyxel.text(2, 142, '7: Gebouw: je kan je beter verdedigen (+5)                      ',14)
    #     pyxel.text(2, 152, '   je zichtbaarheid gaat omhoog +2, je word moeilijker gezien   ',14)
    #     pyxel.text(2, 162, '   maar je zicht daalt waardoor je minder ver kan zien (-1)     ',14)
    #     pyxel.text(2, 172, '                                                                ', 7)
    #     pyxel.text(2, 182, '                                                                ', 7)
    #     pyxel.text(2, 192, '                                                                ', 7)
    #     pyxel.text(2, 202, '                                                                ', 7)
    #     pyxel.text(2, 212, '                                                                ', 7)
    #     pyxel.text(2, 172, '                                                                ', 7)
    #     pyxel.text(2, 182, '                                                                ', 7)
    #     pyxel.text(2, 192, '                                                                ', 7)
    #     pyxel.text(2, 202, '                                                                ', 7)
    #     pyxel.text(2, 212, '                                                                ', 7)
    #     pyxel.rect(0, 18, game.breedte, 1, 7)
    # if game.menu_pagina == EENHEDEN:
    #     pyxel.text(2,  12, 'Eenheden                                                        ', 7)
    #     pyxel.text(2,  22, 'Nivo I = Soldaat                                                ', 7)
    #     pyxel.text(2,  32, 'Nivo II = Sergeant                                              ', 7)
    #     pyxel.text(2,  42, 'Nivo III = Kapitein                                             ', 7)
    #     pyxel.text(2,  52, 'Nivo IV = Generaal                                              ', 7)
    #     pyxel.text(2,  62, 'Hieronder vind je de eigenschappen van de verschillende eenheden', 7)
    #     pyxel.text(2,  72, '   Deze kwaliteiten zijn niet afhankelijk van de kleur          ', 7)
    #     pyxel.text(2,  82, '            Zwaard| Speer| Paard| Kanon| Boogschutter| Ingenieur', 7)
    #     pyxel.text(2,  92, 'Aanvallen  |+     |-     |+     |+     |             |-         ', 7)
    #     pyxel.text(2, 102, 'Verdedigen |+     |++    |      |-     |-            |-         ', 7)
    #     pyxel.text(2, 112, 'Bewegen    |      |      |++    |-     |nivoI+       |          ', 7)
    #     pyxel.text(2, 122, 'Bereik     |      |      |      |++    |             |          ', 7)
    #     pyxel.text(2, 132, 'Zicht      |      |      |nivoI+|      |             |          ', 7)
    #     pyxel.text(2, 142, 'Extra      |      |      |      |      |             |bouwen    ', 7)
    #     pyxel.text(2, 152, 'De waarde van je eenheden zie je rechts onderaan in dit kader   ', 7)
    #     pyxel.text(2, 162, 'Let op: per kleur kan dit verschillen                           ', 7)
    #     pyxel.text(2, 172, 'Ook kan je de sterkte herkennen aan de sterren rechts bovenaan  ', 7)
    #     pyxel.text(2, 182, 'Extra                                                           ', 7)
    #     pyxel.text(2, 192, 'Enkel de ingenieur kan ‘bouwen’                                 ', 7)
    #     pyxel.text(2, 202, '   Dit betekent dat hij volgende veranderingen kan doen:        ', 7)
    #     pyxel.text(2, 212, 'Bos --> gras                                                    ', 7)
    #     pyxel.text(2, 222, 'Gras --> weg                                                    ', 7)
    #     pyxel.text(2, 232, 'Water --> brug                                                  ', 7)
    #     pyxel.rect(0, 18, game.breedte, 1, 7)
    # if game.menu_pagina == BOOTEN:
    #     pyxel.text(2,  12, 'Boten                                                           ', 7)
    #     pyxel.text(2,  22, 'druk op   om boten te kunnen plaatsen                           ', 7) ,pyxel.text(30, 22, '(b)', 10)
    #     pyxel.text(2,  32, 'boten kunnen alleen op water bewegen                            ', 7)
    #     pyxel.text(2,  42, 'bij transportboten is het net als of er een weg onder is        ', 7)
    #     pyxel.text(2,  52, 'hierdoor kunnen eenheden gemakelijker een rivier over           ', 7)
    #     pyxel.text(2,  62, 'LET OP                                                          ', 7)
    #     pyxel.text(2,  72, 'je kunt de eenheden niet op de boot zeten                       ', 7)
    #     pyxel.text(2,  82, '                                                                ', 7)
    #     pyxel.text(2,  92, '                                                                ', 7)
    #     pyxel.text(2, 102, '                                                                ', 7)
    #     pyxel.text(2, 112, '                                                                ', 7)
    #     pyxel.text(2, 122, '                                                                ', 7)
    #     pyxel.text(2, 132, '                                                                ', 7)
    #     pyxel.text(2, 142, '                                                                ', 7)
    #     pyxel.text(2, 152, '                                                                ', 7)
    #     pyxel.text(2, 162, '                                                                ', 7)
    #     pyxel.text(2, 172, '                                                                ', 7)
    #     pyxel.text(2, 182, '                                                                ', 7)
    #     pyxel.text(2, 192, '                                                                ', 7)
    #     pyxel.text(2, 202, '                                                                ', 7)
    #     pyxel.text(2, 212, '                                                                ', 7)
    #     pyxel.text(2, 222, '                                                                ', 7)
    #     pyxel.text(2, 232, '                                                                ', 7)
    #     pyxel.rect(0, 18, game.breedte, 1, 7)
    # if game.menu_pagina == AANVALLEN:
    #     pyxel.text(2,  12, 'Aanvallen                                                       ', 7)
    #     pyxel.text(2,  22, 'Je valt een vijand aan door op je rechtermuisknop te klikken    ', 7)
    #     pyxel.text(2,  32, 'Je klikt hiervoor op de eenheid van de andere kleur             ', 7)
    #     pyxel.text(2,  42, '1: algemene aanval                                              ', 7)
    #     pyxel.text(2,  52, 'Om een vijand aan te vallen moet hij binnen je bereik zijn      ', 7)
    #     pyxel.text(2,  62, 'Dit wil zeggen dat je naast je vijand moet staan                ', 7)
    #     pyxel.text(2,  72, 'of in een rechte lijn naar je vijand moet kunnen bewegen        ', 7)
    #     pyxel.text(2,  82, 'Een aanval op je vijand zorgt ervoor                            ', 7)
    #     pyxel.text(2,  92, 'dat hij moraal en gezondheid verliest                           ', 7)
    #     pyxel.text(2, 102, 'Tip: Een aanval met een aanloop bezorgt je vijand meer schade   ', 7)
    #     pyxel.text(2, 112, 'Hoe groter de aanloop, hoe meer schade                          ', 7)
    #     pyxel.text(2, 122, 'Wanneer je aanvalt is er de mogelijkheid                        ', 7)
    #     pyxel.text(2, 132, 'dat de eenheid van je vijand verplaatst naar achteren           ', 7)
    #     pyxel.text(2, 142, '                                                                ', 7)
    #     pyxel.text(2, 152, '2 Schieten                                                      ', 7)
    #     pyxel.text(2, 162, 'Om een vijand aan te vallen moet hij binnen je bereik zijn      ', 7)
    #     pyxel.text(2, 172, 'Je kan op de vijand schieten wanneer er een doelwit op staat    ', 7)
    #     pyxel.text(2, 182, '                                                                ', 7)
    #     pyxel.text(2, 192, '                                                                ', 7)
    #     pyxel.text(2, 202, '                                                                ', 7)
    #     pyxel.text(2, 212, '                                                                ', 7)
    #     pyxel.rect(0, 18, game.breedte, 1, 7)
    # if game.menu_pagina == MUNITIE:
    #     pyxel.text(2,  12, 'munitie                                                         ', 7)
    #     pyxel.text(2,  22, 'de munitie van een eenheid is                                   ', 7)
    #     pyxel.text(2,  32, 'het aantal keren dat het kan schieten                           ', 7)
    #     pyxel.text(2,  42, 'als dit bij een boogschuter of kanon op 0 graakt                ', 7)
    #     pyxel.text(2,  52, 'veranderd deze eenheid in een zwaardvechter van dat nivo        ', 7)
    #     pyxel.text(2,  62, '                                                                ', 7)
    #     pyxel.text(2,  72, '                                                                ', 7)
    #     pyxel.text(2,  82, '                                                                ', 7)
    #     pyxel.text(2,  92, '                                                                ', 7)
    #     pyxel.text(2, 102, '                                                                ', 7)
    #     pyxel.text(2, 112, '                                                                ', 7)
    #     pyxel.text(2, 122, '                                                                ', 7)
    #     pyxel.text(2, 132, '                                                                ', 7)
    #     pyxel.text(2, 142, '                                                                ', 7)
    #     pyxel.text(2, 152, '                                                                ', 7)
    #     pyxel.text(2, 162, '                                                                ', 7)
    #     pyxel.text(2, 172, '                                                                ', 7)
    #     pyxel.text(2, 182, '                                                                ', 7)
    #     pyxel.text(2, 192, '                                                                ', 7)
    #     pyxel.text(2, 202, '                                                                ', 7)
    #     pyxel.text(2, 212, '                                                                ', 7)
    #     pyxel.rect(0, 18, game.breedte, 1, 7)
    # if game.menu_pagina == UITHOUDING_EN_BEWEGEN:
    #     pyxel.text(2,  12, 'Uithouding                                                      ', 7)
    #     pyxel.text(2,  22, 'Verliezen                                                       ', 7)
    #     pyxel.text(2,  32, 'Je verliest uithouding bij bewegingen                           ', 7)
    #     pyxel.text(2,  42, 'De hoeveelheid hangt af van de ondergrond waarover je beweegt   ', 7)
    #     pyxel.text(2,  52, '(Staat aangegeven bij de terreininformatie)                     ', 7)
    #     pyxel.text(2,  62, '                                                                ', 7)
    #     pyxel.text(2,  72, 'Bijkrijgen                                                      ', 7)
    #     pyxel.text(2,  82, 'Je uithouding gaat terug omhoog na iedere beurt,                ', 7)
    #     pyxel.text(2,  92, 'de hoeveelheid uithouding is afhankelijk van je type en nivo    ', 7)
    #     pyxel.text(2, 102, '                                                                ', 7)
    #     pyxel.text(2, 112, '                                                                ', 7)
    #     pyxel.text(2, 122, 'Bewegen                                                         ', 7)
    #     pyxel.text(2, 132, 'Als je een eenheid hebt geselecteerd die je wil verplaatsen,    ', 7)
    #     pyxel.text(2, 142, 'kan je met je muis naar een vakje bewegen waar je naartoe wil   ', 7)
    #     pyxel.text(2, 152, 'Wanneer dit oplicht kan je je naar dat vakje verplaatsen        ', 7)
    #     pyxel.text(2, 162, '                                                                ', 7)
    #     pyxel.text(2, 172, '                                                                ', 7)
    #     pyxel.text(2, 182, '                                                                ', 7)
    #     pyxel.text(2, 192, '                                                                ', 7)
    #     pyxel.text(2, 202, '                                                                ', 7)
    #     pyxel.text(2, 212, '                                                                ', 7)
    #     pyxel.rect(0, 18, game.breedte, 1, 7)
    #     pyxel.rect(0, 128, game.breedte, 1, 7)
    # if game.menu_pagina == ZICHT_EENHEDEN:
    #     pyxel.text(2,  12, 'Zicht                                                           ', 7)
    #     pyxel.text(2,  22, 'Eenheden                                                        ', 7)
    #     pyxel.text(2,  32, 'Je kan zien wanneer je het zicht van je eenheid                 ', 7)
    #     pyxel.text(2,  42, 'min de zichtbaarheid van je vijand                              ', 7)
    #     pyxel.text(2,  52, 'min het aantal vakjes verschil doet en dit groter is dan 0      ', 7)
    #     pyxel.text(2,  62, 'Bijvoorbeeld                                                    ', 7)
    #     pyxel.text(2,  72, 'Zicht eigen eenheid - zichtbaarheid vijand - vakjes verschil >0 ', 7)
    #     pyxel.text(2,  82, '8 - 4 - 1 = 3                                                   ', 7)
    #     pyxel.text(2,  92, 'Zicht eigen eenheid                                             ', 7)
    #     pyxel.text(2, 102, 'Je zicht is standaard 8 maar kan veranderen met terrein         ', 7)
    #     pyxel.text(2, 112, 'Het zicht is ook afhankelijk van welke eenheid je gebruikt      ', 7)
    #     pyxel.text(2, 122, 'Zichtbaarheid vijand                                            ', 7)
    #     pyxel.text(2, 132, 'De zichtbaarheid van je vijand is standaard 4                   ', 7)
    #     pyxel.text(2, 142, 'maar kan veranderen met terrein (bos, berg, …)                  ', 7)
    #     pyxel.text(2, 152, 'Aantal vakjes verschil                                          ', 7)
    #     pyxel.text(2, 162, 'Het aantal vakjes dat aanwezig is tussen                        ', 7)
    #     pyxel.text(2, 172, 'jouw eenheid en die van de vijand                               ', 7)
    #     pyxel.text(2, 182, 'Het vakje waarop je tegenstander staat telt ook mee als 1       ', 7)
    #     pyxel.text(2, 192, 'DUS 2 vakjes tussen jou en je vijand wordt geteld als 3 vakjes  ', 7)
    #     pyxel.text(2, 202, '                                                                ', 7)
    #     pyxel.text(2, 212, '                                                                ', 7)
    #     pyxel.rect(0,  18, game.breedte, 1, 7)
    #     pyxel.rect(0,  28, game.breedte / 1.35, 1, 7)
    #     pyxel.rect(0,  98, game.breedte / 2.8, 1, 7)
    #     pyxel.rect(0, 128, game.breedte / 2.8, 1, 7)
    #     pyxel.rect(0, 158, game.breedte / 2.8, 1, 7)
    # if game.menu_pagina == ZICHT_TERREIN:
    #     pyxel.text(2,  12, 'Zicht                                                           ', 7)
    #     pyxel.text(2,  22, 'Terrein                                                         ', 7)
    #     pyxel.text(2,  32, 'Je kan zien wanneer je het zicht van je eenheid                 ', 7)
    #     pyxel.text(2,  42, 'min de zichtbaarheid van het terrein                            ', 7)
    #     pyxel.text(2,  52, 'min het aantal vakjes verschil doet en dit groter is dan 0      ', 7)
    #     pyxel.text(2,  62, 'Bijvoorbeeld                                                    ', 7)
    #     pyxel.text(2,  72, 'Zicht eigen eenheid - zichtbaarheid terrein - vakjes verschil >0', 7)
    #     pyxel.text(2,  82, '8 - 4 - 1 = 3                                                   ', 7)
    #     pyxel.text(2,  92, 'Zicht eigen eenheid                                             ', 7)
    #     pyxel.text(2, 102, 'Je zicht is standaard 8 maar kan veranderen met terrein         ', 7)
    #     pyxel.text(2, 112, 'Het zicht is ook afhankelijk van welke eenheid je gebruikt      ', 7)
    #     pyxel.text(2, 122, 'Zichtbaarheid terrein                                           ', 7)
    #     pyxel.text(2, 132, 'De zichtbaarheid is terug te vinden bij de terrein info         ', 7)
    #     pyxel.text(2, 142, 'Een berg kan je van verder zien                                 ', 7)
    #     pyxel.text(2, 152, 'Aantal vakjes verschil                                          ', 7)
    #     pyxel.text(2, 162, 'Het aantal vakjes dat aanwezig is tussen                        ', 7)
    #     pyxel.text(2, 172, 'jouw eenheid en het terrein                                     ', 7)
    #     pyxel.text(2, 182, '                                                                ', 7)
    #     pyxel.text(2, 192, '                                                                ', 7)
    #     pyxel.text(2, 202, '                                                                ', 7)
    #     pyxel.text(2, 212, '                                                                ', 7)
    #     pyxel.rect(0,  18, game.breedte, 1, 7)
    #     pyxel.rect(0,  28, game.breedte / 1.35, 1, 7)
    #     pyxel.rect(0,  98, game.breedte / 2.8, 1, 7)
    #     pyxel.rect(0, 128, game.breedte / 2.8, 1, 7)
    #     pyxel.rect(0, 158, game.breedte / 2.8, 1, 7)
    # if game.menu_pagina == KNOPPEN:
    #     begin_y = 180
    #     if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
    #         pyxel.rect(65, 65, 60, 79, 9)
    #     if pyxel.btn(pyxel.MOUSE_BUTTON_MIDDLE):
    #         pyxel.rect(125, 81, 6, 54, 9)
    #     if pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT):
    #         pyxel.rect(131, 65, 60, 79, 9)
    #     if pyxel.btn(pyxel.KEY_TAB):
    #         pyxel.rect(51, begin_y, 14, 7, 9)
    #         pyxel.text(86, begin_y - 30, 'volgende eenheid', 7)
    #     # if pyxel.btn(pyxel.KEY_A):
    #     #     pyxel.rect(66, 196, 7, 7, 9)
    #     #     pyxel.text(86, 166, 'kleiner terrein', 7)
    #     # if pyxel.btn(pyxel.KEY_Z):
    #     #     pyxel.rect(74, 196, 7, 7, 9)
    #     #     pyxel.text(86, 166, 'groter terrein', 7)
    #     if pyxel.btn(pyxel.KEY_Q):
    #         pyxel.rect(69, begin_y + 8, 7, 7, 9)
    #         pyxel.text(86, begin_y - 30, 'minder punten', 7)
    #     if pyxel.btn(pyxel.KEY_S):
    #         pyxel.rect(77, begin_y + 8, 7, 7, 9)
    #         pyxel.text(86, begin_y - 30, 'meer punten', 7)
    #     if pyxel.btn(pyxel.KEY_R):
    #         pyxel.rect(90, begin_y, 7, 7, 9)
    #         pyxel.text(86, begin_y - 30, 'random terrein', 7)
    #     if pyxel.btn(pyxel.KEY_C):
    #         pyxel.rect(88, begin_y + 16, 7, 7, 9)
    #         pyxel.text(86, begin_y - 30, 'volgende kleur', 7)
    #     if pyxel.btn(pyxel.KEY_B):
    #         pyxel.rect(104, begin_y + 16, 7, 7, 9)
    #         pyxel.text(86, begin_y - 30, 'veranderen tussen boten en eenheden', 7)
    #     if pyxel.btn(pyxel.KEY_I):
    #         pyxel.rect(122, begin_y, 7, 7, 9)
    #         pyxel.text(86, begin_y - 30, 'terrein info', 7)
    #     if pyxel.btn(pyxel.KEY_SPACE):
    #         pyxel.rect(88, begin_y + 24, 40, 7, 9)
    #         pyxel.text(86, begin_y - 30, 'geselecteerde eenheid beurt overslaan', 7)
    #     if pyxel.btn(pyxel.KEY_P):
    #         pyxel.rect(138, begin_y, 7, 7, 9)
    #         pyxel.text(86, begin_y - 30, 'begingen spelen', 7)
    #     if pyxel.btn(pyxel.KEY_M):
    #         pyxel.rect(141, begin_y + 8, 7, 7, 9)
    #         pyxel.text(86, begin_y - 30, 'menu', 7)
    #     if pyxel.btn(pyxel.KEY_LEFT):
    #         pyxel.rect(153, begin_y + 16, 7, 7, 9)
    #         pyxel.text(86, begin_y - 30, 'vorig type', 7)
    #     if pyxel.btn(pyxel.KEY_UP):
    #         pyxel.rect(161, begin_y + 8, 7, 7, 9)
    #         pyxel.text(86, begin_y - 30, 'hoger nivo', 7)
    #     if pyxel.btn(pyxel.KEY_DOWN):
    #         pyxel.rect(161, begin_y + 16, 7, 7, 9)
    #         pyxel.text(86, begin_y - 30, 'lager nivo', 7)
    #     if pyxel.btn(pyxel.KEY_RIGHT):
    #         pyxel.rect(169, begin_y + 16, 7, 7, 9)
    #         pyxel.text(86, begin_y - 30, 'volgend type', 7)
    #     if pyxel.btn(pyxel.KEY_KP_ENTER):
    #         pyxel.rect(184, begin_y + 8, 7, 15, 9)
    #         pyxel.text(86, begin_y - 30, 'begin / einde beurt', 7)
    #     pyxel.blt(64, 64, 2, 0, 24, 128, 80, pyxel.COLOR_GRAY)
    #     pyxel.blt(48, begin_y - 2, 2, 0, 104, 144, 40, pyxel.COLOR_BLACK)
    # if game.menu_pagina == TERREININSTELLINGEN:
    #     pyxel.text(2,  12, 'terreininstellingen                                             ', 7)
    #     pyxel.text(2,  22, '                    kans                    grootte             ', 7)
    #     pyxel.text(2,  32, 'weg                                                             ', 7) ,pyxel.text(89, 33, str(game.weg_kans), 7) ,pyxel.text \
    #         (189, 33, str(game.weg_grote), 7)
    #     pyxel.text(2,  42, 'rivier                                                          ', 7) ,pyxel.text(89, 43, str(game.rivier_kans), 7) ,pyxel.text \
    #         (189, 43, str(game.rivier_grote), 7)
    #     pyxel.text(2,  52, 'bos                                                             ', 7) ,pyxel.text(89, 53, str(game.bos_kans), 7) ,pyxel.text \
    #         (189, 53, str(game.bos_grote), 7)
    #     pyxel.text(2,  62, 'berg                                                            ', 7) ,pyxel.text(89, 63, str(game.berg_kans), 7) ,pyxel.text \
    #         (189, 63, str(game.berg_grote), 7)
    #     pyxel.text(2,  72, 'meer                                                            ', 7) ,pyxel.text(89, 73, str(game.meer_kans), 7) ,pyxel.text \
    #         (189, 73, str(game.meer_grote), 7)
    #     pyxel.text(2,  82, 'zee                                                             ', 7) ,pyxel.text(89, 83, str(game.zee_kans), 7) ,pyxel.text \
    #         (189, 83, str(game.zee_grote), 7)
    #     pyxel.text(2,  92, 'gebouw                                                          ', 7) ,pyxel.text(89, 93, str(game.gebouw_aantal), 7) ,pyxel.text \
    #         (189, 93, str(game.gebouw_grote), 7)
    #     pyxel.text(2, 102, '                                                                ', 7)
    #     pyxel.text(2, 112, '                                                                ', 7)
    #     pyxel.text(2, 122, '                                                                ', 7)
    #     pyxel.text(2, 132, '                                                                ', 7)
    #     pyxel.text(2, 142, '                                                                ', 7)
    #     pyxel.text(2, 152, '                                                                ', 7)
    #     pyxel.text(2, 162, '                                                                ', 7)
    #     pyxel.text(2, 172, '                                                                ', 7)
    #     pyxel.text(2, 182, '                                                                ', 7)
    #     pyxel.text(2, 192, '                                                                ', 7)
    #     pyxel.text(2, 202, '                                                                ', 7)
    #     pyxel.text(2, 212, '                                                                ', 7)
    #     pyxel.text(2, 172, '                                                                ', 7)
    #     pyxel.text(2, 182, '                                                                ', 7)
    #     pyxel.text(2, 192, '                                                                ', 7)
    #     pyxel.text(2, 202, '                                                                ', 7)
    #     pyxel.text(2, 212, '                                                                ', 7)
    #     pyxel.rect(0, 18, game.breedte, 1, 7)
    #     pyxel.blt( 78, 32, 2, 64, 16, 8, 8, pyxel.COLOR_BLACK)
    #     pyxel.blt( 94, 32, 2, 72, 16, 8, 8, pyxel.COLOR_BLACK)
    #     pyxel.blt(178, 32, 2, 64, 16, 8, 8, pyxel.COLOR_BLACK)
    #     pyxel.blt(194, 32, 2, 72, 16, 8, 8, pyxel.COLOR_BLACK)
    #
    #     pyxel.blt( 78, 42, 2, 64, 16, 8, 8, pyxel.COLOR_BLACK)
    #     pyxel.blt( 94, 42, 2, 72, 16, 8, 8, pyxel.COLOR_BLACK)
    #     pyxel.blt(178, 42, 2, 64, 16, 8, 8, pyxel.COLOR_BLACK)
    #     pyxel.blt(194, 42, 2, 72, 16, 8, 8, pyxel.COLOR_BLACK)
    #
    #     pyxel.blt( 78, 52, 2, 64, 16, 8, 8, pyxel.COLOR_BLACK)
    #     pyxel.blt( 94, 52, 2, 72, 16, 8, 8, pyxel.COLOR_BLACK)
    #     pyxel.blt(178, 52, 2, 64, 16, 8, 8, pyxel.COLOR_BLACK)
    #     pyxel.blt(194, 52, 2, 72, 16, 8, 8, pyxel.COLOR_BLACK)
    #
    #     pyxel.blt( 78, 62, 2, 64, 16, 8, 8, pyxel.COLOR_BLACK)
    #     pyxel.blt( 94, 62, 2, 72, 16, 8, 8, pyxel.COLOR_BLACK)
    #     pyxel.blt(178, 62, 2, 64, 16, 8, 8, pyxel.COLOR_BLACK)
    #     pyxel.blt(194, 62, 2, 72, 16, 8, 8, pyxel.COLOR_BLACK)
    #
    #     pyxel.blt( 78, 72, 2, 64, 16, 8, 8, pyxel.COLOR_BLACK)
    #     pyxel.blt( 94, 72, 2, 72, 16, 8, 8, pyxel.COLOR_BLACK)
    #     pyxel.blt(178, 72, 2, 64, 16, 8, 8, pyxel.COLOR_BLACK)
    #     pyxel.blt(194, 72, 2, 72, 16, 8, 8, pyxel.COLOR_BLACK)
    #
    #     pyxel.blt( 78, 82, 2, 64, 16, 8, 8, pyxel.COLOR_BLACK)
    #     pyxel.blt( 94, 82, 2, 72, 16, 8, 8, pyxel.COLOR_BLACK)
    #     pyxel.blt(178, 82, 2, 64, 16, 8, 8, pyxel.COLOR_BLACK)
    #     pyxel.blt(194, 82, 2, 72, 16, 8, 8, pyxel.COLOR_BLACK)
    #
    #     pyxel.blt( 78, 92, 2, 64, 16, 8, 8, pyxel.COLOR_BLACK)
    #     pyxel.blt( 94, 92, 2, 72, 16, 8, 8, pyxel.COLOR_BLACK)
    #     pyxel.blt(178, 92, 2, 64, 16, 8, 8, pyxel.COLOR_BLACK)
    #     pyxel.blt(194, 92, 2, 72, 16, 8, 8, pyxel.COLOR_BLACK)

