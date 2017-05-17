# implementation of card game - Memory

import simplegui
import random

a = 0
b = 0
a_pos = 0
b_pos = 0
set_flag = [False] * 16

# helper function to initialize globals
def new_game():
    global card_content
    global state
    global TURNS
    card_content = [1,2,3,4,5,6,7,8] * 2
    random.shuffle(card_content)
    print card_content
    state = 0
    TURNS = 0
    a = 0
    b = 0
    a_pos = 0
    b_pos = 0
    set_flag = [False] * 16
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state
    global TURNS
    global a
    global b
    global a_pos
    global b_pos
    global set_flag
    global match
    
    if state == 0:
        state = 1
        a_pos = pos[0] // 50
        a = card_content[a_pos]
        set_flag[a_pos] = True
    elif state == 1:
        b_pos = pos[0] // 50
        if a_pos != b_pos and set_flag[a_pos] == True and set_flag[b_pos] == False:
            state = 2
            b = card_content[b_pos]
            set_flag[b_pos] = True
            if a == b:
                match = True
            elif a != b:
                match = False
            else:
                pass
        else:
            pass
    else:
        if match == False:
            set_flag[a_pos] = False
            set_flag[b_pos] = False
        a_pos = pos[0] // 50
        a = card_content[a_pos]
        set_flag[a_pos] = True
        state = 1
        TURNS += 1
        label.set_text("Turns = " + str(TURNS))
        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    #draw cards
    #draw numbers
    for i in range(16):
        canvas.draw_text(str(card_content[i]), (12.5 + 50 * i, 50), 30, 'White')

    #draw hidden card
    for i in range(16):
        if set_flag[i] == False:
            canvas.draw_polygon([(50*i, 0), (50 + 50*i, 0), (50 + 50*i, 100), (50*i, 100)], 3, 'Brown', 'Green')

    #draw separatedly lines
    for i in range(15):
        canvas.draw_polygon([(50 + 50*i, 0), (50 + 50*i, 100)], 3, 'Brown')

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
