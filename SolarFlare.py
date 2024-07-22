import turtle as tur

tur.bgcolor("black")
tur.speed(0)
tur.hideturtle()

colors = ['yellow','yellow','red','red']
for i in range(200):
    for c in colors:
        tur.color(c)
        tur.left(200)
        tur.circle(200-i, 80)
tur.mainloop()