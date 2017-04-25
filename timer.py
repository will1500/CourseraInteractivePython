import simplegui
global counter
global stopcount
global score
score = 0
stopcount = 0
counter = 0
def format(t):
    tenth_sec = (t) % 10
    sec = int(t /10) % 10
    minutes = int(t / 600) % 600 
    ten_min = int(t /100) % 6
    string = str(minutes) + ":" + str(ten_min) + str(sec) + "." + str(tenth_sec)
    return string
def tick():
    global counter

    counter += 1

def start():
    timer.start()
def stop():
    global stopcount
    global score
    global counter
    stop = True
    timer.stop()
    if stop == True:
        stopcount += 1
        print stopcount
    if counter % 10 == 0:
        score += 1
        print score
        print "hey"

    
def restart():
    global counter
    counter = 0
    score = 0
    stopcount = 0
def draw(canvas):
    text = format(counter)
    canvas.draw_text(text, [100,100], 45,"blue")




frame = simplegui.create_frame("Home", 300, 200)
frame.set_canvas_background('white')
frame.add_button("Start",start, 100)
frame.add_button("Stop",stop, 100)
frame.add_button("Restart",restart, 100)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(10, tick)

frame.start()
