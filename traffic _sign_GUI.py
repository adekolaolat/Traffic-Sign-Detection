import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy as np
from keras.models import load_model
from my_util import csv_to_dict

# Dictionary to label all traffic sign classes
classes = csv_to_dict('traffic_sign_labels.csv')

# Load model
model = load_model('traffic_model.h5')

# Initialize Graphical User Interface
window = tk.Tk()
window.geometry('800x600')
window.title('Traffic Sign Detection')
window.configure(bg='#2B2B2B')  # Set dark background color

label_font = ('Helvetica', 15, 'bold')  # Define label font
button_font = ('Helvetica', 10, 'bold')  # Define button font

label = tk.Label(window, bg='#2B2B2B', fg='#FFFFFF', font=label_font)  # Set label colors and font
sign_image = tk.Label(window)
classify_button = None  # Store reference to the "Detect" button

# Function to classify image 
def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((30, 30))
    image = image.convert("RGB")
    image = np.array(image)
    pred = model.predict(np.expand_dims(image, axis=0))
    pred_class = np.argmax(pred, axis=1)[0]
    sign = classes[pred_class + 1]
    
    label.configure(foreground='#FFFFFF', text=sign)  # Set label colors

def show_classify_button(file_path):
    global classify_button
    if classify_button is not None:
        classify_button.destroy()  # Destroy the previous "Detect" button if it exists

    classify_button = tk.Button(frame, text="Detect", command=lambda: classify(file_path), padx=10, pady=5,
                                bg='#364156', fg='#FFFFFF', font=button_font, relief='flat')  # Set button colors and font
    classify_button.config(borderwidth=0)  # Remove button border
    classify_button.pack(side='left')

def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((window.winfo_width() / 2.25), (window.winfo_height() / 2.25)))
        im = ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image = im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass

frame = tk.Frame(window, bg='#2B2B2B')  # Frame to hold the buttons
frame.pack(side='bottom', pady=20)

upload = tk.Button(frame, text="Upload Sign", command=upload_image, padx=10, pady=5,
                   bg='#364156', fg='#FFFFFF', font=button_font, relief='flat')  # Set button colors and font
upload.config(borderwidth=0)  # Remove button border
upload.pack(side='left')

# Add spacing between buttons
spacing = tk.Label(frame, bg='#2B2B2B', width=2)  # Blank label for spacing
spacing.pack(side='left')

sign_image.pack(expand=True)

label.pack(side='bottom', pady=20)

heading = tk.Label(window, text="Detect Traffic Sign", pady=20, font=('Helvetica', 20, 'bold'))  # Set heading font
heading.configure(bg='#2B2B2B', fg='#FFFFFF')  # Set heading colors
heading.pack()

window.mainloop()
