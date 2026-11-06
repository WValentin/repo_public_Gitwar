def draw_rectangle( width, height):
    for x in range(height):
        print (" | " + "-" * (width-2) + "|")
draw_rectangle( 24, 6)