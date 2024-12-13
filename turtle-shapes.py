#The following is the code the I have written to draw a square, a rectangle and a triangle using the turtle module.
#function to draw a square, given a single length
def draw_square(side_length):
#the for loop will run four times, once for each side of a square
    for i in range(4):
        tom.forward(side_length)
        tom.left(90)

#function to draw an equilateral triangle
def draw_triangle(side_length):
    for i in range(3):
        tom.forward(side_length)
        #external angle of a perfect triangle is 120 degrees
        tom.left(120)

#function to draw a rectangle given two different lengths
def draw_rectangle(side_length, second_length):
    #if statement to prevent program from running if the lengths are equal
    if side_length == second_length:
        print("Lengths can't be equal")
        return
    for i in range(2):
        tom.forward(side_length)
        tom.right(90)
        tom.forward(second_length)
        tom.right(90)
#draw a square in terminal
#will print as many lines as asterisks per line to form a square
def draw_square_here(side_length):
    for i in range(side_length):
        print("*" * side_length)
        
#draw a triangle in terminal
#will print as many asterisks as iterations of the loop to form a triangle
def draw_triangle_here(height):
    for i in range(1, height + 1):
        print("*" * i)

