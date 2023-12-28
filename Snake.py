from turtle import Turtle,Screen
import turtle as t


class Snake():
    def __init__(self):
        self.segments = []
        self.seg_distance = {}
        self.initialsnake()

        #create position marker



    def initialsnake(self):
        x_axis = 0
        self.segments = []
        self.blk = self.block()
        # Create an initial snake
        for _ in range(3):
            seg_1 = self.create_seg()
            seg_1.goto(x_axis, 0)

            x_axis -= 20
            self.segments.append(seg_1)
    def create_seg(self):
        seg_1 = Turtle("square")
        seg_1.color("red")
        print("The turtle size is")

        seg_1.penup()
        return seg_1

    def snake_movement(self,my_screen):

        i = 0

        for segs in range(len(self.segments) - 1, 0, -1):
            x_cor = round(self.segments[segs - 1].xcor(),1)
            y_cor = round(self.segments[segs - 1].ycor(),1)
            self.segments[segs].goto(x_cor, y_cor)



        self.segments[0].forward(20)

        #Check for colision




        if self.segments[0].xcor() >= 250:
            self.segments[0].goto(-250, self.segments[0].ycor())


        elif self.segments[0].ycor() >= 250:

            self.segments[0].goto(self.segments[0].xcor(), -250)


        elif self.segments[0].xcor() <= -250:
            self.segments[0].goto(250, self.segments[0].ycor())


        elif self.segments[0].ycor() <= -250:
            self.segments[0].goto(self.segments[0].xcor(), 250)

        my_screen.update()



    def move_snake(self,myscreen):
        myscreen.onkey(key="Right", fun=self.moves_right)
        myscreen.onkey(key="Left", fun=self.moves_left)
        myscreen.onkey(key="Up", fun=self.moves_up)
        myscreen.onkey(key="Down", fun=self.moves_down)


    # Define the moving functions
    def moves_right(self):
        if self.segments[0].heading() == 180:
            return 0
        else:
            self.segments[0].setheading(0)
            self.segments[0].forward(20)

    def moves_left(self):
        if self.segments[0].heading() == 0:
            return 0
        else:
            self.segments[0].setheading(180)
            self.segments[0].forward(20)

    def moves_up(self):
        if self.segments[0].heading() == 270:
            return 0
        else:
            self.segments[0].setheading(90)
            self.segments[0].forward(20)

    def moves_down(self):
        if self.segments[0].heading() == 90:
            return 0
        else:
            self.segments[0].setheading(270)
            self.segments[0].forward(20)
    def find_cor(self):
        x_corlast = self.segments[-1].xcor()
        x_corseclast = self.segments[-2].xcor()
        x_cornew = 0
        y_cornew = 0
        if (x_corseclast-x_corlast)>0:
            x_cornew = x_corlast - 1
            if x_cornew<=-250 :
                x_cornew = 250
        elif (x_corseclast-x_corlast)<0:
            x_cornew = x_corlast + 1
            if x_cornew >= 250:
                x_cornew = -250
        else:
            y_corlast = self.segments[-1].ycor()
            y_corseclast = self.segments[-2].ycor()
            if (y_corseclast - y_corlast) > 0:
                y_cornew = y_corlast - 1
                if y_cornew <= -250:
                    y_cornew = 250
            elif (y_corseclast - y_corlast) < 0:
                y_cornew = y_corlast + 1
                if y_cornew >= 250:
                    y_cornew = -250

        return x_cornew,y_cornew




    def snake_grow(self,food):
        x_cor = food.xcor()
        y_cor = food.ycor()
        head_xcor = self.segments[0].xcor()
        head_ycor = self.segments[0].ycor()


        '''if (head_ycor <= y_cor+10) and (head_ycor >= y_cor):
            if (head_xcor <= x_cor+10) and (head_xcor <= x_cor):
                new_seg = self.create_seg()
                x_cornew,y_cornew = self.find_cor()
                new_seg.goto(x_cornew,y_cornew)
                self.position[(x_cornew,y_cornew)] = True
                self.segments.append(new_seg)'''
        if self.segments[0].distance(food) < 15:
            new_seg = self.create_seg()
            x_cornew, y_cornew = self.find_cor()
            new_seg.goto(x_cornew, y_cornew)

            self.segments.append(new_seg)
            return True

        return False

    def detect_collision(self,my_screen):
        #check position coordinate marker dictionary for collision



        head_x = int(self.segments[0].xcor())
        head_y = int(self.segments[0].ycor())
        x = len(self)

        for segs in self.segments[1:]:

            if self.segments[0].distance(segs)<10:
                return True


        if self.segments[0].distance(self.blk) <= 30:
            print("TRUEEEEE")
            return True

        return False


    def block(self):
        blk = Turtle("square")
        blk.color("blue")
        blk.penup()
        blk.goto(-200, 200)
        blk.shapesize(stretch_wid=2,stretch_len=2)

        return blk

