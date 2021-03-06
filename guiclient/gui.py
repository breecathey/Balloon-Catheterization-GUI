import tkinter as tk
from tkinter import Button
from tkinter import Entry
from tkinter import Frame
from tkinter import Label
from tkinter import Radiobutton
from tkinter import StringVar
from tkinter import IntVar

from client import Client

client = Client(port=25565)

master = tk.Tk("Phantom - Client")

message = StringVar(master)
host = StringVar(master, value=client.get_hostname())

hr = StringVar(master, value=0)
threshold = StringVar(master, value=0)

position = StringVar(master, value='SVC')

pathway_1 = IntVar(master, value=0)
pathway_2 = IntVar(master, value=0)

def connect():
    # client.set_hostname(host.get())
    client.start()

def send_command():
    client.send_data(message.get())

def send_customisations():
    client.send_data("update")
    client.send_data("{},{}".format(hr.get(), threshold.get()))

def send_position():
    client.send_data("start-pos")
    client.send_data(position.get())

def stop_position():
    client.send_data("stop-pos")

# ============ Connection Space ===============
frame_connection = Frame(master)
frame_connection.pack(pady=5)

Label(frame_connection, text="Hostname", font='Times').pack(side=tk.LEFT)

entry_hostname = Entry(frame_connection, textvariable=host, font='Times')
entry_hostname.pack(side=tk.LEFT)

btn_connect = Button(frame_connection, text="Connect", font='Times', command=connect, fg="green")
btn_connect.pack(side=tk.LEFT)

# ============ Customisation Space ===============
frame_signal = Frame(master)
frame_signal.pack(pady=5)

Label(frame_signal, text="Heart Rate", font='Times 12 bold').grid(row=0, column=0)

entry_hr = Entry(frame_signal, textvariable=hr)
entry_hr.grid(row=0, column=1)

Label(frame_signal, text="Pacing Threshold", font='Times 12 bold').grid(row=1, column=0)

entry_threshold = Entry(frame_signal, textvariable=threshold)
entry_threshold.grid(row=1, column=1)

btn_send_customisations = Button(frame_signal, text="Send", font='Times', command=send_customisations, fg="green")
btn_send_customisations.grid(row=2, columnspan=2)

# ============ Command Space ===============
frame_command = Frame(master)
frame_command.pack(pady=5)

Label(frame_command, text="Command", font='Times').pack(side=tk.LEFT)

entry_command = Entry(frame_command, textvariable=message)
entry_command.pack(side=tk.LEFT)

btn_send_command = Button(frame_command, text="Send", font='Times', command=send_command, fg="green")
btn_send_command.pack(side=tk.LEFT)

# ============ Position Selection ===============
frame_position = Frame(master)
frame_position.pack(pady=5)

POSITIONS = [
    ("Superior Vena Cava", "SVC"),
    ("High Right Atrium", "HRA"),
    ("Mid Right Atrium", "MRA"),
    ("Low Right Atrium", "LRA"),
    ("Inferior Vena Cava", "IVC"),
    ("Right Ventricle", "RV"),
    ("Right Ventricular Wall", "RVW"),
    ("Pulmonary Artery", "PA"),
    ("Asystole", "RIP"),
]

Label(frame_position, text="Heart Positions", font='Times 16 underline').pack()

for button_text, position_value in POSITIONS:
    Radiobutton(frame_position, text=button_text, font='Times 12 bold', value=position_value, variable=position).pack()

btn_send_position = Button(frame_position, text="Send", font='Times', command=send_position, fg="green")
btn_send_position.pack()

btn_stop_position = Button(frame_position, text="Stop", font='Times', command=stop_position, fg="red")
btn_stop_position.pack()

# ========== Pathway Selection ==============
frame_pathway = Frame(master)
frame_pathway.pack(pady=5)

PATHWAYS_1 = [
    ("Low Right Atrium", 0),
    ("Inferior Vena Cava", 10)
]

PATHWAYS_2 = [
    ("Right Ventricular Wall", 0),
    ("Pulmonary Artery", 10)
]

def callback_pathway_1(*args):
    client.send_data("chpa1")
    client.send_data("%d" % pathway_1.get())

def callback_pathway_2(*args):
    client.send_data("chpa2")
    client.send_data("%d" % pathway_2.get())

pathway_1.trace('w', callback_pathway_1)
pathway_2.trace('w', callback_pathway_2)

Label(frame_pathway, text="Pathway Selection 1", font='Times 16 underline').pack(pady=5)

for button_text, pathway_value in PATHWAYS_1:
    Radiobutton(frame_pathway, text=button_text, font='Times 12 bold', value=pathway_value, variable=pathway_1).pack()

Label(frame_pathway, text="Pathway Selection 2", font='Times 16 underline').pack(pady=5)

for button_text, pathway_value in PATHWAYS_2:
    Radiobutton(frame_pathway, text=button_text, font='Times 12 bold', value=pathway_value, variable=pathway_2).pack()

tk.mainloop()

client.stop()
