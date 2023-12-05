import turtle
import pandas

screen = turtle.Screen()
screen.title("US-State")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv("50_states.csv")
list = data["state"].tolist()
cor_x = data["x"]
cor_y = data["y"]
guessed = []

while len(guessed) < 50:
    prompt = screen.textinput(title=f"{len(guessed)}/50 is guessed", prompt="Whats your guess?").title()
    if prompt == "Exit":
        missing_states = []
        for states in list:
            if states not in guessed:
                missing_states.append(states)
        states = pandas.DataFrame(missing_states)
        states.to_csv("Not_answered.csv")
        break
    for n in list:
        if prompt == n:
            guessed.append(n)
            cor = data[data.state == n]
            X = cor["x"]
            Y = cor["y"]
            t  = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.color("black")
            t.goto(float(X),float(Y))
            t.write(n)






turtle.mainloop()