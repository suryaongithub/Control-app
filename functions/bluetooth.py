from kivy.app import App
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
import subprocess

Window.size = (400, 200)
Window.clearcolor = get_color_from_hex("#23262e")

from kivy.lang import Builder
Builder.load_file("open.kv")

class bluetooth(App):
       
    def build(self):
        return Builder.load_file("bluetooth.kv")
    
    def proceed(self):
        # subprocess.run(r"C:\the programs\Control\Scripts\Listed.vbs", shell=True)
        # subprocess.run(r"C:\the programs\Control\Scripts\Open.bat", shell=True)
        # Do something to connect to my bluetooth device, i have the mac address
        Window.close()

    def terminate(self):
        Window.close()

if __name__ == "__main__":
    bluetooth().run()
