#
# CoCo : Command Container
#
import os
import csv
from tkinter import Tk, Entry, Button, StringVar, LabelFrame, Scrollbar, Canvas, Frame, RIGHT, Y, BOTH

# Command file
commands_file = 'coco.csv'

# Load commands from a CSV file
def load_commands(file):
    commands = []
    try:
        with open(file, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                # Ensure the row is not empty
                if row[1] and row[2]:
                    commands.append(row)
    except FileNotFoundError:
        pass
    return commands

# Save commands to the CSV file, removing empty commands
def save_commands(file, commands):
    # Filter out empty commands
    filtered_commands = [command for command in commands if command[1] and command[2]]
    
    with open(file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(filtered_commands)

# Add a new empty line
def add_line():
    index = len(commands)
    commands.append([index, "", ""])  # New empty entry
    create_interface([index, "", ""])  # Create a new line in the GUI

# Save all commands from the interface
def save_all():
    for i, (name_input, command_input) in enumerate(entries):
        name = name_input.get().strip()
        command = command_input.get().strip()
        commands[i][1] = name
        commands[i][2] = command
    save_commands(commands_file, commands)

# Create the interface for each command
def create_interface(element):
    group = LabelFrame(canvas_frame, bg="grey", padx=5, pady=5)
    name_input = StringVar(master, value=element[1])
    command_input = StringVar(master, value=element[2])
    
    # Change the order: first name, then command, then Do it!
    Entry(group, textvariable=name_input, width=30).pack(side="left", padx=5)  # Command name
    Entry(group, textvariable=command_input, width=50).pack(side="left", padx=5)  # Command
    Button(group, text='Do it!', command=lambda: os.system(command_input.get())).pack(side="left")  # Do it! button
    
    entries.append((name_input, command_input))  # Save reference to the inputs
    group.pack(fill="x", pady=2)

# Close the main window and save changes
def close_app():
    save_all()
    master.destroy()

# Main window configuration
master = Tk()
master.title("CoCo - Command Container")
master.geometry("900x600")  # Larger window

# Create frame with scrollbar
canvas = Canvas(master)
scrollbar = Scrollbar(master, orient="vertical", command=canvas.yview)
canvas_frame = Frame(canvas)  # Correctly importing Frame here
canvas.create_window((0, 0), window=canvas_frame, anchor='nw')
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill=BOTH, expand=True)
scrollbar.pack(side=RIGHT, fill=Y)

# Load commands from the file
commands = load_commands(commands_file)
entries = []  # List to store references to the inputs

# Create an interface for the three buttons (New, Save, Exit) instead of the command list
button_frame = LabelFrame(canvas_frame, bg="grey", padx=5, pady=5)
Button(button_frame, text='New', command=add_line, width=10).pack(side="left", padx=5)
Button(button_frame, text='Save', command=save_all, width=10).pack(side="left", padx=5)
Button(button_frame, text='Exit', command=close_app, width=10).pack(side="left", padx=5)
button_frame.pack(fill="x", pady=10)  # Place the buttons before the command list

# Create an interface for each existing command
for element in commands:
    create_interface(element)

# Update the scrollbar
def adjust_scroll(event=None):
    canvas.configure(scrollregion=canvas.bbox('all'))

canvas_frame.bind("<Configure>", adjust_scroll)

# Start the application
master.mainloop()
