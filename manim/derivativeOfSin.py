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
        
        # TODO: use better animations
        self.play(Create(text))
        self.wait(1)
        self.play(Transform(text, MathTex("^{lim}_{h\\rightarrow0}\\ \\frac{sin(x+h)-sin(x)}{h}")))
        self.wait(1)
        self.play(Transform(text, MathTex("^{lim}_{h\\rightarrow0}\\ \\frac{sin(x)cos(h)+cos(x)sin(h)-sin(x)}{h}")))
        self.wait(1)
        self.play(Transform(text, MathTex("^{lim}_{h\\rightarrow0}\\ \\frac{sin(x)(cos(h)-1)+cos(x)sin(h)}{h}")))
        self.wait(1)
        self.play(Transform(text, MathTex("^{lim}_{h\\rightarrow0}\\ \\frac{sin(x)(cos(h)-1)}{h}+\\frac{cos(x)sin(h)}{h}")))
        self.wait(1)
        self.play(Transform(text, MathTex("^{lim}_{h\\rightarrow0}\\ \\frac{sin(x)(cos(h)-1)}{h}+^{lim}_{h\\rightarrow0}\\ \\frac{cos(x)sin(h)}{h}")))
        self.wait(1)
        self.play(Transform(text, MathTex("0+cos(x)")))
        self.wait(1)
        self.play(Transform(text, MathTex("\\frac{d}{dx}\\ sin(x)=cos(x)")))
        self.wait(1)
        
        self.play(FadeOut(text))
