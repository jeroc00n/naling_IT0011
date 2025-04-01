from typing import List, Dict, Callable
import tkinter as tk
from tkinter import ttk, messagebox, PhotoImage
from datetime import datetime
from typing import Callable, Dict, Optional
from PIL import Image, ImageTk
import os

class SignUpForm(tk.Toplevel):
    def __init__(self, parent, on_submit: Callable):
        super().__init__(parent)
        self.title("Sign Up Form")
        self.geometry("500x600")
        self.resizable(False, False)
        self.on_submit = on_submit
        
        self._setup_ui()
        self._center_window()

    def _center_window(self):
        """Center the window on the screen"""
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'+{x}+{y}')

    def _setup_ui(self):
        """Set up the user interface"""
        # Header with image
        header_frame = tk.Frame(self, bg="#2c3e50")
        header_frame.pack(fill=tk.X, padx=10, pady=10)

        header_label = tk.Label(
            header_frame, 
            text="Client Registration", 
            font=("Arial", 16, "bold"), 
            fg="white", 
            bg="#2c3e50"
        )
        header_label.pack(side=tk.LEFT, pady=10)

        # Form fields
        form_frame = tk.Frame(self)
        form_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        # First Name
        tk.Label(form_frame, text="First Name:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.first_name_entry = tk.Entry(form_frame, width=30)
        self.first_name_entry.grid(row=0, column=1, pady=5, padx=10)

        # Middle Name
        tk.Label(form_frame, text="Middle Name:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.middle_name_entry = tk.Entry(form_frame, width=30)
        self.middle_name_entry.grid(row=1, column=1, pady=5, padx=10)

        # Last Name
        tk.Label(form_frame, text="Last Name:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.last_name_entry = tk.Entry(form_frame, width=30)
        self.last_name_entry.grid(row=2, column=1, pady=5, padx=10)

        # Birthday
        tk.Label(form_frame, text="Birthday (YYYY-MM-DD):").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.birthday_entry = tk.Entry(form_frame, width=30)
        self.birthday_entry.grid(row=3, column=1, pady=5, padx=10)

        # Gender
        tk.Label(form_frame, text="Gender:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.gender_var = tk.StringVar(value="Male")
        gender_frame = tk.Frame(form_frame)
        gender_frame.grid(row=4, column=1, sticky=tk.W, pady=5, padx=10)
        tk.Radiobutton(gender_frame, text="Male", variable=self.gender_var, value="Male").pack(side=tk.LEFT)
        tk.Radiobutton(gender_frame, text="Female", variable=self.gender_var, value="Female").pack(side=tk.LEFT)
        tk.Radiobutton(gender_frame, text="Other", variable=self.gender_var, value="Other").pack(side=tk.LEFT)

        # Submit button
        submit_btn = tk.Button(
            self, 
            text="Submit", 
            command=self._on_submit, 
            bg="#27ae60", 
            fg="white", 
            padx=20, 
            pady=5
        )
        submit_btn.pack(pady=20)

    def _on_submit(self):
        """Handle form submission"""
        try:
            record = {
                "first_name": self.first_name_entry.get().strip(),
                "middle_name": self.middle_name_entry.get().strip(),
                "last_name": self.last_name_entry.get().strip(),
                "birthday": self._validate_birthday(),
                "gender": self.gender_var.get()
            }

            # Validate required fields
            if not record["first_name"] or not record["last_name"] or not record["birthday"]:
                raise ValueError("First name, last name, and birthday are required")

            if self.on_submit(record):
                messagebox.showinfo("Success", "Record added successfully!")
                self.destroy()
            else:
                messagebox.showerror("Error", "Failed to add record")

        except ValueError as e:
            messagebox.showerror("Validation Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

    def _validate_birthday(self) -> str:
        """Validate and format the birthday"""
        birthday_str = self.birthday_entry.get().strip()
        try:
            datetime.strptime(birthday_str, "%Y-%m-%d")
            return birthday_str
        except ValueError:
            raise ValueError("Birthday must be in YYYY-MM-DD format")

