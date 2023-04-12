from selenium import webdriver
from time import sleep
import webbrowser

def Screenshot(a):
  #a = input('Input username')

  webbrowser.open('https://www.instagram.com/'+ a +'/')
