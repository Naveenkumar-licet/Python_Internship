from turtle import Turtle,Screen,Shape
#Defining_Screen
screen=Screen()
screen.setup(600,400)
 #Defining_boundries
PlayTop=screen.window_height()/2-100
PlayBottom=-screen.window_height()/2+100
PlayLeft=-screen.window_width()/2+50
PlayRight=screen.window_width()/2-50
#Define_Play_Field
area=Turtle()
area.hideturtle()
area.penup()
area.goto(PlayRight,PlayTop)
area.pendown()
area.goto(PlayLeft,PlayTop)
area.goto(PlayLeft,PlayBottom)
area.goto(PlayRight,PlayBottom)
area.goto(PlayRight,PlayTop)
#Defining_Ball
ball=Turtle()
ball.penup()
ball.shape("circle")
ball.shapesize(0.5,0.5)
ball_radius=10*0.5
#Defining_Paddles
L=Turtle()
R=Turtle()
L.penup()
R.penup()
#Defining_Paddle_Shape
paddle_w_half=10/2
paddle_h_half=40/2
paddle_shape=Shape("compound")
paddle_points=((-paddle_h_half,-paddle_w_half),
               (-paddle_h_half,paddle_w_half),
               (paddle_h_half,paddle_w_half),
               (paddle_h_half,-paddle_w_half))
paddle_shape.addcomponent(paddle_points,"black")
screen.register_shape("paddle",paddle_shape)
L.shape("paddle")
R.shape("paddle")
#Define_Starting_Position
L.setx(PlayLeft+10)
L.setx(PlayRight-10)
#Defining_Score
score=Turtle()
score.penup()
score.hideturtle()
score_L=0
score_R=0

def write_score():
    score.clear()
    score.goto(-screen.window_width()/4,screen.window_height()/2-80)
    score.write(score_L,align="center",font=("Arial",32,"bold"))
    score.goto(screen.window_width()/4,screen.window_height()/2-80)
    score.write(score_R,align="center",font=("Arial",32,"bold"))
write_score()
