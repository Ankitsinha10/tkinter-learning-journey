import tkinter as tk
# Create the main root object
root =tk.Tk()
root.title("Digital Post-it")
root.geometry("300x150")
''' Create the Label widget
#    - Its parent is 'root' (it lives inside the main window).
#    - The text it will display is "Time to learn Tkinter!".
#    - We'll also set a font for style. Font is a tuple: (font_family, font_size, style).'''
message_label = tk.Label(root, text="Learning Tkinter", font= ("Arial", 14))
'''
"Pack" the label into the window to make it visible.
#    - pady=20 adds 20 pixels of padding on the top and bottom.
#    - padx=10 adds 10 pixels of padding on the left and right.
#    - This gives our text some breathing room.
'''
message_label.pack(pady= 20, padx=10)
#start the application main loop
root.mainloop()