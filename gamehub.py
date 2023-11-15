from consolemenu import *
from consolemenu.format import *
from consolemenu.items import *

def ae():
    print("test")
test = ae()

menu = ConsoleMenu("Main Menu All-in-one Games By CS", '''
  _________  ___   __   __     _____  __  ____  _  ______
 / ___/ __/ / _ | / /  / /    /  _/ |/ / / __ \/ |/ / __/
/ /___\ \  / __ |/ /__/ /__  _/ //    / / /_/ /    / _/  
\___/___/ /_/ |_/____/____/ /___/_/|_/  \____/_/|_/___/''', formatter=MenuFormatBuilder())

# Create some items

worda = ConsoleMenu("Select Version", ''' _       __               __   ___       __                 __                
| |     / /___  _________/ /  /   | ____/ /   _____  ____  / /___  __________ 
| | /| / / __ \/ ___/ __  /  / /| |/ __  / | / / _ \/ __ \/ __/ / / / ___/ _ \
| |/ |/ / /_/ / /  / /_/ /  / ___ / /_/ /| |/ /  __/ / / / /_/ /_/ / /  /  __/
|__/|__/\____/_/   \__,_/  /_/  |_\__,_/ |___/\___/_/ /_/\__/\__,_/_/   \___/''', formatter=MenuFormatBuilder())
wordas = SubmenuItem("Word Adventure", worda, menu)
command_item1 = CommandItem("Word Adventure",  "main.py")
word_hard = CommandItem("Word Adventure (With Jumpscare + Sound)",  "main.py")
word_hard1 = FunctionItem("e", ae)
worda.append_item(word_hard)
worda.append_item(word_hard1)

# A SelectionMenu constructs a menu from a list of strings
selection_menu = ConsoleMenu("Select your game", '''    __         __ _          ____  __
   / /   ___  / /( )_____   / __ \/ /___ ___  __
  / /   / _ \/ __/// ___/  / /_/ / / __ `/ / / /
 / /___/  __/ /_  (__  )  / ____/ / /_/ / /_/ /
/_____/\___/\__/ /____/  /_/   /_/\__,_/\__, /
                                       /____/''', formatter=MenuFormatBuilder())

selection_menu.append_item(wordas)

# A SubmenuItem lets you add a menu (the selection_menu above, for example)
# as a submenu of another menu
submenu_item = SubmenuItem("Play", selection_menu, menu)
submenu_2 = ConsoleMenu("Third Submenu", "This Time with Double-Line Borders.",
                            prologue_text="This is my prologue. I am currently showing my top and bottom borders, but \
they are hidden by default. Also notice that my text is really long, so it extends beyond a single line, and should \
wrap properly within the menu borders. This is a useful place to put instructions to the user about how to use \
the menu.",
                            epilogue_text="This is my epilogue. My borders are currently hidden.",
                            formatter=MenuFormatBuilder()
                            .set_title_align('center')
                            .set_subtitle_align('center')
                            .set_border_style_type(MenuBorderStyleType.DOUBLE_LINE_BORDER)
                            .show_prologue_top_border(True)
                            .show_prologue_bottom_border(True))
main_credits = SubmenuItem("Credits", submenu=submenu_2)

# Once we're done creating them, we just add the items to the menu
menu.append_item(submenu_item)
menu.append_item(main_credits)
menu.show()