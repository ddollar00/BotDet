
import PySimpleGUI as sg
import os
from dataRetrieve import collect
from instadataRetrieve import instacollection
from twitDet import twitPredict
from instaDet import instaPredict
#GUI work

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Welcome to ProfDetect')],
    [sg.Text('select which platform you want to use')],[ sg.Button('Instagram')],[sg.Button('Twitter')],
     [sg.Button('Cancel')]]

# Create the Window
window = sg.Window('Profile Detector', layout)


# Event Loop to process "events" and get the "values" of the inputs
while True:
  event, values = window.read()
  if event == sg.WIN_CLOSED or event == 'Cancel':
    
    break

  elif event == 'Twitter':
    
    layout2 = [[sg.Text('Enter a user ')],[sg.InputText()],[sg.Text(" "),sg.Text(key='-rof-')],[sg.Button('enter')],[sg.Button('close')]]
    window2 = sg.Window('Twitter Detector', layout2)
   
    window2.read()

    while True:
          event2, values2 = window2.read()
          if event2 == sg.WIN_CLOSED or event2 == 'close':
              
              break
          elif event2 == 'enter' :
              
              collect(str(values2[0])) #collect data for user entered
              
              c=twitPredict() # decision tree makes prediction on user based on data collected
              window2['-rof-'].Update(f'This profile is {c}')
             
    window2.close()
  elif event == 'Instagram':
    layout3 = [[sg.Text('Enter a user ')],[sg.InputText()],[sg.Text(" "),sg.Text(key='-rof-')],[sg.Button('enter')],[sg.Button('close')]]
    window3 = sg.Window('Instagram detector', layout3)
    window3.read()
    while True:
         event3, values3 = window3.read()
         if event3 == sg.WIN_CLOSED or event3 == 'close': # if user closes window or 		  clicks cancel
              
              break
         elif event3 == 'enter' :
              
              instacollection(str(values3[0]))
              
              c=instaPredict()
              window3['-rof-'].Update(f'This profile is  {c}')
    window3.close()
window.close()




