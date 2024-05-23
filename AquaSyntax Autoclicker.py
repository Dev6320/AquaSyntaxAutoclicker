import pyautogui
import keyboard
print("""
> Please enter a keybind to enable autoclicker when pressed.
  Please use a letter key. Capitalized letters
  and lowercase letters do not make a difference, but
  they both work.
  
  For example, if u entered 'o', the mouse would
  click rapidly if you press 'o', but won't if you don't.
  Feel free to minimize the program and/or switch to
  a different program, as it will still run.
  
  Please note that we cannot garuntee any keys
  other than letter keys will work.

  Thank you for using AquaSyntax Autoclicker!
  

"""
)
keybind = str(input("> Please enter keybind here."))
while True:
    if keyboard.is_pressed("o"):
        pyautogui.click()
        pyautogui.PAUSE = 1.0
