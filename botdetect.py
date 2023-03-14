 
import PySimpleGUI as sg
import os
from dataRetrieve import collect
from instadataRetrieve import instacollection
from twitDet import twitPredict
from instaDet import instaPredict
#GUI work

sg.theme('DarkGrey10')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Social Media Bot Detector')],
    [sg.Text('select the app you want to use')],[sg.Image('instagram.png',pad=(0,0)), sg.Button('Instagram',size=(7,1))],
    [sg.Image('twitter.png',pad=(0,0)),sg.Button('Twitter',size=(7,1))],
   [sg.Button('Cancel',size=(7,1),pad=(0,0),button_color=('red'))]]

# Create the Window
window = sg.Window('Profile Detector', layout)


# Event Loop to process "events" and get the "values" of the inputs
while True:
  event, values = window.read()
  if event == sg.WIN_CLOSED or event == 'Cancel':
    
    break

  elif event == 'Twitter':
    
    layout2 = [[sg.Text('Enter a user ')],[sg.InputText()],[sg.Text('Status: ')],[sg.Text(" "),sg.Text(key='-rof-')],
              [sg.Push(),sg.Button('enter'),sg.Push()],[sg.Push(),sg.Button('close',button_color=('red')),sg.Push()],[sg.Image('twitter.png')]]
    window2 = sg.Window('Twitter Detector', layout2)
   
    window2.read()

    while True:
          event2, values2 = window2.read()
          if event2 == sg.WIN_CLOSED or event2 == 'close':
              
              break
          elif event2 == 'enter' :
              try:
                    collect(str(values2[0])) #collect data for user entered
                    c=twitPredict() # decision tree makes prediction on user based on data collected
                    window2['-rof-'].Update(f'This profile is {c}')
              except:
                    window2['-rof-'].Update(f'Account suspended or doesnt exist')
              
              
             
    window2.close()
  elif event == 'Instagram':
    layout3 = [[sg.Text('Enter a user ')],[sg.InputText()],[sg.Text('Status: ')],[sg.Text(" "),sg.Text(key='-rof-')],
[sg.Push(),sg.Button('enter'),sg.Push()],[sg.Push(),sg.Button('close',button_color=('red')),sg.Push()],[sg.Image('instagram.png')]]
    window3 = sg.Window('Instagram detector', layout3)
    window3.read()
    while True:
         event3, values3 = window3.read()
         if event3 == sg.WIN_CLOSED or event3 == 'close': # if user closes window or licks cancel
              
              break
         elif event3 == 'enter' :
              try:
                    instacollection(str(values3[0]))
              
                    c=instaPredict()
                    window3['-rof-'].Update(f'This profile is {c}')
              except:
                    window3['-rof-'].Update(f'Account suspended or doesnt exist')
    window3.close()
window.close()



