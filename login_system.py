import tkinter as tk
import hashlib
import sqlite3 as sql
# Create the main window
root = tk.Tk()
root.title("Login Screen")
root.attributes("-fullscreen", True)

class Login:    
    def validate_login(self):
        conn  =  sql.connect ( 'teste_database.db' )
        cursor  =  conn.cursor ()
        cur = conn.cursor()
        user = self.password_entry.get()
        password = self.password_entry.get()
        password = hashlib.sha256(password.encode()).hexdigest()
        cur.execute(f"SELECT * from user WHERE user='{user}' AND password='{password}'")
        result = cursor.fetchone()
        if not cur.fetchone():
            self.label.config(text="Invalid login", fg="red")
        else:
            self.label.config(text="Login successful", fg="green")
            from excel import screen 
            screen()

    def link01(self):
        from sing_system import Sing 
        Sing()


    def __init__(self, root):
        # Create a label for the username
        self.username_label = tk.Label(root, text="Username:")
        self.username_label.pack()

        # Create a text entry for the username
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        # Create a label for the password
        self.password_label = tk.Label(root, text="Password:")
        self.password_label.pack()

        # Create a text entry for the password
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        self.label = tk.Label(root, text="")
        self.label.pack()

        # Create a login button
        self.login_button = tk.Button(root, text="Login", command=self.validate_login)
        self.login_button.pack()

        self.validate_button = tk.Button(root, text="Don't have an account", command=self.link01)
        self.validate_button.pack()

        self.quit_button = tk.Button(root, text="Quit", command=quit)
        self.quit_button.pack()


login = Login(root)

# Start the window's event loop
root.mainloop()

