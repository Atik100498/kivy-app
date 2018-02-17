from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.clock import Clock
import time
from datetime import datetime
import serial

Builder.load_string('''
<MainScreen>:
    rows:2
    cols:2
    name: 'main'
    padding: 10
    spacing: 10
    id:new

    the_time: _id_lbl_time
    BoxLayout:
        
        Label:
            text:"GPS"
            font_size: 60
        Label:
            id: _id_lbl_time   
            font_size: 30
    BoxLayout:
        Label:
            text:"GPS"
            font_size: 60
        Label:
            id:co
            font_size: 30
    BoxLayout:
        Label:
            text: "Heart Beats"
            font_size: 30
        Label:
            id:entry
            font_size: 30
    
            
            
        
 ''')

class MainScreen(GridLayout):
    ArduinoSerial = serial.Serial('/dev/ttyACM0', 115200, timeout=.1)
    def update_time(self, sec):
        MyTime = time.strftime("%H:%M:%S")
        sec = int(time.strftime("%S"))
        self.the_time.text = MyTime
        self.ids.co.text = "x: "+str(float(125.32+sec))+" N"+"\n"+"Y: "+str(float(63.32+sec))+" w"
        a = self.ArduinoSerial.readline()
        self.ids.entry.text = str(a)+" BPS"
        
    def on(self,data):
        #self.ArduinoSerial.write(b'1')
        self.ids.on.text = data
    def off(self):
        #self.ArduinoSerial.write(b'2')
        self.ids.on.text = data


class ScreenManagerApp(App):

    def build(self):
        self.main_screen = MainScreen()
        
        return self.main_screen

    def on_start(self):
        Clock.schedule_interval(self.main_screen.update_time, 1)

ScreenManagerApp().run()
