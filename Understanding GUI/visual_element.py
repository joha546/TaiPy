from taipy import Gui

text="Original version"

page = """
# Getting Started with Simple Taipy GUI
 ----------------
My Text <|{text}|>
<|{text}|input|> """

Gui(page).run()