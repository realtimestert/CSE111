# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    draw_pine_tree(canvas, 265, 70, 220)
    draw_text(canvas, 400, 450, "The More You Know!")

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)

# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="sky blue")
    
#drawing clouds here
    draw_oval(canvas, 100, 100, 350, 250, fill = "white")
    draw_oval(canvas, 450, 300, 300, 200, fill = "white")
    
#The little yellow one is the sun
    draw_oval(canvas, 750, 450, 790, 490, fill = "yellow")

def draw_ground(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0,
    scene_width, scene_height / 3, width=0, fill="tan4")

# Draw a pine tree.
    tree_center_x = 170
    tree_bottom = 100
    tree_height = 200
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

# Draw another pine tree.
    tree_center_x = 90
    tree_bottom = 70
    tree_height = 220
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

#Drawing yet another pine tree
    tree_center_x = 450
    tree_bottom = 75
    tree_height = 210
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
#Small pine tree
    tree_center_x = 650
    tree_bottom = 25
    tree_height = 150
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

#drawing snowmen
    draw_snowman(canvas, 500, 100, 300)
    draw_snowman(canvas, 600, 120, 250)
    draw_snowman(canvas, 120, 30, 350)

#Function to draw a snowman. 
def draw_snowman(canvas, center_x, bottom, height):
    """draw a snowman with three snowballs and a carrot in the nose.
    Each snowball should get smaller the higher up it gets. """

    #draw bottom snowball
    snow_width = height / 10
    snow_height = height / 10
    snow_left = center_x - snow_width / 2
    snow_right = center_x + snow_width / 2
    snow_top = bottom + snow_height
    draw_oval(canvas, 
            snow_left, snow_top, snow_right, bottom,
            outline = "black", width = 1, fill = "white")

    #draw middle snowball
    snow_width = height / 13
    snow_height = height / 13
    snow_left = center_x - snow_width / 2
    snow_right = center_x + snow_width / 2
    snow_top = bottom + snow_height
    draw_oval(canvas, 
            snow_left, snow_top+20, snow_right, bottom+20,
            outline = "black", width = 1, fill = "white")

    #draw head
    snow_width = height / 17
    snow_height = height / 17
    snow_left = center_x - snow_width / 2
    snow_right = center_x + snow_width / 2
    snow_top = bottom + snow_height
    draw_oval(canvas, 
            snow_left, snow_top+35, snow_right, bottom+35,
            outline = "black", width = 1, fill = "white")


def draw_pine_tree(canvas, center_x, bottom, height):
    """Draw a single pine tree.
    Parameters
        canvas: The canvas where this function
            will draw a pine tree.
        center_x, bottom: The x and y location in pixels where
            this function will draw the bottom of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=1, fill="#08B07C")

# Call the main function so that
# this program will start executing.
main()