import os
import json
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from typing import List, Dict, Optional
from PIL import Image, ImageTk

class ClientDatabase:
    """Integrated database system for client records"""
    def __init__(self, filename: str = "client_records.json"):
        self.filename = filename
        self.records = []
        self._initialize()

    def _initialize(self):
        """Initialize the database file"""
        try:
            if not os.path.exists(self.filename):
                with open(self.filename, 'w') as f:
                    json.dump([], f)
            self._load()
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to initialize: {e}")

    def _load(self):
        """Load records from file"""
        try:
            with open(self.filename, 'r') as f:
                self.records = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            self.records = []
        except Exception as e:
            messagebox.showerror("Load Error", f"Failed to load records: {e}")

    def _save(self):
        """Save records to file"""
        try:
            with open(self.filename, 'w') as f:
                json.dump(self.records, f, indent=4)
        except Exception as e:
            messagebox.showerror("Save Error", f"Failed to save records: {e}")

    def add_client(self, client_data: Dict) -> bool:
        """Add a new client record"""
        try:
            required = ['first_name', 'last_name', 'birthday', 'gender']
            if not all(field in client_data for field in required):
                raise ValueError("Missing required fields")

            client_data['id'] = len(self.records) + 1
            client_data['created_at'] = datetime.now().isoformat()
            
            self.records.append(client_data)
            self._save()
            return True
        except Exception as e:
            messagebox.showerror("Add Error", f"Failed to add client: {e}")
            return False

    def get_all_clients(self) -> List[Dict]:
        """Retrieve all client records"""
        return self.records.copy()

    def search_clients(self, query: str, field: str = 'first_name') -> List[Dict]:
        """Search client records"""
        try:
            return [s for s in self.records 
                   if query.lower() in str(s.get(field, '')).lower()]
        except Exception as e:
            messagebox.showerror("Search Error", f"Search failed: {e}")
            return []
        
    def delete_client(self, client_id: int) -> bool:
        """Delete a client record by ID"""
        try:
            initial_count = len(self.records)
            self.records = [record for record in self.records if record.get('id') != client_id]
            
            if len(self.records) < initial_count:
                self._save()
                return True
            return False
        except Exception as e:
            messagebox.showerror("Delete Error", f"Failed to delete client: {e}")
            return False

class SignUpForm(tk.Toplevel):
    """Form for registering new clients"""
    def __init__(self, parent, onSubmit):
        super().__init__(parent)
        self.title("Client Registration")
        self.geometry("400x500")
        self.configure(bg='#D8BFD8')
        self.onSubmit = onSubmit
        
        # Form fields
        tk.Label(self, text="First Name:", bg='#D8BFD8').pack(pady=5)
        self.first_name = tk.Entry(self)
        self.first_name.pack(pady=5)
        
        tk.Label(self, text="Middle Name:", bg='#D8BFD8').pack(pady=5)
        self.middle_name = tk.Entry(self)
        self.middle_name.pack(pady=5)
        
        tk.Label(self, text="Last Name:", bg='#D8BFD8').pack(pady=5)
        self.last_name = tk.Entry(self)
        self.last_name.pack(pady=5)
        
        tk.Label(self, text="Birthday (YYYY-MM-DD):", bg='#D8BFD8').pack(pady=5)
        self.birthday = tk.Entry(self)
        self.birthday.pack(pady=5)
        
        tk.Label(self, text="Gender:", bg='#D8BFD8').pack(pady=5)
        self.gender = ttk.Combobox(self, values=["Male", "Female", "Other"])
        self.gender.pack(pady=5)
        
        tk.Button(self, text="Submit", bg='#6F4685', fg='white', command=self._submit).pack(pady=20)

    def _submit(self):
        """Handle form submission"""
        client = {
            'first_name': self.first_name.get(),
            'middle_name': self.middle_name.get(),
            'last_name': self.last_name.get(),
            'birthday': self.birthday.get(),
            'gender': self.gender.get()
        }
        
        if self.onSubmit(client):
            self.destroy()

