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
        self.play(Transform(text, createGroup(MathTex("^{lim}_{h\\rightarrow0}\\ "), MathTex("sin(x+h){{-sin(x)}} \\over h"))))
        self.wait(1)
        
        # addition formula
        self.play(Transform(text, createGroup(MathTex("^{lim}_{h\\rightarrow0}\\ "), MathTex("sin(x)cos(h)+cos(x)sin(h){{-sin(x)}} \\over h"))))
        self.play(Transform(text, createGroup(MathTex("^{lim}_{h\\rightarrow0}\\ "), MathTex("sin(x)cos(h){{+cos(x)sin(h)}}-sin(x) \\over {{h}}")), run_time = 0))
        self.wait(1)
        self.play(Transform(text, createGroup(MathTex("^{lim}_{h\\rightarrow0}\\ "), MathTex("sin(x)(cos(h)-1){{+cos(x)sin(h)}} \\over {{h}}"))))
        self.play(Transform(text, createGroup(MathTex("^{lim}_{h\\rightarrow0}\\ "), MathTex("{{sin(x)(cos(h)-1)}}+{{cos(x)sin(h)}} \\over h")), run_time = 0))
        self.wait(1)
        
        # splitting fractions
        self.play(Transform(text, createGroup(MathTex("^{lim}_{h\\rightarrow0}\\ "), MathTex("{{sin(x)(cos(h)-1)}} \\over h"), MathTex("+"), MathTex("{{cos(x)sin(h)}} \\over h"))))
        self.wait(1)
        self.play(Transform(text, createGroup(MathTex("^{lim}_{h\\rightarrow0}\\ "), MathTex("{{sin(x)(cos(h)-1)}}", " \\over h"), MathTex("+\\ ", "^{lim}_{h\\rightarrow0}\\ "), MathTex("{{cos(x)sin(h)}}", " \\over h"))))
        self.wait(1)
        
        # limit
        self.play(Transform(text, createGroup(MathTex("^{lim}_{h\\rightarrow0}\\ "), MathTex("sin(x)(0)", " \\over h"), MathTex("+\\ ", "^{lim}_{h\\rightarrow0}\\ "), MathTex("cos(x)sin(h)", " \\over h"))))
        self.wait(1)
        self.play(Transform(text, createGroup(MathTex("^{lim}_{h\\rightarrow0}\\ "), MathTex("0", " \\over h"), MathTex("+\\ ", "^{lim}_{h\\rightarrow0}\\ "), MathTex("cos(x)sin(h)", " \\over h"))))
        self.wait(1)
        self.play(Transform(text, createGroup(MathTex("0"), MathTex("+\\ ", "^{lim}_{h\\rightarrow0}\\ "), MathTex("cos(x)sin(h)", " \\over h"))))
        self.wait(1)
        self.play(Transform(text, createGroup(MathTex("^{lim}_{h\\rightarrow0}\\ "), MathTex("cos(x)sin(h)", " \\over h"))))
        self.wait(1)
        self.play(Transform(text, createGroup(MathTex("^{lim}_{h\\rightarrow0}\\ "), MathTex("cos(x)h", " \\over h"))))
        self.wait(1)
        self.play(Transform(text, createGroup(MathTex("^{lim}_{h\\rightarrow0}\\ "), MathTex("cos(x)"))))
        self.wait(1)
        self.play(Transform(text, MathTex("cos(x)")))
        self.wait(1)
        
        # result
        self.play(Transform(text, MathTex("\\frac{d}{dx}\\ sin(x)=", "cos(x)")))
        self.wait(1)
        
        self.play(FadeOut(text))
