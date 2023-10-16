from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.clipboard import Clipboard
import string as st
import random

class Tela(Screen):
    pass
Window.clearcolor = 1,1,1,1
Window.size = (350,610)


class WindowManager(ScreenManager):
    pass



kv = Builder.load_file('main.kv')


class MyApp(App):
    def build(self):
        return kv

    def texto(self, txt_id):
        letras = st.ascii_letters + st.digits + st.punctuation
        letras2 = "".join(random.sample(letras,15))
        txt_id.text = str(letras2)
        Clipboard.copy(txt_id.text)







if __name__ == '__main__':
    MyApp().run()