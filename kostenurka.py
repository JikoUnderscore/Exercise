from turtle import *
import random


DYLZINA = 1000
VISOCINA = 700
glaven_prozorec = Screen()
glaven_prozorec.title('ОТКАЧЕНА КОСТЕНУРКА')
glaven_prozorec.screensize(DYLZINA, VISOCINA)

KILLER_SPEED = 25
VICTIM_SPEED = 10
BROJ_KOSTENURKI = 20

def proizvol():
    return random.randint(1, 100)


def proizvol2():
    return random.randint(-230, 230)


def ljavo_djasno():
    return random.randint(0, 1)





class Kostenurka(Turtle):
    def __init__(self, *args, **kwargs):
        super(Kostenurka, self).__init__(*args, **kwargs)
        # color(cvjat)
        # goto(kor)
        self.speed(0)
        self.penup()
        self.dead = False


    def ime_na_var(self):
        for k, v in globals().items():
            if v is self:
                return k

    def hit_boxxx(self, subekt_visocina, subekt_dylzina, obekt, obekt_visocina, obekt_dylzina):
        global KILLER_SPEED
        if abs(abs(obekt.xcor()) - abs(self.xcor())) < 30 and not self.dead or\
             abs(abs(obekt.ycor()) - abs(self.ycor())) < 35 and not self.dead:
            self.forward(35)
        # if abs(obekt.xcor()) > abs(self.xcor()) - 30 and not self.dead or\
        #      abs(obekt.ycor()) > abs(self.ycor()) - 30 and not self.dead:
        #     self.forward(35)

        if self.xcor() < obekt.xcor() + obekt_dylzina and \
                self.xcor() + subekt_dylzina > obekt.xcor() and \
                self.ycor() < obekt.ycor() + obekt_visocina and \
                self.ycor() + subekt_visocina > obekt.ycor() and not self.dead:


            print('hit', self)
            KILLER_SPEED = KILLER_SPEED + 1

            # for n in range(100, 201, 10):
            #     #obekt.shapesize(n/100)
            #     self.shapesize(2.5-(n/100))
            obekt.shapesize(2)
            self.write('dead', font=("Arial", 10, "normal"))
            self.color('red')

    def skorost(self, skorostta):
        if self.color()[1] == 'red':
            # self.granici(50, -50, -50, 50)
            # self.goto(0, 0)
            self.forward(0)
            self.dead = True
            return

        self.forward(skorostta)
        if ljavo_djasno() == 0:
            self.left(proizvol())
        elif ljavo_djasno() == 1:
            self.right(proizvol())
        self.granici(350, -350, -300, 300)

    def granici(self, gore, dolu, ljavo, djasno):
        if self.xcor() > gore:
            self.goto(dolu, self.ycor())
        if self.xcor() < dolu:
            self.goto(gore, self.ycor())
        if self.ycor() > djasno:
            self.goto(self.xcor(), ljavo)
        if self.ycor() < ljavo:
            self.goto(self.xcor(), djasno)

    def na_lov(self, mjasto_na_zertvi):
        cvetove_na_kostenurki = [c.color()[1] for c in mjasto_na_zertvi]

        if 'black' not in cvetove_na_kostenurki:
            self.setheading(self.towards(0,0))
            # self.forward(1)

            if self.xcor() < 25 and self.xcor() > -20 and self.ycor() < 10 and self.ycor() > -10:
                self.color('red')
                self.write('ALL ARE DEAD',align='center', font=("Arial", 50, "bold"))
                self.color('blue')
                done()
            return

        for n in range(len(mjasto_na_zertvi)):
            #print(mjasto_na_zertvi[n].color()[1])
            if mjasto_na_zertvi[n].color()[1] == 'black':
                self.setheading(self.towards(mjasto_na_zertvi[n]))
                return

    def narisuvaj_granici(self, gore, dolu, ljavo, djasno):
        self.pensize(10)
        self.penup()
        self.goto(dolu, djasno)
        self.pendown()
        self.goto(dolu, ljavo)
        self.goto(gore,ljavo)
        self.goto(gore, djasno)
        self.goto(dolu, djasno)

gr = Kostenurka()
gr.narisuvaj_granici(380, -380, -320, 320)
tplayer = Kostenurka('turtle')
tplayer.color('blue')


