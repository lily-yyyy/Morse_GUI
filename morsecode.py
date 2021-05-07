from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

BlinkLed = LED(4) 


win = Tk()
win.title("Morse Code")
myFont = tkinter.font.Font(family = "Helvetica", size = 12, weight = "bold")


def dot():
    BlinkLed.on()
    sleep(0.25)
    BlinkLed.off()
    sleep(0.90)


def dash():
    BlinkLed.on()
    sleep(0.75)
    BlinkLed.off()
    sleep(.90)
   

def MorseCode():
    result = text.get()
    result = result.upper()
    
    if (len(result) <= 12):
        for input in result:
                       
            if (input == 'A'):
                dot()
                dash()
    
            elif (input == 'B'):
                dash()
                dot()
                dot()
                dot()
    
            elif (input == 'C'):
                dash()
                dot()
                dash()
                dot()
      
            elif (input == 'D'):
                dash()
                dot()
                dot()

            elif (input == 'E'):
                dot()
    
            elif (input == 'F'):
                dot()
                dot()
                dot()
                dash()

            elif (input == 'G'):
                dash()
                dot()
                dot()

            elif (input == 'H'):
                dot()
                dot()
                dot()
                dot()

            elif (input == 'I'):
                dot()
                dot()

            elif (input == 'J'):
                dot()
                dash()
                dash()
                dash()

            elif (input == 'K'):
                dash()
                dot()
                dash()

            elif (input == 'L'):
                dot()
                dash()
                dot()
                dot()

            elif (input == 'M'):
                dash()
                dash()

            elif (input == 'N'):
                dash()
                dot()

            elif (input == 'O'):
                dash()
                dash()
                dash()

            elif (input == 'P'):
                dot()
                dash()
                dash()
                dot()

            elif (input == 'Q'):   
                dash()
                dash()
                dot()
                dash()

            elif (input == 'R'):
                dot()
                dash()
                dot()

            elif (input == 'S'):
                dot()
                dot()
                dot()

            elif (input == 'T'):
                dash()

            elif (input == 'U'):
                dot()
                dot()
                dash()

            elif (input == 'V'):
                dot()
                dot()
                dot()
                dash()

            elif (input == 'W'):
                dot()
                dash()
                dash()

            elif (input == 'X'):
                dash()
                dot()
                dot()
                dash()

            elif (input == 'Y'):
                dash()
                dot()
                dash()
                dash()
    
            elif (input == 'Z'):
                dash()
                dash()
                dot()
                dot()

            elif (input == '1'):
                dot()
                dash()
                dash()
                dash()
                dash()

            elif (input == '2'):
                dot()
                dot()
                dash()
                dash()
                dash()

            elif (input == '3'):
                dot()
                dot()
                dot()
                dash()
                dash()

            elif (input == '4'):
                dot()
                dot()
                dot()
                dot()
                dash()

            elif (input == '5'):
                dot()
                dot()
                dot()
                dot()
                dot()

            elif (input == '6'):
                dash()
                dot()
                dot()
                dot()
                dot()

            elif (input == '7'):
                dash()
                dash()
                dot()
                dot()
                dot()

            elif (input == '8'):
                dash()
                dash()
                dash()
                dot()
                dot()

            elif (input == '9'):
                dash()
                dash()
                dash()
                dash()
                dot()

            elif (input == '0'):
                dash()
                dash()
                dash()
                dash()
                dash()

            elif (input == '.'):
                dot()
                dash()
                dot()
                dash()
                dot()
                dash()
              
            elif (input == ','):
                dash()
                dash()
                dot()
                dot()
                dash()
                dash()

            elif (input == '?'):
                dot()
                dot()
                dash()
                dash()
                dot()
                dot()

            elif (input == '/'):
                dash()
                dot()
                dot()
                dash()
                dot()
              
            elif (input == ' '):
                sleep(0.75)
    else:
        print("You exceeded the number of character! try again")


def close():
    GPIO.cleanup()
    win.destroy()



Label(win, text="Enter A word *Max 12 Char* ", bg = "white").grid(row=0, column=0)
text = Entry(win)
text.grid(row = 1, column = 0)


MorseButton = Button(win, text = "Morse Convert", font = myFont, command = MorseCode, bg = "green", height = 1, width = 24)
MorseButton.grid(row = 2, column = 0)


exitButton = Button(win, text = "Exit", font = myFont, command = close, bg = "red", height = 1, width = 24)
exitButton.grid(row = 3, column = 0)



mainloop()