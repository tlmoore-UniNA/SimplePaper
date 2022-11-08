#!/usr/bin/env python3

"""
This is a simple script to create a GUI for grabbing
papers through the IIT portal
"""
import tkinter as tk
import webbrowser


# Main Window
window = tk.Tk()
window.geometry('350x350')
window.resizable(0,0)
window.title("IIT Access Paper Grabber")

# Make DOI entry line
doi_lab = tk.Label(text="DOI:")
doi_lab.place(x=10, y = 50)
doi_entry = tk.Entry()
doi_entry.place(x = 50, y = 50,
        width=250)

# Get paper program
def get_paper():
    doi = doi_entry.get()
    doi_entry.delete(0, tk.END)
    url = "https://doi-org.biblio.iit.it/"+doi
    webbrowser.open_new_tab(url)
manuscript = tk.Button(text = "Get paper!", command = get_paper)
manuscript.place(x = 50, y = 90)

def func(event):
    doi_2 = doi_entry.get()
    doi_entry.delete(0, tk.END)
    url_2 = "https://doi-org.biblio.iit.it/"+doi_2
    webbrowser.open_new_tab(url_2)
window.bind('<Return>', func)

# Make 'close window' button
def close_window():
    window.destroy()
close = tk.Button(text = "Close", command = close_window)
close.place(x=150, y=310)
window.mainloop()
