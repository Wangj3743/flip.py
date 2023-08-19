from taipy.gui import Gui, Markdown, navigate, Html
import pandas as pd
from fuzzy_match import algorithims
import time

root_md=f'<|navbar|>'
output="out"
tempFront=""
tempBack=""
front=[]
back=[]
username=""
password=""
text=" "
current_card_id=""
i=0
questionNum=1
questions=["Chemical Formula for sodium hydroxide", "What is the color of bananas"]
answers=["NaOH", "yellow"]
difficulties=[5, 2]
totalQuestions=len(questions)
tempAnswer=""
userAnswers=[]
currentQuestion=questions[i]
currentAnswer=answers[i]
# Variable that is true if the question is shown, false if the answer is shown
currentQuestionShown=True
finished=False
score=0

example_deck = {
    'id': 'dsjfgkhskdf',
    'name': 'dfsjgkl',
    'created_by': 'ooooo'
}

###### DECK ######

def deck_adapter(deck):
  return f"""
    <tr>
        <td>
            <taipy:button on_action='handle_deck_play' id="{deck['id']}">▶</taipy:button>
        </td>
        <td>{deck['name']}</td>
        <td>{deck['created_by']}</td>
    </tr>"""

decks_list = [example_deck, example_deck]

decks=Html(f"""
<taipy:button on_action="handle_deck_create" id="create-button">+</taipy:button>
<taipy:input value='{text}'></taipy:input>
<taipy:button on_action="handle_search">
    🔍
</taipy:button>
<table>
<thead>
<th>&nbsp;</th>
<th>Name</th>
<th>Created by</th>
</thead>
<tbody>
{"".join(map(deck_adapter, decks_list))}
</tbody>
</table>
""")

def handle_deck_create(state):
    navigate(state=state, to='create')

def handle_deck_play(state, id):
    state.current_card_id=id
    navigate(state=state, to="play")

def handle_search(state):
    pass
    #state.text = "Button Pressed"
    #navigate(state=state, to='create')


##### CREATE #####

create = """
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



##### LOGIN #####

login = """
<|layout|columns=1|id=login-page-wrapper|
<|layout|columns=1|id=login-page|
# Login to flip.py {: .blue}
<|layout|columns=1|id=login-form|
<|{username}|input|label=Username|class_name=login-input|> <br />
<|{password}|input|password|label=Password|class_name=login-input|>
<|Login|button|on_action=handle_login|id=login-button|>
|>
|>
|>
"""

def handle_login(state):
    if (state.username == '' or state.password == ''):
        return
    navigate(state=state, to="decks")


##### PLAY #####

play = """  
<|part|class_name="playUI"|
<|part|render={not finished}|
Question: <|{questionNum}|> / <|{totalQuestions}|>

<|{questions[i]}|>

<|part|render={currentQuestionShown}|class_name=userAnswers|
<|{tempAnswer}|input|>
<|>|button|on_action=revealAnswer|>
|>

<|part|render={not currentQuestionShown}|class_name=ShowAnswers|
<|{answers[i]}|>

<|{userAnswers[i]}|>
<|next|button|on_action=nextQuestion|>
|>
|>
<|part|render={finished}|
You finished!

Your score is <|{score}|>
|>
|>
"""

def revealAnswer(state): 
    state.userAnswers.append(state.tempAnswer)
    if state.tempAnswer==state.answers[state.i]:
        print("correct")
        state.score += int((state.difficulties[state.i]+1)*100)
        print(state.score)
    state.tempAnswer=""
    state.currentQuestionShown = False
    # print(state.userAnswers)

def nextQuestion(state):
    state.i+=1 
    state.currentQuestionShown = True
    if state.i >= state.totalQuestions:
        print("finished")
        state.finished = True
    else:
        state.currentQuestionShown = True
        state.questionNum += 1
        print(state.i)
        

##### MISC FUNCTIONS #####

def on_init(state):
    if (state.username == ""):
            # print('trying to navigate')
        navigate(state=state, to="login")
            # print('theoretically should have navigated')


def on_change(state, var_name, var_value):
    if var_name == "tempFront":
        state.tempFront = var_value
    elif var_name == "tempBack":
        state.tempBack = var_value
    elif var_name == "username":
        state.username = var_value
    elif var_name == "password":
        state.password = var_value
    

##### RUNNING THE GUI #####

stylekit = {
  "color_primary": "#0022FF",
  "root_margin": 0
}

sb="## This is page 2"
tourney="## This is page 2"

pages = {
    '/': root_md,
    'login': login,
    'decks': decks,
    'create': create,
    "sb": sb,
    "tournament": tourney,
    "play": play
}
    

Gui(pages=pages, css_file="style.css").run(port=5777, dark_mode=False, stylekit=stylekit, use_reloader=True)
