# Snake game
# Author: Sam. M
# Date: 20/11/26
# Ver: 1

# Importing packages to make the game work
import turtle # Used to create the GUI
import random # Randomise fruit appearance
import time # For speed increase of snake

# Creating the screen
screen = turtle.Screen()
screen.setup(width=700, height=700)
screen.title("Year 10 Snake Demo")
screen.bgcolor("black")
screen.tracer(0)

# Create the boarder
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310, 250)
turtle.pendown()
turtle.color("blue")
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle() # Hides the pen that made the boarder

# Snake
snake = turtle.Turtle()
snake.speed()
snake.shape("square")
snake.color("green")
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

# Define how the snake/player moves
def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"
def snake_go_down ():
    if snake.direction != "up":
        snake.direction = "down"
def snake_go_left ():
    if snake.direction != "right":
        snake.direction = "left"
def snake_go_right ():
     if snake.direction != "left":
            snake.direction = "right"




# Main game loop
while True:
    screen.update() # Keeps our game window open and refreshes the screen
