def setup():
    size(1500,700)
    
head=0
body=0
leg_one = 0
leg_two = 5

turtle_h = 0
turtle_b = 0
turtle_lone = 0
turtle_ltwo = 0

def movement_variables():
    
    global head
    global body
    global leg_one
    global leg_two
    
    global turtle_h
    global turtle_b
    global turtle_lone
    global turtle_ltwo
    
    if head>=1500:
        head = -50;
    if body>=1500:
        body = -50;
    if leg_one>= 38:
        leg_one = 10;
    if leg_two>= 38:
        leg_two = 10;
    if turtle_h >=1500:
        turtle_h = -50;
    if turtle_b >= 1500:
        turtle_b = -50;
    if turtle_lone >= 20:
        turtle_lone = 5;
    if turtle_ltwo >= 20.5:
        turtle_ltwo = 5.5;
        
    y = height
     
    head+=7
    body+=7
    leg_one+=5
    leg_two+=5
    turtle_h +=1
    turtle_b +=1
    turtle_lone +=0.5
    turtle_ltwo +=0.5
     
     
def walking_animals():
    
    global head
    global body
    global leg_one
    global leg_two
    
    global turtle_h
    global turtle_b
    global turtle_lone
    global turtle_ltwo
    
    y = height
    
     #walking animal part
    #dog
    fill(105,62,32)
    ellipse(head+30,y-125,50,50)
    ellipse(body,y-90, 75,45)
    ellipse(body+26, y-65, leg_one, 58)
    ellipse(body-26, y-65, leg_two, 58)
    fill(181,101,29)
    ellipse(body+15, y-135, 23, 30)
    ellipse(body-35, y-90, 25,25)
    
    #turtle
    #shell
    fill(105,65,25)
    ellipse(turtle_h+30, y-63, 30,30)
    ellipse(turtle_b, y-60, 50, 20)
    
    fill(0,100,20)
    ellipse(turtle_b, y-65, 55,18)
    
    fill(110,70,35)
    ellipse(turtle_b+12,y-48, turtle_lone,15)
    ellipse(turtle_b-12, y-48, turtle_ltwo, 15)
    
    fill(255,10,10)
    rect(1380,450,60,220)
    
def mousePressed():
    
    global head
    global body 
    global leg_one
    global leg_two
    
    head = 50
    body = 50
    leg_one = 50 
    leg_two = 50 
    
    

def mountain():
    noStroke()
    background(10,20,180)
    
    fill(0,100,0)
    ellipse(0,700,600,800)
    ellipse(300,600,700,850)
    ellipse(600,450, 500, 750)
    ellipse(800,600,550,770)
    ellipse(1000, 500, 600, 820)
    ellipse(1270, 690, 580, 700)
    ellipse(1350, 560, 720, 800)  
    
    fill(120,180,120)
    ellipse(0,700,500,700)
    ellipse(500,600,600,700)
    ellipse(800, 450, 400, 650)
    ellipse(1300,600, 450, 700)
    ellipse(1150, 570, 500, 600)
    
    fill(96,96,96)
    rect(000,660,1500,200)
    
    fill(253,184,19)
    ellipse(0,0,100,100)
    
    
def draw():
    mountain()
    movement_variables()
    walking_animals()
    
    
    
    
    
    
    
    
    
    
    
