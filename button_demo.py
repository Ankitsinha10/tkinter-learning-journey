import tkinter as tk
# Create the main root object
root =tk.Tk()
root.title("Digital Post-it")
root.geometry("300x150")
#Function which prints a message to the terminal
def on_button_click ():
    print ("Button was Clicked ! Hello from the terminal.")

''' Create the Label widget
#    - Its parent is 'root' (it lives inside the main window).'''
info_label = tk.Label(root, text="Click the button below.")

# Here is our new widget: tk.Button
# The most important new option is 'command'.
# We link it to the function we defined above.
# IMPORTANT: Notice there are NO parentheses () after on_button_click.

greet_button =tk.Button(root, text ="Click Me!", command= on_button_click)

#Placing the widget on screen below
info_label.pack(pady=10)
greet_button.pack(pady=20)

#start the application main loop
root.mainloop()