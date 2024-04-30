import tkinter as tk
from tkinter import messagebox
import random

class WordleGame(tk.Tk):
    def setup_game(self, word_file='words.txt'):
        self.title('Wordle Game')
        self.geometry('400x600')
        self.load_words(word_file)
        self.choose_word()
        self.create_interface()
        
    def create_interface(self):
        if hasattr(self, 'labels'):
            for row in self.labels:
                for label in row:
                    label.grid_forget()
            self.entry.grid_forget()
            self.check_button.grid_forget()
            self.restart_button.grid_forget()
        
        self.labels = [[tk.Label(self, font=('Helvetica', 24), width=2, borderwidth=2, relief='solid')
                        for _ in range(len(self.target_word))] for _ in range(self.max_attempts)]
        for i, row in enumerate(self.labels):
            for j, label in enumerate(row):
                label.grid(row=i, column=j)
        
        self.entry = tk.Entry(self, font=('Helvetica', 24), width=len(self.target_word))
        self.entry.grid(row=self.max_attempts+1, columnspan=len(self.target_word))
        self.check_button = tk.Button(self, text='Check', command=self.check_word)
        self.check_button.grid(row=self.max_attempts+2, columnspan=len(self.target_word))
        
        self.restart_button = tk.Button(self, text='Tee uesti', command=self.restart_game)
        self.restart_button.grid(row=self.max_attempts+3, columnspan=len(self.target_word))
        
    def choose_word(self):
        self.target_word = random.choice(self.word_list)
        self.attempts = 0
        self.max_attempts = 6
        
    def check_word(self):
        guess = self.entry.get()
        if len(guess) != len(self.target_word):
            messagebox.showinfo("Error", "Enter a valid word!")
            return
        if guess not in self.word_list:
            messagebox.showinfo("Error", "Word not in list!")
            return
        
        for i, char in enumerate(guess):
            color = 'black'
            if char == self.target_word[i]:
                color = 'green'
            elif char in self.target_word:
                color = 'yellow'
            self.labels[self.attempts][i].config(text=char, bg=color)
        
        self.attempts += 1
        self.entry.delete(0, tk.END)
        
        if guess == self.target_word:
            messagebox.showinfo("Congratulations", "You've guessed the word!")
            self.choose_word()  
            self.create_interface()  
        elif self.attempts == self.max_attempts:
            messagebox.showinfo("Game Over", f"The word was {self.target_word}")
            self.choose_word()  
            self.create_interface() 
        
    def restart_game(self):
        self.choose_word()  
        self.create_interface()  

if __name__ == "__main__":
    app = WordleGame()
    app.mainloop()
