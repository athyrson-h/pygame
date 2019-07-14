import turtle

class shape(turtle.Turtle):
  def __init__(self, goto):
    turtle.Turtle.__init__(self)
    self.shape("square")
    self.color("black")
    self.penup()
    self.goto(goto, 0)
    self.shapesize(5, 0.5)
#forma dos play
class player(shape):
  def __init__(self, goto):
    shape.__init__(self, goto)
    self.shapesize(5, 0.5)

  def up(self):
    self.sety(self.ycor() + 20)

  def down(self):
    self.sety(self.ycor() - 20)

#form e velocidade bola
class ball(shape):
  def __init__(self, goto):
    shape.__init__(self, goto)
    self.shape("circle")
    self.shapesize(1,1)
    self.dx=3
    self.dy=3

#localização e dinamica player
  def update(self, play_1, play_2):
    self.collision(play_1, play_2)
    self.setx(self.xcor() + self.dx)
    self.sety(self.ycor() + self.dy)

  def collision(self, play_1, play_2):
    if self.ycor() > 290:
        self.sety(290)
        self.dy *= -1
    elif self.ycor() < -290:
          self.sety(-290)
          self.dy *= -1

    if self.xcor() < -335 and self.diff(play_1):
      self.dx *= -1
    if self.xcor() > 335 and self.diff(play_2):
      self.dx *= -1

  def diff(self, player):
    return self.ycor() < player.ycor() + 60 and self.ycor() > player.ycor() -60

#placar

class Score(shape):
  def __init__(self, goto):
    shape.__init__(self, goto)
    self.goto(0, goto)
    self.score_1 = 0
    self.score_2 = 0
    self.hideturtle()
    self.draw()

  def update(self, bola):
    if bola.xcor() > 345:
      self.score_1 += 1
      self.clear()
      self.draw()
      bola.goto(0, 0)
    elif bola.xcor() < - 345:
      self.score_2 += 1
      self.clear()
      self.draw()
      bola.goto(0, 0)

  def draw(self):
      self.write("jogador 1: {}  Jogador 2: {}". format(self.score_1, self.score_2), font=("arial", 22, "normal"), align = "center")

#espaço e localização placar, bola e players
play_1 = player(-350)
play_2 = player(350)
bola = ball(0)
score = Score(260)

#espaço do jogo
win = turtle.Screen()
win.title("pong game")
win.bgcolor("red")
win.setup(width=800, height=600)

#teclas
win.listen()
win.onkeypress(play_1.up, "w")
win.onkeypress(play_1.down, "s")
win.onkeypress(play_2.up, "Up")
win.onkeypress(play_2.down, "Down")

while True:
  win.update()
  bola.update(play_1, play_2)
  score.update(bola)