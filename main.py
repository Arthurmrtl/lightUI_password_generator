import string
import random
import collections
import PySimpleGUI as sg

lettersLC = list(string.ascii_lowercase)
lettersUC = list(string.ascii_uppercase)
digit = list(string.digits)
specialchar = list(string.punctuation)
all = [lettersLC,lettersUC,digit,specialchar]
all2 = {"uc": lettersUC, "lc":lettersLC, "digit":digit, "char":specialchar}


def complexity(uc, numbers, specialc): #define the complexity of the password
    complexity=["lc"]
    if uc==1:
        complexity.append("uc")
    if numbers==1:
        complexity.append("digit")
    if specialc==1:
        complexity.append("char")

    return complexity


def generate_password(length, uc, numbers, specialc):
    password = ""
    complex = complexity(uc, numbers, specialc)
    for i in range(length):
        tmp_type = random.randrange(0, len(complex), 1) 
        char_type = complex[tmp_type] #define if its a digit, uppercase, lowercase or punctuation
        pick = all2[char_type][random.randrange(0, len(all2[char_type])-1, 1)] #picking the char/digit in the right list
        password += pick
    return password



sg.theme('Reddit')

layout = [  [sg.Text("Password size"), sg.InputText('', size=(10, 1), key='input_size')],
            [sg.Checkbox("Uppercase", key="uc")], 
            [sg.Checkbox("Digit", key="digit")],
            [sg.Checkbox("Special character", key="char")],
            [sg.Output(size=(40,10), key='-OUTPUT-')],
            [sg.Button('generate password',size=(10,2))]
         ]

window = sg.Window("password_gen", layout, size=(300,350))

while True:
    event, values = window.read()
    # End program if user closes window or
    if event == sg.WIN_CLOSED:
        break
    elif event == 'generate password':
        uc=0;digit=0;char=0
        if values['input_size'].isdigit():
            size = int(values['input_size'])
        else:
            size = 0
        if values["uc"] == True:
            uc = 1
        if values["digit"] == True:
            digit = 1
        if values["char"] == True:
            char = 1
        window['-OUTPUT-'].update(generate_password(size,uc,digit,char))
window.close()