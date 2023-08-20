from taipy.gui import Gui, Markdown, navigate, Html
import pandas as pd
from fuzzy_match import algorithims
import time

##### VARIABLES #####

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

# Variable to keep track of all of the decks
all_decks = []

example_deck = {
    'id': 'pcgr-uu0e-ckrx',
    'name': 'dfsjgkl',
    'created_by': 'studier-334'
}


###### DECK ######

def deck_adapter(deck):
  return f"""
    """


decks=Html("""
<taipy:button on_action="handle_deck_create" id="create-button">+</taipy:button>
<table>
<thead>
<th>&nbsp;</th>
<th>Name</th>
<th>Created by</th>
<th></th>
</thead>
<tbody>

<taipy:part render={len(all_decks) >= 1} class_name="create-input-part">
    <tr>
        <td>
            <taipy:button on_action='handle_deck_play' class="button_deck_play" id="{len(all_decks) >= 1 and all_decks[0]['id']}">▶</taipy:button>
        </td>
        <td>{len(all_decks) >= 1 and all_decks[0]['name']}</td>
        <td>{len(all_decks) >= 1 and all_decks[0]['created_by']}</td>
        <td>
            <taipy:button on_action='handle_deck_delete' class="button_deck_delete" id="{len(all_decks) >= 1 and all_decks['id']}"></taipy:button>
        </td>
     </tr>
</taipy:part>
</tbody>
</table>
""")

def handle_deck_create(state):
    navigate(state=state, to='create')

def handle_deck_play(state, id):
    state.current_card_id=id
    navigate(state=state, to="play")

def handle_deck_delete(state, id):
    pass

def handle_search(state):
    pass
    #state.text = "Button Pressed"
    #navigate(state=state, to='create')


##### CREATE #####

new_deck_name = " "
new_deck_card_0_front = ' '
new_deck_card_0_back = ' '
new_deck_card_1_front = ' '
new_deck_card_1_back = ' '
new_deck_card_2_front = ' '
new_deck_card_2_back = ' '
new_deck_card_3_front = ' '
new_deck_card_3_back = ' '
new_deck_card_4_front = ' '
new_deck_card_4_back = ' '
new_deck_card_5_front = ' '
new_deck_card_5_back = ' '
new_deck_card_6_front = ' '
new_deck_card_6_back = ' '
new_deck_card_7_front = ' '
new_deck_card_7_back = ' '
new_deck_card_length = 1
new_deck_cards = [{ 'front': '', 'back': ''}]


create = """
### New deck name: <|{new_deck_name}|input|>

<|{new_deck_card_0_front}|input|on_change=card_change|label=Front|class_name=create-input|>
<|{new_deck_card_0_back}|input|on_change=card_change|label=Back|class_name=create-input|>
<|part|render={new_deck_card_length > 1}|class_name=create-input-part|
<|{new_deck_card_1_front}|input|on_change=card_change|label=Front|class_name=create-input|>
<|{new_deck_card_1_back}|input|on_change=card_change|label=Back|class_name=create-input|>
|>
<|part|render={new_deck_card_length > 2}|class_name=create-input-part|
<|{new_deck_card_2_front}|input|on_change=card_change|label=Front|class_name=create-input|>
<|{new_deck_card_2_back}|input|on_change=card_change|label=Back|class_name=create-input|>
|>
<|part|render={new_deck_card_length > 3}|class_name=create-input-part|
<|{new_deck_card_3_front}|input|on_change=card_change|label=Front|class_name=create-input|>
<|{new_deck_card_3_back}|input|on_change=card_change|label=Back|class_name=create-input|>
|>
<|part|render={new_deck_card_length > 4}|class_name=create-input-part|
<|{new_deck_card_4_front}|input|on_change=card_change|label=Front|class_name=create-input|>
<|{new_deck_card_4_back}|input|on_change=card_change|label=Back|class_name=create-input|>
|>
<|part|render={new_deck_card_length > 5}|class_name=create-input-part|
<|{new_deck_card_5_front}|input|on_change=card_change|label=Front|class_name=create-input|>
<|{new_deck_card_5_back}|input|on_change=card_change|label=Back|class_name=create-input|>
|>
<|part|render={new_deck_card_length > 6}|class_name=create-input-part|
<|{new_deck_card_6_front}|input|on_change=card_change|label=Front|class_name=create-input|>
<|{new_deck_card_6_back}|input|on_change=card_change|label=Back|class_name=create-input|>
|>
<|part|render={new_deck_card_length > 7}|class_name=create-input-part|
<|{new_deck_card_7_front}|input|on_change=card_change|label=Front|class_name=create-input|>
<|{new_deck_card_7_back}|input|on_change=card_change|label=Back|class_name=create-input|>
|>


<|+ New Card|button|on_action={create_card}|>

<|Create deck|button|on_action=create_new_deck|>
"""

def create_card(state):
    print('new_card')
    state.new_deck_card_length += 1
    state.new_deck_cards.append({ 'front': '', 'back': ''})

def card_change(state, var_name, var_value):
    print(var_name)

    front_back = 'front' if var_name.endswith('front') else 'back'
    state.new_deck_cards[int(var_name[14:((-1)*len(front_back)) - 1])][front_back] = var_value

def create_new_deck(state):
    
    d_questions = [x["front"] for x in state.new_deck_cards]
    d_answers = [x["back"] for x in state.new_deck_cards]

    state.all_decks.append({ 'id': d_questions, 'name': d_answers, 'created_by': 'studier334' })
    print(state.all_decks)

    navigate(state=state, to='decks')

##### LOGIN #####

login = """
<|part|class_name=center-page-wrapper|
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
<|part|class_name=center-page-wrapper|
<|part|render={not finished}|class_name=play_card|
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
    print('something changed')
    if var_name == "tempFront":
        state.tempFront = var_value
    elif var_name == "tempBack":
        state.tempBack = var_value
    elif var_name == "username":
        state.username = var_value
    elif var_name == "password":
        state.password = var_value
    elif var_name == "new_deck_name":
        state.new_deck_name = var_value
    

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
    

Gui(pages=pages, css_file="style.css").run(port=5174, dark_mode=False, stylekit=stylekit, use_reloader=True)