koste = [Kostenurka('turtle') for i in range(BROJ_KOSTENURKI)]
for kostenurkataa in koste:
    kostenurkataa.goto(proizvol2(), proizvol2())
# t1 = Kostenurka('turtle')
# t2 = Kostenurka('turtle')
# t3 = Kostenurka('turtle')
# t4 = Kostenurka('turtle')
# t5 = Kostenurka('turtle')
# t6 = Kostenurka('turtle')
# t7 = Kostenurka('turtle')
# t8 = Kostenurka('turtle')
# t9 = Kostenurka('turtle')
# t10 = Kostenurka('turtle')
# t11 = Kostenurka('turtle')
# t1.setpos(proizvol2(), proizvol2())
# t2.setpos(proizvol2(), proizvol2())
# t3.goto(proizvol2(), proizvol2())
# t4.goto(proizvol2(), proizvol2())
# t5.goto(proizvol2(), proizvol2())
# t6.goto(proizvol2(), proizvol2())
# t7.goto(proizvol2(), proizvol2())
# t8.goto(proizvol2(), proizvol2())
# t9.goto(proizvol2(), proizvol2())
# t10.goto(proizvol2(), proizvol2())
# t11.goto(proizvol2(), proizvol2())

# tplayer.shapesize(2,2)

run = True

while run:
    for kostenurkataa in koste:
        kostenurkataa.hit_boxxx(30, 30, tplayer, 30, 30)
        kostenurkataa.skorost(VICTIM_SPEED)
    koste[1].skorost(15)
    koste[-1].skorost(15)
    # t1.hit_boxxx(30, 30, tplayer, 30, 30)
    # t2.hit_boxxx(30, 30, tplayer, 30, 30)
    # t3.hit_boxxx(30, 30, tplayer, 30, 30)
    # t4.hit_boxxx(30, 30, tplayer, 30, 30)
    # t5.hit_boxxx(30, 30, tplayer, 30, 30)
    # t6.hit_boxxx(30, 30, tplayer, 30, 30)
    # t7.hit_boxxx(30, 30, tplayer, 30, 30)
    # t8.hit_boxxx(30, 30, tplayer, 30, 30)
    # t9.hit_boxxx(30, 30, tplayer, 30, 30)
    # t10.hit_boxxx(30, 30, tplayer, 30, 30)
    # t11.hit_boxxx(30, 30, tplayer, 30, 30)


    # t1.skorost(15)
    # t2.skorost(7)
    # t3.skorost(7)
    # t4.skorost(7)
    # t5.skorost(7)
    # t6.skorost(7)
    # t7.skorost(7)
    # t8.skorost(7)
    # t9.skorost(7)
    # t10.skorost(7)
    # t11.skorost(15)

    listen()
    onkeypress(lambda: tplayer.left(10), 'Left')
    onkeypress(lambda: tplayer.right(10), 'Right')

    #tplayer.granici(350, -350, -300, 300)
    tplayer.na_lov(koste)
    #tplayer.na_lov([t1, t2, t3, t4, t5, t6, t7, t8,t9,t10,t11])
    tplayer.forward(KILLER_SPEED)
    #tplayer.pendown()


    #print('t1',abs(tplayer.xcor()) , abs(t1.xcor()), abs(tplayer.ycor()), abs(t1.ycor()))
    #print('t2',abs(abs(tplayer.xcor()) - abs(t2.xcor())), abs(abs(tplayer.ycor()) - abs(t2.ycor())))
    # print('t3',abs(abs(tplayer.xcor()) - abs(t3.xcor())), abs(abs(tplayer.ycor()) - abs(t3.ycor())))
    # print('t4',abs(abs(tplayer.xcor()) - abs(t4.xcor())), abs(abs(tplayer.ycor()) - abs(t4.ycor())))
    # print('t5',abs(abs(tplayer.xcor()) - abs(t5.xcor())), abs(abs(tplayer.ycor()) - abs(t5.ycor())))
    # print('t6',abs(abs(tplayer.xcor()) - abs(t6.xcor())), abs(abs(tplayer.ycor()) - abs(t6.ycor())))
    # print('t7',abs(abs(tplayer.xcor()) - abs(t7.xcor())), abs(abs(tplayer.ycor()) - abs(t7.ycor())))
    # print(tplayer.xcor(), tplayer.ycor())
    onkey(lambda: done(), 'q')
#mainloop()
