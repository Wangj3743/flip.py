from taipy.gui import Gui

output="out"
tempFront=""
tempBack=""
front=[]
back=[]



page = """
# flip.py {: .blue }
## Create a card:
front side: <|{tempFront}|input|multiline|>
back side: <|{tempBack}|input|multiline|>
<|create|button|on_action=create_card|>

output: <|{output}|>
"""

def create_card(state):
    # notify(state, 'info', f'The text is: {state.text}')
    state.front.append(state.tempFront)
    state.back.append(state.tempBack)
    state.output = "hello" #output var
    state.tempFront=""
    state.tempBack=""
    print(state.front, state.back)


def on_change(state, var_name, var_value):
    if var_name == "tempFront":
        state.tempFront = var_value
        return
    elif var_name == "tempBack":
        state.tempBack = var_value
        return

stylekit = {
  "color_primary": "#0022FF"
}

Gui(page, css_file="style.css").run(dark_mode=False, stylekit=stylekit)
