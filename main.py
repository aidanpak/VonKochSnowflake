from graphics import *
import math

def vonKochSegment(level, start, heading, length, window):
    if level == 0:
        end = Point(start.getX() + length*math.cos(math.radians(heading)),
                    start.getY() - length*math.sin(math.radians(heading)))
        line = Line(start, end)
        line.setFill("blue")
        line.draw(window)
        return end
    else:
        seg1 = vonKochSegment(level-1, start, heading, length/3, window)
        seg2 = vonKochSegment(level-1, seg1, heading-60, length/3, window)
        seg3 = vonKochSegment(level-1, seg2, heading+60, length/3, window)
        seg4 = vonKochSegment(level-1, seg3, heading, length/3, window)
        return seg4

def vonKoch(length, level):
    window = GraphWin('von Koch Snowflake', length*1.5, length*1.5)
    p1 = Point(length/4, length)
    p2 = vonKochSegment(level, p1, 0.0, length, window)
    p3 = vonKochSegment(level, p2, 120.0, length, window)
    p4 = vonKochSegment(level, p3, 240.0, length, window)


vonKoch(500, 4)
