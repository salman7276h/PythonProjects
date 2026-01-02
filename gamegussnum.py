import tkinter as tk
import random

class GuessNumberApp:
    def __init__(self, master):
        self.master = master
        master.title("🎮 Guess the your number")
        master.geometry("420x550")
        master.configure(bg="#1F1D36")  # Modern deep purple theme

        self.name = ""
        self.age = 0

        self.create_intro_screen()

    def create_intro_screen(self):
        """User se naam aur umar lene wala screen"""
        self.clear_window()

        tk.Label(
            self.master, text="Welcome Player!", font=("Helvetica", 22, "bold"),
            bg="#1F1D37", fg="#E4C1f0"
        ).pack(pady=20)

        tk.Label(self.master, text="Naam likho:", font=("Helvetica", 14),
                 bg="#1F1D36", fg="#FFFFFF").pack()
        self.name_entry = tk.Entry(self.master, font=("Helvetica", 14), justify="center")
        self.name_entry.pack(pady=10)

        tk.Label(self.master, text="Umar likho:", font=("Helvetica", 14),
                 bg="#1F1D36", fg="#FFFFFF").pack()
        self.age_entry = tk.Entry(self.master, font=("Helvetica", 14), justify="center")
        self.age_entry.pack(pady=10)

        tk.Button(
            self.master,
            text="Start Game",
            font=("Helvetica", 14, "bold"),
            bg="#FF70A6", fg="white",
            activebackground="#FF9770",
            command=self.start_game
        ).pack(pady=20)

    def start_game(self):
        self.name = self.name_entry.get()
        try:
            self.age = int(self.age_entry.get())
        except ValueError:
            self.age = 0

        if not self.name or self.age <= 0:
            print('your not able to ply ')
            return

        self.setup_game_screen()

    def setup_game_screen(self):
        self.clear_window()
        self.secret = random.randint(1, 100)
        self.attempts = 0

        tk.Label(
            self.master,
            text=f"Hello, {self.name}! 🎉",
            font=("Helvetica", 20, "bold"),
            fg="#FCE38A",
            bg="#1F1D36"
        ).pack(pady=10)

        tk.Label(
            self.master,
            text="Guess the number (1 se 100):",
            font=("Helvetica", 14),
            fg="#FFFFFF",
            bg="#1F1D36"
        ).pack(pady=5)

        self.canvas = tk.Canvas(self.master, width=260, height=10, bg="#1F1D36", highlightthickness=0)
        self.canvas.pack()

        self.guess_entry = tk.Entry(self.master, font=("Helvetica", 16), justify="center")
        self.guess_entry.pack(pady=20)
        self.guess_entry.bind("<Return>", lambda event: self.check_guess())

        self.result_label = tk.Label(self.master, text="", font=("Helvetica", 14), fg="#FFFA65", bg="#1F1D36")
        self.result_label.pack(pady=10)

        self.attempts_label = tk.Label(self.master, text="Attempts: 0", font=("Helvetica", 12), fg="#FFFFFF", bg="#1F1D36")
        self.attempts_label.pack(pady=5)

        tk.Button(
            self.master,
            text="Check",
            font=("Helvetica", 14, "bold"),
            command=self.check_guess,
            bg="#38A3A5", fg="#FFFFFF",
            activebackground="#22577A"
        ).pack(pady=10)

        tk.Button(
            self.master,
            text="Reset Game",
            font=("Helvetica", 12),
            command=self.create_intro_screen,
            bg="#EF233C", fg="#FFFFFF",
            activebackground="#8D0801"
        ).pack(pady=5)

        self.guess_entry.focus_set()

    def clear_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
        except ValueError:
            self.result_label.config(text="Sirf number likho!", fg="#FFB627")
            return

        self.attempts += 1
        self.attempts_label.config(text=f"Attempts: {self.attempts}")

        if guess < self.secret:
            self.result_label.config(text="Zyāda baṛā number socho 🔼", fg="#9AEBA3")
        elif guess > self.secret:
            self.result_label.config(text="Zyāda choṭā number socho 🔽", fg="#9AEBA3")
        else:
            self.result_label.config(text=f"Mubārak ho {self.name}, sahi jawab {self.secret} 🎉", fg="#00FFAB")

        self.update_progress()
        self.guess_entry.delete(0, tk.END)

    def update_progress(self):
        max_attempts = 10
        width_per_attempt = 25
        self.canvas.delete("all")

        for i in range(self.attempts):
            x0 = i * width_per_attempt
            x1 = x0 + width_per_attempt - 2
            self.canvas.create_rectangle(x0, 0, x1, 10, fill="#FF70A6", width=0)

        self.canvas.create_rectangle(0, 0, max_attempts * width_per_attempt - 2, 10, outline="#FFFFFF")

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    GuessNumberApp(root)
    root.mainloop()
