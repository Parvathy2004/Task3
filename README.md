# Task3
Creating GUI to Extract Lyrics from Songs Using Python
### Documentation for "Song Lyrics Extractor" Application

This documentation provides an overview of the "Song Lyrics Extractor" application built using Python's `tkinter` library. The application allows users to fetch song lyrics based on the song title and artist name.

---

#### 1. **Overview**
The "Song Lyrics Extractor" is a simple GUI application that allows users to enter a song title and the artist's name to retrieve the lyrics of the song from an online API. The application uses the `lyrics.ovh` API to fetch the lyrics.

---

#### 2. **Key Components**
- **Root Window (`root`)**: The main window of the application, configured with a title and a background color.
  
- **Main Frame (`mainframe`)**: A frame within the root window that contains all the main widgets, including labels, entry fields, and buttons.

- **Label (`label`)**: Displays the title "Get some lyrics!" at the top of the application.

- **Entry Fields (`song_entry`, `artist_entry`)**: Input fields where users can enter the song title and artist name. These fields have placeholder text and are initially disabled.

- **Text Widget (`lyrics_text`)**: A text area where the fetched lyrics are displayed.

- **Button (`lyrics_button`)**: A button labeled "Get Lyrics" that triggers the process of fetching and displaying the lyrics.

---

#### 3. **Functionality**

- **Placeholder Management**
  - **`on_click(var, entry, placeholder)`**: This function is triggered when the user clicks on an entry field. It clears the placeholder text and enables the entry field.
  
  - **`on_focusout(var, entry, placeholder)`**: This function is triggered when the user clicks away from the entry field. If the entry is empty, it restores the placeholder text and disables the entry field.

- **Fetching Lyrics**
  - **`get_lyrics(song, artist)`**: This function constructs a request URL using the song title and artist name, sends the request to the `lyrics.ovh` API, and retrieves the lyrics. If the lyrics are found, they are returned; otherwise, an error message is displayed.

- **Submit Button**
  - **`submit()`**: This function is triggered when the "Get Lyrics" button is clicked. It validates the input fields, fetches the lyrics if the fields are valid, and displays the lyrics in the text widget.

---

#### 4. **User Interaction**
- The user starts by clicking on the entry fields to enter the song title and artist name.
- Once the fields are filled out, the user clicks the "Get Lyrics" button.
- The application retrieves the lyrics and displays them in the text widget.
- If the fields are left empty, a warning message is displayed, prompting the user to fill in both fields.

---

#### 5. **Design Choices**
- **Color Scheme**: The application uses a "wheat" and "lightyellow" color scheme to create a visually pleasing and consistent design.
- **Placeholder Text**: The use of placeholders helps guide users on what information is required in each entry field.
- **Error Handling**: The application provides feedback if lyrics are not found or if the input fields are incomplete, improving the user experience.

---

#### 6. **Challenges Faced**
- **API Integration**: Ensuring that the API requests were properly formatted and handled to fetch the correct data.
- **Input Validation**: Implementing a mechanism to manage placeholder text and validate user input before making the API call.

---

### 7. **Conclusion**
The "Song Lyrics Extractor" is a user-friendly application that fetches song lyrics based on user input using the `lyrics.ovh` API. It features a clean GUI with effective placeholder management and error handling, making it an intuitive tool for retrieving and displaying song lyrics.
