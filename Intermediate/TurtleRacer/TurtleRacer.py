import turtle
import time
import random

WIDTH,HEIGHT=500,500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

def start_Turtle():
    screen=turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title('Turtle Racing!')

def get_Number_Of_Racers():
    while True:
        racer_Count = input("Please enter how many racers you would like? (2-10) ")

        if racer_Count.isdigit() and 2 <= int(racer_Count) <= 10:
            return int(racer_Count)
        else:
            print("Enter a valid amount of racers")

def race(colors):
	turtles = create_turtles(colors)

	while True:
		for racer in turtles:
			distance = random.randrange(1, 20)
			racer.forward(distance)

			x, y = racer.pos()
			if y >= HEIGHT // 2 - 10:
				return colors[turtles.index(racer)]

def create_turtles(colors):
	turtles = []
	spacingx = WIDTH // (len(colors) + 1)
	for i, color in enumerate(colors):
		racer = turtle.Turtle()
		racer.color(color)
		racer.shape('turtle')
		racer.left(90)
		racer.penup()
		racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
		racer.pendown()
		turtles.append(racer)

	return turtles
  
def main():
    racer_Count = get_Number_Of_Racers()
    start_Turtle()
    random.shuffle(COLORS)
    colors = COLORS[:racer_Count]
    print(f"Turtle {race(colors)} won the race")

    time.sleep(5)

main()
