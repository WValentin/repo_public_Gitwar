def draw_triangle(height):
    print(" " * height + "/\\")

    for i in range(1, height):
        print(" " * (height - i) + "/  " + "  " * (i - 1) + "\\")

    print(" " + "-" * (height *  2))

draw_triangle(5)