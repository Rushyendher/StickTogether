import simplegui
import random
import math
width = 600
height = 600
initial_pos = [width / 2, height / 2]
time = 2
vel = [1,0]
a = 5
value = 0
score = 0
ball_pos = [width/2,height/2]
ball_vel = [-random.randrange(60, 180)/60,random.randrange(120, 240)/60]

#format for stop watch
def format(t):
    a = t // 600
    b = ((t // 10) % 60) // 10
    c = ((t // 10) % 60) % 10
    d = t % 10
    return str(a) + ":" + str(b) + str(c) + "." +str(d) 
def reset():
    global score,value
    score = 0
    
    value = 0
    timer2.stop()
    
    
def timer():
    global value
    value = value + 1
    return value
    
 
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_vel[1] = - random.randrange(60,180)/60
    if direction == "RIGHT":
        ball_vel[0] = random.randrange(120, 240)/60
    elif direction == "LEFT":
        ball_vel[0] = -random.randrange(120, 240)/60
    
def new_game():
    spawn_ball("LEFT")
def draw(canvas):
    timer2.start()
    global score,initial_pos,initial_pos2
    
    initial_pos[0] = initial_pos[0] + a * vel[0]
    initial_pos[1] = initial_pos[1] + a * vel[1]
    
    if initial_pos[0] <= 20:
        vel[0] = - vel[0]
    elif initial_pos[1] <= 20:
        vel[1] = -vel[1]
    elif initial_pos[0] >= (width - 20) - 1:
        vel[0] = - vel[0]
    elif initial_pos[1] >= (height - 20) - 1:
        vel[1] = - vel[1]
    #canvas for stop watch
    canvas.draw_text(format(value),[40,40],36,"Yellow","sans-serif")
        
  # updating big ball and collisions
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if ball_pos[1] >= (height - 60) - 1:
        ball_vel[1] = -ball_vel[1]
    elif ball_pos[1] <= 60:
        ball_vel[1] = -ball_vel[1]
    elif ball_pos[0] >= (width - 60) - 1:
        ball_vel[0] = -ball_vel[0]
    elif ball_pos[0] <= 60:
        ball_vel[0] = -ball_vel[0]
    
    if math.sqrt((((ball_pos[0] - initial_pos[0]) ** 2) + ((ball_pos[1] - initial_pos[1]) ** 2)) + 20) < 60:
        score = score +1
         
    

    canvas.draw_text(str(score),[500,40],44,"Green")
    canvas.draw_circle(ball_pos,60,3,"Red","White")
    canvas.draw_circle(initial_pos,20,3,"Red","Blue")

   
def keydown(key):
   
    
    
    ball_pos = [0,0]
    if key == simplegui.KEY_MAP["left"]:
        vel[1] = 0
        vel[0] = -1
        ball_pos[0] = initial_pos[0] - vel[0]
    if key == simplegui.KEY_MAP["right"]:
        vel[0] = 1
        vel[1] = 0
        ball_pos[0] = initial_pos[0] + vel[0]
    if key == simplegui.KEY_MAP["up"]:
        vel[0] = 0
        vel[1] = -1
        ball_pos[1] = initial_pos[1] - vel[1]
    if key == simplegui.KEY_MAP["down"]:
        vel[0] = 0
        vel[1] = 1
        ball_pos[1] = initial_pos[1] + vel[1]
        
        
        
    
frame = simplegui.create_frame("escape", 600, 600)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.add_button("RESET",reset,100)
timer2 = simplegui.create_timer(100,timer)
timer2.start()

frame.start()
