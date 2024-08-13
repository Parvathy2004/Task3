import tkinter as tk
from tkinter import messagebox
import requests

root = tk.Tk()
root.title("Song Lyrics Extractor")
root.configure(bg='wheat')

mainframe = tk.Frame(root, padx=20, pady=20, bg='lightyellow')
mainframe.pack(anchor = tk.CENTER, padx=20, pady=20)

label = tk.Label(mainframe, text="Get some lyrics!",
                 font=('Courier New Greek', 20, 'bold', 'italic'),
                 cursor= 'hand2', padx=10, pady=10, relief=tk.RAISED,
                 bg= 'wheat', fg= 'brown')
label.pack(pady=30)



def on_click(var,entry,placeholder):
    if var.get() == placeholder:
        var.set("")
        entry.configure(state="normal")

        

def on_focusout(var,entry,placeholder):
    if var.get() == "":
        entry.insert(0, placeholder)
        entry.configure(state="disabled")

        

def get_lyrics(song,artist):
    url = f"https://api.lyrics.ovh/v1/{artist}/{song}"

    response = requests.get(url)
    data = response.json()

    if 'lyrics' in data:
        return data['lyrics']
    else:
        messagebox.showerror('Error','Lyrics not found')



def submit():
    song = song_entry.get()
    artist = artist_entry.get()
    song_entry.delete(0, tk.END)
    artist_entry.delete(0, tk.END)
    artist_entry.insert(0, artist_placeholder)
    song_entry.insert(0, song_placeholder)
    song_entry.config(state='disabled')
    artist_entry.config(state='disabled')
    if song == song_placeholder or artist == artist_placeholder:
        messagebox.showwarning('Warning','Please fill both fields!')
    else:
        lyrics = get_lyrics(song,artist)
        lyrics_text.delete(1.0,tk.END)
        if lyrics:
            lyrics_text.insert(tk.END, lyrics)
            lyrics_text.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

    

frame1 = tk.Frame(mainframe, padx=20, pady=20, bg='wheat')
frame1.pack(anchor = tk.CENTER, padx=20, pady=20)

song_var = tk.StringVar()
artist_var = tk.StringVar()



song_label = tk.Label(frame1, text="Song", font=("Times New Roman", 10, "bold"),bg='wheat',fg='brown')
song_entry = tk.Entry(frame1, textvariable=song_var, width=40, bg='lightyellow', fg='brown')
song_placeholder = "Enter the song"
song_entry.insert(0, song_placeholder)
song_entry.configure(state="disabled",disabledbackground='white',disabledforeground='brown')
song_entry.bind("<Button-1>", lambda event: on_click(song_var,song_entry,song_placeholder))
song_entry.bind("<FocusOut>", lambda event: on_focusout(song_var,song_entry,song_placeholder))

artist_label = tk.Label(frame1, text="Artist", font=("Times New Roman", 10, "bold"),bg='wheat',fg='brown')
artist_entry = tk.Entry(frame1, textvariable=artist_var, width=40, bg='lightyellow', fg='brown')
artist_placeholder = "Enter the song"
artist_entry.insert(0, artist_placeholder)
artist_entry.configure(state="disabled",disabledbackground='white',disabledforeground='brown')
artist_entry.bind("<Button-1>", lambda event: on_click(artist_var,artist_entry,artist_placeholder))
artist_entry.bind("<FocusOut>", lambda event: on_focusout(artist_var,artist_entry,artist_placeholder))


lyrics_button = tk.Button(mainframe, text="Get Lyrics", command = submit, font=("Times New Roman", 10, "bold"),bg='brown',fg='wheat')

lyrics_text = tk.Text(root, wrap=tk.WORD, font=("Helvetica",12))


song_label.grid(row=0, column=0, padx=20)
song_entry.grid(row=0, column=1)
artist_label.grid(row=1, column=0, pady=20, padx=20)
artist_entry.grid(row=1, column=1)
lyrics_button.pack(pady=10)


root.mainloop()

