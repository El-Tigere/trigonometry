from manim import *
from colorThemes import *
import derivativeOfSin

class Trigonometry(Scene):
    COLORS = DARK_THEME
    def construct(self):
        self.camera.background_color = self.COLORS["background"]
        Tex.set_default(color = self.COLORS["foreground"])
        MathTex.set_default(color = self.COLORS["foreground"])
        Mobject.set_default(color = self.COLORS["foreground"])
        Dot.set_default(color = self.COLORS["foreground"])
        
        #self.wait(1)
        derivativeOfSin.DerivSin.construct(self)
        #self.wait(3)

class Title(Scene):
    COLORS = DARK_THEME
    def construct(self):
        self.camera.background_color = self.COLORS["background"]
        Tex.set_default(color = self.COLORS["foreground"])
        MathTex.set_default(color = self.COLORS["foreground"])
        Mobject.set_default(color = self.COLORS["foreground"])
        Dot.set_default(color = self.COLORS["foreground"])
        
        title = Tex("Die Ableitung von Sinus")
        title.font_size = 80
        self.play(Create(title))
        self.wait(3)
        self.play(FadeOut(title, shift = UP))
        self.wait(0.5)
