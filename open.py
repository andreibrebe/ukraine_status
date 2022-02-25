from time import strftime,localtime
import webbrowser
from playsound import playsound

playsound('startup.mp3')

pages = {
    1: 'https://www.twitch.tv/nemicotv',                    # Ukraine multi-camera stream, occasional commentary
    2: 'https://liveuamap.com/',                            # Live map with news
    3: 'https://boards.4chan.org/pol/',                     # The only proper place for political commentary
    4: 'https://globe.adsbexchange.com/',                   # Air traffic map
    5: 'https://www.marinetraffic.com/',                    # Marine traffic map
    6: 'https://uvb-76.net/',                               # UVB-76, "The Buzzer" (coded cyka military radio)
    7: 'https://www.saveecobot.com/en/radiation-maps',      # Gamma radiation map around Ukraine
    8: 'https://www.youtube.com/watch?v=ENyxseq59YQ'        # Theme song
        }    

def mainmenu():
    menu_ls = ['\nGood day, commander!\nIt is currently',
        strftime("%T on %A, %d %b %Y", localtime()),
        '\n0 - Main setup (stream, warmap, /pol/)',
        '1 - Multi-camera stream with occasional news and commentary',
        '2 - Live warmap with news',
        '3 - /pol/',
        '4 - Air traffic map',
        '5 - Marine traffic map',
        '6 - UVP-76, \"The Buzzer\"',
        '7 - Ukraine radiation map',
        '8 - Theme song',
        'X - Exit'
        ]
    for n in menu_ls:
        print(n)

def setup():
    webbrowser.open(pages.get(1))
    webbrowser.open(pages.get(2))
    webbrowser.open(pages.get(3))


mainmenu()
while(True):
    selected = input("\nWhat shall we open, sir?\n")
    if (selected.lower() == 'x'):
        exit()
    else:
        try: 
            selected = int(selected)
            if (selected in range(0,len(pages))):
                if (selected == 0):
                    setup()
                else:
                    webbrowser.open(pages.get(selected))
            else:
                print("Invalid input, try again")
        except:
            print("Invalid input, try again")
