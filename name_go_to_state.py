from turtle import Turtle

class MapState(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('black')
        self.showturtle()

    def map_place(self, name_state, x_cor, y_cor):
        self.hideturtle()
        self.penup()
        self.goto(int(x_cor), int(y_cor))
        self.write(f'{name_state}', align='center', font=('Arial', 10, 'normal'))