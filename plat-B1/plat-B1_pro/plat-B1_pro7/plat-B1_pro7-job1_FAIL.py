# --------------- TASK -----------------------------

# WRITE A PROGRAM THAT CAN PRINT IN OUTPUT A RECTANGLE WITH "-" and "|" DEPENDING OF THE
# PARAMETERS INSERTED BY THE USER NAMED "width" and "height"
#
# EXAMPLE: 
# draw_rectangle(5, 3):
# > |-----|
# > |     |
# > |-----|
# 
# ---- Marks:
# > # Comment - might have TO DO or WIP or anything as a note
# > ## Description of the comment
# > # // Code put as a comment
# > # -> Indent
# > # --> Double indent
# > # ------ XY ------- category
# > # //Try// Verification print - dont forget to add a clarification of what it verify and which one
# ---- INFO:
# 1) Len = règle
# Si len dans boucle, then len value can be used as a ruler
# 2) une boucle dans une boucle permet de restart la boucle principale si echec
#  3) You can make a while loop with only True/False and break/continue to restart it instead of should_restart
# --- VERSIONS :
# -- v.1-2026-10-20 // Initial prog + plan, finished the VALUES category
# -- V.2-2026-10-21 // Changed height_draw + width_draw to middle_line_draw + startEnd_line_draw
# -- v.3-2026-10-21 // changed while to for, line and len() removed to just i var


## --------------- VALUES ---------------------------
# --- STATUS :
# -- Plan 1 (DONE)
# -- WIP (DONE)
# -- //Try// added (DONE)
# -- CODE v.1-2026.10.20
## First loop restart if fail
should_restart = True
while should_restart:
    should_restart = False 
    
    ## values of the user input    
    print("type width and height of the rectangle. must not shape a square")
    print("width: ")   
    width = int(input())
    print("height: ")
    height = int(input())  

    ## Verify if it's a rectangle AND user inserted int
    if width == height:
        print("Please create a rectangle. It can't have the same two lengths.")                                      
        should_restart = True
    else:
        should_restart = False

print("broke loop") # test boucle cassée

# DONE - loop til user has input right values (so NOT A SQUARE)
# //Try// print("broke loop") # test boucle cassée
# DONE - make an if to verify it doesnt make a square
# DONE - make an if to verify its fucking int value
# DONE -> in the if make a loop to proceed to restart program
# DONE -> print the error(s) and restart

# ---------------- FUNCTIONS -----------------------
# --- STATUS :
# -- PLAN 1 (DONE)
# -- WIP
# -- //Try// added
# -- CODE v.

# WIP - func width draw
## horizontal line, depend of the parameter inserted beforehand
def startEnd_line_draw(width): # NOT SURE - should take width as a parameter
    # WIP - while loop repeated til width == len(width)
    for i in width:
        if i == 0: # WIP - start of the line
            print("|", end="")
            i += 1
        elif i > 0: # WIP - not start nor end
            print("-", end="")
            i += 1
        elif i == width: # end of the line
            print("|")
    # WIP - incrementation of len(width + 1)

# TO DO / WIP - func height draw
## vertical line, depend of the parameter inserted beforehand and the parameter of width to know how many spaces inbetween
### print as a horizontal line
def middle_line_draw(height): # NOT SURE - should take width as a parameter
    # WIP - loop til height == len(height)
    for i in height:
        if i == 0:# WIP - start of the line
            print("|", end="")
            i += 1
        elif line > 0: # TO DO - middle of line
            print(" ", end="")
            i += 1
        elif line == len(width): # end of line
            print("|", end="")
    # WIP - incrementation of len(width +1)


# WIP - func draw rectangle
## INFO - Equivalent of a main()
def draw_rectangle():
# width func must be called only in the first line and the end line
    startEnd_line_draw(width)
    middle_line_draw(height)
    startEnd_line_draw(width)
    print("\n Here is a rectangle of ", width, " per ", height)
# make an if to verify its the first or the last line
# THE FUNCTION IS WROTE INSTEAD OF A THOUSAND OF VALUES SO WHEN YOU NEED IT IT PRINT ITSELF
# -> in the if of the last line
# --> print("\n here is a rectangle of ", width, " per ", height)

# ------------------ FUNC CALL ---------------------------
# here goes nothing
draw_rectangle()