class RecordsView(tk.Toplevel):
    def __init__(self, parent, records: List[Dict], db=None):
        super().__init__(parent)
        self.title("View All Records")
        self.geometry("800x600")
        self.configure(bg='#D8BFD8')
        self.db = db
        self._setup_ui(records)
        self._center_window()

    def _center_window(self):
        """Center the window on the screen"""
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'+{x}+{y}')

    def _setup_ui(self, records: List[Dict]):
        """Set up the user interface"""
        # Header
        header_frame = tk.Frame(self, bg="#6F4685")
        header_frame.pack(fill=tk.X, padx=10, pady=10)
        
        try:
            img = Image.open("project/assets/logo.png") if os.path.exists("project/assets/records.png") else None
            if img:
                img = img.resize((50, 50), Image.Resampling.LANCZOS)
                self.records_img = ImageTk.PhotoImage(img)
                img_label = tk.Label(header_frame, image=self.records_img, bg="#6F4685")
                img_label.pack(side=tk.LEFT, padx=10)
        except Exception as e:
            print(f"Error loading image: {e}")

        header_label = tk.Label(
            header_frame, 
            text="Client Records", 
            font=("Arial", 16, "bold"), 
            fg="white", 
            bg="#6F4685"
        )
        header_label.pack(side=tk.LEFT, pady=10)

        tree_frame = tk.Frame(self)
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        button_frame = tk.Frame(self, bg='#D8BFD8')
        button_frame.pack(fill=tk.X, padx=10, pady=10)

        if self.db:  
            delete_btn = tk.Button(
                button_frame, 
                text="Delete Selected", 
                command=self._delete_record, 
                bg="#e74c3c", 
                fg="white", 
                padx=20, 
                pady=5
            )
            delete_btn.pack(side=tk.RIGHT)

        scrollbar = ttk.Scrollbar(tree_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree = ttk.Treeview(
            tree_frame,
            columns=("ID", "First Name", "Middle Name", "Last Name", "Birthday", "Gender"),
            yscrollcommand=scrollbar.set,
            selectmode="browse"
        )
        scrollbar.config(command=self.tree.yview)

        # Configure columns
        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.column("ID", width=50, anchor=tk.CENTER)
        self.tree.column("First Name", width=150, anchor=tk.CENTER)
        self.tree.column("Middle Name", width=150, anchor=tk.CENTER)
        self.tree.column("Last Name", width=150, anchor=tk.CENTER)
        self.tree.column("Birthday", width=100, anchor=tk.CENTER)
        self.tree.column("Gender", width=80, anchor=tk.CENTER)

        # Create headings
        self.tree.heading("ID", text="ID")
        self.tree.heading("First Name", text="First Name")
        self.tree.heading("Middle Name", text="Middle Name")
        self.tree.heading("Last Name", text="Last Name")
        self.tree.heading("Birthday", text="Birthday")
        self.tree.heading("Gender", text="Gender")

        self.tree.pack(fill=tk.BOTH, expand=True)
        
        # Insert records
        for record in records:
            self.tree.insert("", tk.END, values=(
                record.get("id", ""),
                record.get("first_name", ""),
                record.get("middle_name", ""),
                record.get("last_name", ""),
                record.get("birthday", ""),
                record.get("gender", "")
            ))
    
    def _delete_record(self):
        """Delete the selected record"""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a record to delete")
            return

        item_data = self.tree.item(selected_item)
        record_id = item_data['values'][0]  

        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this record?"):
            if self.db.delete_client(record_id):
                self.tree.delete(selected_item)
                messagebox.showinfo("Success", "Record deleted successfully")
            else:
                messagebox.showerror("Error", "Failed to delete record")


class SearchForm(tk.Toplevel):
    """Form for searching client records"""
    def __init__(self, parent, onSearch):
        super().__init__(parent)
        self.title("Search Clients")
        self.geometry("400x300")
        self.configure(bg='#D8BFD8')
        self.onSearch = onSearch
        
        tk.Label(self, text="Search Term:", bg='#D8BFD8').pack(pady=10)
        self.term = tk.Entry(self)
        self.term.pack(pady=10)
        
        tk.Label(self, text="Search Field:", bg='#D8BFD8').pack(pady=10)
        self.field = ttk.Combobox(self, 
                                values=["first_name", "last_name", "birthday", "gender"])
        self.field.set("first_name")
        self.field.pack(pady=10)
        
        tk.Button(self, text="Search", bg="#6F4685", fg= 'white', command=self._search).pack(pady=20)

    def _search(self):
        """Execute search"""
        term = self.term.get()
        field = self.field.get()
        if term and field:
            self.onSearch(term, field)
            self.destroy()

class ClientRecordApp:
    """Main application window"""
    def __init__(self, root):
        self.root = root
        self.root.title("Aster/Risk Management System")
        self.root.geometry("450x600")
        self.root.configure(bg='#D8BFD8')
        
        # Initialize database
        self.db = ClientDatabase()
        
        # Setup UI
        self._setup_ui()

    def _setup_ui(self):
        """Create main interface"""
        # Header with title
        header = tk.Frame(self.root, bg="#6F4685", height=70)
        header.pack(fill=tk.X)
        
        
        tk.Label(header, text="Aster/Risk Management", 
                font=("Times New Roman", 14), fg="white", bg="#6F4685").pack(side=tk.LEFT)
        
        main_container = tk.Frame(self.root, bg='#D8BFD8')
        main_container.pack(expand=True, fill=tk.BOTH)
        
        try:
            img = Image.open("project/assets/logo.png").resize((150, 150))
            self.logo = ImageTk.PhotoImage(img)
            logo_frame = tk.Frame(main_container, bg='#D8BFD8')
            logo_frame.pack(pady=(0, 30))
            tk.Label(main_container, image=self.logo, bg="#D8BFD8").pack()
        except:
            pass
        
        button_frame = tk.Frame(main_container, bg='#D8BFD8')
        button_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        btn_data = [
            ("Register Client", "#5D3F6A", self._open_signup),
            ("View All Records", "#6F4685", self._view_records),
            ("Search Records", "#9867C5", self._open_search),
            ("Exit", "#9E7BB5", self.root.quit)
        ]
        
        btn_style = {
        'font': ('Arial', 10, 'bold'),
        'width': 15,
        'height': 1,
        'bd': 0,  
        'relief': tk.RAISED,
        'activebackground': '#555555',  
        'activeforeground': 'white',
        'padx': 5,
        'pady':5
    }
        
        for text, color, cmd in btn_data:
            btn = tk.Button(
            button_frame,
            text=text,
            bg=color,
            fg="white",
            command=cmd,
            **btn_style
        )
            btn.pack(pady=13, fill=tk.X)  
        

    def _open_signup(self):
        """Open registration form"""
        SignUpForm(self.root, self.db.add_client)

    def _view_records(self):
        """Display all records"""
        records = self.db.get_all_clients()
        if records:
            RecordsView(self.root, records, self.db)
        else:
            messagebox.showinfo("Info", "No client records found")

    def _open_search(self):
        """Open search form"""
        SearchForm(self.root, lambda term, field: 
                 RecordsView(self.root, self.db.search_clients(term, field), self.db))

if __name__ == "__main__":
    root = tk.Tk()
    app = ClientRecordApp(root)
    root.mainloop()