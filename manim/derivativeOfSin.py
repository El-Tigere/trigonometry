from manim import *

class DerivSin(Scene):
    def construct(self):
        
        text = MathTex("\\frac{d}{dx}\\ sin(x)")
        
        self.play(Create(text))
        self.wait(1)
        self.play(FadeOut(text))
