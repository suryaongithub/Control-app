from kivy.app import App
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
import subprocess
from kivy.lang import Builder



Window.size = (400, 200)
Window.clearcolor = get_color_from_hex("#23262e")

class Control(App):
    
    def build(self):
        return Builder.load_file("main.kv")
    
    def open(self):
        subprocess.Popen(r"C:\the programs\Control\Scripts\transition\Open.bat", shell=True)

    def exit(self):
        Window.close()

    def reload(self):
        subprocess.Popen(r"C:\the programs\Control\Scripts\transition\reload.bat", shell=True)
        Window.close()
        
    def bluetooth(self, instance):
        subprocess.Popen(r"C:\the programs\Control\Scripts\transition\bluetooth.bat", shell=True)
        
if __name__ == "__main__":
    Control().run()
