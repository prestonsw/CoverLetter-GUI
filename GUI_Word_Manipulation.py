# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 12:07:07 2021

@author: prest
"""

import PySimpleGUI as sg
from docxtpl import DocxTemplate
from docx import Document
import datetime
import os

def main(): 
    layout = [[sg.Text('Press the tab button for maximum speed.')],
              [sg.Text('Job Title Here', size = (20,1)), sg.InputText()], 
              [sg.Text("Company Name Here", size = (20,1)), sg.InputText()], 
              [sg.Text("Location Here", size = (20,1)), sg.InputText()], 
              [sg.Text('Click X in titlebar or the Exit button')],
              [sg.Button('Go'), sg.Button('Exit')]]

    window = sg.Window('Window Title', layout)
    
    cl = open("Cover Letter - Data Manipulation - No Recruiter.docx", 'rb')
    doc2 = Document('Resume_General.docx')

    while True:
        doc = DocxTemplate(cl)
        event, values = window.read()
        if event == 'Go':
            position_name = values[0]
            company_name = values[1]
            address = values[2]
            
            today_date = datetime.datetime.today().strftime('%m/%d/%Y')
                    
            context = { 'today_date': today_date, 
                        'company_name' : company_name, 
                        'position_name' : position_name,
                        'address' : address}

            doc.render(context)

            os.chdir("C:\\Users\\prest\\OneDrive\\Desktop\\Learning\\Areas of Interest\\Programming, Etc\\Python\\CoverLetter-GUI\\CL")
            doc.save('Cover_letter_'+company_name+'_'+position_name+'.docx')
            

            # Now do the Resume
            # os.chdir("C:\\Users\\prest\\OneDrive\\Desktop\\Learning\\Areas of Interest\\Programming, Etc\\Python\\CoverLetter-GUI")
            

            os.chdir("C:\\Users\\prest\\OneDrive\\Desktop\\Learning\\Areas of Interest\\Programming, Etc\\Python\\CoverLetter-GUI\\Resume")
            doc2.save('Resume_'+company_name+'_'+position_name+'.docx')
            

        elif event == sg.WIN_CLOSED or event == 'Exit':
            break


    window.close()

main()