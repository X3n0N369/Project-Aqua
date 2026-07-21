import turtle as t
import colorsys as c
t.width(30)
t.tracer(20)
t.bgcolor('black')
t.setup(1537,865)
r=0.0
for i in range(2000):
    r+=0.01
    color=c.hsv_to_rgb(r,1,1)
    t.pencolor(color)
    t.fd(i)
    t.rt(200)
    t.fd(i)
    t.begin_fill()
    t.circle(i,270)
    t.fd(i)
    t.rt(180)
    t.bk(i)
    t.lt(10)
    t.bk(i)
    t.rt(20)
    t.end_fill()

t.done() 