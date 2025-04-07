import tkinter as tk
from tkinter import messagebox

# Morse code dictionaries
MORSE_CODE_DICT = {
    'A': '.-',    'B': '-...',  'C': '-.-.', 
    'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',
    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',
    'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..',
    "'": '.----.', '!': '-.-.--', '/': '-..-.',
    '(': '-.--.',  ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.',  '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    ' ': '/'
}
REVERSE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

# Translator functions
def text_to_morse(text):
    text = text.upper()
    return ' '.join(MORSE_CODE_DICT.get(c, '?') for c in text)

def morse_to_text(morse):
    words = morse.strip().split(' / ')
    decoded = []
    for word in words:
        letters = word.split()
        decoded.append(''.join(REVERSE_DICT.get(l, '?') for l in letters))
    return ' '.join(decoded)

# GUI app
class MorseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Morse Code Translator")
        self.root.geometry("500x350")
        self.root.resizable(False, False)

        self.mode = tk.StringVar(value="text_to_morse")

        # Mode selection
        tk.Label(root, text="Mode:", font=("Arial", 12)).pack(pady=5)
        mode_frame = tk.Frame(root)
        mode_frame.pack()
        tk.Radiobutton(mode_frame, text="Text to Morse", variable=self.mode, value="text_to_morse").pack(side=tk.LEFT, padx=10)
        tk.Radiobutton(mode_frame, text="Morse to Text", variable=self.mode, value="morse_to_text").pack(side=tk.LEFT, padx=10)

        # Input text box
        tk.Label(root, text="Input:", font=("Arial", 12)).pack(pady=(10, 0))
        self.input_box = tk.Text(root, height=5, width=55)
        self.input_box.pack()

        # Translate button
        tk.Button(root, text="Translate", command=self.translate).pack(pady=10)

        # Output text box
        tk.Label(root, text="Output:", font=("Arial", 12)).pack(pady=(10, 0))
        self.output_box = tk.Text(root, height=5, width=55, state='disabled')
        self.output_box.pack()

    def translate(self):
        input_text = self.input_box.get("1.0", tk.END).strip()
        if not input_text:
            messagebox.showwarning("Input Required", "Please enter something to translate.")
            return

        try:
            if self.mode.get() == "text_to_morse":
                result = text_to_morse(input_text)
            else:
                result = morse_to_text(input_text)

            self.output_box.config(state='normal')
            self.output_box.delete("1.0", tk.END)
            self.output_box.insert(tk.END, result)
            self.output_box.config(state='disabled')

        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong: {e}")

# Run the GUI app
if __name__ == "__main__":
    root = tk.Tk()
    app = MorseApp(root)
    root.mainloop()
