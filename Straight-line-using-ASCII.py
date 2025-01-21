#This code is to generate straight line using ASCII

# Define the slope (m) and intercept (b)
m = 0.5  # Slope
b = 5    # Y-intercept

# Canvas size
height = 20
width = 40

# Create a blank grid
grid = [[" " for _ in range(width)] for _ in range(height)]

# Populate the grid with the line equation
for x in range(width):
    y = round(m * x + b)  # Calculate y using the line equation
    if 0 <= y < height:  # Ensure y is within the grid
        grid[height - y - 1][x] = "*"  # Place the point (inverted y-axis for text output)

# Print the grid
for row in grid:
    print("".join(row))
