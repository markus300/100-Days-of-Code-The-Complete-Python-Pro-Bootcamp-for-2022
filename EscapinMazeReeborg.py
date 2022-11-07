#Try in the link
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    


while not at_goal():
    if wall_on_right() and front_is_clear():
        move()
    elif wall_in_front() and wall_on_right():
        turn_left()
    elif wall_in_front():
        turn_right()
        move()
    else:
        turn_right()
        move()
        