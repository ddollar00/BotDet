 
import PySimpleGUI as sg
import os
from dataRetrieve import collect,picc
from instadataRetrieve import instacollection,pic
from twitDet import twitPredict
from instaDet import instaPredict
import io
import cloudscraper
from PIL import Image
from tqdm import tqdm

#GUI work

sg.theme('DarkGrey10')   # Add a touch of color
# All the stuff inside your window.
font = ("Arial", 18)
font2 =("Calibri", 12)
layout = [  [sg.Text('Social Media Bot Detector', key ='-text-', font =font)],
    [sg.Text('select the app you want to use', key = '-text-', font = font2)],[sg.Image('instagram.png',pad=(10,16)), sg.Button('Instagram',button_color=('purple'), font = font)],
    [sg.Image('twitter.png',pad=(10,17)),sg.Button('Twitter', button_color=('blue'),font = font)],
   [sg.Button('Cancel',pad=(12,19),button_color=('red'),font = font)]]

# Create the Window
window = sg.Window('Profile Detector', layout, size=(310, 310))


# Event Loop to process "events" and get the "values" of the inputs
while True:
  event, values = window.read()
  if event == sg.WIN_CLOSED or event == 'Cancel':
    
    break

  elif event == 'Twitter':
    
    layout2 = [[sg.Text('Enter a user ', font = font)],[sg.InputText(font = font)],[sg.ProgressBar(3,orientation='h',expand_x=True,size=(20,20),key='-pbar-')],[sg.Text('Status: ', font = font),sg.Text(key='-rof-')],
    [sg.Push(),sg.Image(key='-img-',visible=True),sg.Push()],
              [sg.Push(),sg.Button('enter', font = font, button_color =('green')),sg.Push()],[sg.Push(),sg.Button('close',button_color=('red'), font = font),sg.Push()],[sg.Image('twitter.png')]]
    window2 = sg.Window('Twitter Detector', layout2)
   
    window2.read()

    while True:
          event2, values2 = window2.read()
          if event2 == sg.WIN_CLOSED or event2 == 'close':
              window2['-pbar-'].Update(max=3)
              break
          elif event2 == 'enter' :
              try:
                    r=0 
                    collect(str(values2[0])) #collect data for user entered
                    window2['-pbar-'].Update(current_count=r+1)
                    r+=1
                    c=twitPredict() # decision tree makes prediction on user based on data collected
                    window2['-pbar-'].Update(current_count=r+1)
                    r+=1
                    d = picc(str(values2[0]))# collects profile picture data and converts it to a usable format,png
                    window2['-pbar-'].Update(current_count=r+1)

                    window2['-rof-'].Update(f'            This profile is {c}', font =font)
                    window2['-img-'].Update(size=(300,300),data=d)

                    window2['-pbar-'].Update(current_count=0)
              except:
                    window2['-rof-'].Update(f'Account suspended or doesnt exist', font = font)
              
              
             
    window2.close()
  elif event == 'Instagram':
    layout3 = [[sg.Text('Enter a user ', font = font)],[sg.InputText(font = font)],[sg.ProgressBar(3,orientation='h',expand_x=True,size=(20,20),key='-pbar-')],[sg.Text('Status: ', font = font),sg.Text(key='-rof-')],[sg.Push(),sg.Image(key='-img-',visible=True),sg.Push()],
[sg.Push(),sg.Button('enter', font = font, button_color =('green')),sg.Push()],[sg.Push(),sg.Button('close',button_color=('red'), font = font),sg.Push()],[sg.Image('instagram.png')]]
    window3 = sg.Window('Instagram detector', layout3)
    window3.read()
    while True:
         event3, values3 = window3.read()
         if event3 == sg.WIN_CLOSED or event3 == 'close': # if user closes window or licks cancel
              window3['-pbar-'].Update(max=3)
              break
         elif event3 == 'enter' :
              try:  
                    r=0
                    instacollection(str(values3[0]))
                    window3['-pbar-'].Update(current_count=r+1)
                    r+=1
                    d=pic(str(values3[0]))        
                    window3['-pbar-'].Update(current_count=r+1)
                    r+=1
                    c=instaPredict()
                    window3['-pbar-'].Update(current_count=r+1)
                    window3['-rof-'].Update(f'          This profile is {c}', font = font)
                    window3['-img-'].Update(data=d)
                    window3['-pbar-'].Update(current_count=0)
              except:
                    window3['-rof-'].Update(f'Account suspended or doesnt exist', font = font)
    window3.close()
window.close()



