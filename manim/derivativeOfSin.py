from manim import *

# creates a VGroup from two VMobjects and alignes them next to each other
def createGroup(*objects):
    group = VGroup()
    last = None
    for object in objects:
        if last is not None:
            object.next_to(last, RIGHT)
        group.add(object)
        last = object
    group.move_to([0, 0, 0])
    return group

class DerivSin(Scene):
    def construct(self):
        
        text = MathTex("\\frac{d}{dx}\\ sin(x)")
        
        # derivative of sin
        self.play(Create(text))
        self.wait(1)
        self.play(Transform(text, createGroup(MathTex("\\lim_{h\\rightarrow0}\\ "), MathTex("sin(x+h){{-sin(x)}} \\over h"))))
        self.wait(1)
        
        # addition formula
        self.play(Transform(text, createGroup(MathTex("\\lim_{h\\rightarrow0}\\ "), MathTex("sin(x)cos(h)+cos(x)sin(h){{-sin(x)}} \\over h"))))
        self.play(Transform(text, createGroup(MathTex("\\lim_{h\\rightarrow0}\\ "), MathTex("sin(x)cos(h){{+cos(x)sin(h)}}-sin(x) \\over {{h}}")), run_time = 0))
        self.wait(1)
        self.play(Transform(text, createGroup(MathTex("\\lim_{h\\rightarrow0}\\ "), MathTex("sin(x)(cos(h)-1){{+cos(x)sin(h)}} \\over {{h}}"))))
        self.play(Transform(text, createGroup(MathTex("\\lim_{h\\rightarrow0}\\ "), MathTex("{{sin(x)(cos(h)-1)}}+{{cos(x)sin(h)}} \\over h")), run_time = 0))
        self.wait(1)
        
        # splitting fractions
        self.play(Transform(text, createGroup(MathTex("\\lim_{h\\rightarrow0}\\ "), MathTex("{{sin(x)(cos(h)-1)}} \\over h"), MathTex("+"), MathTex("{{cos(x)sin(h)}} \\over h"))))
        self.wait(1)
        self.play(Transform(text, createGroup(MathTex("\\lim_{h\\rightarrow0}\\ "), MathTex("{{sin(x)(cos(h)-1)}}", " \\over h"), MathTex("+\\ ", "\\lim_{h\\rightarrow0}\\ "), MathTex("{{cos(x)sin(h)}}", " \\over h"))))
        self.play(Transform(text, createGroup(MathTex("\\lim_{h\\rightarrow0}\\ "), MathTex("sin(x)(cos(h)-1)", " \\over h"), MathTex("+\\ ", "\\lim_{h\\rightarrow0}\\ "), MathTex("cos(x)sin(h)", " \\over h")), run_time = 0))
        self.wait(1)
        
        # limit
        self.play(Transform(text, createGroup(MathTex("sin(x)\\ ", "\\lim_{h\\rightarrow0}\\ "), MathTex("cos(h)-1", " \\over h"), MathTex("+\\ ", "\\lim_{h\\rightarrow0}\\ "), MathTex("cos(x)sin(h)", " \\over h"))))
        self.wait(1)
        self.play(Transform(text, createGroup(MathTex("sin(x)\\ ", "\\lim_{h\\rightarrow0}\\ "), MathTex("cos(h)-1", " \\over h"), MathTex("+\\ ", "cos(x)\\ ", "\\lim_{h\\rightarrow0}\\ "), MathTex("sin(h)", " \\over h"))))
        self.wait(1)
        self.play(Transform(text, createGroup(MathTex("sin(x)\\ ", "\\lim_{h\\rightarrow0}\\ "), MathTex("0", " \\over h"), MathTex("+\\ ", "cos(x)\\ ", "\\lim_{h\\rightarrow0}\\ "), MathTex("sin(h)", " \\over h"))))
        self.wait(1)
        self.play(Transform(text, createGroup(MathTex("sin(x)\\ "), MathTex("0"), MathTex("+\\ ", "cos(x)\\ ", "\\lim_{h\\rightarrow0}\\ "), MathTex("sin(h)", " \\over h"))))
        #self.play(Transform(text, createGroup(MathTex("sin(x)\\ "), MathTex("0"), MathTex("+\\ "), MathTex("cos(x)\\ ", "\\lim_{h\\rightarrow0}\\ "), MathTex("sin(h)", " \\over h")), run_time = 0))
        self.wait(1)
        self.play(FadeOut(text[0]), FadeOut(text[1]), FadeOut(text[2][0]))
        text.remove(text[0])
        text.remove(text[0])
        text[0].remove(text[0][0])
        self.play(Transform(text[0], MathTex("cos(x)\\ ", "\\lim_{h\\rightarrow0}\\ "), run_time = 0)) # i have no idea what I am doing but it works!!!
        text[0].next_to(text[1], LEFT)
        self.play(text.animate.move_to([0, 0, 0]))
        self.play(Transform(text, createGroup(MathTex("cos(x)\\ ", "\\lim_{h\\rightarrow0}\\ "), MathTex("sin(h)", " \\over h")), run_time = 0))
        self.wait(1)
        #self.play(Transform(text, createGroup(MathTex("sin(x)\\ ", "0", "+\\ ", "cos(x)\\ ", "\\lim_{h\\rightarrow0}\\ "), MathTex("sin(h)", " \\over h")), run_time = 0))
        #self.wait(1)
        #fakeGroup = createGroup(MathTex("cos(x)\\ ", "\\lim_{h\\rightarrow0}\\ "), MathTex("sin(h)", " \\over h"))
        #fakeGroup.add_to_back(MathTex("0", "\\ +").next_to(fakeGroup[0], LEFT))
        #self.play(Transform(text, fakeGroup))
        #self.wait(1)
        #self.play(FadeOut(fakeGroup[2]))
        #fakeGroup.remove(fakeGroup[2])
        #self.play(Transform(text, createGroup(MathTex("cos(x)\\ ", "\\lim_{h\\rightarrow0}\\ "), MathTex("sin(h)", " \\over h"))))
        #self.wait(1)
        self.play(Transform(text, createGroup(MathTex("cos(x)\\ ", "\\lim_{h\\rightarrow0}\\ "), MathTex("h", " \\over h"))))
        self.wait(1)
        self.play(Transform(text, createGroup(MathTex("cos(x)\\ ", "\\lim_{h\\rightarrow0}\\ "), MathTex("1"))))
        self.wait(1)
        self.play(Transform(text, MathTex("cos(x)")))
        self.wait(1)
        
        # result
        self.play(Transform(text, MathTex("\\frac{d}{dx}\\ sin(x)=", "cos(x)")))
        self.wait(1)
        
        self.play(FadeOut(text))
