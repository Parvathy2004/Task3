import tkinter as tk  # Importing the Tkinter module for creating GUI applications
from tkinter import messagebox  # Importing messagebox from Tkinter for displaying message boxes
import requests  # Importing the requests module to make HTTP requests

# Creating the main application window
root = tk.Tk()
root.title("Song Lyrics Extractor")  # Setting the window title
root.configure(bg='wheat')  # Setting the background color of the window

# Creating the main frame that holds all widgets, with padding and background color
mainframe = tk.Frame(root, padx=20, pady=20, bg='lightyellow')
mainframe.pack(anchor=tk.CENTER, padx=20, pady=20)  # Positioning the frame in the center

# Creating and configuring the label that serves as the title in the main frame
label = tk.Label(mainframe, text="Get some lyrics!",
                 font=('Courier New Greek', 20, 'bold', 'italic'),
                 cursor= 'hand2', padx=10, pady=10, relief=tk.RAISED,
                 bg= 'wheat', fg= 'brown')
label.pack(pady=30)  # Adding padding around the label

# Function to handle the click event on entry fields
def on_click(var, entry, placeholder):
    if var.get() == placeholder:  # Check if the current text is the placeholder
        var.set("")  # Clear the placeholder
        entry.configure(state="normal")  # Enable the entry field for user input

# Function to handle focus-out event on entry fields
def on_focusout(var, entry, placeholder):
    if var.get() == "":  # If the entry field is empty
        entry.insert(0, placeholder)  # Insert the placeholder text
        entry.configure(state="disabled")  # Disable the entry field

# Function to fetch lyrics using the API
def get_lyrics(song, artist):
    url = f"https://api.lyrics.ovh/v1/{artist}/{song}"  # Constructing the API URL with the song and artist

    response = requests.get(url)  # Sending a GET request to the API
    data = response.json()  # Parsing the JSON response

    if 'lyrics' in data:  # If the lyrics are found in the response
        return data['lyrics']  # Return the lyrics
    else:
        messagebox.showerror('Error', 'Lyrics not found')  # Show an error message if lyrics are not found

# Function to handle the submit button click event
def submit():
    song = song_entry.get()  # Get the song input from the entry field
    artist = artist_entry.get()  # Get the artist input from the entry field
    song_entry.delete(0, tk.END)  # Clear the song entry field
    artist_entry.delete(0, tk.END)  # Clear the artist entry field
    artist_entry.insert(0, artist_placeholder)  # Insert the placeholder in the artist entry field
    song_entry.insert(0, song_placeholder)  # Insert the placeholder in the song entry field
    song_entry.config(state='disabled')  # Disable the song entry field
    artist_entry.config(state='disabled')  # Disable the artist entry field
    if song == song_placeholder or artist == artist_placeholder:  # Check if placeholders are still present
        messagebox.showwarning('Warning', 'Please fill both fields!')  # Show a warning if fields are empty
    else:
        lyrics = get_lyrics(song, artist)  # Fetch the lyrics using the get_lyrics function
        lyrics_text.delete(1.0, tk.END)  # Clear the text area
        if lyrics:  # If lyrics were found
            lyrics_text.insert(tk.END, lyrics)  # Insert the lyrics into the text area
            lyrics_text.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)  # Pack the text area with padding

# Creating a frame to hold the song and artist entry fields and their labels
frame1 = tk.Frame(mainframe, padx=20, pady=20, bg='wheat')
frame1.pack(anchor=tk.CENTER, padx=20, pady=20)  # Positioning the frame in the center

# Creating StringVars to hold the text values for the entry fields
song_var = tk.StringVar()
artist_var = tk.StringVar()

# Creating and configuring the label and entry field for the song input
song_label = tk.Label(frame1, text="Song", font=("Times New Roman", 10, "bold"), bg='wheat', fg='brown')
song_entry = tk.Entry(frame1, textvariable=song_var, width=40, bg='lightyellow', fg='brown')
song_placeholder = "Enter the song"  # Placeholder text for the song entry
song_entry.insert(0, song_placeholder)  # Insert the placeholder into the entry field
song_entry.configure(state="disabled", disabledbackground='white', disabledforeground='brown')  # Disable the entry
song_entry.bind("<Button-1>", lambda event: on_click(song_var, song_entry, song_placeholder))  # Bind click event
song_entry.bind("<FocusOut>", lambda event: on_focusout(song_var, song_entry, song_placeholder))  # Bind focus-out event

# Creating and configuring the label and entry field for the artist input
artist_label = tk.Label(frame1, text="Artist", font=("Times New Roman", 10, "bold"), bg='wheat', fg='brown')
artist_entry = tk.Entry(frame1, textvariable=artist_var, width=40, bg='lightyellow', fg='brown')
artist_placeholder = "Enter the artist"  # Placeholder text for the artist entry
artist_entry.insert(0, artist_placeholder)  # Insert the placeholder into the entry field
artist_entry.configure(state="disabled", disabledbackground='white', disabledforeground='brown')  # Disable the entry
artist_entry.bind("<Button-1>", lambda event: on_click(artist_var, artist_entry, artist_placeholder))  # Bind click event
artist_entry.bind("<FocusOut>", lambda event: on_focusout(artist_var, artist_entry, artist_placeholder))  # Bind focus-out event

# Creating and configuring the "Get Lyrics" button
lyrics_button = tk.Button(mainframe, text="Get Lyrics", command=submit, font=("Times New Roman", 10, "bold"), bg='brown', fg='wheat')

# Creating a text area to display the fetched lyrics
lyrics_text = tk.Text(root, wrap=tk.WORD, font=("Helvetica", 12))

# Positioning the song label and entry field in the grid
song_label.grid(row=0, column=0, padx=20)
song_entry.grid(row=0, column=1)

# Positioning the artist label and entry field in the grid
artist_label.grid(row=1, column=0, pady=20, padx=20)
artist_entry.grid(row=1, column=1)

# Positioning the "Get Lyrics" button
lyrics_button.pack(pady=10)

# Starting the Tkinter event loop
root.mainloop()
