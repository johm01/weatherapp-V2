import ttkbootstrap as tk 
from ttkbootstrap.constants import * 
import requests

class App:
    def __init__(self) -> None:
        self.root = tk.Window(size=(1080,720))
        self.root.resizable(False,False)

        self.zip = 0

        self.e1 = tk.Entry(self.root)
        self.e1.pack()

        self.b1 = tk.Button(self.root,command=lambda :self.get_weather(self.e1.get()))
        self.b1.pack()

        self.temp_gauge = tk.Meter(self.root)
        self.temp_gauge.pack()

        self.root.mainloop()

    def get_weather(self,zip):
        key = f'http://api.weatherapi.com/v1/current.json?key=9882b06f04a14ed49fd02510222704&q={zip}&aqi=no'
        try:
            self.zip = zip 
            r = requests.get(key)
            d = r.json()
            print(d)

        except TypeError:
            print('Not a valid Zip code!')

if __name__ == '__main__':
    app = App()

    