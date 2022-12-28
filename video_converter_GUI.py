import subprocess
import tkinter as tk
from tkinter import filedialog

# Create the main window
window = tk.Tk()
window.title("Video Converter")

# Function to select the input file
def select_input_file():
    input_file = filedialog.askopenfilename()
    input_file_label.config(text=input_file)

# Function to select the output file
def select_output_file():
    output_file = filedialog.asksaveasfilename()
    output_file_label.config(text=output_file)

# Function to start the video conversion
def start_conversion():
    input_file = input_file_label["text"]
    output_file = output_file_label["text"]
    subprocess.run(["ffmpeg", "-i", input_file, output_file])

# Create the input file selection button
input_button = tk.Button(text="Select Input File", command=select_input_file)
input_button.pack()

# Create the label to display the input file path
input_file_label = tk.Label(text="No input file selected")
input_file_label.pack()

# Create the output file selection button
output_button = tk.Button(text="Select Output File", command=select_output_file)
output_button.pack()

# Create the label to display the output file path
output_file_label = tk.Label(text="No output file selected")
output_file_label.pack()

# Create the convert button
convert_button = tk.Button(text="Convert", command=start_conversion)
convert_button.pack()

# Run the main loop
window.mainloop()
