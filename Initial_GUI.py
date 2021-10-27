# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 12:07:07 2021

@author: prest
"""

import PySimpleGUI as sg

layout = [[sg.Text('Press the tab button for maximum speed.')],
          [sg.Text('Job Title Here', size = (20,1)), sg.InputText()], 
          [sg.Text("Company Name Here", size = (20,1)), sg.InputText()], 
          [sg.Text("Location Here", size = (20,1)), sg.InputText()], 
          [sg.Text('Click X in titlebar or the Exit button')],
          [sg.Button('Go'), sg.Button('Exit')]]

window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    if event == 'Go':
        job = values[0]
        company = values[1]
        location = values[2]
        cover_letter = f"Dear Hiring Manager, I am interested in your {job} position at {company} in {location}."
        print(cover_letter) 
        sg.popup("Your cover letter reads: ", cover_letter)
        #print(cover_letter)
    elif event == sg.WIN_CLOSED or event == 'Exit':
        break


window.close()