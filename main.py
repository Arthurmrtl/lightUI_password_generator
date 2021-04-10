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
layout = [  [sg.Button('generate password',size=(10,2))], 
            [sg.Output(size=(40,1), key='-OUTPUT-')]   ]


window = sg.Window("password_gen", layout, size=(300,300))
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == sg.WIN_CLOSED:
        break
    elif event == 'generate password':
        window['-OUTPUT-'].update(generate_password(25,1,1,1))

window.close()