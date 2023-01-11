import ttkbootstrap as tk 
from ttkbootstrap.constants import * 
import requests

class App:
    def __init__(self) -> None:
        self.root = tk.Window(
            size=(1280,720),
            themename='solar',
            resizable=(False,False),
            )

        # Meter Frame 
        self.f1 = tk.Frame(self.root)
        self.f1.place(x=150,y=150)
        self.m2 = tk.Meter(self.f1,amounttotal=110,amountused=0,metersize=150,stepsize=10,subtext='Temp F',textright='F')
        self.m2.grid(column=1,row=1)
        self.m3 = tk.Meter(self.f1,amounttotal=100,amountused=0,metersize=150,stepsize=10,subtext='Humidity',showtext=True)
        self.m3.grid(column=0,row=1)
        self.m4 = tk.Meter(self.f1,amounttotal=100,amountused=0,metersize=150,stepsize=10,subtext='Wind Speed',showtext=True,textright='Mph')
        self.m4.grid(column=0,row=2)
        self.m5 = tk.Meter(self.f1,amounttotal=100,amountused=0,metersize=150,stepsize=10,subtext='Temp C',textright='C')
        self.m5.grid(column=1,row=2)
        
        # Entry and Button frame
        self.f2 = tk.Frame(self.root)
        self.f2.pack()
        self.e1 = tk.Entry(self.f2)
        self.e1.pack()
        self.b1 = tk.Button(self.f2,command=lambda :self.get_weather(self.e1.get()),text='Enter')
        self.b1.pack()

        # Frame for location info and other info 
        self.f3 = tk.Frame(self.root)
        self.f3.place(x=825,y=150)
        self.l1 = tk.Label(self.f3,font=('Terminus (TTF)',25),style="success.TLabel")
        self.l1.pack()
        self.l2 = tk.Label(self.f3,font=('Terminus (TTF)',20),style="success.TLabel")
        self.l2.pack()
        self.l3 = tk.Label(self.f3,font=('Terminus (TTF)',10),style="success.TLabel")
        self.l3.pack()
        self.root.mainloop()

    def get_weather(self,zip):
        # Link for API call and API key 
        key = f'http://api.weatherapi.com/v1/current.json?key=&q={zip}&aqi=no'
            
        # Making a request to the weather API
        try:
            r = requests.get(key)
            data = r.json()
            print(data)
            if data:
                try:
                    current = data['current']
                    location = data['location']
                    
                    self.m2['amountused'] = int(current['temp_f'])
                    self.m3['amountused'] = int(current['humidity'])
                    self.m4['amountused'] = int(current['wind_mph'])
                    self.m5['amountused'] = int(current['temp_c'])
                    self.l1['text'] = location['name'] +', '+ location['region']
                    self.l2['text'] = 'Feels like ' + str(int(current['feelslike_f']))
                    self.l3['text'] = current['condition']['text']
                except:
                    print('Error: '+data['error']['code'])
        except:
            print('Not a valid Zip code!')

if __name__ == '__main__':
    app = App()
