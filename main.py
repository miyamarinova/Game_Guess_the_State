import turtle
import pandas
from name_go_to_state import MapState

screen = turtle.Screen()
state_on_map = MapState()

screen.title('US-states-game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

correct_states = 0
def get_mouse_click_coor(x, y):
    print(x, y)

# gives the coordinates of the place where we click with the mouse
#turtle.onscreenclick(get_mouse_click_coor)
#turtle.mainloop()

# pop-up window, where we should input the guess of the state's name
answer_state = screen.textinput(title='Guess the State', prompt="What's another state's name?").title()

#map_state = MapState()
data = pandas.read_csv('50_states.csv')
state_names_list = data['state'].to_list()

#while len(state_names_list) > 0:
while len(state_names_list) > 0:
    if answer_state == 'Exit':
        break
    elif answer_state not in state_names_list:
        pass
    elif answer_state in state_names_list:
        state = data[data.state == answer_state]
        state_on_map.map_place(answer_state, state.x, state.y)
        state_names_list.remove(answer_state)
        correct_states += 1
    answer_state = screen.textinput(title=f'{correct_states} /50States Correct', prompt="What's another state's name?")

new_data = pandas.DataFrame(state_names_list)

new_data.to_csv('states_to_learn.csv', header=['state'])

