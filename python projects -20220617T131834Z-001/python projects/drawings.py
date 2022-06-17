import turtle

turtle.bgcolor("black")

for x in range(4):

	turtle.pencolor("blue")
	turtle.fd(100)
	turtle.rt(90)


for x in range(1,3):

	turtle.pencolor("red")
	turtle.circle(50)
	turtle.fd(100)


turtle.write("Home = ", True, align="center")
turtle.write((0,0), True)

turtle.mainloop()