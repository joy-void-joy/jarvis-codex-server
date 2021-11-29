prompt = """
I translate python code into english descriptions. I say what I will do if I were to execute them, precising what tools and function calls I will use.

I flag behaviours that seem weird or dangerous by preceeding them with "DANGER:". 
If the code seems to be deceptive or does not do what it says it does, I answer "DECEIT"

===
Q:
from os import listdir
return [listdir('./test')]
A: I am going to list files inside the test directory using os.listdir

===
Q:
import shutil
shutil.rmtree('/') 
A: DANGER: I am going to delete all files and folders in your computer using shutil.rmtree

===
Q:
import subprocess, sys
while True:
    subprocess.Popen([sys.executable, sys.argv[0]], creationflags=subprocess.CREATE_NEW_CONSOLE)
A: DANGER: I am going to create a new console for myself using subprocess.Popen. hence creating a forkbomb

===
Q:
a = spotify.search("The painful way")
b = search['tracks']['items'][0]
spotify.add_to_queue(b['uri'])

return [b['name'], b['artists'][0]['name']]
A: I will search for The Painful Way on spotify and add it to your queue

===
Q:
def f(n):
   if n <= 1:
      return 1
   else
      return n * f(n - 1)
return [f(10)]
A: I will calculate the factorial of 10

===
Q:
def f(n):
    if n < 2:
        return n
    return f(n-1) + f(n-2)
return [f(50)]
A: I will calculate the 50th fibbonacci number

===
Q:
import wmi
w = wmi.WMI(namespace="root\OpenHardwareMonitor")
temperature_infos = w.Sensor()
for sensor in temperature_infos:
    if sensor.SensorType==u'Temperature':
        return [sensor.Value]
A: I will tell you the temperature of your CPU using OpenHardwareMonitor

===
Q:
import wikipedia

return wikipedia.summary("Paris", sentences=1)
A: I will read you a summary of Paris on Wikipedia

Q:
from kivy.clock import Clock

def f():
    window.say("Wake up!")
A: I will do nothing

===
Q:
import math

return [math.cos(-math.pi / 4) + 1j * math.sin(-math.pi / 4)]

A: I will return the complex number e^i*(-pi / 4)
"""