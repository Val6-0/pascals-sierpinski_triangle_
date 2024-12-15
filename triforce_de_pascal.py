import turtle 
turtle.speed(1000000)
turtle.setup(1500, 750)

def pascal(n):
    pas = [["1"]]
    count = 2
    for i in range(n-1):
        x = count * ["0"]
        x[0] = "1"
        x[count-1] = "1"
        count += 1
        pas.append(x)
    for i in range(2, len(pas)):
        for j in range(1, len(pas[i])-1):
            pas[i][j] = int(pas[i-1][j-1]) + int(pas[i-1][j])
    return pas

def circ(color, pos):
    turtle.up()
    turtle.goto(pos)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.color(color)
    turtle.circle(5)
    turtle.end_fill()

liste = pascal(100)
coord = [0, 150]
x = 0
for i in range(len(liste)):
    for j in range(len(liste[i])):
        if int(liste[i][j]) % 2 == 0:
            circ("blue", coord)
        else:
            circ("red", coord)
        coord[0] += 5
    coord[1] -= 5
    x -= 2.5
    coord[0] = x


turtle.done()
    