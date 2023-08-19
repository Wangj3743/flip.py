from taipy.gui import Gui

output="out"
tempFront=""
tempBack=""
front=[]
back=[]



page = """
# flip.py
## Create a card:
front side: <|{tempFront}|input|>
back side: <|{tempBack}|input|>
<|create|button|on_action=create_card|>

output: <|{output}|>
"""

def create_card(state):
    # notify(state, 'info', f'The text is: {state.text}')
    front.append(tempFront)
    back.append(tempBack)
    state.output = "hello" #output var
    tempFront=""
    tempBack=""


Gui(page).run(dark_mode=False)
