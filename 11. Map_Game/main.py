import pandas
import turtle
data = pandas.read_csv('50_states.csv')
state_list = data.state.to_list()
print(state_list)
screen = turtle.Screen()
screen.title("U.S. Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")


gauss_state = 0

while gauss_state<51:
  input_state = screen.textinput(title="State",prompt='Input')
  if input_state in state_list:
      gauss_state += 1
      tur = turtle.Turtle()
      tur.hideturtle()
      tur.penup()
      axis = data[data.state == input_state]
      tur.goto(int(axis.x),int(axis.y))
      tur.write(input_state)
screen.exitonclick()        