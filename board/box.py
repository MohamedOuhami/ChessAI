import pygame

class Box:
    def __init__(self,id,color,x,y,drawrect) -> None:
        self.id = id
        self.color = color
        self.x = x
        self.y = y
        isFree = None
        self.drawrect = drawrect
        
        
