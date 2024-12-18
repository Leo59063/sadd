import turtle
import time

# Setup screen for turtle
screen = turtle.Screen()
screen.setup(width=400, height=400)
screen.bgcolor("white")

# Create a turtle to draw
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Define constants for the grid size
GRID_SIZE = 5
CELL_SIZE = 40  # Size of each cell (LED)

# Create the 5x5 grid of turtle "pen" objects
leds = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Function to draw a single cell
def draw_cell(x, y):
    # Adjust coordinates to ensure correct orientation
    t.penup()
    t.goto(y * CELL_SIZE - (CELL_SIZE * GRID_SIZE / 2), -(x * CELL_SIZE - (CELL_SIZE * GRID_SIZE / 2)))
    t.pendown()
    t.setheading(0)  # Ensure the turtle is facing "up"
    t.begin_fill()
    for _ in range(4):
        t.forward(CELL_SIZE)
        t.left(90)
    t.end_fill()


# Function to set a LED's state (ON or OFF)
def set_led(x, y, state):
    if state:
        t.fillcolor("black")  # ON (black color)
    else:
        t.fillcolor("white")  # OFF (white color)
    
    draw_cell(x, y)

# Function to initialize the grid (clear the display)
def initialize_grid():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            leds[i][j] = False  # All LEDs are initially OFF
            set_led(i, j, leds[i][j])

# Function to display a heart pattern
def show_heart():
    heart = [
        [False, True, False, True, False],
        [True, True, True, True, True],
        [True, True, True, True, True],
        [False, True, True, True, False],
        [False, False, True, False, False]
    ]
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            leds[i][j] = heart[i][j]
            set_led(i, j, leds[i][j])

# Function to display a smile pattern
def show_smile():
    smile = [
        [False, False, False, False, False],
        [False, True, False, True, False],
        [False, False, False, False, False],
        [True, False, False, False, True],
        [False, True, True, True, False]
    ]
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            leds[i][j] = smile[i][j]
            set_led(i, j, leds[i][j])

# Function to display a sad pattern
def show_sad():
    sad = [
        [True, True, True, True, True],
        [True, False, False, False, True],
        [True, False, True, False, True],
        [True, True, True, True, True],
        [True, True, True, True, True]
    ]
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            leds[i][j] = sad[i][j]
            set_led(i, j, leds[i][j])


def amoung_us():
    amoung = [
        [False, False, False, False, False],
        [False, True, True, True, False],
        [False, False, False, true, True],
        [False, True, True, True, True],
        [False, True, False, True, False],
    ]
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            leds[i][j] = amoung[i][j]
            set_led(i, j, leds[i][j])

# Function to clear the grid
def clear():
    """Clears the 5x5 grid by turning off all LEDs."""
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            leds[i][j] = False
            set_led(i, j, False)

# Function to scroll a message (just a simple placeholder for now)
def scroll_message(message):
    print("Scrolling message: ", message)

# Function to interpret and execute commands from a Python file
def execute_script_from_file(filename):
    try:
        with open(filename, 'r') as file:
            code = file.read()
            exec(code)  # Execute the code from the file in the current context
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"Error executing the script: {e}")

# Initialize the grid
initialize_grid()

# Start interpreting commands from a file
filename = input("Enter the Python filename (e.g., microbit_code.py): ").strip()

# Execute the commands in the Python file
execute_script_from_file(filename)

# Keep the Turtle window open
turtle.done()
