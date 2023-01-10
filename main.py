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
        self.f1 = tk.Frame(self.root,style='danger.TFrame')
        self.f1.place(x=150,y=150)
        self.m2 = tk.Meter(self.f1,amounttotal=100,amountused=0,metersize=100,stepsize=10)
        self.m2.grid(column=1,row=1)
        self.m3 = tk.Meter(self.f1,amounttotal=100,amountused=0,metersize=100,stepsize=10)
        self.m3.grid(column=0,row=1)
        
        # Entry and Button frame
        self.f2 = tk.Frame(self.root)
        self.f2.pack()
        self.e1 = tk.Entry(self.f2)
        self.e1.pack()
        self.b1 = tk.Button(self.f2,command=lambda :self.get_weather(self.e1.get()),text='Enter')
        self.b1.pack()

        # Frame for location info and other info 
        self.f3 = tk.Frame(self.root)
        self.f3.place(x=750,y=150)
        self.l1 = tk.Label(self.f3,font=('',20))
        self.l1.pack()
        self.l2 = tk.Label(self.f3,font=('',15))
        self.l2.pack()

        self.root.mainloop()

    def get_weather(self,zip):
        # Link for API call and API key 
        key = f'http://api.weatherapi.com/v1/current.json?key=9882b06f04a14ed49fd02510222704&q={zip}&aqi=no'
            
        # Making a request to the weather API
        r = requests.get(key)
        try:
            data = r.json()
            if data:
                current = data['current']
                location = data['location']
                try:
                    widget = [self.m2,self.m3,self.l1,self.l2]
                    widget[0]['amountused'] = int(current['temp_f'])
                    widget[1]['amountused'] = current['humidity'] 
                    widget[2]['text'] = location['name'] +', '+ location['region']
                    widget[3]['text'] = 'Feels like ' + str(current['feelslike_f'])
                except:
                    print('Error: '+data['error']['code'])
        except:
            print('Not a valid Zip code!')

if __name__ == '__main__':
    app = App()
