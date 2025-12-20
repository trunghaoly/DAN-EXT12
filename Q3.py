import turtle

# Input data
L = int(input('Enter initial length (L): '))
D = int(input('Enter recursion depth (D): '))
N = int(input('Enter number of sides (N): '))

# Setup Turtle
t = turtle.Turtle()
t.speed(0)

# Recursive function to draw Koch curve
def draw_koch(L,D):

    # Recursive step: apply Koch pattern
    if D > 0:
        
        # Draw 1st segment
        draw_koch(L/3,D - 1)
        
        # Turn to start triangle
        t.left(60)
        
        # Draw 2nd segment (up)
        draw_koch(L/3,D - 1)
        
        # Turn to go down
        t.right(120)
        
        # Draw 3rd segment (down)
        draw_koch(L/3,D - 1)
       
       # Turn back to original direction
        t.left(60)
        
        # Draw 4th segment
        draw_koch(L/3,D - 1)
    else:
        # Base case: draw a straight line
        t.forward(L)

# Loop N times to draw the full polygon
for i in range(N):
    
    # Draw one fractal side
    draw_koch(L,D)

    # Rotate to form the closed polygon
    t.left(360/N)

turtle.done()