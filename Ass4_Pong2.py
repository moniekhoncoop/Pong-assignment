# Implementation of classic arcade game Pong
# Code by Moniek Honcoop
# Build on Mac with Safari v 9.1.1

""" 
23 June 2016:
Build the Pong assignment from the online coursera Python course from Rice University.
Added some extra functionalities:
- Paddle changes color when it's hit by the ball
- If a player has 3 wins, he/she wins the game

"""

import simplegui
import random

# Initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]
paddle1_pos = HEIGHT / 2
paddle2_pos = HEIGHT / 2
paddle1_vel = 0 # Vertical velocity of the left paddle
paddle2_vel = 0 # Vertical velocity of the right paddle
score1 = 0
score2 = 0

# Initialize ball_pos and ball_vel for new bal in middle of table
def spawn_ball(direction):
    """ 
    If direction is RIGHT, the ball's velocity is upper right
    If direction is LEFT, the ball's velocity is upper left
    """
    global ball_pos, ball_vel # These are vectors stored as lists
    
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel[0] = random.randrange(120, 240)
    ball_vel[1] = random.randrange(60, 180)
    
    if direction == RIGHT:
        ball_vel = [1, -1] # Spawns upwards and to the right
    elif direction == LEFT:
        ball_vel = [-1, -1] # Spawns upwards and to the left
    
# Event handlers
def new_game():
    """ Reset the score and calls function spawn_ball with argument LEFT """
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    
    score1 = 0
    score2 = 0
    
    spawn_ball(LEFT)
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
    
    # Mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White") # Midline
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White") # Left gutter
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White") # Right gutter
        
    # Update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # Draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "#ffff66", "#ffff66")

    # Collide and reflection with top and bottom wal
    if ball_pos[1] <= BALL_RADIUS:               # Top wall
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] >= HEIGHT - BALL_RADIUS:    # Bottom wall
        ball_vel[1] = - ball_vel[1]
    
    # Update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    
    if paddle1_pos <= 0 + HALF_PAD_HEIGHT:
        paddle1_vel = - paddle1_vel
    elif paddle1_pos >= HEIGHT - HALF_PAD_HEIGHT:
        paddle1_vel = - paddle1_vel
    elif paddle2_pos <= 0 + HALF_PAD_HEIGHT:
        paddle2_vel = - paddle2_vel
    elif paddle2_pos >= HEIGHT - HALF_PAD_HEIGHT:
        paddle2_vel = - paddle2_vel
    
    # Draw paddles    
    canvas.draw_line([0, paddle1_pos], [PAD_WIDTH, paddle1_pos], PAD_HEIGHT, "#3399ff")
    canvas.draw_line([WIDTH - PAD_WIDTH, paddle2_pos], [WIDTH, paddle2_pos], PAD_HEIGHT, "#3399ff")
                         
    # Determine whether paddle and ball collide 
    # If player has 3 wins the game will stop
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH: # Left gutter
        if ball_pos[1] <= paddle1_pos - HALF_PAD_HEIGHT: # Above left paddle
            if score2 < 2: # Score stop increasing at 3
                score2 += 1
                spawn_ball(RIGHT)
            else: # Background, paddles and ball become invisible
                frame.set_canvas_background('White') 
                canvas.draw_line([0, paddle1_pos], [PAD_WIDTH, paddle1_pos], PAD_HEIGHT, "White")
                canvas.draw_line([WIDTH - PAD_WIDTH, paddle2_pos], [WIDTH, paddle2_pos], PAD_HEIGHT, "White")
                canvas.draw_text('Right player wins', [165, HEIGHT / 2], 40, '#6dc066')
                ball_pos = [-700, -500]
                ball_vel = [0, 0]
        elif ball_pos[1] >= paddle1_pos + HALF_PAD_HEIGHT: # Beneath left paddle
            if score2 < 2: # Score stop increasing at 3
                score2 += 1
                spawn_ball(RIGHT)
            else: # Background, paddles and ball become invisible
                frame.set_canvas_background('White')
                canvas.draw_line([0, paddle1_pos], [PAD_WIDTH, paddle1_pos], PAD_HEIGHT, "White")
                canvas.draw_line([WIDTH - PAD_WIDTH, paddle2_pos], [WIDTH, paddle2_pos], PAD_HEIGHT, "White")
                canvas.draw_text('Right player wins', [165, HEIGHT / 2], 40, '#6dc066')
                ball_pos = [-700, -500]
                ball_vel = [0, 0]
        else:
            canvas.draw_line([0, paddle1_pos], [PAD_WIDTH, paddle1_pos], PAD_HEIGHT, "#4169e1") # The left paddle changes color when hit
            ball_vel[0] = - 1.1 * ball_vel[0]
            ball_vel[1] = - 1.1 * ball_vel[1]
    elif ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH: # Right gutter
        if ball_pos[1] <= paddle2_pos - HALF_PAD_HEIGHT: # Above right paddle
            if score1 < 2: # Score stop increasing at 3
                score1 += 1
                spawn_ball(LEFT)
            else: # Background, paddles and ball become invisible
                frame.set_canvas_background('White')
                canvas.draw_line([0, paddle1_pos], [PAD_WIDTH, paddle1_pos], PAD_HEIGHT, "White")
                canvas.draw_line([WIDTH - PAD_WIDTH, paddle2_pos], [WIDTH, paddle2_pos], PAD_HEIGHT, "White")
                canvas.draw_text('Left player wins', [165, HEIGHT / 2], 40, '#6dc066')
                ball_pos = [700, 500]
                ball_vel = [0, 0]
        elif ball_pos[1] >= paddle2_pos + HALF_PAD_HEIGHT: # Beneath right paddle
            if score1 < 2: # Score stop increasing at 3
                score1 += 1
                spawn_ball(LEFT)
            else: # Background, paddles and ball become invisible
                frame.set_canvas_background('White')
                canvas.draw_line([0, paddle1_pos], [PAD_WIDTH, paddle1_pos], PAD_HEIGHT, "White")
                canvas.draw_line([WIDTH - PAD_WIDTH, paddle2_pos], [WIDTH, paddle2_pos], PAD_HEIGHT, "White")
                canvas.draw_text('Left player wins', [165, HEIGHT / 2], 40, '#6dc066')
                ball_pos = [700, 500]
                ball_vel = [0, 0]
        else:
            canvas.draw_line([WIDTH - PAD_WIDTH, paddle2_pos], [WIDTH, paddle2_pos], PAD_HEIGHT, "#4169e1") # The right paddle changes color when hit
            ball_vel[0] = - 1.1 * ball_vel[0]
            ball_vel[1] = - 1.1 * ball_vel[1]
    
    # Draw scores
    canvas.draw_text(str(score1), [150, 100], 50, 'White')
    canvas.draw_text(str(score2), [450, 100], 50, 'White')
    
def button_handler():
    """ Reset game """
    frame.set_canvas_background('Black') # Background is set back to visible
    new_game()    

def keydown(key):
    """ The left and right paddles will move if w, s, up or down is pressed """
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel -= 1.8
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel += 1.8
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel -= 1.8
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel += 1.8
    
def keyup(key):
    """ The left and right paddles stop moving if the keys are released """ 
    global paddle1_vel, paddle2_vel
        
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0

# Create frame and register event handlers
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
restart_button = frame.add_button('Restart', button_handler)


# Start frame
new_game()
frame.start()
